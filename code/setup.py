import json
import os
import requests
import subprocess
import sys
import xmltodict as xtd

os.system("clear")

header = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0"}
# ^^^ Need to properly get this (((HOWWWWWWWWWWWWWWWWWWWWWWWWWW??????????????????????????????????????????????????????????)))

while True: # Nation loop
    
    # Get user's nation
    print("Input nation name")
    nation = input("> ")
    url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nation + ";q=census;scale=all;mode=score"

    response = requests.get(url, headers=header)

    # Verify nation exists.
    if response.status_code == 404:
        print("Nation does not exist.")
    else:
        break

while True:

    # Ask for volume   
    print("Volume")
    vol = input("> ")
    break

while True:

    # Ask if debug
    print("Enable debug mode?")
    debug = input("> ")
    if debug not in ["true", "false"]:
        print("Must be a boolean (true, false).")
    else:
        break

# Convert response into dict

xml = xtd.parse(response.text)
data = xml

scores = data["NATION"]["CENSUS"]["SCALE"]

# Dictionaries

census = {} # Will add more keys during for loop

# Get census data