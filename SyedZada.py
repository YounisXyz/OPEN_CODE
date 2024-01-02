#!/usr/bin/python3
#-*-coding:utf-8-*-

try:
        import requests
except ImportError:
        print('\n[+] requests module installing...\n')

        os.system('pip install requests')

try:
        import mechanize
except ImportError:
        print('\n [+] mechanize module installing...\n')

        os.system('pip install mechanize')

try:
        import bs4
except ImportError:
        print('\n [+] bs4 module installing...\n')

        os.system('pip install bs4')

try:
        import concurrent.futures
except ImportError:
        print('\n [+] future module installing...\n')
        os.system('pip install future')


Y = "\x1b[1;93m"
G = "\x1b[1;92m"
R = "\x1b[1;91m"

import os,requests,re,json,bs4,os,zlib,random,sys,time
from bs4 import BeautifulSoup
from os import system
agent = ["Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36 EdgA/100.0.1185.50","Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36 EdgA/100.0.1185.50","Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36 EdgA/100.0.1185.50","Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36 EdgA/100.0.1185.50","Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34"]
ua = random.choice(agent)

def xox(z):

        for e in z + '\n':
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.02)

logo = """
     \033[1;92m╔═══╗╔╗──╔╗╔═══╗╔═══╗  ╔════╗╔═══╗╔═══╗╔═══╗
     \033[1;92m║╔═╗║║╚╗╔╝║║╔══╝╚╗╔╗║  ╚══╗═║║╔═╗║╚╗╔╗║║╔═╗║
     \033[1;92m║╚══╗╚╗╚╝╔╝║╚══╗─║║║║    ╔╝╔╝║║─║║─║║║║║║─║║
     \033[1;93m╚══╗║─╚╗╔╝─║╔══╝─║║║║   ╔╝╔╝─║╚═╝║─║║║║║╚═╝║
     \033[1;93m║╚═╝║──║║──║╚══╗╔╝╚╝║  ╔╝═╚═╗║╔═╗║╔╝╚╝║║╔═╗║
     \033[1;92m╚═══╝──╚╝──╚═══╝╚═══╝  ╚════╝╚╝─╚╝╚═══╝╚╝─╚╝
\033[1;93m______________________________________________________

 \033[1;93m(*)\033[1;92m Developer : 🔥SYED-ZADA🔥 X 🔥QAISER ABBASS🔥
 \033[1;93m(*)\033[1;92m Tool Type : SIM & CNIC DETAILS \033[1;93m(Only For Pak)
 \033[1;93m(*)\033[1;92m YouTube   : SYED ZADA
 \033[1;93m(*)\033[1;92m Github    : https://github.com/syedzada1100
\033[1;93m______________________________________________________"""

try:
        import os, storage
except ImportError:
        os.system('termux-setup-storage')
        os.system('git pull')

        os.system('git pull')
        os.system('clear')

def main():
        os.system("clear");print(logo)
       # os.system('xdg-open https://youtube.com/c/SYEDZADA1100')
        print("")
        xox("\033[1;93m[+] WARNING : \033[1;92mDO NOT MISUSE THIS TOOL WARNING.. ⚠️")
        print(54 * "\x1b[1;93m_")
        print("")
        print (" \t[\x1b[1;97m\x1b[1;41m   THIS TOOL IS FREE NOT FOR PAID   \x1b[0m\x1b[1;93m]")
        print(54 * "\x1b[1;93m_")
        print ("")
        print("\x1b[1;93m[1] \x1b[1;92mStart To Use Tool")
        print("\x1b[1;93m[2] \x1b[1;92mjoin Our Facebook Gruop ")
        print("\x1b[1;93m[3] \x1b[1;92mjoin Our WhatsApp Gruop ")
        print("\x1b[1;93m[4] \x1b[1;92mSubscribe Our YouTube ")
        print("\x1b[1;93m[0] \x1b[1;92mExit")
        print(54 * "\x1b[1;93m_")
        print("")
        SYED = input('\x1b[1;93m[+] Choose Option: \x1b[1;92m')
        if SYED == '':
                print("\x1b[1;91mFill in correctly")
                main()
        elif SYED == '1':
                meta_data()
        elif SYED == '2':
                os.system('xdg-open https://www.facebook.com/groups/499609241591106/?ref=share_group_link')
                main()
        elif SYED == '3':
                os.system('xdg-open https://chat.whatsapp.com/Cm2EOgvNjBk9BGCHxzdcDG')
                main()
        elif SYED == '4':
                os.system('xdg-open https://youtube.com/c/SYEDZADA1100')
                main()
        elif SYED == '0':
                os.system('exit')
        else:
                print ('\x1b[1;91m[!] Please select a valid option')
                time.sleep(2)
                main()

