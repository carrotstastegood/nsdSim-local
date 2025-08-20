import asyncio
import json
import os
import requests
import xml.etree.ElementTree as xml

os.system("clear")

with open("json/prefs.jsonc", "r") as p:
    prefs = json.load(p)
setup = prefs.get("setup", False)
with open("json/prefs.jsonc", "w") as p:
    prefs["setup"] = True
    json.dump(prefs, p, indent=4)

print("")

agent = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0"}

nation = input("")