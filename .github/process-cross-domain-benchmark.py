import base64
import json
import os
import urllib.request

repo = os.environ["GITHUB_REPOSITORY"]
token = os.environ["GITHUB_TOKEN"]
url = f"https://api.github.com/repos/{repo}/contents/.github/process-final-experience-batch.py?ref=consolidation-control"
request = urllib.request.Request(
    url,
    headers={
        "Authorization": "Bearer " + token,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    },
)
with urllib.request.urlopen(request) as response:
    obj = json.load(response)
code = base64.b64decode(obj["content"]).decode("utf-8")
needle = '        {"path": WORKFLOW_PATH, "mode": "100644", "type": "blob", "sha": None},\n'
replacement = (
    needle
    + '        {"path": ".github/process-cross-domain-benchmark.py", "mode": "100644", "type": "blob", "sha": None},\n'
    + '        {"path": ".github/process-aralearn-reference.py", "mode": "100644", "type": "blob", "sha": None},\n'
    + '        {"path": ".github/workflows/process-aralearn-reference.yml", "mode": "100644", "type": "blob", "sha": None},\n'
)
assert needle in code
code = code.replace(needle, replacement, 1)
exec(compile(code, ".github/process-final-experience-batch.py", "exec"))
