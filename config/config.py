import platform

# System detection to set a custom command
sys = platform.system()

if sys == "Windows":
    osCmd = "cls"
else:
    osCmd = "clear"

# Default player file
defaultPlayer = [f"hp = 20\n", f"atk = 7\n", f"gold = 0\n", f"exp = 0\n", f"lv = 0\n", f"hpot = 3\n"]

# Enemy stats
enm_hp = 10
enm_atk = 5

# Shop values
hpot_price = 5