import cmd
import json
import os
import sys
import commentjson as cjson

os.system("clear")

with open("json/usr/prefs.jsonc") as prefs:
    p = cjson.load(prefs)

with open("json/usr/account.jsonc") as acc:
    a = cjson.load(acc)

def dprint(s):
    if p["debug"]:
        print(s)

class main(cmd.Cmd):
    intro = "nsdSim app. \nType help to list commands."
    prompt = "> "

    def do_sim(self, arg):
        if arg == "-i":
            exec(open("code/sim/issue.py").read())
        elif arg == "-f":
            exec(open("code/sim/federal.py").read())

    def do_about(self, arg):
        print("nsdSim (Nationstates Democracy Simulator) is an unoficial tool to simulate elections.")
        dprint("File: /code/app.py | Running from /")

    def do_clear(self, arg):
        os.system("clear")

    def do_exit(self, arg):
        exit()

    def do_restart(self, arg):
        exec(open("nsdSim.py").read())

    # Help

    def help_sim(self):
        print("")

    def help_clear(self):
        print("Clears terminal.")

if __name__ == "__main__":
    main().cmdloop()