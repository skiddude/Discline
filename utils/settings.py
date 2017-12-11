from yaml import safe_load
from blessings import Terminal
import os

def copy_skeleton():
    term = Terminal()
    try:
        from shutil import copyfile
        if not os.path.exists(os.getenv("HOME") + "/.config/Discline"):
            os.mkdir(os.getenv("HOME") + "/.config/Discline")
        
        copyfile("res/settings-skeleton.yaml", os.getenv("HOME") + "/.config/Discline/config", follow_symlinks=True) 
        print(term.green("Skeleton copied!" + term.normal))
    except:
        print(term.red("Error creating skeleton file."))
        quit()


# can't import globals.term due to globals.py needing settings
term = Terminal()

# This runs on the module import, before the client or main() starts
os.system("clear")
if not os.path.exists(os.getenv("HOME") + "/.config/Discline"):
    print(term.yellow("Configuration file not found, creating skeleton..."))
    copy_skeleton()
    print(term.cyan("Your configuration file can be found at ~/.config/Discline"))
    print("\n")

try:
    with open(os.getenv("HOME") + "/.config/Discline/config") as f:
        settings = safe_load(f)
except:
    try:
        with open(os.getenv("HOME") + "/.Discline") as f:
            settings = safe_load(f)
    except:
        try:
            with open("res/settings-skeleton.yaml") as f:
                settings = safe_load(f)
        except:
            print(term.red("ERROR: could not get settings."))
            quit()

# null it when we're done
term = None
