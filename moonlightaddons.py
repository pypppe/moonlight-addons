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
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

print("🕯️ Moonlight Addons Installer 🕯️\n")
print("Choose your platform:\n")
print("Linux - L")
print("Windows (Discontinued) - W\n")

choice = input("Type L for Linux commands, type W for Windows commands: ").strip().upper()
## Some linux commands may not work. BETA VERSION, you have been warned.

if choice == "L":
    clear_screen()
    print("Linux Moonlight Addons has been installed.\n")
    current_platform = "linux"
elif choice == "W":
    clear_screen()
    print("Windows Moonlight Addons has been installed. WARNING: Windows Moonlight Addons is DISCONTINUED.\n")
    current_platform = "windows"
else:
    print("Invalid choice, exiting...")
    exit()

wmi_available = False
if current_platform == "windows":
    try:
        import wmi
        wmi_available = True
    except ImportError:
        wmi_available = False

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
    print("A shining star appears. ✨\n")

def moon_cmd():
    moons = ["🌑","🌒","🌓","🌔","🌕","🌖","🌗","🌘"]
    print(f"Moon Phase: {random.choice(moons)}\n")

def moonphase_cmd():
    phases = ["🌑 New Moon","🌒 Waxing Crescent","🌓 First Quarter","🌔 Waxing Gibbous",
              "🌕 Full Moon","🌖 Waning Gibbous","🌗 Last Quarter","🌘 Waning Crescent"]
    print(f"Moon Phase: {random.choice(phases)}\n")

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

def time_cmd():
    now = datetime.datetime.now()
    print(f"Current Time: {now.strftime('%H:%M:%S')}\n")

def date_cmd():
    today = datetime.datetime.now()
    print(f"Today's Date: {today.strftime('%Y-%m-%d')}\n")

def clear_cmd():
    clear_screen()

def exit_cmd():
    print("Exiting Moonlight Addons...")
    exit()

def screenshot_cmd():
    if screenshot_available:
        path = Path.home() / "Desktop" / f"screenshot_{int(time.time())}.png"
        img = ImageGrab.grab()
        img.save(path)
        print(f"Screenshot saved to {path}\n")
    else:
        print("PIL not installed: pip install pillow\n")

def open_cmd(url=None): 
    if url: webbrowser.open(url)
    else: print("Usage: open [url]\n")
        
if current_platform == "windows":
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

    def sysinfo_cmd():
        print("\nSYSTEM INFORMATION\n")
        print(f"CPU: {platform.processor()}")
        print(f"OS: {platform.system()} {platform.release()}")
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

    def battery_cmd():
        if hasattr(psutil, "sensors_battery"):
            battery = psutil.sensors_battery()
            if battery:
                plugged = "Plugged In" if battery.power_plugged else "Not Plugged"
                print(f"Battery: {battery.percent}% ({plugged})\n")
            else:
                print("Battery information not available.\n")
        else:
            print("Battery info not supported.\n")

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

if current_platform == "linux":
    def sysinfo_cmd():
        uname = platform.uname()
        print("\nSYSTEM INFORMATION\n")
        print(f"System: {uname.system} {uname.release}")
        print(f"Node Name: {uname.node}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")
        ram = round(psutil.virtual_memory().total / (1024**3), 2)
        print(f"RAM: {ram} GB\n")

    def dir_cmd(path="."):
        os.system(f"ls -la {path}")
        print("")

    def delete_cmd(path):
        confirm = input(f"Are you sure you want to delete {path}? (y/n): ").lower()
        if confirm == "y":
            os.system(f"rm -rf {path}")
            print(f"{path} deleted successfully.\n")
        else:
            print("Delete cancelled.\n")

    def mkdir_cmd(path):
        os.makedirs(path, exist_ok=True)
        print(f"Folder created: {path}\n")

    def cd_cmd(path):
        try:
            os.chdir(path)
            print(f"Current directory: {os.getcwd()}\n")
        except Exception as e:
            print(f"Error changing directory: {e}\n")

    def copy_cmd(src, dst):
        os.system(f"cp -r {src} {dst}")
        print(f"{src} copied to {dst}\n")

    def move_cmd(src, dst):
        os.system(f"mv {src} {dst}")
        print(f"{src} moved to {dst}\n")

    def ping_cmd(host):
        os.system(f"ping -c 4 {host}")

    def shutdown_cmd():
        print("Shutting down Linux system...")
        os.system("sudo shutdown now")

    def reboot_cmd():
        print("Rebooting Linux system...")
        os.system("sudo reboot")

all_commands = {
    "help": None,
    "sysinfo": sysinfo_cmd,
    "dir": dir_cmd,
    "delete": delete_cmd,
    "mkdir": mkdir_cmd,
    "cd": cd_cmd,
    "copy": copy_cmd,
    "move": move_cmd,
    "ping": ping_cmd,
    "time": time_cmd,
    "date": date_cmd,
    "clear": clear_cmd,
    "cls": clear_cmd,
    "exit": exit_cmd,
    "close": exit_cmd,
    "screenshot": screenshot_cmd,
    "echo": echo_cmd,
    "star": star_cmd,
    "moon": moon_cmd,
    "moonphase": moonphase_cmd,
    "candle": candle_cmd,
    "fortune": fortune_cmd,
    "roll": roll_cmd,
    "flip": flip_cmd,
    "open": open_cmd,
}

if current_platform == "windows":
    all_commands.update({
        "info": info_cmd,
        "ipconfig": ipconfig_cmd,
        "processes": processes_cmd,
        "battery": battery_cmd,
        "reboot": reboot_cmd,
        "shutdown": shutdown_cmd,
        "bios": bios_cmd,
    })

def help_cmd():
    print("\nList of Commands;\n" + "\n".join(all_commands.keys()) + "\n")
all_commands["help"] = help_cmd

print("🕯️ Moonlight Addons is ready 🕯️")
print("Type 'help' for a list of commands.\n")

while True:
    user_input = input(">> ").strip()
    if not user_input:
        continue
    parts = user_input.split()
    cmd = parts[0].lower()
    args = parts[1:]

    if cmd in all_commands:
        try:
            all_commands[cmd](*args)
        except TypeError:
            print(f"Usage: {cmd} [arguments]\n")
        except Exception as e:
            print(f"Error executing {cmd}: {e}\n")
    else:
        print("Unknown command. Type 'help' for a list of commands.\n")
