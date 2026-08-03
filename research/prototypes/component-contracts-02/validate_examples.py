from __future__ import annotations

import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent
SCHEMA_DIR = ROOT / "schemas"
EXAMPLE_DIR = ROOT / "examples"
MIGRATION_DIR = ROOT / "migrations"

schemas = {}
registry = Registry()
for path in sorted(SCHEMA_DIR.glob("*.schema.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    schemas[path.name] = data
    registry = registry.with_resource(data["$id"], Resource.from_contents(data))

format_checker = FormatChecker()

def validate(schema_name: str, instance: object, label: str) -> None:
    validator = Draft202012Validator(
        schemas[schema_name],
        registry=registry,
        format_checker=format_checker,
    )
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
    if errors:
        details = "\n".join(
            f"{label} at {'/'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}"
            for error in errors
        )
        raise AssertionError(details)

def load_directory(path: Path) -> list[dict]:
    return [json.loads(item.read_text(encoding="utf-8")) for item in sorted(path.glob("*.json"))]

manifests = load_directory(EXAMPLE_DIR / "manifests")
instances = load_directory(EXAMPLE_DIR / "instances")
results = json.loads((EXAMPLE_DIR / "validation-scenarios.json").read_text(encoding="utf-8"))
migrated = load_directory(MIGRATION_DIR / "expected-0.2")

for index, manifest in enumerate(manifests):
    validate("component-manifest.schema.json", manifest, f"manifest[{index}]")

family_schema = {
    "semantic-mathematics": "semantic-mathematics.schema.json",
    "relational-construction": "relational-construction.schema.json",
    "executable-programming": "executable-programming.schema.json",
    "source-argument": "source-argument.schema.json",
}
for group, documents in (("instance", instances), ("migrated", migrated)):
    for index, document in enumerate(documents):
        validate(family_schema[document["family"]], document, f"{group}[{index}]")

for index, result in enumerate(results):
    validate("common.schema.json", {"value": result}, f"validation[{index}]")
    validator = Draft202012Validator(
        {"$ref": schemas["common.schema.json"]["$id"] + "#/$defs/validationResult"},
        registry=registry,
        format_checker=format_checker,
    )
    errors = list(validator.iter_errors(result))
    if errors:
        raise AssertionError(f"validation[{index}]: {errors[0].message}")

print(json.dumps({
    "manifests": len(manifests),
    "component_instances": len(instances),
    "migrated_instances": len(migrated),
    "validation_scenarios": len(results),
    "total": len(manifests) + len(instances) + len(migrated) + len(results),
    "failures": 0,
}, indent=2))
