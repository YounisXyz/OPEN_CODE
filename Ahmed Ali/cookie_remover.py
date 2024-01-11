"""
console.log("Written By Ahmed Ali");
"""

import sys

def remove_cookies():
    print("-"*54+"\nCookie remover\nMade By Ahmed Ali\n"+"-"*54)

    input_file_path = input("Input file path : ")
    try:
        information = open(input_file_path,"r").read().splitlines()
    except FileNotFoundError:
        sys.exit("File not found")

    output_file_path = input("Output file path : ")

    for data in information:
        if data == "":
            break
        try:
            uid,password,cookie = data.split("|")
        except ValueError:
            sys.exit("Ids must be in uid|password|cookie format")
        open(output_file_path,"a").write(f"{uid}|{password}\n")

    sys.exit("SUCCESSFULL")

remove_cookies()
