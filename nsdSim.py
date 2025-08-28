import json
import subprocess
import sys

with open("json/usr/prefs.jsonc", "r") as p:
    d = json.load(p)

setup = d.get("setup", 1)

if setup:
    subprocess.run([sys.executable, "code/app.py"])

elif not setup:
    subprocess.run([sys.executable, "code/setup.py"])


else:
    print("Setup value is missing.")
    subprocess.run([sys.executable, "code/setup.py"])