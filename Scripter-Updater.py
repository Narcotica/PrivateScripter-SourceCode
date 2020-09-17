from colorama import Fore
import requests
import os
import webbrowser
import subprocess


subprocess.call('', shell=True)
os.system("cls && title Updater")


def checkUpdates():
    print("")
    print(Fore.LIGHTBLUE_EX + "Checking for Updates")
    print("")

    link = ""
    f = requests.get(link)

    newversion = str(f.text)
    if newversion != version:
        print(Fore.RED + "Updates found " + Fore.GREEN + "Please install the new updates")
        print("")
        print("Open Website!")
        webbrowser.open_new_tab('DOWNLOAD LINK TO YOUR .exe or so idc XD')
        print("")
    else:
        print(Fore.BLUE + "                                                 No Updates")
        print("")


version = '1.0.0.0'


checkUpdates()
