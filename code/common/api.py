# Refresh api data when needed.

import os
import json
import requests
import xmltodict as xtd

import commentjson as cjson

with open("../../json/account.jsonc", "r") as a:
    acc = cjson.load(a)
    print("api.py: account.jsonc loaded.")
with open("../../json/prefs.jsonc", "r") as p:
    prefs = cjson.load(p)
    print("api.py: prefs.jsonc loaded.")

nation = acc["nationstates"]["nation", "testlandia"]
url = acc["nsdSim"]["url", "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nation + ";q=+population"]

def dprint(s):
    if prefs["debug"]:
        print(s)

confirm = input("Clear? (Y/n) ")
if input in ["Y", "y", ""]:
    os.system("clear")

agent = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0"}

response = requests.get(url, headers=agent)