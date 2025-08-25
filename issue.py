import math
import os
import commentjson as cjson

allowed = [0]

while True: # Input loop
    try:
        issue = int(input("What issue are you simulating? (Answer in a number.) > "))
        if int(issue) not in allowed:
            print("Support for that issue is not provided.")
        else:
            break
    except ValueError:
        print("You must provide an integer.")

idBase = "id" + str(issue) + "c"
iid = ""

with open("json/issueTags.jsonc", "r") as issueTags:
    data = cjson.load(issueTags)

    # Long list of variables.

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

def weigh(n):
    
    global iid
    n = str(n)
    iid = idBase + n

    choice = short[n]
    print(iid)


weigh(1)