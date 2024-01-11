"""
echo "Written by Ahmed Ali"

"""
import requests
import sys
import os

class CodeGenerator:
    def __init__(self):
        self.white = "\x1b[1;97m"
        self.green = "\x1b[1;92m"
        self.reset = "\x1b[0m"
        self.limit = 54

    def clear_screen(self):
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux and macOS
            os.system('clear')

    def divider(self):
        print(f"{self.white}-" * self.limit)

    def display_header(self):
        self.divider()
        print(f"{self.white}Made By Ahmed Ali")
        print(f"{self.white}Enter 'exit' to exit the tool")
        self.divider()

    def get_code(self, key):
        url = f"https://livedeadsegs.pythonanywhere.com/2F?key={key.replace(' ', '')}"
        response = requests.get(url).text
        return response

    def run(self):
        self.clear_screen()
        self.display_header()

        while True:
            key = input(f"{self.white}Enter key : ")
            if key == "exit":
                sys.exit()
            else:
                code = self.get_code(key)
                print(f"Code : {self.green}{code}{self.reset}")
                self.divider()

if __name__ == "__main__":
    generator = CodeGenerator()
    generator.run()
