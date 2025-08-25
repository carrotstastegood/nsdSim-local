import math
import os
import json
import random
import commentjson as cjson

os.system("clear")

with open("json/sys.jsonc", "r") as s:
    sys = cjson.load(s)
    print("json.jsonc loaded.")

with open("json/prefs.jsonc", "r") as p: # Load account settings
    prefs = cjson.load(p)
    print("prefs.jsonc loaded.")

with open("json/account.jsonc", "r") as a:
    acc = json.load(a)
    print("account.jsonc loaded.")

def dprint(s): # Print debug text
    if prefs["debug"]:
        print(s)

if not prefs["debug"]:
    os.system("clear")
dprint("Option 'debug' is set to True")

allowed = [0]

while True: # Input loop
    try:
        issue = int(input("What issue are you simulating? (Answer in a number.) > "))
        if int(issue) not in allowed:
            print("Support for that issue is not provided.")
        else:
            print()
            break
    except ValueError:
        print("You must provide an integer.")

idBase = "id" + str(issue) # Make a base id to use and modify later.
iid = ""

with open("json/issueTags.jsonc", "r") as issueTags: # Load issue tags.
    data = cjson.load(issueTags)

    # Long list of variables.

    #for x in range(sys["suppot"]): # Future logic.
    id0cn = data.get("id0", {}).get("options") # Issue id 0, amount of choices.
    id0c1 = data.get("id0", {}).get("optionOne", {}) # Issue id 0, choise 1.
    id0c2 = data.get("id0", {}).get("optionTwo", {})
    id0c3 = data.get("id0", {}).get("optionThree", {})

civilRights = 64.89
conservatism = 43.67
politicalRights = 52.95
tax = 73.25

weight = {
    "choiceOne" : 0.00,
    "choiceTwo" : 0.00,
    "choiceThree" : 0.00,
    "choiceFour" : 0.00,
    "choiceFive" : 0.00
}

short = {
    "1" : "choiceOne",
    "2" : "choiceTwo",
    "3" : "choiceThree",
    "4" : "choiceFour",
    "5" : "choiceFive"
}

def calc(x, n): # Simulate unperdictability and write final value to weight
    global weight
    choice = short[str(n)] # choiceN
    weight[choice] += round(x + random.uniform(0, 0.10), 2)
    dprint(f"weight['{choice}'] written as {weight[choice]}")
    
calc(0, 1)

def weigh(n):

    global iid
    n = str(n)
    iid = idBase + "c" + n

    if n == "0":
        raise TypeError("weigh() does not take 0.")

    choice = short[n]
    print(iid)

weigh(1)

print(weight)