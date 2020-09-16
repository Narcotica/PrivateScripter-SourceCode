from colorama import Fore
import requests
import subprocess
import os


subprocess.call('', shell=True)
os.system("cls && title ProxyScraper")


print(Fore.LIGHTGREEN_EX + "Welcome to my ProxyScraper")
print("")
print(Fore.LIGHTWHITE_EX + "you can choose of the following Modules: " + Fore.LIGHTCYAN_EX + "HTTP - SOCKS4 - SOCKS5")
print("")
print("")

choice = input(Fore.LIGHTBLACK_EX + "> ")


def HTTPProxies():

    proxylink = 'pastebin link'

    r = requests.get(proxylink)

    text = str(r.text)

    print(text)


def SOCKS4Proxies():

    proxylink = 'pastebin link'

    r = requests.get(proxylink)

    text = str(r.text)

    print(text)


def SOCKS5Proxies():

    proxylink = 'pastebin link'

    r = requests.get(proxylink)

    text = str(r.text)

    print(text)


if choice == "HTTP":
    os.system("cls && title HTTP-ProxyScraper")
    HTTPProxies()

elif choice == "SOCKS4":
    os.system("cls && title SOCKS4-ProxyScraper")
    SOCKS4Proxies()

elif choice == "SOCKS5":
    os.system("cls && title SOCKS5-ProxyScraper")
    SOCKS5Proxies()

os.system("pause")


def ResetProgram():
    print(Fore.LIGHTGREEN_EX + "Welcome to my ProxyScraper")
    print("")
    print(
        Fore.LIGHTWHITE_EX + "you can choose of the following Modules: " + Fore.LIGHTCYAN_EX + "HTTP - SOCKS4 - SOCKS5")
    print("")
    print("")

    choice = input(Fore.LIGHTBLACK_EX + "> ")

    if choice == "HTTP":
        os.system("cls && title HTTP-ProxyScraper")
        HTTPProxies()
    elif choice == "SOCKS4":
        os.system("cls && title SOCKS4-ProxyScraper")
        SOCKS4Proxies()

    elif choice == "SOCKS5":
        os.system("cls && title SOCKS5-ProxyScraper")
        SOCKS5Proxies()


while 1:
    os.system("cls")
    ResetProgram()
