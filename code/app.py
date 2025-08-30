import cmd
import json
import os
import subprocess
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
    intro = "nsdSim app. \nType help or ? to list commands. \nTry running 'help sim'!"
    prompt = "nsdSCLI > "

    def do_sim(self, arg): # Load simulator.
        if arg == "-i":
            subprocess.run([sys.executable, "code/sim/issue.py"])
            quit()
        elif arg == "-f":
            exec(open("code/sim/federal.py").read())

    def do_about(self, arg): # Display information about the app.
        print("nsdSim (Nationstates Democracy Simulator) is an unoficial tool to simulate elections.")
        dprint("File: /code/app.py | Running from /nsdSim.py")

    def do_account(self, arg):
        if arg == "-a":
            print("Account information:")
            print(a)
        elif arg == "-s":
            print("Settings:")
            print(p)
        elif arg == "-u":
            print("User information:")
            print(a)
            print(p)

    def do_settings(self, arg):
        new = input("> ")
        if arg == "debug":
            if new not in ["True", "False"]:
                print("Must be boolean (True, False)")
        p[arg] = new
        print(f"{arg} set to {new}")

    def do_clear(self, arg): # Clear.
        os.system("clear")

    def do_exit(self, arg): # Exit.
        exit()

    def do_restart(self, arg): # Restart the app.
        exec(open("nsdSim.py").read())

    # Help

    def help_sim(self):
        print("Simulate issues. \n  -i | Issue votes \n  -f | Federal elections")

    def help_clear(self):
        print("Clears terminal.")

    def help_settings(self):
        print("Changes settings. \n Input what setting you would like to change, and what to.")

    def help_account(self):
        print("Display account information \n  -a | Account info \n  -s | Settings \n  -u | All")

if __name__ == "__main__":
    main().cmdloop()