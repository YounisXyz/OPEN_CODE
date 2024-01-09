#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,time,re
import urllib3,rich,base64
ses=requests.Session()
sys.stdout.write('\x1b[1;35m\x1b]2; Created by YounisXyz\x07')
#------------[ INDICATION ]---------------#
id = [] 
tokenku = [] 
uid = []
# ------------[ BASIC-COLORS ]--------------#
red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[1;32m' 
blue_color = '\033[1;34m'
purple_color = '\033[1;35m'
white_color = '\033[0;97m'
cyan_color = '\033[1;36m'
default_color = '\33[m'
colors = ["\033[0;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m", "\033[0;100m", "\033[1;100m","\033[0;101m", "\033[1;101m", "\033[0;102m", "\033[1;102m","\033[0;104m", "\033[1;104m", "\033[0;105m", "\033[1;105m", "\033[0;106m", "\033[1;106m"]
A = "\x1b[38;5;248m"
brown = "\x1b[38;5;208m"
black = "\x1b[0;90m"


os.system(f'xdg-open https://chat.whatsapp.com/E9G45DzibkCJe42rCnaiKi')
# ------------[ MAIN-LOGO ]--------------#
def logo():
	clear()
	print(f'''{white_color} 
 ▓█████▄  █    ██   ███▄ ▄███▓ ██▓███        ██ ▓█████▄ 
 ▒██▀ ██▌ ██  ▓██▒ ▓██▒▀█▀ ██▒▓██░  ██     ▒▓██ ▒██▀ ██▌
{green_color}░██   █▌▓██  ▒██░ ▓██    ▓██░▓██░ ██▓▒    ░▒██ ░██   █▌{white_color}
▒░▓█▄   ▌▓▓█  ░██░ ▒██    ▒██ ▒██▄█▓▒ ▒     ░██▒░▓█▄   ▌
░░▒████▓ ▒▒█████▓ ▒▒██▒   ░██▒▒██▒ ░  ░     ░██░░▒████▓ 
{green_color}░ ▒▒▓  ▒  ▒▓▒ ▒ ▒ ░░ ▒░   ░  ░▒▓▒░ ░  ░     ░▓ ░ ▒▒▓  ▒ 
  ░ ▒  ▒  ░▒░ ░ ░ ░░  ░      ░░▒ ░           ▒   ░ ▒  ▒ 
  ░ ░  ░   ░░ ░ ░  ░      ░   ░░             ▒   ░ ░  ░ 
    ░       ░     ░       ░                  ░     ░    {white_color}

{50 * '-'}
 >> Author : Muhammad Younis
 >> Github : https://github.com/YounisXyz
 >> WhatsApp : +923404708884
{50 * '-'}''')

def clear():
    os.system('clear')



def login_check():
	try:
		token = open('/sdcard/XYZ/dump_login/.token.txt','r').read()
		cok = open('/sdcard/XYZ/dump_login/.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			_name_ = json.loads(sy.text)['name']
			_id_ = json.loads(sy.text)['id']
			menu(_name_,_id_)
		except KeyError:
			login()
		except requests.exceptions.ConnectionError:
			print(f"{red_color} Internet Connection Error! ") 
			exit()
	except IOError:
		login()


def login():
	try:
		logo()
		cookie=input(f'{white_color} Put your cookie : ')
		print(50*"\033[0;97m-")
		open("/sdcard/XYZ/dump_login/.cok.txt", "w").write(cookie)
		with requests.Session() as XYZ:
			try:
				XYZ.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
				response = XYZ.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open("/sdcard/XYZ/dump_login/.token.txt", "w").write(token)
					print(f"         [ Logged in successfully !  ] ") 
					print(f" Access token : {token}") 
				else:
					print(f'{yellow_color} Conot Get Token .... ')
			except:
				print('{red_color} Failled Get Token .... ')
		time.sleep(2)
		login_check()
	except Exception as e:
		os.system("rm -f /sdcard/XYZ/dump_login/.token.txt")
		os.system("rm -f /sdcard/XYZ/dump_login/.cok.txt")
		print(f'{white_color} Cookie Not Found, {yellow_color}Please login first .... ')
		print(e)
		exit()
		
		

#------------------[ MAIN-MENU ]----------------#
def menu(_name_,_id_):
	try:
		token = open('/sdcard/XYZ/dump_login/.token.txt','r').read()
		cok = open('/sdcard/XYZ/dump_login/.cok.txt','r').read()
	except IOError:
		logo();print(f'{white_color} Cookie Not Found, {yellow_color}Please login first .... ')
		time.sleep(2)
		login()
	os.system('clear')
	logo()
	print(f"\t    -----({green_color}Active{white_color})----- ")
	print()
	print(f" Welcome {_name_}")
	print(f" User id : {_id_}") 
	print(50*"\033[0;97m-")
	print(f' [1] Dump Multiple  ')
	print(f' [2] Publik ID  Single    ')
	print(f' [0] {red_color}Logout Cookies{white_color}')
	YounisXyz = input(f' Select option > ')
	if YounisXyz in ['1']:
		multi_extract()
	elif YounisXyz in ['2']:
		dump("",{"cookie":cok},token)
		donesingle()
	elif YounisXyz in ['0']:
		os.system('rm -rf /sdcard/XYZ/dump_login/.token.txt')
		os.system('rm -rf /sdcard/XYZ/dump_login/.cookie.txt')
		print(f' {yellow_color}Cookie deleted successfully >>')
		exit()
	else:
		print(f'{red_color} Invalid option selected .... ')
		exit()
		
		
###----------[ dump multi extract public ]----------###
def multi_extract():
	print()
	try:
		token = open('/sdcard/XYZ/dump_login/.token.txt','r').read()
		cok = open('/sdcard/XYZ/dump_login/.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		id_limit = int(input(f' How many ids do you want to add ? : '))
		print(f'\n For Example /sdcar/xyz.txt')
		file_name = input(' Output save file name > ')
		print(f'\n{yellow_color} Note :\n Input Id Friendlist Public{white_color}')
	except ValueError:
	    exit()
	if id_limit<1 or id_limit>1000:
	    exit()
	ses=requests.Session()
	id_number = 0
	for Y0U91SXYZ in range(id_limit):
		id_number+=1
		Enter_id = input(f' ['+str(id_number)+f'] Enter ID link: ')
		uid.append(Enter_id)
	for user in uid:
	    try:
	       head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
	       if len(id) == 0:
	           params = ({'access_token': token,'fields': "friends"})
	       else:
	           params = ({'access_token': token,'fields': "friends"})
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xyz in url['friends']['data']:
	           try:
	               younisxyz = (xyz['id']+'|'+xyz['name']);open(f'%s'%(file_name),'a').write(xyz['id']+'|'+xyz['name']+'\n')
	               abc = (xyz['id'])
	               jj = len(id)
	               x = random.choice(colors)
	               #print(f" {x}Success Dump From : {abc}\033[0m Total ids : {jj}") 
	               if younisxyz in id:pass
	               else:id.append(younisxyz)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print(50*"\033[0;97m-")
	      print(f'{yellow_color} Extracted Successfully Done ')
	      print(f"{white_color} Total ids extract  : "+str(len(id))) 
	      print(f' Your Dump ids Saved in : {green_color}{file_name}{white_color}')
	      print(50*"\033[0;97m-")
	      input(f" [ PRESS ENTER TO GO BACK ]  ") 
	      login_check()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()

#-------------------[ dump public single ]--------------------#    
def dump(fields,cookie,token):
	try:
		print(f'\n For Example /sdcar/xyz.txt')
		file_name = input(' Output save file name > ')
		print(f'{yellow_color}\n Note :\n Input Id Friendlist Public{white_color}')
		idt = input(' Put id : ')
		headers = {"connection": "keep-alive", "accept": "*/*", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors","sec-fetch-site": "same-origin", "sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"}
		if len(id) == 0:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday)"}
		else:
			params = {"access_token": token,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			id.append(i["id"]+"|"+i["name"])
			open(f'%s'%(file_name),'a').write(i['id']+'|'+i['name']+'\n')
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
def donesingle():
	print(50*"\033[0;97m-")
	print(f'{yellow_color} Extracted Successfully Done ')
	print(f"{white_color} Total ids extract  : "+str(len(id))) 
	print(50*"\033[0;97m-")
	input(f" [ PRESS ENTER TO GO BACK ]  ") 
	login_check()
#-----------------------[ --Recoded by YounisXyz-- ]--------------------#
if __name__=='__main__':
	try:os.mkdir("/sdcard/XYZ")
	except:pass
	try:os.mkdir("/sdcard/XYZ/YounisXyz")
	except:pass
	try:os.mkdir("/sdcard/XYZ/dump_login")
	except:pass
	login_check()
	
#Github: https://github.com/YounisXyz
#Facebook: https://facebook.com/xyzhackers
#Whatsapp: +923404708884
#Youtube: https://youtube.com/@YounisXyz
#------------------[ << THE END OF CODE >> ]-----------------#