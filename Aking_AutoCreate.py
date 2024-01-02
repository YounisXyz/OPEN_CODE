#🙃F*cked Lking By Me
# Script Meri thi bs iske hath pata nai kese lag gayi


W = '\x1b[1;37m'
G = '\x1b[1;32m'
R = '\x1b[1;91m'
S = '\x1b[1;36m'
B = '\x1b[1;34m'
Y = '\x1b[1;33m'
P = '\x1b[1;35m'
cnt=0
cp=0
ok=0
ok1=0
loop=0
died=0
live=0
import os,sys,time,re,uuid,base64,zlib,subprocess
from concurrent.futures import  ThreadPoolExecutor as tpe
try:
    import pycurl
    from io import BytesIO
except:
    os.system('pip install pycurl')
    import pycurl
    from io import BytesIO
try:import pycurl
except:os.system('pkg uninstall python;pkg install python -y;pip install pycurl')
try:import pycurl
except:print('\n Pycurl Module Error!\n Contact With Owner! ');exit()
import random
def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)
myid=uuid.uuid4().hex[:5].upper()
try:
    key1 = open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'r').read()
except:
    kok=open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'w');kok.write(myid);kok.close()
uid = os.getuid()
key1 = open('/data/data/com.termux/files/usr/bin/.mrakingxxx-cov', 'r').read()
kex=(f"AKING-XD~CREATE:{uid}TS{key1}110E==")
key2 = base64.b64encode(str(f"{kex}").encode('utf-8'))
key=(f"{key2}")
fkeyx = key.replace("b'","").replace("'","")
def linex():
    print('\033[1;37m------------------------------------------')
def clear():
    import os
    os.system("clear")
    print("""\033[1;37m  ╔═╗┌┐   ╦═╗┌─┐┌─┐
  ╠╣ ├┴┐  ╠╦╝├┤ │ ┬
  ╚  └─┘  ╩╚═└─┘└─┘
------------------------------------------
 Author : Mr. Aking
 Github : AKING110 (Follow Must)
 Tools  : Auto Facebook Register
 Contact: +923203714588
 Version: 1.6
\033[1;37m------------------------------------------""") 
try:
    clear()
    print(' Checking For Updates....')
    linex()
    lik=str(zlib.decompress(b'x\x9c\x05\xc1a\n\xc0 \x08\x06\xd0\x13M\xa3~\x0cv\x9b\x94Z#\xe5\x0b\xf4\xfe\xec\xbd\x95y\xe2av\xe9\xf1\xe95\xbb\x0e\x01\xf6&1\xbcq\x90\xa4p\xae\xa56.7OI\xc0h\xa5\xdb\x0fW1\x146')).replace("b'","").replace("'","")
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, lik)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    c.close()
    body = buffer.getvalue().decode('utf-8')
    response = body
    if "Version-1.5" in response:
        print(" Already Up To Date...")
        linex()
        print(' Checking For Approval....')
        linex()
        if kex in response:
            print('\033[1;32m Your Key is Approved....\033[1;37m');time.sleep(2)
        elif "Trail-30min" in response:
            print('\033[1;36m Enjoy Free Trial ....\033[1;37m');time.sleep(2)
        else:
            print("\033[1;31m Read note first! ")
            linex()
            print(" You cannot run this tool without AKING permeations \n Note: Agar Tool mai Koi Masla Aata HA To Me Jald Se Jald Try Kronga Fix Krne Ke Agr Nhi Hota To May Be kujh time lag jya fix krne me!\n payment krne ka bad return nhi hoge agr buy krna ha to ok else skip,exit")
            linex()
            print(" Your key: "+fkeyx);subprocess.check_output(["am", "start", "https://api.whatsapp.com/send?phone=+923203714588&text="+(" Hi AKING sir i want Buy Auto Create Ids Tool Please Approve My Token\n Token:- "+ fkeyx)]);time.sleep(2)
            exit('\n Run:  python create.py')
            sys.exit()
    else:
        print(' Update done successfully wait for setup! ')
        time.sleep(2)
        os.system('rm -rf AutoCreate && python create.py')
        exit()
except Exception as e:exit('\n Network connection error '+e)
def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('c_user=%s;xs=%s;fr=%s;datr=%s;'%(ran['c_user'],ran['xs'],ran['fr'],ran['datr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s;'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = '; '.join([str(x)+"="+str(y) for x,y in ran])
    return(str(cookie))
    
def a(k):return k
import os,time,_md5,marshal,inspect 
if str(os.system)==str(print):
  exit()
  sys.exit()
  os._exit(0)
def random_ua():
    model = "iPhone"+str(random.randint(4,16))+','+str(random.randint(1,9))
    abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    build = str(random.randint(9,19))+random.choice(abc)+str(random.randint(50,199))
    fbsv = str(random.randint(4,16))+'_'+str(random.randint(1,9))+'_'+str(random.randint(1,9))
    ua1 = 'Mozilla/5.0 (iPhone, CPU iPhone '+fbsv+' like Mac OS '+str(random.randint(8,16))+') AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/'+build+') Safari/604.1'
    ua2 = "Mozilla/5.0 (iPhone "+str(random.randrange(4,6))+" X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/"+str(random.randint(4,13))+".1.1 Mobile/"+model+" Safari/604.1"
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    ua3 = f"Mozilla/5.0 (Linux; Android {str(random.randint(4,13))}; "+dv_typ+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['RMX3686','RMX3393','RMX3081','RMX2170','RMX2061','RMX2020'])
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua4 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['SM-S911B','SM-S908B','SM-G998B','SM-G988B','SM-G973B','SM-N986B'])
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua5 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    a = random.randrange(112,115)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160'])
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])
    dv_ver = random.randrange(100000,250000)
    sd_ver = random.randrange(1,10)
    ch_ver = f'{a}.0.{b}.{c}'
    ua6 = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    ua = random.choice([ua1,ua2,ua3,ua4,ua5,ua6])
    return(ua)
