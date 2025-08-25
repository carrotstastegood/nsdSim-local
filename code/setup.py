import math
import os
import json
import requests
import xmltodict as xtd

os.system("clear")

# Set setup to true


with open("json/prefs.jsonc", "r") as p:
    prefs = json.load(p)
with open("json/account.jsonc", "r") as a:
    acc = json.load(a)

# Prepare for getting user data

agent = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0"}

while True:
    nation = str(input("Name of your nation > "))
    url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nation + ";q=+population"

    if nation in ["gaster", "Gaster", "GASTER"]:
        raise TypeError("im winging my ding")

    # Get user data

    rawData = requests.get(url, headers=agent)

    if rawData.status_code == 404:
        print("Nation does not exist.")
    else:
        xml = rawData.text
        data = xtd.parse(xml)
        break

population = data["NATION"]["POPULATION"]

if int(population) <= 1000000: # Nationstates' api gives a population greater than one billion in a thousand.
    population = int(population) * 1000000

print(f"Population write: {population}")

def newCensus(id):
    global rawData, xml, nation, data, agent

    if id == None:
        raise TypeError(f"id value is not provided: {id}")

    url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nation + ";q=census;scale=" + str(id) + ";mode=score"
    rawData = requests.get(url, headers=agent)
    xml = rawData.text
    data = xtd.parse(xml)
    
    #print(url)
    #print(data)
    #print(data["NATION"]["CENSUS"]["SCALE"]["SCORE"])

percent = 0
complete = 0
shade = ""

#def progress():
    #global percent, shade, complete
    #complete += 1
    #percent = round((complete / 30) * 100)
    #bar = shade + " " + str(percent) + "%"
    #print(bar)

#progress()  

if rawData.status_code == 200: # Do the thing
    
    print()

    #---Actual Configuration---#

    username = input("Enter a username > ")
    if username == "":
        username = "empty"
        print("Empty input: username set to empty. You can change this later.")
    vol = input("Sound volume > ")
    debug = input("Show extra debug information? (y/n) > ")

    if debug == "y":
        debug = True
    else:
        debug = False

    #password goes here

    #---Census Write---#

    # Extra information for debug
    print()
    print("Reference URL (Shows all Census stats) >")
    print(f"https://www.nationstates.net/cgi-bin/api.cgi?nation={nation};q=census;scale=all;mode=score")
    print()
    print("Negative stats are normal.")
    print("cid = Census ID")
    print()

    # Full data fetch.

    newCensus(0) # Civil Rights
    civil = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid0 fetched: {civil}")
    
    newCensus(1) # Economy
    economy = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid1 fetched: {economy}")
    
    newCensus(2) # Political Rights
    political = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid2 fetched: {political}")

    newCensus(4) # Wealth Gaps
    gap = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid4 fetched: {gap}")

    newCensus(5) # Death rate (Unexpected Deaths)
    udeath = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid5 fetched: {udeath}")

    newCensus(10) # Car industry
    auto = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid10 fetched: {auto}")

    newCensus(13) # IT industry
    it = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid13 fetched: {it}")

    newCensus(15) # Fishing
    fishing = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid15 fetched: {fishing}")

    newCensus(16) # Arms manufacturing
    arms = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid16 fetched: {arms}")

    newCensus(17) # Farming
    agriculture = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid17 fetched: {agriculture}")

    newCensus(46) # Defence Forces
    army = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid46 fetched: {army}")

    newCensus(47) # Pacifism
    pacifism = data["NATION"]["CENSUS"]["SCALE"]["SCORE"]
    print(f"cid47 fetched: {pacifism}")

    #---Creating Non-NS Stats---#

    locals()

    #float(arms), float(army), float(pacifism)
    #warSupport = (((arms + army) / 2) - (pacifism * 1.5))
    #print(warSupport)

    with open("json/prefs.jsonc", "w") as p:
        prefs["setup"] = True
        prefs["vol"] = vol
        prefs["debug"] = debug
    
    with open("json/account.jsonc", "w") as a:
        acc["nsdSim"]["username"] = username
        acc["nsdSim"]["url"] = url

    json.dump(prefs, p, indent=4)
    json.dump(acc, all, indent=4)