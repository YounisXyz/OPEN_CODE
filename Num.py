#Coding:utf-8
#Code By : MR.AKING
#Github : AKING10
#Facebook : MR.AKING.007
#Enjoy The Code Love You All ❤️‍🩹
'------------------------------'
logo = f'''\033[1;37m  ____  _____  ____    ____  ______   _______     
 |_   \|_   _||_   \  /   _||_   _ \ |_   __ \    
   |   \ | |    |   \/   |    | |_) |  | |__) |   
   | |\ \| |    | |\  /| |    |  __'.  |  __ /    
  _| |_\   |_  _| |_\/_| |_  _| |__) |_| |  \ \_  
 |_____|\____||_____||_____||_______/|____| |___| \n{50*"-"}
 Author : MR.AKING\n Github : AKING110 \n Fcbook : MR.AKING.007 \n Enjoy Free Number Details Script '''
try:
    import os,requests,re
    from bs4 import BeautifulSoup
    from bs4 import BeautifulSoup as parser
except ModuleNotFoundError:
    print('\n installing modules ...')
    os.system('pip install requests bs4 > /dev/null')
def main():
        os.system("clear")
        print(logo)
        print(50*'-')
        print(' [1] \033[;32mGet Jazz Number Data\033[;37m \n [2] \033[;33mGet Zong Number Data\033[;37m \n [3] \033[;34mGet Warid Number Data\033[;37m \n [4] \033[;35mGet Telenor Number Data\033[;37m \n [5] \033[;36mGet Ufone Number Data\033[;37m \n [6] \033[;37mGet Cinc Number Data\033[;37m \n \033[;37m[0] \033[;31mExit Menu \033[;37m')
        print(50*'-')
        xd = input(' Choose : ')
        if xd =='1':
            jazz()
        elif xd =='2':
            zong()
        elif xd =='3':
            warid()
        elif xd =='4':
            telenor()
        elif xd =='5':
            ufone()
        elif xd =='6':
            cinc()
        elif xd =='0':
            exit(' Thanks for use ')
        else:
            exit(' Option Not in menu ')
def cinc():
    os.system('clear')
    print(logo)
    nmbr = input(f"{50*'-'}\n Put Cinc Number :\033[1;32m ")
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36', 'Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'cnnum': nmbr}
    url = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=data)
    dta = re.findall("\<div(.*?)</table>",str(url.text))
    open(".tt1.txt","w").write(str(dta))
    ndt = open(".tt1.txt","r").read()
    ndt = ndt.replace("</strong>","<strong>")
    ndt = ndt.split("<strong>")
    try:
        print(50*"\033[1;37m-")
        try:print(f" \033[1;37mCinc Num  : \033[1;32m{ndt[5]}")
        except:pass
        try:print(f"\033[1;37m Name.     : \033[1;33m{ndt[3].lower()}")
        except:pass
        try:print(f"\033[1;37m Issue Date : \033[1;34m{ndt[7]}")
        except:pass
        try:print(f"\033[1;37m Birthday  : \033[1;34m{ndt[13]}")
        except:pass
        try:print(f'\033[1;37m City Name : \033[1;33m{ndt[27]}')
        except:pass
        try:print(f"\033[1;37m Address 1 : \033[1;35m{ndt[9].lower()}")
        except:pass
        try:print(f"\033[1;37m Address 2 : \033[1;31m{ndt[23].lower()}")
        except:pass
        try:print(f"\033[1;37m Address 3 : \033[1;32m{ndt[25].lower()}")
        except:pass
        try:print(f"\033[1;37m Address 4 : \033[1;34m{ndt[43].lower()}")
        except:pass
        try:print(f"\033[1;37m Number  1 : \033[1;35m{ndt[1]}")
        except:pass
        try:print(f"\033[1;37m Number  2 : \033[1;34m{ndt[11]}")
        except:pass
        try:print(f"\033[1;37m Number  3 : \033[1;33m{ndt[29]}")
        except:pass
        try:print(f"\033[1;37m Number  4 : \033[1;36m{ndt[37]}")
        except:pass
        print(50*'\033[1;37m-')
    except:
        print(' Sorry Data not Found ')
    input('\033[0m Press enter for run ')
    main()
def jazz():
    os.system('clear')
    print(logo)
    num = input(f"{50*'-'}\n Put Jazz Number :\033[1;32m ")
    if num[0] == '0':
        nmbr = num.replace("03","3")
    else:
        nmbr = num
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36', 'Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'cnnum': nmbr}
    url = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=data)
    dta = re.findall("\<div(.*?)</table>",str(url.text))
    open(".tt1.txt","w").write(str(dta))
    ndt = open(".tt1.txt","r").read()
    ndt = ndt.replace("</strong>","<strong>")
    ndt = ndt.split("<strong>")
    try:
        print(50*"\033[1;37m-")
        try:print(f" \033[1;37mNumber   : \033[1;32m{ndt[9]}")
        except:pass
        try:print(f"\033[1;37m Name.    : \033[1;33m{ndt[1].lower()}")
        except:pass
        try:print(f"\033[1;37m Birthday : \033[1;34m{ndt[15]}")
        except:pass
        try:print(f"\033[1;37m Address  : \033[1;35m{ndt[3].lower()}")
        except:pass
        try:print(f"\033[1;37m Cnic Num : \033[1;36m{ndt[11]}")
        except:pass
        print(50*'\033[1;37m-')
    except:
        print(' Sorry Data not Found ')
    input('\033[0m Press enter for run ')
    main()