def Create():
    clear()
    import requests as r,re,random,os
    from bs4 import BeautifulSoup
    print()
    def rnd(a,b):
      return str(random.randint(a,b))
    
    def find(txtt,wrd):
       xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
       return xx
    m=['Aijaz|Ali', 'Zulfiqar|Ali', 'Kamran|Wassan', 'Shoaib|Shoaib', 'Muhbbat|Wassan', 'Rana|Waseem', 'Paras|Paras', 'Rana|Mohsin', 'Aliali|Aliali', 'Ali|Ali', 'Ghulam|Ghulam', 'Waqar|Lakho', 'Junaid|Chandia', 'Asif|Jan', 'Ali|Gulam', 'Malik|Saab', 'Rana|Zakir', 'Zameer|Ali', 'Irshad|Jan', 'Gulam|Shabir', 'Tariq|Rajput', 'Sajid|Ali', 'Shamshad|Ali', 'Mola|Bux', 'Awais|Rao', 'Shahbaz|Ali', 'Rana|Sahil', 'Khadam|Faqir', 'Mukhtiar|Magsi', 'Ghulam|Ali', 'Shah|Mohammed', 'Rawal|Ali', 'ستار|دادا', 'Abdul|Majeed', 'Mer|Muhammad', 'Ali|Rajput', 'Rana|Farman', 'Ahtisham|Rajput', 'Alideno|Khoso', 'Own|Rana', 'Suhail|Ahmed', 'Gulzar|Ahmed', 'Ahamd|Jam', 'Tasawar|Rajput', 'Fida|Qureshi', 'Shamshad|Rahu', 'سوشل|ميڍيا', 'Sheeraz|Abbasi', 'Bashir|Ustad', 'Zubair|Rao', 'Zafar|Ali', 'Yaqoob|Ali', 'M|Soomar', 'Altaf|Hussain', 'Bahadur|Ali', 'Farman|Ali', 'Waris|Ali', 'Rana|Qurban', 'Muhammad|Khan', 'Asad|Asad', 'Sartaaj|Sartaaj', 'Rana|Kabir', 'Rana|Abdul', 'Ghulam|Hussain', 'Kirshan|Kumar', 'Adil|Rajpoot', 'Sahoowal|Sahoowal', 'عبد|الجبار', 'Imran|Ali', 'Faz|Mahammad', 'Safeel|Nawaz', 'ريا|ض', 'Haroon|Rana', 'Amjad|Ali', 'Kashii|Rajpoot', 'Junejo|Sahib', 'Altaf|Pahore', 'Ali|Rajput', 'Zeeshan|Ali', 'Muhammad|Muktiar', 'Iftikhar|Ahmand', 'Shahzeb|Ali', 'Faiz|Jutt', 'Chanesar|Khan', 'Ali|Shar', 'Zuhair|Ahmed', 'محب|علی', 'Siraj|Khaskheli', 'Rana|Dilshad', 'Ghazanfar|Ali', 'Rao|Awais', 'Jaan|Jaan', 'Syed|Junaid', 'Abdul|Ghaffar', 'Kirshan|Kumar', 'ابومحمد|احمد', 'Nisar|Hussain', 'Nasir|Dahri', 'Hakim|Khan', 'Ahsan|Raza', 'Nadir|Rind', 'Sålmàñ|Çh', 'GhulamNabi|Khaskhali', 'Umar|Lal', 'NabeelHy|Ka', 'Dilshad|Magsi', 'Haaji|Anwar', 'Nisar|Ahmed', 'Barkat|Ali', 'Irfan|Ali', 'Aslam|Khan', 'Hashim|Khoso', 'Abdul|Malik', 'Masroor|Zardari', 'Rao|Bilal', 'Nisarkhoso|Nisarkhoso', 'مرجع|الناطق', 'Sajawal|Rajput', 'Rana|Muhammad', 'Rana|Dilshad', 'Rana|Imran', 'Daniyal|Kazmi', 'Faqeer|Baboo', 'Azan|Jan', 'Gul|Hassan', 'Nadir|Jan', 'NadeemRind|Rind', 'Angel|Rodriguez', 'Allahbux|Rang', 'Ghullam|Muhammad', 'Talib|Hussain', 'Abid|Ali', 'Rana|Noushad', 'Ghulam|Hussain', 'Samir|Samir', 'Shahid|Rana', 'Janib|Janib', 'Maria|Albuquerque', 'Rana|Qasim', 'Faizan|Ali', 'Ali|Gul', 'Madeji|Power', 'Rajput|Faisal', 'Mansoor|Sahito', 'Ali|Dero', 'Razaq|Khaskheli', 'Muneer|Ali', 'Imran|Ali', 'Sakhawat|Ali', 'Khadim|Baloch', 'Rana|Taswar', 'Raouf|Chadhar', 'Umar|Shahzad', 'Shah|Mir', 'Irfsn|Irfsn', 'Abbas|King', 'Aftab|Ali', 'M|Raju', 'Ghulam|Mustafa', 'Gul|Sher', 'Nazim|Hussain', 'Malik|Jawed', 'Deedar|Hussain', 'Maham|Khan', 'Junaid|Rajput', 'Sawan|Ali', 'Sajwal|Rao', 'Ayaz|Ali', 'Irfan|Irfan', 'Hut|Khan', 'Ana|Mendez', 'Shakeel|Khosa', 'Javed|Javed', 'Dil|E', 'Rana|Adil', 'Rahil|Ali', 'Innayat|Ali', 'Aijaz|Abbasi', 'Jamil|Jan', 'Fidah|Khoso', 'Rana|Abdul', 'Rana|Junaid', 'Malik|Sajid', 'Ghulam|Ali', 'Ahsan|Ali', 'Imtiaz|Ali', 'Islam|Baloch', 'Hashim|Khoso', 'Sattar|Buledi', 'Nanik|Ram', 'Gul|Wali', 'Rahman|Khan', 'Ali|Hassan', 'Sooraj|Kumar', 'GhulamAbbas|Channa', 'Muhammad|Saleh', 'Ali|Ali', 'Ayazaliayaz|Ayazaliayaz', 'Asif|Baloch', 'Mujeeb|Bds', 'Rana|Mustak', 'Ali|Rind', 'Amjad|Ali', 'سلامدين|سلامدين', 'Himat|Ali', 'Amanullah|Abro', 'Shookat|Ali', 'Mushoque|Malokhani', 'Zulifqar|Ali', 'Fareed|Abro', 'Zuhaib|Ali', 'Rasmyh|Rasmyh', 'Zubair|Ali', 'Waheed|Ali', 'Mohsin|Shaikh', 'Muzamil|Rajput', 'Gul|Bahar', 'Zaffar|Khoso', 'Akram|Ali', 'Rana|Sajids', 'Noor|Highlights', 'Basher|Baloch', 'Musam|Aill', 'Jamshed|Rana', 'علی|مولا', 'Hero|G', 'Rematullha|Rajpoot', 'Ustad|Hanif', 'Zubair|Ali', 'Rana|Abdul', 'Kamran|Ali', 'Kosar|Vighamal', 'Mansoor|Ali', 'Nadeem|Raza', 'Niaz|Hussan', 'Awais|Malik', 'Ammar|Shoz', 'Atta|Mohmad', 'Naeem|Khan', 'Sanju|Bhai', 'Waseem|Abass', 'Ghulam|M', 'Muhammad|Urs', 'Zahid|Hussain', 'Rana|Rajput', 'Meer|Jan', 'Waris|Ali', 'Inayat|Np', 'Sher|Muhhammd', 'Rana|Muzfar', 'Beni|Solis', 'Suba|Ali', 'Umesh|Kumar', 'Basit|Kahout', 'Rafiq|Khaskali', 'Saira|Khan', 'Rizwan|Ali', 'Shahbaz|Ali', 'Ail|Aagsr', 'M|Rafiq', 'Alom|Alahaj', 'Muhmmad|Waris', 'Sameer|Ali', 'Rana|Qaser', 'Fkgkodfj|Xkxnxuc', 'Saijad|Ali', 'Nadeem|Jan', 'Ajkhoso|Ajkhoso', 'Huzaifa|Ansari', 'Mazhar|Abbas', 'Molaa|Bux', 'Mashuq|Ali', 'Aneel|Kumar', 'Zahid|Hussain', 'Alihyder|Kalhoro', 'Rana|Rana', 'Bashir|Ahmed', 'Khalid|Hussein', 'Mumtaz|Ali', 'Arif|Memon', 'Ayoub|Baloch', 'Tehmoor|Ali', 'Imran|Ali', 'Shamshad|Ali', 'Ghulam|Hussain', 'Sajjad|Panhwar', 'Mole|Deno', 'Farooq|Bhaijan', 'Israr|Jakhrani', 'Imtyaz|Ali', 'Adeel|Masih', 'Gull|Hassan', 'Tando|Adam', 'منظور|راهو', 'Rana|Rehman', 'Mamtaz|Sehto', 'Amjid|Ali', 'Rana|Mubashir', 'Hamidullah|Mangsi', 'Ghulam|Nabi', 'Ahmed|Ali', 'Syedjaved|Shah', 'Rao|Hassan', 'Papoo|Kumar', 'Mehtab|Ali', 'Rana|Kashif', 'Rana|Wnus', 'Farman|Ali', 'Zulifiqar|Zulifqar', 'Sadam|Chandio', 'Mitho|Mallah', 'کاشف|راجپوت', 'Shamshaad|Rahoo', 'Hajan|Abbasi', 'Muneer|Zaib', 'Ayaz|Ayaz', 'Zain|Ali', 'Ghulam|Muhammad', 'Rao|Bilal', 'Babu|Khan', 'Rana|Ikram', 'Rana|Nasir', 'Amen|Rajpot', 'Fardeen|Panhwar', 'نگاھ|حبيب', 'Nadeem|Ali', 'Najaf|Ali', 'عمران|عباسی', 'Sahil|Shah', 'Ali|Hassan', 'Sonu|Jani', 'Ajmal|Abbasi', 'Abn|Rajab', 'Imtiyaz|Yousufzai', 'Dildar|Ali', 'Adil|Rao', 'Badshah|Yt', 'Sawan|Ali', 'Ali|Ahmed', 'Amir|Ali', 'Amjad|Ali', 'Shahid|Khan', 'Siama|Khan', 'Gulam|Shabir', 'Tehmoor|Hassan', 'Ghulam|Ali', 'Masum|Ali', 'Dedar|Ali', 'Shani|Jutt', 'Rintu|Kumar', 'Sikandar|Shah', 'Furqan|Jutt', 'Rahil|Ali', 'Rana|Shehzad', 'Nisha|Kumari', 'Jamshed|Khan', 'Zawar|Safdar', 'Murtaza|Ali', 'Muhammad|Aijaz', 'Punhal|Ali', 'Bisharat|Mirbahar', 'Xtylíśh|Shahmir', 'نصيراحمد|ميمڻ', 'Darya|Khan', 'Imdad|Khoso', 'Allyas|Allyas', 'Amjad|Ali', 'Bhatti|G', 'Faizan|Aziz', 'Rashad|Baloch', 'Abdul|Jabar', 'Rana|Shafiq', 'Hamadullah|Lakho', 'Ziafat|Khan', 'Faqeer|N', 'Rana|Ibrar', 'Shafi|Muhmmad', 'Awees|Ali', 'Amir|Ali', 'Ali|Khan', 'QaMar|ZaMan', 'Rana|Naveed', 'فرینا|فرینا', 'Ghul|Sher', 'Safeer|Khaskhali', 'Rana|Asim', 'Farhan|Ali', 'Ghulam|Abbas', 'Zulfiqar|Ali', 'Zakir|Ali', 'Rhman|Ali', 'Rana|Ali', 'Muneer|Khan', 'Mumtaz|Ali', 'Nadeem|Ali', 'Zameer|Shah', 'Faheem|Ahmad', 'Pordip|Mandal', 'Shahzaib|Rahman', 'Zidi|Bacha', 'Waqar|Rajput', 'Ali|Akbar', 'Ali|Raza', 'Sabir|Ali', 'Rana|Qurban', 'Ali|Bahte', 'Sajad|Ali', 'Ahadattaullah|Malik', 'Muzammil|Hussain', 'Jan|Muhammad', 'Fasial|S', 'Ameer|NaNa', 'Makro|Sharif', 'Mithal|Khaskheli', 'محمدموسا|محمدموسا', 'Mitho|Mallah', 'Muzzamil|Ali', 'Ahmad|Hassan', 'Babar|Babar', 'Zawar|Muhammad', 'Rana|Nadir', 'Mazhar|Ali', 'Rana|Irfan', 'Bilal|Abbasi', 'Ghulam|Jaffar', 'Asif|Rana', 'Mœhäməd|Řhæ', 'M|Nawaz', 'Farooq|Ali', 'Ashfaq|Rahoo', 'Azmat|Ali', 'Mateen|Rana', 'Shan|Ali', 'Çhårîyē|Çhøkrī', 'Parwez|Ali', 'Azhar|Hussain', 'Shahabaz|Ali', 'Syed|Ghot', 'Zahid|Hussain', 'Mir|Babu', 'Zarik|M', 'Shakel|Ansari', 'Hafiz|Imran', 'Shah|Zaib', 'Bilal|Jan', 'Asif|Asif', 'Asif|Asif', 'Muzafar|Rajbut', 'Makhdoom|Ghulam', 'Rana|Farooq', 'Gulam|Yaseen', 'Ashiqe|Jatt', 'Arshad|Brohi', 'Nazeer|Ahmed', 'Sajad|Ali', 'Mircho|Mal', 'Rana|Junaid', 'Lakho|Mal', 'Sajid|Ali', 'Raees|Rahat', 'Irfan|Ali', 'Rana|Imran', 'Ali|Mughal', 'Riaz|Khan', 'Ahsan|Bozdar', 'Shahidalisolangi|Shahidalisolangi', 'Tariq|Tariq', 'Rao|Nasir', 'Zahid|Ali', 'Shahzad|Madni', 'Sarfaraz|Rahu', 'Mubashair|Rana', 'Ahsan|Khoso', 'Jalger|Bhatti', 'Rana|Wajid', 'Lala|Aziz', 'Shakir|Abbasi', 'Ali|Asgar', 'Ruble|Hasan', 'Abdul|Rehman', 'Azizullah|Soomro', 'Abbas|Ali', 'Muhammad|Ali', 'Rana|Wajid', 'Rana|Musharaf', 'Rashid|Qureshi', 'Shahmeer|Chandio', 'Shan|Ali', 'Ahmed|Qureshi', 'Zaheer|Abbas', 'Imran|Ali', 'Asif|Khan', 'Shahid|Ali', 'Mangii|Mangii', 'Momin|Ali', 'Meer|Shan', 'Muqu|Poiro', 'Umar|Shahzad', 'Waris|Ali', 'Numwar|Ali', 'Muhammad|Tahir', 'AKhtar|Ali', 'Rana|Sajid', 'Sarfarazmemon|Attad', 'Salim|Junejo', 'Mashque|Ali', 'Hassnan|Ali', 'Irfan|Ali', 'Adv|Ali', 'Himmat|Ali', 'Khalid|Jamil', 'Mohsin|Rajput', 'Syed|Nadir', 'Raheem|Punho', 'Rana|Abdullah', 'Rana|Noaman', 'Mansoor|Solangi', 'Imran|Jaan', 'Waris|Ali', 'Rana|Mubasher', 'Mujahid|Ali', 'Hussnain|Rajpoot', 'Chaudhary|Abdul', 'Haider|Baloch', 'Ali|Dino', 'Mir|Khan', 'Irfan|Fatima', 'Arshad|Baloch', 'Shakir|Abbasi', 'Naveed|Rind', 'Gul|Muhammad', 'Meer|Murtaza', 'Papo|Papo', 'Nisar|Ali', 'Gbhs|Bhit', 'Sadoro|Jan', 'Rana|Moon', 'Ramzan|Jan', 'Rana|Zakir', 'Rao|Waqas', 'M|Waqas', 'Rana|Rana', 'Rukhsar|Haidry', 'RaNa|BOby', 'M|Juman', 'Sadiq|Ali', 'Manik|Khan', 'Ran|A', 'Ghulab|Hussain', 'Ronaq|Ali', 'Tarique|Ali', 'Abdul|Qadir', 'Zawar|Sohana', 'Mehran|Rajput', 'Sikandar|Ali', 'Ãtîf|Â', 'Meer|Shahzeb', 'Sajjad|Abbasi', 'Rana|Naeem', 'Bashir|Ahmed', 'Rafeh|Rajpoot', 'ẞk|KhÄñ', 'Imtiaz|Khoso', 'Alex|Shahzad', 'Aman|Abbasi', 'Mehran|Rajput', 'Raja|Rajpot', 'Bahdur|Ali', 'Hammad|Ali', 'Salman|Salman', 'Shahzad|Shahzad', 'AtaullAh|Khan', 'Rafique|Mirani', 'Arbab|Ali', 'Nisar|Ali', 'Zahid|Hussain', 'Rana|Shahzad', 'Rana|Ramzan', 'Noro|Mohmad', 'Riaz|Rajput', 'Mahbat|Khan', 'Ahsan|Ali', 'Rana|Ikram', 'Qamar|Abbas', 'Jahanzib|Ali', 'Rana|Sunny', 'Rao|Yasir', 'Muhammad|Mithal', 'Ashiq|Hussain', 'Ha|Ni', 'Abdul|Latif', 'Meer|Mortaz', 'Meer|Zohaib', 'Zahid|Bhatti', 'Awais|Rajput', 'Ali|Bux', 'Abdul|Hakeem', 'Hassnain|Muavia', 'Syed|Junaid', 'Riaz|Machi', 'Ahsan|Abro', 'Hyder|Ali', 'Sattar|Sattar', 'Sayed|Sharafat', 'Syed|Bilalarif', 'Lal|Muhmmad', 'Mohsin|Ali', 'Asif|Ali', 'Juleed|Shah', 'Hayat|Khan', 'Ali|Bux', 'पवन|अल्लापुर', 'Ghulam|Nabi', 'Zaheer|Ali', 'Soomar|Bughio', 'Madad|Ali', 'Naeem|Chohan', 'Javed|Javed', 'Waseem|Raza', 'Saorg|Khan', 'Zeeshan|Zeeshan', 'Aliza|Chaudhary', 'Rana|Shuaib', 'Ali|Khan', 'Rao|Shabbir', 'Commandos|King', 'Arshad|Sli', 'Rana|Shahrukh', 'Ratan|Kumar', 'Umar|Khan', 'Ali|Bhnoo', 'Shahzaib|Shah', 'Aqib|Gakhar', 'Rana|Ishaq', 'Bilal|Rajput', 'Asif|Khan', 'Hazrat|Hussain', 'Zohair|Ali', 'Parvez|Ali', 'Altaf|Hussain', 'Mashooq|Ali', 'Dilshad|Magsi', 'Gulam|Mustafa', 'Safdiar|Khan', 'Tofiq|Khan', 'Sudheer|Ahmad', 'Suhrab|Pardesi', 'Syed|Badshah', 'Ashok|Kumar', 'Ssbri|Chandio', 'Yaseen|Ali', 'Rimsha|Shehzadi', 'Meer|Aamir', 'Lakhiar|Adeel', 'Ariz|Muhammad', 'عبداللہ|کوھارو', 'Yameen|Ali', 'Sahil|Gadehi', 'Sahab|Ali', 'Naimatullah|Ali', 'Baqir|Sajjad', 'مير|حارث', 'M|Slutan', 'Sadaqat|Ali', 'Fahad|Ali', 'Muhammed|Shabeer', 'Khalifo|Chandio', 'Zohaib|Ali', 'Ab|Ghani', 'Ibrahim|Baloch', 'Rehmatullah|Mastoi', 'Mohammed|Younis', 'Shahzadi|Kiran', 'Ahmad|Khan', 'Arshad|SooMro', 'Sadam|Solangi', 'Yamen|Ali', 'Majid|Khan', 'Ab|Aziz', 'Sabir|Khuharo', 'Nazeer|Chandio', 'Md|Samer', 'Kaif|Qureshi', 'MuHammad|HaaDi', 'Altaf|Khan', 'Majid|Ali', 'Muhammad|Abraim', 'Noor|Ahmed', 'Abid|Hussain', 'Ashraf|Buriro', 'Rajib|Ali', 'Ahsan|Ali', 'Aakash|Khuharo', 'Hassan|Ali', 'Awaiz|Memon', 'Asharf|Malah', 'Muslim|Chandio', 'Haji|Saddam', 'Rashid|Ali', 'Assadullah|Kolachi', 'Kashif|Ali', 'Irfan|Ali', 'Zulfqar|Soomro', 'Ghafar|Chandio', 'Younis|Ali', 'Meer|Murtiza', 'Majahd|Ali', 'Rao|Arslan', 'Rana|Tsawar', 'Akbar|Rajput', 'Rana|Yasir', 'Rana|Waqar', 'Rana|Umer', 'Rao|Zeeshan', 'Rana|Aqib', 'Rana|Mudassar', 'Rana|Zubair', 'Rana|Zohaib', 'Rana|Rana', 'Rao|Shoaib', 'Nokhaiz|Rao', 'Rana|G', 'Saeed|Somro', 'Rana|Muklish', 'Muzamil|Rajput', 'Râõ|Zêshãñ', 'Rana|Nasrullah', 'Rana|Naveed', 'Hamza|Rajpoot', 'Rana|Naveed', 'Rana|Zahid', 'Rao|Ali', 'Rao|Ishfaq', 'Ehsan|Rana', 'Ahsan|Rana', 'Mohammed|Akmal', 'Rana|Naeem', 'Rana|Ahmad', 'Rana|Shani', 'Rao|Nasir', 'Rao|M', 'Rana|Imran', 'Rao|Arshad', 'Rao|Sanaullah', 'Ali|Rana', 'Rao|Muhammad', 'Rana|Gulraiz', 'Salal|Rajput', 'Rana|Muhammad', 'Ijaz|Rajpoot', 'M|Farman', 'Rao|Raees', 'Rana|Umar', 'Umair|Rana', 'Shafiq|Rajpoot', 'Rana|Numan', 'Rao|Shb', 'Rana|Yousif', 'Rana|Liaqat', 'Rana|Asad', 'Zafar|Rajpoot', 'Rao|Hamza', 'Abubakar|Rajput', 'Rao|M', 'Rana|Ishaq', 'Waqas|Rajpoot', 'Amir|Sohail', 'Rao|Sohaib', 'Rana|Shazil', 'Rao|Bilal', 'Rao|Altaf', 'Rao|Nabeel', 'Hamza|Rao', 'Asif|Rana', 'Rana|Umair', 'Raokashif|Ali', 'Rao|Qaiser', 'Rana|Attual', 'Rana|Shabaz', 'Rao|Salman', 'Rao|Samad', 'Rao|Shoaib', 'Rana|A', 'Rao|Kashif', 'Rao|Zarar', 'Rana|Tayyub', 'Raja|Kamal', 'Amir|Rajput', 'RaoAlizaman|RaoAlizaman', 'Hamza|Rao', 'Rana|Falak', 'Sikandar|Khan', 'Rao|Shahbaz', 'Rana|Talha', 'Kashif|Rajpoot', 'Hammad|Rana', 'Hamza|Rao', 'Roa|Zahid', 'Rana|Hamza', 'Rao|Saleem', 'Rao|Faryad', 'Rao|Abubakar', 'Bilal|Rajput', 'Rao|Waseem', 'Sonu|Rao', 'Rana|Rizwan', 'Bilal|Rao', 'Rans|Maqsood', 'Rana|Furqan', 'Rao|Ali', 'Rana|Muzamil', 'M|Asif', 'Rao|Sohail', 'Rana|Bahadur', 'Rana|Muhmmad', 'Shahzada|Gs', 'Rao|Farhan', 'Zahgim|Ali', 'Abaid|Raja', 'Rana|Waseem', 'Rana|Ajmal', 'Rao|Latif', 'Rao|Aqib', 'Rana|Ramzan', 'Wajid|Rana', 'Sabir|Rajpoot', 'Rana|Shehryar', 'Rana|Yaqub', 'Rao|Abdul', 'Rajput|Sab', 'Rana|Tasawar', 'Rana|Waseem', 'Rana|Babar', 'Rana|Shahid', 'Rana|Maviya', 'Rana|Saeed', 'Waheed|Rajput', 'Junaid|Rajpoot', 'Rao|Saqib', 'Rao|Azeem', 'Rana|Ali', 'Muhammad|Nadeem', 'Rana|Majid', 'Rana|Sahab', 'Abubakar|Jatoi', 'Sabir|Dogar', 'Ameen|Rana', 'Rana|Shakeel', 'Rao|Tasleem', 'Pʀɩŋcɘ|Nʌsɩʀ', 'Rana|Mani', 'Rana|Jee', 'Zidi|Rana', 'Rana|Kamran', 'Rana|Zabi', 'Mehtab|Rao', 'حسن|راو', 'Rana|Sajid', 'Rao|Aftab', 'Rana|Muhammad', 'Muhammad|Muhammad', 'Rao|Abdulrazaq', 'Rao|MubeenRao', 'Rao|Nazeer', 'Rana|Adnan', 'Rana|Alishan', 'Rana|Wahab', 'Rao|Ali', 'Rana|Rashid', 'Rana|Waqar', 'Dilawar|Rao', 'Rana|Iftkhar', 'Shami|Rana', 'Rana|Hamza', 'Rana|Luqman', 'Rao|Haseeb', 'Rana|Waseem', 'Rana|Abid', 'شہری|راجپوت', 'Rao|Mohammad', 'Rana|Rashid', 'Rana|Hamza', 'Tariq|Javid', 'Rao|Ahtsham', 'Rana|Tauqeer', 'Rao|Zeeshan', 'Ahad|Rajpoot', 'M|Muzamil', 'Rana|Zaid', 'Rana|Asad', 'Usama|Rana', 'Rana|Ali', 'Rana|Sajid', 'Rana|Tokeer', 'Rana|Mikro', 'Rana|Rana', 'Raza|Jafri', 'Rana|Kamran', 'Rao|Sharafat', 'Rana|Awais', 'Rana|Arslan', 'Rana|Qazafi', 'Rana|Waqar', 'Flk|Sher', 'Rana|Danish', 'Rana|Mudassar', 'Rana|Khalid', 'Rana|Nadeem', 'Adil|Rao', 'Rana|Tahseen', 'Rao|Tayyab', 'Rao|Waseem', 'Rana|Faheem', 'Rao|Khaleeq', 'Ali|Adnan', 'Rao|Ikhtiar', 'Rao|Jani', 'Rao|Amir', 'Farman|Rao', 'اشتہاری۔راجپوت|اشتھری۔راجپوت', 'RanaAli|Rana', 'Rao|Shoaib', 'Raozain|Raozain', 'Sajawal|Rajpoot', 'Rana|Tanveer', 'Rao|Aqib', 'Rana|Ehsan', 'Rao|Zubair', 'Rajpoot|Zeeshan', 'Ahsan|Rana', 'Rao|Saad', 'Safdar|Rana', 'Rana|Mubeen', 'Räñâ|Umäir', 'Rao|Jani', 'Rana|Ibrar', 'Rao|Amir', 'Rana|Asif', 'Hussnain|Qureshi', 'Abdullah|Somroo', 'Rana|Nabeel', 'Rana|Gulfam', 'Babar|Rao', 'Zubair|Rao', 'Abubakar|Rao', 'Rana|G', 'Rana|Shair', 'Rana|Haris', 'Rao|Tariq', 'Zain|Rao', 'Muhammad|Qadeer', 'Rao|Naveed', 'Rizwan|Rao', 'Sajid|Ali', 'Rao|Munir', 'Rana|Afaq', 'Rajput|Brand', 'Rao|Hassan', 'Rana|Saim', 'Mukhtiyar|Khan', 'Rana|Sarfraz', 'Rana|Naveed', 'Rana|Faizan', 'Usama|Rana', 'Muzammil|Rao', 'Rahman|Dogar', 'Rana|Danish', 'Rao|Shahryar', 'Rana|Shahzad', 'Naqeeb|Rao', 'Anss|Rana', 'Subhan|Rana', 'عبدالرحمان|راؤ', 'R|A', 'Ch|Asad', 'Nadeem|Rao', 'Raja|Nawaz', 'Rana|Iqbal', 'S|Rao', 'Rana|Maqsood', 'Rao|Qasim', 'Rana|Zahid', 'راؤ|عرفان', 'M|Jamshed', 'Rao|Imran', 'Shahzad|Rajpoot', 'Rana|Shahzaib', 'Muhammad|Sikandar', 'راناعامر|راناعامر', 'Rao|Hasnain', 'Rana|Asif', 'Javed|Rana', 'Raoiqrar|Raoiqrar', 'Zaheer|Rana', 'Mudassir|Rajput', 'Rana|Awais', 'Rao|Waseem', 'Ali|Rao', 'Rao|Asif', 'Haseeb|Rajput', 'Rana|Rizwan', 'Rana|Shuaib', 'Rana|Shoaib', 'Rao|Shoaib', 'Rajpoot|Arslan', 'Rao|Muzammil', 'Rana|Rashid', 'Rana|Shahbaz', 'Rao|Inaam', 'رانا|ندیم', 'Arslan|Rao', 'Rana|Shakeel', 'Zeeshan|Rana', 'Rana|Mansoor', 'رانا|عاطف', 'Bilal|Prince', 'Rana|Shokat', 'Rana|Babar', 'M|Jafar', 'Ranaiqrar|Ranaiqrar', 'Rao|Imran', 'Rao|Arif', 'Fatima|Rajpoot', 'Nomii|Rajput', 'Rao|Junaid', 'Hasnaat|Rajput', 'Rao|Haleem', 'عبداللہ|راجپوت', 'Shoiab|Rana', 'رانا|دانی', 'Rao|Tasawar', 'Sunny|Rao', 'ᎷᎥᏗᏁ|ᏕᏬᏝᏖᏗᏁ', 'Sajjad|Rao', 'Sardar|Ijaz', 'Rao|Akbar', 'Rana|Usama', 'Mujahid|Khanbadani', 'Rao|Amjid', 'Rana|Ahsan', 'Rana|Akram', 'Adnan|Rana', 'Imran|Ashraf', 'Rajab|Rajput', 'Rao|Shakir', 'Rana|Usman', 'رانا|ارسلان', 'رضا|سعید', 'Rao|Tariq', 'Saad|Rajpoot', 'Parvaiz|Parvaiz', 'Rana|Dilo', 'Rana|Rashid', 'Rana|Asif', 'Rao|Ali', 'Sultan|Rao', 'Rana|Umair', 'Rao|Saad', 'Rao|Farhan', 'Rana|Babar', 'Raja|Sahib', 'Umer|Wakeel', 'Rao|M', 'Arslan|Rao', 'Rao|Mudassar', 'Rajpoot|Ramzanrajpoot', 'Wasim|Rao', 'Bilal|Rana', 'Shahbaz|Rajpoot', 'M|Asif', 'Rana|Aftab', 'Usama|Rao', 'Rao|Abdul', 'Amir|Sohail', 'Rafiq|Khan', 'Rao|Tanveer', 'Rana|Fahim', 'Rana|Afaq', 'Rana|Jabbar', 'Rana|Zain', 'Rao|Talha', 'Ahmad|Raza', 'M|Rao', 'Brand|Rao', 'Rao|Waseem', 'Rana|Zeshan', 'Adeel|Khalil', 'Rana|Ahamd', 'Rana|Sajid', 'Rana|Bilal', 'Rao|Amir', 'Rao|Asif', 'Farhad|Rao', 'Rao|Kashif', 'Ibrar|Rajput', 'Rao|Aftab', 'Muhammad|Ali', 'Rao|Ali', 'Hassan|Rajput', 'Rao|Mazhar', 'Rao|F', 'Sijawal|Rana', 'Rana|Intizar', 'Rana|Husnain', 'Rao|Babar', 'Rana|Uzair', 'عثمان|احمد', 'Rana|Ali', 'Rana|Waseem', 'Rana|Rehan', 'Rana|Ahmad', 'Rao|Touqeer', 'Rana|Shahid', 'Rao|Abid', 'Azeem|Rao', 'Rana|Imran', 'Rana|Asgher', 'Rao|Raza', 'Rana|Hussain', 'Rao|Shahryar', 'Rao|G', 'Nouman|Rajpoot', 'Rao|Faisal', 'Rao|Saim', 'Rana|Shahid', 'Rana|Adnan', 'Usman|Usman', 'Rajpoot|Putter', 'Hafiz|Ahtsham', 'Rana|Nadeem', 'Moon|Rao', 'Shana|Rao', 'Rao|Fakhar', 'Rana|Imran', 'Rajpoot|Sufyan', 'Malik|Fiaz']
    def process(pas,mmail):
        global ok
        import requests,re
        requests=requests.Session()
        cookies=None
        def find(txtt,wrd):
               xx = re.findall('name="'+wrd+'" value="(.*?)"',txtt.replace("amp;",""))[0]
               return xx                      
        import requests,re,random
        requests=requests.Session()
        cookies=None
        ua=random_ua()
        from fake_email import Email
        mmail=Email().Mail()
        def rnd(a,b):
            return str(random.randint(a,b))
        em=mmail['mail']
        num="03"+rnd(10,49)+rnd(1111111,9999999)
        headers1 = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        url1 = 'https://m.facebook.com/reg/?is_two_steps_login=0&cid=103&refsrc=deprecated&soft=hjk'
        data1 = None
        response1 = requests.get(url1, headers=headers1, data=data1)    
        headers2 = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB, en;q=0.9, en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        url2 = 'https://mbasic.facebook.com/reg/submit/'
        data2 = {
            'lsd': find(response1.text,"lsd"),
            'jazoest': find(response1.text,"jazoest"),
            'ccp': '2',
            'reg_instance': find(response1.text,"reg_instance"),
            'reg_impression_id': find(response1.text,"reg_impression_id"),
            'ns': '0',
            'app_id': find(response1.text,"app_id"),
            'logger_id': find(response1.text,"logger_id"),
            'suma_create_event': 'suma_redirection_click_create_account',
            'field_names[0]': 'firstname',
            'field_names[1]': 'birthday_wrapper',
            'field_names[2]': 'reg_email__',
            'field_names[3]': 'sex',
            'field_names[4]': 'reg_passwd__',
            'is_birthday_confirmed': 'confirmed',
            'multi_step_form': '1',
            'skip_suma': '0',
            'shouldForceMTouch': '1',
            'ref': 'dbl',
            'firstname': random.choice(m).split("|")[0]+" "+random.choice(m).split("|")[1],
            'reg_email__': num,
            'sex': '1',
            'reg_passwd__':pas,
            'birthday_day': rnd(10,27),
            'birthday_month': '3',
            'birthday_year': rnd(1978,1999),
            'welcome_step_completed': True,
            'submission_request': True,
            'age_step_input': False,
            'did_use_age': False,
            'custom_gender': False,
            'name_suggest_elig': False,
            'was_shown_name_suggestions': False,
            'did_use_suggested_name': False,
            'use_custom_gender': False,
            'zero_header_af_client': '',
            'helper': '',
            'guid': '',
            'pre_form_step': '',
            'korean_tos_is_present': '',
            'checkbox_privacy_policy': '',
            'checkbox_tos': '',
            'checkbox_location_policy': ''}
        response = requests.post(url2, headers=headers2, data=data2)
        response=requests.get("https://mbasic.facebook.com")
        if "checkpoint" in response.text:
            return "chk"
        headers = {
        'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-US, en;q=0.9, en-US;q=0.8, en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
        'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '21',
        'upgrade-insecure-requests': '1',
        'user-agent': random_ua()}
        for i in  re.findall('href="/changeemail(.*?)"',response.text):
          url="/changeemail"+i
        response = requests.get("https://mbasic.facebook.com"+url, headers=headers)
        headers = {
            'accept': 'text/html,application/xhtm 1+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-US, en;q=0.9, en-US;q=0.8, en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not: A-Brand"; v="99", "Chromium";V="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand"; v "99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '21',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        data = {
            'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"',str(response.text)).group(1),
            'jazoest': re.search('name="jazoest" value="(.*?)"',str(response.text)).group(1),
            'old_email': re.search('name="old_email" value="(.*?)"',str(response.text)).group(1),
            'reg_instance': re.search('name="reg_instance" value="(.*?)"',str(response.text)).group(1),
            'new': em,
            'next': '',
            'submit': 'Add'}
        url = "https://m.facebook.com"+re.findall('action="(.*?)"',response.text)[0]
        submit = requests.post(url, headers=headers, data=data)
        r=requests.get("https://mbasic.facebook.com")
        while True:
            h=Email(mmail["session"]).inbox()
            if h:
                j = h['topic'].split('-')[1];hh = j.split(' ')[0]
                cd = hh
                break
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate',
            'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not;A-Brand";v="99","Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not;A-Brand";v="99.0.0.0","Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': 'Android',
            'sec-ch-ua-platform-version': '11.0.0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': random_ua()}
        data = {'contact': em,
            'type': 'submit',
            'is_soft_cliff': False,
            'medium': 'email',
            'code': cd,
            'fb_dtsg': find(r.text,"fb_dtsg"),
            'jazoest': find(r.text,"jazoest"),
            '__user': dict(requests.cookies)['c_user']}
        url = 'https://m.facebook.com/confirmation_cliff/'
        response = requests.post(url, headers=headers, data=data)
        return requests
    def strt():
       try:
           global ok,loop,cp,ok1
           import sys
           loop+=1
           sys.stdout.write('\r\r\033[1;37m [AKING-CREATE] \033[1;32mOK:%s \033[1;37m'%(ok));sys.stdout.flush()
           requests=r.Session()
           from fake_email import Email
           mmail=Email().Mail()
           em=mmail['mail']
           hd = {'authority': 'mbasic.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', 'origin': 'https://mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/reg', 'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Android"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent':random_ua()}
           if "9":
              pas=random.choice(m).replace('|','').lower()+rnd(1111,9999)
              requests=process(pas,mmail)
              if requests=="chk":
                cp+=1
                pass
              elif requests=="0":pass
              else:
                 dc=dict(requests.cookies)
                 cok=";".join([k+"="+v for k,v in dc.items()])
                 uid=re.findall("c_user=(.*?);",cok)[0]
                 coki = cvt('ok',requests.cookies.get_dict())+"dpr=2;locale=en_US;wd=950x1835;m_page_voice="+uid
                 print("\r\r\033[1;32m [AKING-OK] "+uid+'|'+pas+'|'+coki)
                 ok+=1
                 open(file,"a").write(uid+"|"+pas+"|"+coki+"\n")
                 linex()
       except Exception as e:
           if not "urllib" and not "perma" in str(e):print(e)
           pass
    file="/sdcard/AKING/CREATE-OK.txt"
    u=5000
    clear()
    print(' Use Airplane Or Use IP Changer if ids coming cp ')
    print(' ids will be save in /sdcard/AKING/CREATE-OK.txt')
    linex()
    for i in range(50000):
       import time
       time.sleep(2)
       tpe(max_workers=10).submit(strt)
Create()
