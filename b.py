import requests, os, threading, random, time
from colorama import Fore, Back, Style
from pystyle import Colors, Colorate, Center

clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear") # Don't touch this
users = open('check.txt', 'r').read().split('\n')
count = 0
free = 0
taken = 0
error = 0
proxyDebug = False
os.system(f"title Instagram Username Checker - Starting...")
clear()

# Vanity Generator Logo
logo = """
██╗░██████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██████╗░
██║██╔════╝░  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔══██╗
██║██║░░██╗░  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██████╔╝
██║██║░░╚██╗  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══██╗
██║╚██████╔╝  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║░░██║
╚═╝░╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝"""

def printLogo():
        print(Center.XCenter(Colorate.Horizontal(Colors.white_to_green, logo, 1)))

def check():
    global count, free, taken, error
    while True:
        for line in users:
            proxy = random.choice(open("proxies.txt","r").read().splitlines()); proxyDict = {"http": f"http://{proxy}"}
            if proxyDebug == True:
                print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Using proxy: {Fore.GREEN}{proxyDict}{Fore.RESET}")
            else:
                pass
            response = requests.get(f"https://www.instagram.com/{line}/", proxies=proxyDict)
            count += 1
            if (response.status_code == 200):
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Taken: " + line)
                with open ("taken.txt", "a") as f:
                    f.write(line + "\n")
                    taken += 1
            elif (response.status_code == 404):
                print(f"{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}] {Fore.RESET}Free/Termed: "+ line)
                with open ("free.txt", "a") as f:
                    f.write(line + "\n")
                    free += 1
            else:
                print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Error: " + line)
                with open ("error.txt", "a") as f:
                    f.write(line + "\n")
                    error += 1
            os.system(f"title Instagram Username Checker - Checked {count}/{len(users)} - Free: {free} - Taken: {taken} - Error: {error} - Remaining: {len(users)-count}")


clear()
printLogo()
print(f"{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}] {Fore.RESET}Found {Fore.GREEN}{len(users)}{Fore.RESET} accounts to check.")
try:
    while True:
        check()
        print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting.")
        time.sleep(1)
        exit()
except KeyboardInterrupt:
    clear()
    print(f"{Fore.RED}[{Fore.RESET}-{Fore.RED}] {Fore.RESET}Exiting. If it keeps, just close the program.")
    os.system(f"title Instagram Username Checker - Exiting. If it keeps, just close the program.")
    time.sleep(1)
    exit()