def zong():
    os.system('clear')
    print(logo)
    num = input(f"{50*'-'}\n Put Zong Number :\033[1;32m ")
    if num[0] == '0':
        nmbr = num.replace("03","3")
    else:
        nmbr = num
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36', 'Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'cnnum': nmbr}
    url = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=data)
    dta = re.findall("\<div(.*?)</table>",str(url.text))
    open(".tt1.txt","w").write(str(dta))
    ndt = open(".tt1.txt","r").read()
    ndt = ndt.replace("</strong>","<strong>")
    ndt = ndt.split("<strong>")
    try:
        print(50*"\033[1;37m-")
        try:print(f" \033[1;37mNumber   : \033[1;32m{ndt[1]}")
        except:pass
        try:print(f"\033[1;37m Name.    : \033[1;33m{ndt[5].lower()}")
        except:pass
        try:print(f"\033[1;37m Birthday : \033[1;34m{ndt[3]}")
        except:pass
        try:print(f"\033[1;37m Address  : \033[1;35m{ndt[9].lower()}")
        except:pass
        try:print(f"\033[1;37m Cnic Num : \033[1;36m{ndt[7]}")
        except:pass
        print(50*'\033[1;37m-')
    except:
        print(' Sorry Data not Found ')
    input('\033[0m Press enter for run ')
    main()
def warid():
    os.system('clear')
    print(logo)
    num = input(f"{50*'-'}\n Put Warid Number :\033[1;32m ")
    if num[0] == '0':
        nmbr = num.replace("03","3")
    else:
        nmbr = num
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36', 'Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'cnnum': nmbr}
    url = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=data)
    dta = re.findall("\<div(.*?)</table>",str(url.text))
    open(".tt1.txt","w").write(str(dta))
    ndt = open(".tt1.txt","r").read()
    ndt = ndt.replace("</strong>","<strong>")
    ndt = ndt.split("<strong>")
    try:
        print(50*"\033[1;37m-")
        try:print(f" \033[1;37mNumber   : \033[1;32m{ndt[1]}")
        except:pass
        try:print(f"\033[1;37m Name.    : \033[1;33m{ndt[3].lower()}")
        except:pass
        try:print(f"\033[1;37m Birthday : \033[1;34m{ndt[7]}")
        except:pass
        try:print(f"\033[1;37m Address  : \033[1;35m{ndt[9].lower()}")
        except:pass
        try:print(f"\033[1;37m Cnic Num : \033[1;36m{ndt[5]}")
        except:pass
        print(50*'\033[1;37m-')
    except:
        print(' Sorry Data not Found ')
    input('\033[0m Press enter for run ')
    main()
def telenor():
    os.system('clear')
    print(logo)
    num = input(f"{50*'-'}\n Put Telenor Number :\033[1;32m ")
    if num[0] == '0':
        nmbr = num.replace("03","3")
    else:
        nmbr = num
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36', 'Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'cnnum': nmbr}
    url = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=data)
    dta = re.findall("\<div(.*?)</table>",str(url.text))
    open(".tt1.txt","w").write(str(dta))
    ndt = open(".tt1.txt","r").read()
    ndt = ndt.replace("</strong>","<strong>")
    ndt = ndt.split("<strong>")
    try:
        print(50*"\033[1;37m-")
        try:print(f" \033[1;37mNumber   : \033[1;32m{ndt[1]}")
        except:pass
        try:print(f"\033[1;37m Name.    : \033[1;33m{ndt[5].lower()}")
        except:pass
        try:print(f"\033[1;37m Address  : \033[1;35m{ndt[9].lower()}")
        except:pass
        try:print(f"\033[1;37m Cnic Num : \033[1;36m{ndt[7]}")
        except:pass
        print(50*'\033[1;37m-')
    except:
        print(' Sorry Data not Found ')
    input('\033[0m Press enter for run ')
    main()
def ufone():
    os.system('clear')
    print(logo)
    num = input(f"{50*'-'}\n Put Ufone Number :\033[1;32m ")
    if num[0] == '0':
        nmbr = num.replace("03","3")
    else:
        nmbr = num
    head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36', 'Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'cnnum': nmbr}
    url = requests.post('https://freepicccs.com/search-result2.php',headers=head,data=data)
    dta = re.findall("\<div(.*?)</table>",str(url.text))
    open(".tt1.txt","w").write(str(dta))
    ndt = open(".tt1.txt","r").read()
    ndt = ndt.replace("</strong>","<strong>")
    ndt = ndt.split("<strong>")
    try:
        print(50*"\033[1;37m-")
        try:print(f" \033[1;37mNumber   : \033[1;32m{ndt[1]}")
        except:pass
        try:print(f"\033[1;37m Name.    : \033[1;33m{ndt[5].lower()}")
        except:pass
        try:print(f"\033[1;37m Birthday : \033[1;34m{ndt[3]}")
        except:pass
        try:print(f"\033[1;37m City Name: \033[1;35m{ndt[9].lower()}")
        except:pass
        try:print(f"\033[1;37m Cnic Num : \033[1;36m{ndt[11]}")
        except:pass
        print(50*'\033[1;37m-')
    except:
        print(' Sorry Data not Found ')
    input('\033[0m Press enter for run ')
    main()
main()
