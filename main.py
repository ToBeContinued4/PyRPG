import player as pl
import os, platform, time

# System detection
sys = platform.system()

if sys == 'Windows':
    cmd = "cls"
else:
    cmd = "clear"

# Main menu
def main():
    print("Hola wenas\n")
    time.sleep(1)
    exit()

# Checks if the player is new, if yes,
if pl.new:
    while True:
        os.system(cmd)

        print("What is your name?\n")

        new_name = input("> ")

        os.system(cmd)

        print("Select a difficulty")
        print("1. Normal\n2. Hard\n")

        new_diff = input("> ")

        if new_diff == '1' or new_diff == '2':
            with open("player.py", "w") as plFile:
                plFile.writelines([f"new = False\n", f"name = \"{new_name}\"\n", f"diff = {new_diff}\n"])
            plFile.close()

            os.system(cmd)
            print("Relaunch the game...\n")
            time.sleep(0.5)

            exit()
else:
    main()