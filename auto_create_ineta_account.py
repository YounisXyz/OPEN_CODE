#SOURCE BY: Younis john
#Github : https://github.com/YounisXyz
#Facebook : https://www.facebook.com/xyzhackers
import requests,random,threading,json,sys
from string import ascii_letters, ascii_lowercase, digits
from datetime import datetime
from uuid import uuid4
import time as sleper
requests.packages.urllib3.disable_warnings()
class YounisXyz:
	def __init__(self):
		self.start_time = sleper.time()
		self.time = int(datetime.now().timestamp())
		Numbers = '123456789'
		self.chars = 'qwertyuiopasdfghjklzxcvbnm1234567890'
		self.length = random.randint(6,8)
		self.Created = 0
		self.Status = None
		self.password = ''.join(random.choice(ascii_letters + digits) for _ in range(random.randint(8, 14)))
		self.APPID = str("".join(random.choice(Numbers)for i in range(15)))
		self.year = random.randint(1990,1999)
		self.month = random.randint(1,12)
		self.day = random.randint(1,20)
		self.ig_did = str(uuid4()).upper()
	
	def SendToBot(self,message):
		try:
			with open('bot.json', 'r') as f:
				data = json.load(f)
				self.id = data['id']
				self.token = data['token']
				requests.post(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.id}&text={message}')
		except :
			pass
	
	def SetCookies(self):
		url = 'https://i.instagram.com/api/v1/public/landing_info/'
		headers  = {
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1'
		}
		Response = requests.get(url,headers=headers).cookies
		try:
			self.mid = Response['mid']
			self.csrftoken = Response['csrftoken']
			return True
		except:
			return False
	def CheckUsername(self):
		if YounisXyz.SetCookies():
			url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
			headers = {
				'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
				'X-IG-App-ID':f'{self.APPID}',
				'Content-Type':'application/x-www-form-urlencoded',
				'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
				'X-CSRFToken':f'{self.csrftoken}'
			}
			while True:
				self.username = str("".join(random.choice(self.chars)for i in range(self.length)))
				data = f'email=&username={self.username}&first_name=&opt_into_one_tap=false'
				response = requests.post(url,headers=headers,data=data)
				if 'username_is_taken' not in response.text and response.status_code == 200 :
					print('[1] Checking username')
					return True
					break
				else:
					print(f"Searching for available username")
	def CreateEmail(self):
		if YounisXyz.CheckUsername():
			url = 'https://api.internal.temp-mail.io/api/v3/email/new'
			headers = {
			'User-Agent':'Temp%20Mail/30 CFNetwork/1220.1 Darwin/20.3.0',
			'Content-Type':'application/json'
			}
			data = {
			"min_name_length" : 5,
			"max_name_length" : 7
			}
			try:
				response = requests.post(url,headers=headers,json=data,verify=False)
				if 'email' in response.text:
					self.email = response.json()['email']
 
					print('[2] Creating Email')				
					return True
				else:
					return False
			except Exception as e :
				print(e)
				return False
		else:
			print('Missing Cookies ')
	def CheckBirthday(self):
		if YounisXyz.CreateEmail():
			url = 'https://www.instagram.com/web/consent/check_age_eligibility/'
			data = f'day={self.day}&month={self.month}&year={self.year}'
			headers = {
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
			'X-IG-App-ID':f'{self.APPID}',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
			'X-CSRFToken':f'{self.csrftoken}'
			}	
			check = requests.post(url,headers=headers,data=data)
			if '"status":"ok"' in check.text:
				return True
			else:
				return False
		else:
			print('Email Not Created')
	def Retry_Send_Code(self,email):
			url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/'
			data = f'device_id=&email={email}'
			headers = {
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
			'X-IG-App-ID':f'{self.APPID}',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
			'X-CSRFToken':f'{self.csrftoken}'
			}
			send = requests.post(url,headers=headers,data=data)
	def Account_Status(self,username):
		url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'
		headers = {
			'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
			'X-IG-App-ID':'1217981644879628',	
			'X-ASBD-ID':'198387'
		}
		response = requests.get(url,headers=headers)
		if 'id' in response.text:
			return 'Active'
		else:
			return 'Suspend'
	def SaveInfo(self,Account,Session):
		with open('YounisXyz-accounts.txt','a') as f:
			f.write(f'{Account}\n')
		with open('YounisXyz-sessions.txt','a') as s:
			s.write(f'session:{Session}\n')
	def SendCode(self):
		if YounisXyz.CheckBirthday():
			url = 'https://i.instagram.com/api/v1/accounts/send_verify_email/'
			data = f'device_id=&email={self.email}'
			headers = {
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
			'X-IG-App-ID':f'{self.APPID}',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
			'X-CSRFToken':f'{self.csrftoken}'
			}
			send = requests.post(url,headers=headers,data=data)
			if '"email_sent":true' in send.text:		
				print('[3] Sending Verification code')
				sleper.sleep(4)
				return True
			else:
				return False
		else:
			print('Error In Check Birthday')
	def GetCode(self):
		if YounisXyz.SendCode():
			url = f'https://api.internal.temp-mail.io/api/v3/email/{self.email}/messages'
			headers = {
				'User-Agent':'Temp%20Mail/30 CFNetwork/1220.1 Darwin/20.3.0',
				'Content-Type':'application/json'
			}
			
			while True:
				
				for i in range(5):
					response = requests.get(url,headers=headers,verify=False)
					if 'Instagram' in response.text:
						for messages in response.json():
							subject = messages['subject']
							self.code = subject.split(' is your Instagram code')[0]
							return True
							break
					else:				
						print(f'\r[4] Waiting Verification code',end='')
						sleper.sleep(5)
				print('\rResend',end='')
				YounisXyz.Retry_Send_Code(self.email)
				
				
		else:
			print('Email Not sent')
	def CheckCode(self):
		if YounisXyz.GetCode():
			print('\n[5] Verifying The Code')
			url = 'https://i.instagram.com/api/v1/accounts/check_confirmation_code/'
			data = f'code={self.code}&device_id=&email={self.email}'
			headers = {
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
			'X-IG-App-ID':f'{self.APPID}',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
			'X-CSRFToken':f'{self.csrftoken}'
			}
			response = requests.post(url,headers=headers,data=data)
			if 'signup_code' in response.text:
				self.signup_code = response.json()['signup_code']
				return True
			else:
				print(response.text)
				return False
		
	def CreateAccount(self):
		if YounisXyz.CheckCode():
			print('[6] Creating Account')
			url = 'https://www.instagram.com/accounts/web_create_ajax/'
			time = int(datetime.now().timestamp())
			data = f'enc_password=#PWD_INSTAGRAM_BROWSER:0:{time}:{self.password}&email={self.email}&username={self.username}&first_name=Created By YounisXyz\n&month={self.month}&day={self.day}&year={self.year}&client_id=&seamless_login_enabled=1&tos_version=row&force_sign_up_code={self.signup_code}'
			headers = {
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
			'X-IG-App-ID':f'{self.APPID}',
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':f'csrftoken={self.csrftoken}; ig_did={self.ig_did}; ig_nrcb=1; mid={self.mid}',
			'X-CSRFToken':f'{self.csrftoken}'
			}
			response = requests.post(url,headers=headers,data=data)
			if 'user_id' in response.text:
				self.end_time = sleper.time()
				self.elapsed_time = int(self.end_time - self.start_time)
				print('-'*40)
				print('Successfully Created')
				print(f'username : {self.username}')
				print(f'password : {self.password}')
				print(f'email : {self.email}')
				print(f'Account Status : {YounisXyz.Account_Status(self.username)}')
				print(f'The process took {self.elapsed_time} seconds')
				print('account saved in "YounisXyz-accounts.txt"')
				print('-'*40)
				Session = response.cookies['sessionid']
				Account = f'{self.username}:{self.password}'
				message = f'New IG Account Created\nusername: {self.username}\npassword: {self.password}\nemail: {self.email}\nAccount Status : {YounisXyz.Account_Status(self.username)}\nDeveloper : https://www.instagram.com/f09l/'
				YounisXyz.SaveInfo(Account,Session)
				YounisXyz.SendToBot(message)
				
			else:
				print('-'*40)
				print(response.text)
				print('-'*40)
		else:
			print('Faild To Create Account')
			
	
print("""
 
 Younis john
""")
YounisXyz = YounisXyz()
try:
	count = int(input('accounts count : '))
except :
	count = 0
for _ in range(count):
	YounisXyz.CreateAccount()
 