def meta_data():
        system("clear");print(logo)
        print("")
        xox("\033[1;93m[+] NOTE :\033[1;92m SOME TIME YOUR IP WAS BLOCK SO IF NO RESULT USE AIRPLANE ✈️ MODE ON 5 SECOND..")
        print(54 * "\x1b[1;93m_")
        print("")
        print("")
        print("\t    [\033[1;97m\033[1;41m  PUT NUMBER WITHOUT (0)  \033[0m\033[1;93m]")
        print("")
        print("")
        number = input(f"{G}[+] PUT TARGET NUM & CNIC :{Y} ")
        if str("3478618390") in number:
                print("")
                print("")
                xox(f"{R}[×] DON'T TYPE OWNER NUMBER ")
                time.sleep(2)
                meta_data()
        if number[0] == str("0"):
                print("")
                print("")
                xox(f"{G}[+] TYPE NUMBER WITHOUT 0 EXAMPLE 3106217519")
                time.sleep(3)
                meta_data()
        done = []
        pk="pak"
        u1=f"{pk}siminfo.com"
        head = {
                "Host": u1,
                "Connection": "keep-alive",
                "Content-Length": "14",
                "Cache-Control": "max-age=0",
                "Upgrade-Insecure-Requests": "1",
                "Origin": f"https://{u1}",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": ua,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Referer": f"https://{u1}/search-pro.php",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9"
        }

        dataa = {
                "num": number
        }
        #dividing link safe from strings chor
        u2="result"
        sz = requests.post(f"https://{u1}/search-{u2}-pro.php",headers=head,data=dataa)
        soup = BeautifulSoup(sz.text, 'html.parser')
        # searching by class tags
        s = soup.find_all('td', {'class':'tg-iu1i'}) #number 1,2
        s1 = soup.find_all('td', {'class':'tg-de5r'}) #name 1,2
        s2 = soup.find_all('td', {'class':'tg-xfje'}) #cnic 1,2
        s3 = soup.find_all('td', {'class':'tg-wgsn'}) #address 1,2
        for szs in range(15):
                pic="freepicccs"
                o1=f"{pic}.com"
                if str("to search this number") in soup.text:
                        headers = {
                                "Host": o1,

                                "Connection": "keep-alive",
                                "Content-Length": "16",
                                "Cache-Control": "max-age=0",
                                "Upgrade-Insecure-Requests": "1",
                                "Origin": f"https://{o1}/",
                                "Content-Type": "application/x-www-form-urlencoded",
                                "User-Agent": ua,
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "Referer": f"https://{o1}/",
                                "Accept-Encoding": "gzip, deflate",
                                "Accept-Language": "en-US,en;q=0.9"
                        }

                        data = {
                                'cnnum': number
                        }

                        sz2 = requests.post(f'https://{o1}/search-result2.php', headers=headers, data=data)
                        # soup2 = BeautifulSoup(sz2.text, 'html.parser')
                        sk = re.findall('<div(.*?)</table>',str(sz2.content))
                        s22 = re.findall('<strong>(.*?)</strong>', str(sk))
                        if str(f"Record {szs+1}") in str(sk):
                                print(f"\n{G}[+] " + str(szs + 1) + " RECORD ")
                                print("")
                                print(f"{Y}[✓] NAME    :{G} {s22[2]}")
                                print(f"{Y}[✓] NUMBER  :{G} {s22[0]}")
                                print(f"{Y}[✓] CNIC    :{G} {s22[3]}")
                                print(f"{Y}[✓] ADDRESS :{G} {s22[4]}")
                                print(f"{Y}[✓] DATE    :{G} {s22[1]}")
                                done.append("done")
                                break
                if str(f"{szs+1}.") in soup.text:
                        print(f"\n{G}[+] "+str(szs+1)+" RECORD ")
                        print("")
                        print(f"{Y}[✓] NAME    :{G} {s1[szs].text}")
                        print(f"{Y}[✓] NUMBER  :{G} {s[szs].text}")
                        print(f"{Y}[✓] CNIC    :{G} {s2[szs].text}")
                        print(f"{Y}[✓] ADDRESS :{G} {s3[szs].text}")
                        done.append("done")
                else:
                        pass
        if str("done") in done:
                print("")
                input(f"{G}[+] PRESS ENTER TO BACK ")
                meta_data()

        else:
                print("")
                xox(f"{R}[×] THIS NUMBER DATA NOT FOUND")
                time.sleep(2)
                meta_data()
main()
