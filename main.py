from config import config
from player import player
import os, time

cmd = config.osCmd
enm_hp_bak = config.enm_hp

# Game main menu
def main():
    if player.exp >= 200:
        player.exp = 0
        player.lv += 1

    config.enm_hp = enm_hp_bak

    os.system(cmd)

    print("====== Main ======")
    print("1. Fight!\n2. Player\n3. Shop\n4. Save & Exit")
    print("==================")

    main_input = input("> ")

    if main_input == "1":
        fight()
    elif main_input == "2":
        os.system(cmd)

        print("====== Player ======")
        print(f"Name: {player.name}\n------\nEXP: {player.exp}\nLV: {player.lv}")
        print("====================")

        input("<>")

        main()
    elif main_input == "3":
        shop()
    elif main_input == "4":
        save(player.new, player.name, player.diff, player.hp, player.atk, player.gold, player.exp, player.lv, player.hpot)
    else:
        main()

# Game battle menu
def fight():
    if config.enm_hp <= 0:
        main()

    os.system(cmd)

    print("====== Battle ======")
    print(f"HP: {player.hp}\nEnemy HP: {config.enm_hp}\n----------\n1. Fight\n2. Heal - x{player.hpot}\n3. Run")
    print("====================")

    fight_input = input("> ")

    if fight_input == "1":
        player.hp -= config.enm_atk
        config.enm_hp -= player.atk
        fight()
    elif fight_input == "2":
        if player.hpot <= 0:
            print("You don\'t have enough Healing Potions!")
            input("<>")
        else:
            player.hpot -= 1
            player.hp += 5
        fight()
    elif fight_input == "3":
        main()
    else:
        fight()

# Game shop menu
def shop():
    os.system(cmd)

    print("====== Shop ======")
    print(f"Gold: {player.gold}\n------\n1. Healing Potion - {config.hpot_price}\n2. Return")
    print("==================")

    shop_input = input("> ")

    if shop_input == "1":
        if player.gold <= config.enm_hp:
            print("You don\'t have enough Gold!")
            input("<>")
            shop()
        else:
            player.gold -= config.hpot_price
            player.hpot += 1
            shop()
    elif shop_input == "2":
        main()

def save(new, name, diff, hp, atk, gold, exp, lv, hpot):
    os.system(cmd)

    with open("player/player.py", "w") as playerFile:
        playerFile.writelines([f"new = {new}\n", f"name = \"{name}\"\n", f"diff = {diff}\n", f"hp = {hp}\n", f"atk = {atk}\n", f"gold = {gold}\n", f"exp = {exp}\n", f"lv = {lv}\n", f"hpot = {hpot}"])
    playerFile.close()

    exit()

# Sets the player file with all default values
def setNewPlayer():
    os.system(cmd)

    print("What is your name?")
    new_name = input("> ")

    if new_name == "":
        setNewPlayer()

    os.system(cmd)

    print("Set a difficulty")
    print("1. Normal\n2. Hard\n")
    new_diff = input("> ")

    if new_diff == "1":
        os.system(cmd)

        with open("player/player.py", "w") as playerFile:
            playerFile.writelines([f"new = False\n", f"name = \"{new_name}\"\n", f"diff = {new_diff}\n"])
            playerFile.writelines(config.defaultPlayer)
        playerFile.close()

        print("Relaunch the game...\n")
        time.sleep(0.5)

        exit()
    elif new_diff == "2":
        os.system(cmd)

        print("Hard difficulty is in development\n")
        input("<>")

        exit()
    else:
        setNewPlayer()

# Verifies if the player is new or not
if player.new:
    os.system(cmd)

    print(f"Setting for: {config.sys}\n")
    time.sleep(2)

    setNewPlayer()
else:
    os.system(cmd)

    print("Welcome to PyRPG!!\n")
    time.sleep(1.5)

    main()
