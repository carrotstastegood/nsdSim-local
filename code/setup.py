import asyncio
import nationstates
import os
import json

os.system("clear")

# Set setup to true

def writeSetup():
    with open("json/prefs.jsonc", "r") as p:
        prefs = json.load(p)
    setup = prefs.get("setup", False)
    with open("json/prefs.jsonc", "w") as p:
        prefs["setup"] = True
        json.dump(prefs, p, indent=4)
writeSetup

# Prepare for getting user data

api = nationstates.Nationstates("Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0")

nation = str(input("Name of your nation:"))
nationurl = "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nation + ";q=+population+census;scale=all"

# Get user data

data = api.nation(nation)
thing = data.get_shards("animal")

print(thing["animal"])