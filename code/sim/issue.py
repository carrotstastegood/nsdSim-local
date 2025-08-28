import commentjson as cjson
import math
import os
import json
import random
import requests
import subprocess
import sys
import xmltodict as xtd

os.system("clear")

with open("json/app/app.jsonc", "r") as s: # Load software settings
    app = cjson.load(s)
    print("json.jsonc loaded.")

with open("json/usr/prefs.jsonc", "r") as p: # Load account settings
    prefs = json.load(p)
    print("prefs.jsonc loaded.")

with open("json/usr/account.jsonc", "r") as a: # Load accound information
    acc = json.load(a)
    print("account.jsonc loaded.")

with open("json/app/issueTags.jsonc", "r") as i: # Load issue tags.
    data = cjson.load(i)
    print("issueTags.jsonc loaded.")

print(prefs)
def dprint(s): # Print debug text
    if prefs["debug"]:
        print(s)

def ifprint(d, n): # Print debug text or normal text depending on user settings.
    if prefs["debug"]:
        print(d)
    else:
        print((n))

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

civilRights = 64.89
conservatism = 43.67
politicalRights = 52.95
tax = 73.25

weight = { # Main data to determine who wins. Higher the weight, higher the vote.
    "choiceOne" : 0.00,
    "choiceTwo" : 0.00,
    "choiceThree" : 0.00,
    "choiceFour" : 0.00,
    "choiceFive" : 0.00
}

short = { # Convert numbers into key names used in weight dict.
    "1" : "choiceOne",
    "2" : "choiceTwo",
    "3" : "choiceThree",
    "4" : "choiceFour",
    "5" : "choiceFive"
}

options = data[idBase]["options"] # Used in sim() function in ln 119 to determine how much times it should run.

def calc(x, n): # Simulate unperdictability and write final value to weight
    global weight
    choice = short[str(n)] # choiceN
    weight[choice] += round(x + random.uniform(-0.10, 0.10), 2)
    dprint(f"weight['{choice}'] written as {weight[choice]}")

def weigh(n): # Sim

    if n == "0": # Raise error before the next one to tell whoever wrote the code that you cant put in a zero. Saves time.
        raise TypeError("weigh() does not take 0.")

    # Get Variables.

    global iid
    n = str(n)
    iid = idBase + "c" + n
    points = 0 # Will be added to weight
    key = "option" + n
    tags = data[idBase][key] # Simplify dictionary down to used tags.
    dprint(f"weigh() Issue Tags = {tags}")
    
    # Logic | Use tags.get to make sure it does not crash upon finding nothing; may be common because different issues vary in results.
    # If someone can find a better way to do this than feel free to try.

    match tags.get("civilRights"):
        case "down":
            if civilRights == 80:
                points -= 0.05
            elif civilRights >= 70:
                points -= 0.15
            elif civilRights >= 50:
                points -= 1.00
            else:
                points -= 1.75
        case "up":
            if civilRights == 80:
                points += 0.10
            elif civilRights >= 70:
                points += 0.45
            elif civilRights >= 50:
                points += 1.75
            else:
                points += 2.00

    if tags.get("neverVote"): # Future logic.
        pass

    calc(points, n) # Finish by writing weight.

def sim(): # Simplify the simulation process.
    for r in range(int(options)):
        r += 1 # R starts at 0.
        print(f"sim(): Turn {r}")
        weigh(r)

sim() # Actually do the simulation.

print(weight)

# Calculate and show final scores

total = 0 # DO THIS OR IT RETURNS STUPID BULLSHIT 
trueTotal = 0

def finish():
    global total
    for x in range(5): # Check if the weight key exists, then add the weight to the total.
        x += 1
        print(f"finish(): Turn {x}")
        if weight.get(short[str(x)]) != None: # Does choiceX exist
            total += weight[short[str(x)]] # Write to key.
            print(weight.get(short[str(x)]))

finish()

# If all numbers are negative or positive it works fine. But if there are both positive and negative numbers, it returns percentages totaling over 100%.
# Might wait untill the actuall simulation part of the script is done to look at this further.

trueTotal += (weight["choiceOne"] + weight["choiceTwo"] + weight["choiceThree"] + weight["choiceFour"] + weight["choiceFive"])
dprint(f"trueTotal : {trueTotal}")

try: # Calculate percentages
    dprint(f"Total : {total}")
    one = round((weight["choiceOne"] / total) * 100, 2)
    two = round((weight["choiceTwo"] / total) * 100, 2)
    three = round((weight["choiceThree"] / total) * 100, 2)
    four = round((weight["choiceFour"] / total) * 100, 2)
    five = round((weight["choiceFive"] / total) * 100, 2)
except ZeroDivisionError:
    raise ZeroDivisionError(f"Total weight is {total}, read as zero.")

victor = max(weight, key=weight.get) # Find option with largest weight.
popularity = 75.00 # Will be loaded one it exists; It will be used / needed later.

print("Final scores:")
print()
print(f"Option one: {one}% ({weight['choiceOne']})")
print(f"Option two: {two}% ({weight['choiceTwo']})")
print(f"Option three: {three}% ({weight['choiceThree']})")
print(f"Option four: {four}% ({weight['choiceFour']})")
print(f"Option five: {five}% ({weight['choiceFive']})")
print()
print(f"Winning option: {victor}")
print()

while True:
    vote = input("Which choice will you implement? (full word) > ")
    if vote != victor and vote in ["one", "two", "three", "four", "five"]:
        for x in range(round(weight[victor] / 50)):
            popularity -= (weight[victor] / 8)
            dprint(f"Popularity: {popularity}")
        print(f"Current party populatity: {popularity}")
        break
    elif vote == victor:
        break
    else:
        print("Input must be a whole word (ex. one), and must be in all lower case")

auto = input("Do you want to automatically answer? (WON'T GIVE TRADING CARDS) (y/N) ") # Will answer the issue later.
while True:
    if auto in ["n", "N", ""]:
        subprocess.run([sys.executable, "code/app.py"])
        break
    elif auto in ["y", "Y"]:
        auto = True
        break
    else:
        print("Invalid input.")

# Auto answer

if not auto:
    input("Press enter to exit > ")

agent = acc["nsdSim"]["agent"]
nation = acc["nsdSim"]["nation"]
url = "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nation

response = requests.get(url, headers=agent)

if response.status_code == 404:
    print("Invalid data for either usr agent or url:")
    print(agent)
    print(url)

xml = response.text
parse = xtd.parse(xml)

print("Leaving to main app...")
subprocess.run([sys.executable, "code/app.py"])
