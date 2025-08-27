import json

with open("json/usr/prefs.jsonc", "r") as p:
    d = json.load(p)

setup = d.get("setup", 1)

if setup:
    exec(open("code/app.py").read())
elif setup == 1:
    print("Setup value is missing.")
    exec(open("code/setup.py").read())
else:
    exec(open("code/setup.py").read())