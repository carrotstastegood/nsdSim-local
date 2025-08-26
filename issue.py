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

def weigh(n):

    if n == "0":
        raise TypeError("weigh() does not take 0.")

    global iid
    n = str(n)
    iid = idBase + "c" + n
    points = 0 # Establish common variable.

    choice = short[n]
    print(iid)
    calc(points, n)

weigh(1)

print(weight)

# Calculate and show final scores

total = weight["choiceOne"] + weight["choiceTwo"] + weight["choiceThree"] + weight["choiceFour"] + weight["choiceFive"]
while True:
    try:
        one = (weight["choiceOne"] / total) * 100
        two = (weight["choiceTwo"] / total) * 100
        three = (weight["choiceThree"] / total) * 100
        four = (weight["choiceFour"] / total) * 100
        five = (weight["choiceFive"] / total) * 100
        break
    except ZeroDivisionError:
        total = 1
        print(f"Total weight is {total}, read as zero.")


scores = { # Used for checking the largest value - the winner
    "one" : one,
    "two" : two,
    "three" : three,
    "four" : four,
    "five" : five
}

victor = max(scores, key=scores.get)
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
        for x in range(round(scores[victor] / 50)):
            popularity -= (scores[victor] / 8)
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
        break
    elif auto in ["y", "Y"]:
        break
    else:
        print("Invalid input.")

input("Press enter to exit: ")