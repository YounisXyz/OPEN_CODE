# decompyle3 version 3.3.2
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.10.2 (main, Mar  1 2022, 12:58:00) [Clang 12.0.8 (https://android.googlesource.com/toolchain/llvm-project c935d99d7
# Compiled at: 2020-07-16 04:45:22
# Size of source mod 2**32: 543 bytes
import os
try:
    os.mkdir('/data/data/com.termux/files/home/termux_properties')
except OSError:
    pass
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

import requests, os, re, bs4, platform, sys, json, time, random, datetime, subprocess, threading, itertools, base64, uuid, zlib
import concurrent.futures as qaiserabba
from datetime import datetime
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
import platform
import concurrent.futures as ThreadPool
ct = datetime.now()
month = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']


current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

P = '\x1b[1;97m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;97m'
B = '\x1b[1;97m'
U = '\x1b[1;97m'
O = '\x1b[1;97m'
N = '\x1b[0m'
my_color = [P,
 M, H, K, B, U,
 O, N]
warna = random.choice(my_color)
data, data2 = {}, {}
aman, cp, salah = (0, 0, 0)
ubahP, fuck, pwBaru = [], [], []
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = 'https://lookup-id.com/'
url_mb = 'https://m.facebook.com'
url_ip = 'https://www.httpbin.org/ip'
header_grup = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'}
bulan_ttl = {'01':'January',  '02':'February',
 '03':'March',  '04':'April',
 '05':'May',  '06':'June',  '07':'July',  '08':'Augustus',  '09':'September',  '10':'October',
 '11':'November',  '12':'December'}
done = False
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20','21']
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth':repr(bd),  'x-fb-sim-hni':repr(sim),
 'x-fb-net-hni':repr(sim),  'x-fb-connection-quality':'EXCELLENT',  'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3',
 'x-fb-connection-type':'unknown',  'content-type':'application/x-www-form-urlencoded',  'x-fb-http-engine':'Liger'}
urlxnxx = 'https://mbasic.facebook.com'

if os.path.exists('.oun.txt'):
    open('.oun.txt', 'w').close()

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def login():
    os.system('clear')
    print(logo)
    tok = input('  Token Here : ')
    if 'EAAB' not in tok:
        jalan('\x1b[1;91mToken is not valid for File Creating\x1b[0m')
        input('Press Enter To See Video For Token : ')
        os.system('xdg-open https://youtu.be/6PitUufz2TY')
        caseher()
        os.sys.exit()
    try:
        u = requests.get('https://graph.facebook.com/me?access_token=' + tok).text
        u1 = json.loads(u)
        name = u1['name']
        ts = open('access_token.txt', 'w')
        ts.write(tok)
        ts.close()
        print('\n \x1b[1;92msuccessfully\x1b[0m')
        time.sleep(1)
        caseher()
    except KeyError:
        print('\n Token Invalid Bro ')
        time.sleep(1)
        login()

logo = '   \n\n   .d88888b.   .d8888b.  8888888b.       \n  d88P" "Y88b d88P  Y88b 888   Y88b      \n  888     888 Y88b.      888    888      \n  888     888  "Y888b.   888   d88P      \n  888     888     "Y88b. 8888888P"       \n  888 Y8b 888       "888 888 T88b        \n  Y88b.Y8b88P Y88b  d88P 888  T88b       \n   "Y888888"   "Y8888P"  888   T88b      \n         Y8b\n\x1b[1;97m===========================================\n\x1b[1;32mADMIN\x1b[0m ! QAISER \x1b[1;91m & \x1b[0m \x1b[1;92mTOOL\x1b[0m ! PAID \x1b[1;91m & \x1b[0m \x1b[1;92mV\x1b[0m = 3\n\x1b[1;97m===========================================    '

def hasil(OK,cp):
        if not len(OK) != 0:
            pass
        if len(cp) != 0:
            print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mSSB_OK.txt' % (H, P, str(len(ok))))
            print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mSSB_CP.txt' % (H, P, str(len(cp))))
            input("\x1b[1;97mPress enter to back SSB Menu ")
            sarfraz()

def caseher():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print('')
    print(' [1] Start File Cloning [Method-1-Basic]')
    print(' [2] Start File Cloning [Method-2-Local]')
    print(' [3] Public Cloning [Login-OK]')
    print(' [4] Random Cloning ')
    print(' [5] Create File')
    print(' [E] Exit ')
    print('')
    _caseher___ = input(' [?] Choose option : ')
    if _caseher___ in ('1','01'):
        __xxx__().caseherx(id)
    elif _caseher___ in ('2','02'):
        bootstrap()
        crack()
    elif _caseher___ in ('3','03'):
        __xnx__().caseherx(id)
    elif _caseher___ in ('4','04'):
        print('\nSoon Coming ★ ')
        time.sleep(2)
        caseher()
    elif _caseher___ in ('5','05'):
        create_file()
    elif _caseher___ in ('E','ee'):
        exit('Thanks For Using janu')
    else:
        jalan('        Invalid Select')
        time.sleep(1)
        caseher()

def create_file():
    os.system('clear')
    print(logo)

    time.sleep(1)
    os.system('clear')
    print(logo)
    os.system('clear')
    print(logo)
    time.sleep(0.5)
    print('  [1] Create file method 1.Mbasic')
    print('  [2] Create file method 2.Loclhst')
    print('============================================')
    cf = input(' Select : ')
    if cf == '1':
        autoo()
    elif cf == '2':
        autoo()
    elif cf == 'Bb' or cf == 'b' or 'cf' == 'B':
        caseher()
    else:
        print('\n  Choose correct option ...')
        time.sleep(1)
        create_file()

def autoo():
    os.system('rm -rf qssrrr1.txt')
    try:
        token = open('token.txt', 'r').read()
    except FileNotFoundError:
        ()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token).text
        q = json.loads(r)
        uname = q['name']
    except KeyError:
        ()
        os.system('clear')
    print(logo)
    os.system('rm -rf qssrrr1.txt')
    os.system('rm -rf qssrrr2.txt')
    nusrat = 0
    try:
        limit_user = int(input(' Total Ids To Add '))
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count += 1
        udit = input('  Put id%s: ' % count)
        try:
            token = open('token.txt', 'r').read()
            fr = requests.get('https://graph.facebook.com/' + udit + '/friends?access_token=' + token).text
            qfr = json.loads(fr)
            temp_save = open('qssrrr1.txt', 'a')
            for data in qfr["data"]:
                uids = data['id']
                if uids not in nusrat:
                    nusrat.append(uids)
                    temp_save.write(uids + '\n')
                    temp_save.close()
        except KeyError:
            pass
        if 'invalid' in str(fr):
            print('  Logged token has expired ...')
        else:
            print('Friend Is Private ' + udit)
    os.system('clear')
    print(logo)
    print('   Total ids')
    print('--------------------------------------------------')
    try:
        ask_link = 2
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed += 1
        li = input('  %s Link start with: ' % completed)
        os.system('cat qssrrr1.txt | grep "' + li + '" >> qssrrr2.txt')
    save_file = input('Example /sdcard/xxx.txt\n Save File As : ')
    os.system('clear')
    linesx = open('qssrrr22.txt', 'r').readlines()
    print(logo)
    print('  Ids to Dump : ' + str(len(linesx)))
    print('  Starting Process Wait ... ')
    print('============================================')
    fileid = 'qssrrr2.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            token = open('token.txt', 'r').read()
            rg = requests.get('https://graph.facebook.com/' + ids + '/friends?access_token=' + token).text
            rgq = json.loads(rg)
            idsave = open('/sdcard/' + save_file, 'a')
            for inayat in rgq["data"]:
                uids = inayat['id']
                dill.append(uids)
                nm = inayat['name']
                first_name = nm.split(' ')[0]
                try:
                    last_name = nm.split(' ')[1]
                except:
                    last_name = 'Khan'
                idsave.write(uids + '|' + first_name + '|' + last_name + '\n')
            print(' \x1b[1;92m Sucessfully Dump from ' + ids + '\x1b[0m')
            idsave.close()
        except Exception as e:
            try:
                if 'invalid' in str(rg):
                    print('  Token has expired, try again ...')
                    os.system('rm -rf qssrrr1.txt')
                else:
                    print('\x1b[1;92mError Friendlist Not Dump\x1b[0m')
                    os.system('rm -rf qssrrr1.txt')
            except:
                e = None
                del e
        lenid = open('/sdcard/' + save_file, 'r').readlines()
        print(' \x1b[0m Process Completed  ')
        os.system('rm -rf qssrrr*')
        print('  Total ids: ' + str(len(lenid)))
        print('  File saved as: ' + save_file)
        input('  Press enter to back ')
        caseher()

if os.path.exists('.qsrwork.txt'):
    open('.qsrwork.txt', 'w').close()


caseher()
