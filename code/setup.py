import asyncio
import os
import json

from awesomeNations import AwesomeNations

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

api = AwesomeNations("Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0")

#nation = str(input("Name of your nation > "))
nation = "umidus"
nationurl = "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nation + ";q=+population+census;scale=all"

if nation in ["gaster", "Gaster", "GASTER"]:
    raise TypeError("im winging my ding")

# Get user data

data = api.Nation(nation)
census = data.get_shards("census", scale=0)

def newShard(id):
    global data
    global census

    census = data.get_shards("census", scale=id)

# census["nation"]["census"]["scale"][]

newShard(2)
print(census)
score = census["nation"]["census"]["scale"]["score"]
print(score)

#print(thing["animal"])