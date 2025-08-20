import math
import os
import json
import requests
import xml.etree.ElementTree as xml

with open("json/issueTags.jsonc", "r") as issueTags:
    data = json.load(issueTags)

# Long list of variables.

id0cn = data.load("id0", {}).get("options") # Issue id 0, amount of choices.
id0c1 = data.load("id0", {}).get("optionOne", {}) # Issue id 0, choise 1.
id0c2 = data.load("id0", {}).get("optionTwo", {})
id0c3 = data.load("id0", {}).get("optionThree", {})

civilRights = 64.89
conservatism = 43.67
politicalRights = 52.95
tax = 73.25

libWeight = {

    "choiceOne" : 0.00,
    "choiceTwo" : 0.00,
    "choiceThree" : 0.00,
    "choiceFour" : 0.00,
    "choiceFive" : 0.00

}

def scanTags(lib, c): # lib should be in the format of id0c1
    
    if lib["civilRightsDown"]:
        if civilRights >= 65 and civilRights is not 85:
            libWeight[c] += 0.05
        elif civilRights >= 85:
            libWeight[c] += 0.07
        else:
            libWeight[c] -= 2



print(id0c1)