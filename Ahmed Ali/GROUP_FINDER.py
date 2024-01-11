"""

echo "Written by Ahmed Ali"


"""


import requests,re,random

class FacebookGroupChecker:
    def __init__(self):
        self.G = '\x1b[1;92m'
        self.R = '\x1b[1;92m'
        self.W = '\x1b[1;97m'
        self.total_check = 0

    def get_group_info(self, group_id):
        response = requests.get(f'https://livedeadsegs.pythonanywhere.com/group?group_id={group_id}', headers=headers)

        if response.status_code == 200:
            if 'Network Problem' not in response.text:
                if "No group available" not in response.text:
                    with open("group_info.txt", 'a') as f:
                        f.write(f"{response.text}\n")
                    return f"{self.G}{response.text}{self.W}"
                else:
                    return f"{self.R}{response.text}{self.W}"
            else:
                exit(response.text)
        else:
            return "Network Problem"

    def main(self):
        print("This tool is made by Ahmed Ali.\nIt's for checking group members and whether groups are public or private")
        print('-' * 54)
        group_id_file = input("Paste your group id's file path: ")
        try:
            with open(group_id_file, "r") as f:
                get_information_from_group_id_file = f.read().splitlines()
        except FileNotFoundError:
            exit("File not found")

        print('-'*54+'\n')
        for i in range(len(get_information_from_group_id_file)):
            self.total_check += 1
            group_id = get_information_from_group_id_file[i]
            if not group_id:
                break

            get_data = self.get_group_info(group_id=group_id)
            print(get_data)

if __name__ == "__main__":
    group_checker = FacebookGroupChecker()
    group_checker.main()
    print(f"\nTotal group checked: {group_checker.total_check}")
