#!/usr/bin/env python3
"""Validate ARA component-contract prototype schemas and examples."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent
SCHEMAS = ROOT / "schemas"
EXAMPLES = ROOT / "examples"


def load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def build_registry(schema_documents: dict[str, dict[str, Any]]) -> Registry:
    registry = Registry()
    for filename, schema in schema_documents.items():
        resource = Resource.from_contents(schema)
        registry = registry.with_resource(schema["$id"], resource)
        registry = registry.with_resource(filename, resource)
    return registry


def validate(
    schema: dict[str, Any],
    instance: Any,
    registry: Registry,
    label: str,
) -> list[str]:
    validator = Draft202012Validator(
        schema,
        registry=registry,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    return [
        f"{label}: {'/'.join(str(part) for part in error.path) or '<root>'}: {error.message}"
        for error in errors
    ]


def main() -> int:
    schema_documents = {
        path.name: load(path)
        for path in sorted(SCHEMAS.glob("*.schema.json"))
    }
    registry = build_registry(schema_documents)

    manifests = load(EXAMPLES / "manifests.json")
    instances = load(EXAMPLES / "component-instances.json")
    microsequences = load(EXAMPLES / "microsequences.json")
    scenarios = load(EXAMPLES / "validation-scenarios.json")

    errors: list[str] = []
    for index, item in enumerate(manifests, start=1):
        errors.extend(
            validate(
                schema_documents["component-manifest.schema.json"],
                item,
                registry,
                f"manifest-{index}",
            )
        )

    track_schemas = [
        "semantic-mathematics.schema.json",
        "relational-construction.schema.json",
        "executable-programming.schema.json",
        "source-argument.schema.json",
    ]
    for schema_name, item in zip(track_schemas, instances, strict=True):
        errors.extend(validate(schema_documents[schema_name], item, registry, schema_name))

    for index, item in enumerate(microsequences, start=1):
        errors.extend(
            validate(
                schema_documents["microsequence-prototype.schema.json"],
                item,
                registry,
                f"microsequence-{index}",
            )
        )

    validation_ref = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$ref": "common.schema.json#/$defs/validationResult",
    }
    for index, scenario in enumerate(scenarios, start=1):
        errors.extend(
            validate(
                validation_ref,
                scenario["result"],
                registry,
                f"validation-scenario-{index}",
            )
        )

    if errors:
        print("\n".join(errors))
        return 1

    total = len(manifests) + len(instances) + len(microsequences) + len(scenarios)
    print(f"Validated {total} prototype documents with no schema errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
