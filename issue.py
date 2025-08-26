import math
import os
import json
import random
import commentjson as cjson

os.system("clear")

with open("json/sys.jsonc", "r") as s: # Load software settings
    sys = cjson.load(s)
    print("json.jsonc loaded.")

with open("json/prefs.jsonc", "r") as p: # Load account settings
    prefs = cjson.load(p)
    print("prefs.jsonc loaded.")

with open("json/account.jsonc", "r") as a: # Load accound information
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

with open("json/issueTags.jsonc", "r") as i: # Load issue tags.
    data = cjson.load(i)

print(data)

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

run = data[idBase]["options"]

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
    print(f"weigh() TAGS: {tags}")
    
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

    calc(points, n) # Finish by writing weight.

def sim(): # Simplify the simulation process.
    for r in range(int(run)):
        r + 1
        weigh(r)

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