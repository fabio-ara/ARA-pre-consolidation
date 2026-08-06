import base64
import json
import os
import urllib.request

repo = os.environ["GITHUB_REPOSITORY"]
token = os.environ["GITHUB_TOKEN"]
url = f"https://api.github.com/repos/{repo}/contents/.github/process-model-domain-1.py?ref=consolidation-control"
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
exec(compile(code, ".github/process-model-domain-1.py", "exec"))

# Cleanup after the processor has atomically materialized the batch.
head = api("GET", f"/repos/{repo}/git/ref/heads/consolidation-control")["object"]["sha"]
commit = api("GET", f"/repos/{repo}/git/commits/{head}")
new_tree = api("POST", f"/repos/{repo}/git/trees", {
    "base_tree": commit["tree"]["sha"],
    "tree": [
        {"path": ".github/process-final-experience-batch.py", "mode": "100644", "type": "blob", "sha": None},
        {"path": ".github/process-cross-domain-benchmark.py", "mode": "100644", "type": "blob", "sha": None},
    ],
})["sha"]
cleanup_commit = api("POST", f"/repos/{repo}/git/commits", {
    "message": "chore: restore clean control root",
    "tree": new_tree,
    "parents": [head],
})["sha"]
api("PATCH", f"/repos/{repo}/git/refs/heads/consolidation-control", {"sha": cleanup_commit, "force": False})
try:
    api("DELETE", f"/repos/{repo}/git/refs/heads/consolidation-control-temp-should-not-use")
except Exception:
    pass
print("cleanup_commit:", cleanup_commit)
