# Author            : Rizky Nurahman
# Source Get Token  : Dapunta Kx
# Script Created In : 17-Oktober-2023


# --> Module
import os
import re
import sys
import time
import json
import random
import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs


# --> CallBack
id_member = []
id_publik = []
times = datetime.now()
name_file = '%s-%s-%s.txt'%(times.hour,times.month,times.year) 


# --> Clear
def clear():
	if "win" in sys.platform.lower():
		os.system('cls')
	else:
		os.system('clear')


# --> Banner
def banner():
	clear()
	print("┏┓┏┓┳┳┓   ┓\n ┃┃ ┃┃┃┏┓┏┫       © 2023\n┗┛┗┛┛ ┗┗┛┗┻       by XMod\n")


# --> Menu
def menu():
	banner()
	data = auth().check()
	print('Hello   : %s'%(data[0]))
	print('Your Id : %s\n'%(data[1]))
	print('1. Dump Id Friendlist   [ Graphfb ]')
	print('2. Dump Id Followers    [ Graphfb ]')
	print('3. Dump Id Group Member [ Graphql ]')
	pilih = input('Pilih : ')
	if pilih in ['01','1','a']:
		dump().friends()
	elif pilih in ['02','2','b']:
		dump().followers()
	elif pilih in ['03','3','c']:
		dump().groups()
	else:
		pass


# --> Class Auth
class auth:
	def __init__(self):
		try:
			self.cookie = {'cookie': open('DATA/account/.cookie.txt','r').read()}
			self.token_eaag = open('DATA/account/.token-eaag.txt','r').read()
			self.token_eaat = open('DATA/account/.token-eaat.txt','r').read()
		except:
			print('Data Account Not Definned, Wait To Login')
			time.sleep(3);self.login()

	# --> Check Account
	def check(self):
		try:
			get = requests.get('https://graph.facebook.com/v18.0/me?fields=id,name&access_token='+self.token_eaag, cookies=self.cookie)
			name = json.loads(get.text)['name']
			ids = json.loads(get.text)['id']
			return name,ids
		except requests.ConnectionError:
			print('No Internet');exit()
		except:
			print('Failled Check Account, Wait To Login')
			time.sleep(3);self.login()

	# --> Login
	def login(self):
		try:
			banner()
			cook = input('Input Cookies : ')
			cookie = {'cookie': cook}
			open('DATA/account/.cookie.txt', 'w').write(cook)
			with requests.Session() as rsn:
				# --> Get Token Eaat
				try:
					data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
					post = rsn.post('https://graph.facebook.com/v18.0/device/login/',data=data).json()
					code, user_code = post['code'], post['user_code']
					url = 'https://graph.facebook.com/v18.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(code)
					get = bs(rsn.get('https://mbasic.facebook.com/device',cookies=cookie).content,'html.parser')
					form = get.find('form',{'method':'post'})
					data1 = {'jazoest'   : re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),'fb_dtsg'   : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form)).group(1),'qr'        : '0','user_code' : user_code}
					url1 = 'https://mbasic.facebook.com' + form['action']
					post1 = bs(rsn.post(url1,data=data1,cookies=cookie).content,'html.parser')
					data2 = {}
					form1 = post1.find('form',{'method':'post'})
					for x in form1('input',{'value':True}):
						try:
							if x['name'] == '__CANCEL__' :
								pass
							else:
								data2.update({x['name']:x['value']})
						except Exception as e:
							pass
					url2 = 'https://mbasic.facebook.com' + form1['action']
					pos = bs(rsn.post(url2,data=data2,cookies=cookie).content,'html.parser')
					get_token = rsn.get(url,cookies=cookie).json()
					token = get_token['access_token']
					open('DATA/account/.token-eaat.txt', 'w').write(token)
				except:
					print('Failled Get Token EAAT')

				# --> Get Token Eaag
				try:
					get_token_eaag = rsn.get('https://business.facebook.com/business_locations',cookies=cookie)
					token_eaag = re.search('(\["EAAG\w+)', get_token_eaag.text).group(1).replace('["','')
					open('DATA/account/.token-eaag.txt', 'w').write(token_eaag)
					print('Login Succes')
				except:
					print('Failled Get Token EAAG')
				exit()

		except Exception as e:
			print('Login Failled')
			exit()



