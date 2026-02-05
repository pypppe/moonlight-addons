import os
import platform
import socket
import psutil
import shutil
import subprocess
import datetime
import random
import time
import webbrowser
from pathlib import Path

try:
    from PIL import ImageGrab
    screenshot_available = True
except ImportError:
    screenshot_available = False

os.system('cls')

try:
    import wmi
    wmi_available = True
except ImportError:
    wmi_available = False

commands = {}

def info_cmd():
    print("\nMOONLIGHT ADDON INFORMATION\n")
    print("Ver: 0.0.2")
    print("BETA Phase: Yes")
    print("Created in: UK")
    print("GitHub: yes")
    print("Created for: Windows OS")
    print("Created with: Python\n")

    print("PC INFORMATION;\n")
    print(f"CPU: {platform.processor()}")
    print(f"OS: {platform.system()} {platform.release()} ({platform.version()})")
    print(f"Hostname: {socket.gethostname()}")
    print(f"Username: {os.getlogin()}")
    print(f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    if wmi_available:
        w = wmi.WMI()
        gpus = w.Win32_VideoController()
        for i, gpu in enumerate(gpus):
            print(f"GPU {i+1}: {gpu.Name}")
    else:
        print("GPU: WMI not installed (pip install wmi)")
    print("")

def moon_cmd():
    moons = ["🌑","🌒","🌓","🌔","🌕","🌖","🌗","🌘"]
    print(f"Moon Phase: {random.choice(moons)}\n")

def candle_cmd():
    print(r"""
        /\
       /  \
       \/\/
        ~|
       !~~-!
       |` ,!
       |'` |
       |   |
       |   |
       |   |
       |   |
_______|___|_______
\                 /
 \_______________/
    """)
    print("A candle has been lit. ✨\n")

def wait_cmd(seconds):
    try:
        sec = int(seconds)
        print(f"Waiting for {sec} seconds...")
        time.sleep(sec)
        print("Done waiting!\n")
    except:
        print("Usage: wait [seconds]\n")

def echo_cmd(text):
    print(f"{text}\n")

def star_cmd():
    print("""
*       *       * 
  *     *     *   
    *   *   *     
      * * *       
* * * * * * * * * 
      * * *       
    *   *   *     
  *     *     *   
*       *       * 
""")
    print("A shining star appears. ✨\n") # this deadass looks like the UK flag bro im crine son

def moonphase_cmd():
    phases = ["🌑 New Moon","🌒 Waxing Crescent","🌓 First Quarter","🌔 Waxing Gibbous",
              "🌕 Full Moon","🌖 Waning Gibbous","🌗 Last Quarter","🌘 Waning Crescent"]
    print(f"Moon Phase: {random.choice(phases)}\n")

def fortune_cmd():
    fortunes = [
        "You will find something you lost.",
        "A pleasant surprise is waiting for you.",
        "Today is a good day to try something new.",
        "Trust your instincts.",
        "Something unexpected will make you smile."
    ]
    print(f"Fortune: {random.choice(fortunes)}\n")

def roll_cmd():
    print(f"Dice roll: {random.randint(1,6)}\n")

def flip_cmd():
    print(f"Coin flip: {'Heads' if random.randint(0,1)==0 else 'Tails'}\n")

def sysinfo_cmd():
    print("\nSYSTEM INFORMATION\n")
    print(f"CPU: {platform.processor()}")
    print(f"OS: {platform.system()} {platform.release()}") # this will most likely be windows 10 or 11 but it will be good to have the exact version as well because this isnt supported on mac, or linux.
    print(f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print(f"Hostname: {socket.gethostname()}")
    if shutil.which("wmic"):
        try:
            gpu_info = subprocess.check_output("wmic path win32_videocontroller get name", shell=True)
            print(f"GPU(s): {gpu_info.decode().strip()}")
        except:
            print("GPU: Could not detect")
    print("")

def dir_cmd(path="."):
    try:
        items = os.listdir(path)
        for item in items:
            print(item)
        print("")
    except FileNotFoundError:
        print(f"Directory not found: {path}\n")

def delete_cmd(path):
    if os.path.exists(path):
        confirm = input(f"Are you sure you want to delete {path}? (y/n): ").lower()
        if confirm == "y":
            try:
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)
                print(f"{path} deleted successfully.\n")
            except Exception as e:
                print(f"Error deleting {path}: {e}\n")
        else:
            print("Delete cancelled.\n")
    else:
        print(f"File/Folder not found: {path}\n")

def mkdir_cmd(path):
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Folder created: {path}\n")
    except Exception as e:
        print(f"Error creating folder: {e}\n")

def cd_cmd(path):
    try:
        os.chdir(path)
        print(f"Current directory: {os.getcwd()}\n")
    except Exception as e:
        print(f"Error changing directory: {e}\n")

def copy_cmd(src, dst):
    try:
        shutil.copy2(src, dst)
        print(f"{src} copied to {dst}\n")
    except Exception as e:
        print(f"Error copying: {e}\n")

def move_cmd(src, dst):
    try:
        shutil.move(src, dst)
        print(f"{src} moved to {dst}\n")
    except Exception as e:
        print(f"Error moving: {e}\n")

def ping_cmd(host):
    os.system(f"ping {host}")

def ipconfig_cmd():
    os.system("ipconfig")

def processes_cmd():
    print("\nPID\tCPU%\tMEM%\tName\t\tPath")
    print("-"*60)
    for proc in psutil.process_iter(['pid','name','cpu_percent','memory_percent','exe']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            cpu = proc.info['cpu_percent']
            mem = round(proc.info['memory_percent'],2)
            path = proc.info['exe'] if proc.info['exe'] else "N/A"
            line = f"{pid}\t{cpu}\t{mem}\t{name}\t{path}"
            if cpu>50 or mem>50:
                line += " <--⚠️⚠️⚠️ High usage⚠️⚠️⚠️"
            print(line)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    print("")

def time_cmd():
    now = datetime.datetime.now()
    print(f"Current Time: {now.strftime('%H:%M:%S')}\n")

def date_cmd():
    today = datetime.datetime.now()
    print(f"Today's Date: {today.strftime('%Y-%m-%d')}\n")

def clear_cmd():
    os.system('cls')

def battery_cmd():
    if hasattr(psutil, "sensors_battery"):
        battery = psutil.sensors_battery()
        if battery:
            plugged = "Plugged In" if battery.power_plugged else "Not Plugged"
            print(f"Battery: {battery.percent}% ({plugged})\n")
        else:
            print("Battery information not available. You may be using an All in one or a PC.\n") # added this because my all in one dell pc obviously doesnt have any battery, so its good to note that you might be using an all in one or a PC.
    else:
        print("Battery info not supported.\n")

def screenshot_cmd():
    if screenshot_available:
        path = Path.home() / "Desktop" / f"screenshot_{int(time.time())}.png"
        img = ImageGrab.grab()
        img.save(path)
        print(f"Screenshot saved to {path}\n")
    else:
        print("PIL not installed: pip install pillow\n")

def reboot_cmd():
    os.system("shutdown /r /t 0")

def shutdown_cmd():
    os.system("shutdown /s /t 0")

def bios_cmd():
    confirm = input("Are you sure you want to boot into BIOS? (y/n): ").lower()
    if confirm == "y":
        print("Restarting into BIOS!")
        os.system("shutdown /r /fw /t 1")
    else:
        print("Cancelled boot into BIOS.\n")

def wifiis_cmd(): # woo hoo over here lily if it goes wrong blame you / NVM IT DIDNT FUCKING BREAK LETS GO
    print("\nConnected Wi-Fi Network")
    print("-"*30)
    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True, text=True)
        ssid = "Not connected"
        for line in output.splitlines():
            if "SSID" in line and "BSSID" not in line:
                ssid = line.split(":", 1)[1].strip()
                break
        print(f"Wi-Fi Name: {ssid}")
    except subprocess.CalledProcessError:
        print("Unable to get Wi-Fi info.")
    print("")

def whois_cmd(domain=None):
    print("")
    if domain:
        url = f"https://who.is/whois/{domain}"
        webbrowser.open(url)
        print(f"Opening who.is for: {domain}\n")
    else:
        print("Usage: whois [domain]\n")

def git_cmd():
    webbrowser.open("https://git-scm.com/download/win")
def gith_cmd(): webbrowser.open("https://github.com")
def githd_cmd(): os.system('start "" "C:\\Users\\%USERNAME%\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"')
def gitd_cmd(): os.system('start "" "C:\\Program Files\\Git\\git-bash.exe"')
def tm_cmd(): os.system("start taskmgr")
def zandovo_cmd(): webbrowser.open("https://open.astrarune.com")
def githr_cmd(): webbrowser.open("https://github.com/pypppe")
def yt_cmd(): webbrowser.open("https://youtube.com")
def twitter_cmd(): webbrowser.open("https://twitter.com")
def reddit_cmd(): webbrowser.open("https://reddit.com")
def open_cmd(url=None): 
    if url: webbrowser.open(url)
    else: print("Usage: open [url]\n") # for some fucking reason it uses mircosft edge instead of my default browser, im not changing it though too bad too sad innit

def exit_cmd():
    print("Exiting Moonlight Addons...")
    exit()

all_commands = {
    "help": None,
    "info": info_cmd,
    "moon": moon_cmd,
    "candle": candle_cmd,
    "wait": wait_cmd,
    "echo": echo_cmd,
    "star": star_cmd,
    "moonphase": moonphase_cmd,
    "fortune": fortune_cmd,
    "roll": roll_cmd,
    "flip": flip_cmd,
    "sysinfo": sysinfo_cmd,
    "dir": dir_cmd,
    "delete": delete_cmd,
    "mkdir": mkdir_cmd,
    "cd": cd_cmd,
    "copy": copy_cmd,
    "move": move_cmd,
    "ping": ping_cmd,
    "ipconfig": ipconfig_cmd,
    "processes": processes_cmd,
    "time": time_cmd,
    "date": date_cmd,
    "clear": clear_cmd,
    "cls": clear_cmd,
    "battery": battery_cmd,
    "screenshot": screenshot_cmd,
    "reboot": reboot_cmd,
    "shutdown": shutdown_cmd,
    "git": git_cmd,
    "gith": gith_cmd,
    "githd": githd_cmd,
    "gitd": gitd_cmd,
    "tm": tm_cmd,
    "taskmanager": tm_cmd,
    "taskmgr": tm_cmd,
    "zandovo": zandovo_cmd,
    "githr": githr_cmd,
    "youtube": yt_cmd,
    "twitter": twitter_cmd,
    "reddit": reddit_cmd,
    "open": open_cmd,
    "exit": exit_cmd,
    "close": exit_cmd,
    "bios": bios_cmd,
    "wifiis": wifiis_cmd,
    "whois": whois_cmd
}

def help_cmd():
    print("\nList of Commands;\n" + "\n".join(all_commands.keys()) + "\n")
all_commands["help"] = help_cmd

commands = all_commands

print("🕯️ Moonlight Addons has been imported 🕯️")
print("Type 'help' for a list of commands.")
print("Type 'info' for Moonlight Addons information.\n")

while True:
    user_input = input(">> ").strip()
    if not user_input:
        continue
    parts = user_input.split()
    cmd = parts[0].lower()
    args = parts[1:]

    if cmd in commands:
        try:
            commands[cmd](*args)
        except TypeError:
            print(f"Usage: {cmd} [arguments]\n")
    else:
        print("Unknown command. Type 'help' for a list of commands.\n")

        # holy shit
