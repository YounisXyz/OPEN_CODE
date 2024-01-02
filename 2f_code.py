
import requests
import sys
import os
import time

R = "\033[1;91m"
P = "\033[1;97m"
H = "\033[1;92m"
reset = "\x1b[0m"

class Code:
    def __init__(self):
        self.l = 54

    def clear(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system("clear")

    def divider(self):
        print(f"{P}-" * self.l)

    def display_header(self):
        self.divider()
        print(f"{P}THE 2FA CODE GENERATOR")
        print(f"{P}MADE BY GARRYX")
        self.divider()

    def get_code(self, key):
        url = f"https://livedeadsegs.pythonanywhere.com/2F?key={key.replace(' ','')}"
        response = requests.get(url).text
        return response

    def run(self):
        self.clear()
        self.display_header()
        while True:
            key = input(f"{P}Enter Key: ")
            if key == "":
            	print(f"{R}Do Not Empty!");time.sleep(2);generator.run()
            if key == "none":
                sys.exit()
            else:
                code = self.get_code(key)
                print(f"Code: {H}{code}{reset}")
                self.divider()

if __name__ == "__main__":
    generator = Code()
    generator.run()