# --> Class Dump Id
class dump:
	def __init__(self):
		try:
			self.cookie = {'cookie': open('DATA/account/.cookie.txt', 'r').read()}
			self.token_eaat = open('DATA/account/.token-eaat.txt', 'r').read()
			self.token_eaag = open('DATA/account/.token-eaag.txt', 'r').read()
		except:
			print('Data Account Not Definned, Wait To Login')
			time.sleep(3);auth().login()

	# --> Dump Friends
	def friends(self):
		try:
			target_id = input('Input Id Target : ')
			type_dump = input('Infinity Dump !, y/t ? : ')
			get = requests.get('https://graph.facebook.com/%s?fields=friends&access_token=%s'%(target_id, self.token_eaat), cookies=self.cookie).json()
			for x in get['friends']['data']:
				try:
					user_id, user_name = x['id'], x['name']
					id_publik.append(user_id)
					open('DATA/result/%s.text'%(target_id),'a').write(user_id+'|'+user_name+'\n')
					print('\rSucces Dump %s User '%(len(id_publik)),end='')
				except:pass

			if type_dump in ['y','1']:
				while True:
					try:
						get1 = requests.get('https://graph.facebook.com/%s?fields=friends&access_token=%s'%(random.choice(id_publik), self.token_eaat), cookies=self.cookie).json()
						for x in get1['friends']['data']:
							try:
								if x['id'] in id_publik:
									pass
								else:
									user_id, user_name = x['id'], x['name']
									id_publik.append(user_id)
									open('DATA/result/%s.text'%(target_id),'a').write(user_id+'|'+user_name+'\n')
									print('\rSucces Dump %s User '%(len(id_publik)),end='')
							except:pass
					except:
						pass

			print('\nSucces Dump Id, File Save In DATA/result/%s.txt'%(target_id))
		except requests.ConnectionError:
			print('No Internet Connection !');exit()

		except:
			print('Failled Dump ID');exit()

	# --> Dump Followers
	def followers(self):
		try:
			target_id = input('Input Id Target : ')
			get = requests.get('https://graph.facebook.com/%s/subscribers?limit=10000&access_token=%s'%(target_id, self.token_eaag), cookies=self.cookie).json()
			data = []
			for x in get['data']:
				try:
					user_id, user_name = x['id'], x['name']
					data.append(user_id+'|'+user_name)
					open('DATA/result/%s.text'%(target_id),'a').write(user_id+'|'+user_name+'\n')
					print('\rSucces Dump %s User '%(len(data)),end='')
				except:pass
			print('\nSucces Dump Id, File Save In DATA/result/%s.txt'%(target_id))
		except requests.ConnectionError:
			print('No Internet Connection !')
			exit()
		except:
			print('Failled Dump ID')

	# --> Dump Member Group
	def groups(self):
		try:
			target_id = input('Input Id Target : ')
			with requests.Session() as session:
				session.headers.update({'authority': 'www.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9,id;q=0.8', 'cache-control': 'no-cache', 'dpr': '1', 'pragma': 'no-cache', 'sec-ch-prefers-color-scheme': 'dark', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '""', 'sec-ch-ua-platform': '"Linux"', 'sec-ch-ua-platform-version': '"6.4.0"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36', 'viewport-width': '415'})
				get = session.get('https://www.facebook.com/groups/%s/members'%(target_id), cookies=self.cookie).text
				user = re.search('"ACCOUNT_ID":"(.*?)"', get).group(1)
				haste = re.search('"haste_session":"(.*?)"', get).group(1)
				client = re.search('"client_revision"\:(.*?)\,', get).group(1)
				spin_r = re.search('"__spin_r"\:(.*?)\,', get).group(1)
				spin_t = re.search('"__spin_t"\:(.*?)\,', get).group(1)
				hsi = re.search('"hsi":"(.*?)"', get).group(1)
				dtsg = re.search('"DTSGInitialData"\,\[\]\,{"token":"(.*?)"', get).group(1)
				lsd = re.search('"LSD"\,\[\]\,{"token":"(.*?)"', get).group(1)
				jazoest = re.search('jazoest=(.*?)"', get).group(1)
				cursor = re.search('"has_next_page":true,"end_cursor":"(.*?)"', get).group(1)
				self.get_members(user=user,haste=haste,client=client,spin_r=spin_r,spin_t=spin_t,hsi=hsi,dtsg=dtsg,lsd=lsd,jazoest=jazoest,cursor=cursor,target_id=target_id)
		except Exception as e:
			print('Failled Get Groups Info')

    # --> Get List Member
	def get_members(self, **kwargs):
		try:
			with requests.Session() as session:
				post = session.post('https://www.facebook.com/api/graphql/',
					headers = {
						'authority': 'www.facebook.com',
						'accept': '*/*',
						'accept-language': 'en-US,en;q=0.9,id;q=0.8',
						'cache-control': 'no-cache',
						'content-type': 'application/x-www-form-urlencoded',
						'dpr': '1',
						'origin': 'https://www.facebook.com',
						'pragma': 'no-cache',
						'referer': 'https://www.facebook.com/groups/305740434613408/members',
						'sec-ch-prefers-color-scheme': 'dark',
						'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
						'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"',
						'sec-ch-ua-mobile': '?0',
						'sec-ch-ua-model': '""',
						'sec-ch-ua-platform': '"Linux"',
						'sec-ch-ua-platform-version': '"6.4.0"',
						'sec-fetch-dest': 'empty',
						'sec-fetch-mode': 'cors',
						'sec-fetch-site': 'same-origin',
						'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
						'viewport-width': '415',
						'x-asbd-id': '129477',
						'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
						'x-fb-lsd': kwargs['lsd']
					},
					data = {
						'av': kwargs['user'],
						'__user': kwargs['user'],
						'__a': '1',
						'__req': 'm',
						'__hs': kwargs['haste'],
						'dpr': '1',
						'__ccg': 'MODERATE',
						'__rev': kwargs['client'],
						'__s': '',
						'__hsi': kwargs['hsi'],
						'__dyn': '',
						'__csr': '',
						'__comet_req': '15',
						'fb_dtsg': kwargs['dtsg'],
						'jazoest': kwargs['jazoest'],
						'lsd': kwargs['lsd'],
						'__aaid': '0',
						'__spin_r': kwargs['spin_t'],
						'__spin_b': 'trunk',
						'__spin_t': kwargs['spin_t'],
						'qpl_active_flow_ids': '431626709',
						'fb_api_caller_class': 'RelayModern',
						'fb_api_req_friendly_name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
						'variables': '{"count":10,"cursor":"%s","groupID":"%s","recruitingGroupFilterNonCompliant":false,"scale":1,"id":"%s"}'%(kwargs['cursor'], kwargs['target_id'], kwargs['target_id']),
						'server_timestamps': 'true',
						'doc_id': '7093752180659727'
					}, cookies=self.cookie).json()

				for i in post['data']['node']['new_members']['edges']:
					id_member.append(i['node']['id']+'|'+i['node']['name'])
					open('DATA/result/%s.text'%(kwargs['target_id']),'a').write(i['node']['id']+'|'+i['node']['name']+'\n')
					print('\rSucces Dump %s User '%(len(id_member)),end='')

				try:
					cursor = post['data']['node']['new_members']['page_info']['end_cursor']
					self.get_members(user=kwargs['user'],haste=kwargs['haste'],client=kwargs['client'],spin_r=kwargs['spin_r'],spin_t=kwargs['spin_t'],hsi=kwargs['hsi'],dtsg=kwargs['dtsg'],lsd=kwargs['lsd'],jazoest=kwargs['jazoest'],cursor=cursor,target_id=kwargs['target_id'])
				except Exception as e:
					pass

		except Exception as e:
			print('Failled Dump Id')


# --> Running
if __name__=='__main__':
	try:
		os.listdir('DATA')
	except:
		os.system('mkdir DATA')
		os.system('mkdir DATA/account')
		os.system('mkdir DATA/result')

	menu()