import json
import os
import urllib.error
import urllib.request

TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ["GITHUB_REPOSITORY"]
BRANCH = "consolidation-control"
TEMP_BRANCH = "consolidation-control-temp-should-not-use"
SELF_PATH = ".github/process-final-experience-batch.py"


def api(method, path, payload=None):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        "https://api.github.com" + path,
        data=data,
        method=method,
        headers={
            "Authorization": "Bearer " + TOKEN,
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request) as response:
        body = response.read()
        return json.loads(body) if body else None

# Delete only the accidental temporary branch. Treat an already-absent ref as success.
try:
    api("DELETE", f"/repos/{REPO}/git/refs/heads/{TEMP_BRANCH}")
except urllib.error.HTTPError as error:
    if error.code != 422 and error.code != 404:
        raise

# Remove this helper from consolidation-control in a fast-forward commit.
head = api("GET", f"/repos/{REPO}/git/ref/heads/{BRANCH}")["object"]["sha"]
commit = api("GET", f"/repos/{REPO}/git/commits/{head}")
new_tree = api("POST", f"/repos/{REPO}/git/trees", {
    "base_tree": commit["tree"]["sha"],
    "tree": [{"path": SELF_PATH, "mode": "100644", "type": "blob", "sha": None}],
})["sha"]
new_commit = api("POST", f"/repos/{REPO}/git/commits", {
    "message": "chore: restore clean control root",
    "tree": new_tree,
    "parents": [head],
})["sha"]
api("PATCH", f"/repos/{REPO}/git/refs/heads/{BRANCH}", {"sha": new_commit, "force": False})
print("temporary_branch_removed:", TEMP_BRANCH)
print("cleanup_commit:", new_commit)
