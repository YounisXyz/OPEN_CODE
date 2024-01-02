# -*- coding: utf-8 -*-
 
import os
import time
import requests
import json
import sys
 
threads = """
   ___ _______        ___ ______  _______ _______
  |   |   _   |______|   |   _  \|   _   |   _   |
  |.  |.  1   |______|.  |.  |   |.  1___|.  |   |
  |.  |.  ____|      |.  |.  |   |.  __) |.  |   |
  |:  |:  |          |:  |:  |   |:  |   |:  1   |
  |::.|::.|          |::.|::.|   |::.|   |::.. . |
  `---`---'          `---`--- ---`---'   `-------'
---------------------------------------------------
 Author : Muhammad Younis
 Github : https://github.com/YounisXyz
 Fb : https://www.facebook.com/xyzhackers
-------------------------------------------------
"""
 
class ip_info(object):
    def __init__(self) -> None:
        os.system("clear")
        print(threads)
        print(" [1] Get information own your ipaddress")
        print(" [2] Get information custom anyuser ipaddress")
        print(" [3] Exit")
        print()
        self.main = input(" select an option :- ")
        if "1" in self.main:
            os.system("clear")
            print(threads)
            self.here = requests.get("http://ip-api.com/json/")
            self.recorde = self.here.json()
            print("\t IPADDRESS LOOKUP INFORMATION ")
            time.sleep(1)
            print()
            print(" Ipaddress :- "+self.recorde["query"])
            time.sleep(0.05)
            print(" Status :- "+self.recorde["status"])
            time.sleep(0.05)
            print(" Country :- "+self.recorde["country"])
            time.sleep(0.05)
            print(" Country Code :- "+self.recorde["countryCode"])
            time.sleep(0.05)
            print(" Region :- "+self.recorde["regionName"])
            time.sleep(0.05)
            print(" City :- "+self.recorde["city"])
            time.sleep(0.05)
            exit()
        elif "2" in self.main:
            os.system("clear")
            print(threads)
            self.here = str(input(" enter Ipaddress :- "))
            self.ips = requests.get("http://ip-api.com/json/"+self.here)
            self.recorde = self.ips.json()
            print()
            print("\t IPADDRESS LOOKUP INFORMATION ")
            time.sleep(1)
            print()
            print(" Ipaddress :- "+self.recorde["query"])
            time.sleep(0.05)
            print(" Status :- "+self.recorde["status"])
            time.sleep(0.05)
            print(" Country :- "+self.recorde["country"])
            time.sleep(0.05)
            print(" Country Code :- "+self.recorde["countryCode"])
            time.sleep(0.05)
            print(" Region :- "+self.recorde["regionName"])
            time.sleep(0.05)
            print(" City :- "+self.recorde["city"])
            time.sleep(0.05)
            exit()
        elif "3" in self.main:
            exit()
        else:
            print()
            print("\tFuck! Please select an valid option duddy :)")
            time.sleep(3)
            ip_info()
 
if __name__ == '__main__':
    class version(object):
        def __init__(self) -> None:
            os.system("clear")
            if sys.version_info>(3,9):
                print()
                ip_info()
            elif sys.version_info<(3,9):
                os.system("clear")
                sys.stderr.write(" your are too old python version!\n");time.sleep(1)
                sys.stderr.write(" Please upgrade lastest python version\n");time.sleep(1)
                sys.stderr.write(" contact admin : https://www.facebook.com/xyzhackers\n");time.sleep(1)
                pass
            else:
                print()
                print("\t This project is only support python3")
                time.sleep(2)
                version()
                pass
            pass
    version()
   #feel me more :)
 