import base64
import json
import os
import urllib.request

repo = os.environ["GITHUB_REPOSITORY"]
token = os.environ["GITHUB_TOKEN"]
url = f"https://api.github.com/repos/{repo}/contents/.github/process-aralearn-reference.py?ref=consolidation-control"
request = urllib.request.Request(url, headers={"Authorization":"Bearer "+token,"Accept":"application/vnd.github+json","X-GitHub-Api-Version":"2022-11-28"})
with urllib.request.urlopen(request) as response:
    obj = json.load(response)
code = base64.b64decode(obj["content"]).decode("utf-8")
exec(compile(code, ".github/process-aralearn-reference.py", "exec"))
