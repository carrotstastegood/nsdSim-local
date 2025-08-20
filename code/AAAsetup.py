import os
import requests
import sqlite3
import xml.etree.ElementTree as et

os.system("clear")

db = sqlite3.connect("website/database/users.db") # SQL Database for later
dbWrite = db.cursor()

temp = {}
tags = {"cid0" : 0} #Temporary dictionary for census id stats. Will be replaced by the databases' stats.

agent = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0"}

nation = "umidus"
url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nation + ";q=+population+census;scale=all"
# ^^^ URL where user's Nationstates public shards are.


# If you don't know what shards are, please read nationstates.net/pages/api.html

print(f"Geting data from: {url}")

#  Get nation data from Nationstates.

pull = requests.get(url, headers=agent) # Grab shards
#Parse Functions
fuckXML = et.fromstring(pull.text)

def pullCensus(id):
    global url
    global pull
    url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nation + ";q=census;scale=" + str(id)
    pull = pull = requests.get(url, headers=agent)

if pull.status_code == 200:
    population = fuckXML.find("POPULATION").text
    civilRights = fuckXML.find(".//SCORE").text
    pullCensus(1)
    print(url)
    economy = fuckXML.find(".//SCORE").text
    print(population)
    print(civilRights)
    print(economy)

    if population == None:
        print("Parsing XML failed. Incorrect NS shard?")

# Handle HTTP errors

elif pull.status_code == 403:
    print("403 Forbidden. Invalid User Agent?")

elif pull.status_code == 404:
    print("404 Not Found. Nation does not exist")

#Write into database

("Safety Compassion")