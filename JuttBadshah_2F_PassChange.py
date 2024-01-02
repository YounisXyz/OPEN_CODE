#!/usr/bin/python3
#-*-coding:utf-8-*-
#made by coding jutt badshah
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import concurrent.futures
except ImportError:
    print ('\n [×] Modul Futures Not installed!...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
try:
    import os, sys, time, datetime, re, bs4, json, random, requests, subprocess, platform, uuid, string, base64
    from concurrent.futures import ThreadPoolExecutor as JuttBadshah
    from datetime import datetime
    from bs4 import BeautifulSoup
    from requests.exceptions import ConnectionError
except (ModuleNotFoundError,FileNotFoundError):
    os.system('clear')
    print ('\033[0;97mSome modules are not found run again all pkgs')
    exit()
    sys.exit()
os.system('git pull')
os.system('clear')
logo4 = """
\x1b[1;91m
\x1b[1;92m
\x1b[1;96m
\x1b[1;92m         {|} {|}  {|} {|}{|}{|} {|}{|}{|}
\x1b[1;97m         {|} {|}  {|}    {|}       {|}
\x1b[1;93m         {|} {|}  {|}    {|}       {|}
\x1b[1;96m         {|} {|}  {|}    {|}       {|}
\x1b[1;94m     {|}{|}   {|}{|}     {|}       {|}
\x1b[1;93m
\x1b[1;92m         Jutt Badshah Brand~
\x1b[1;91m-----------------------------------------------
\x1b[1;97m> Author : Jutt Badshah
\x1b[1;97m> Github : https://github.com/SHOOTER-MAKER
\x1b[1;97m> Facebok: Jutt Badshah
\x1b[1;97m> Version: 2fa + pass change
\x1b[0;97m-----------------------------------------------"""
ses = requests.Session()

def menu():
    try:
        os.system('clear')
        print (logo4)
        print ('~~~~~~~~~~~~~~~main menu~~~~~~~~~~~~~~')
        print (47*'-')
        print ('[1] two factor on')
        print ('[2] Password change')
        print ('[0] Back menu')
        print (47*'-')
        put=input('Select: ')
        if put == '1':
            tfa()
        elif put == '2':
            change()
        elif put == '0':
            os.system('python Juttbrand.py')
        else:
            print ('Select valid option')
            time.sleep(1)
            menu()
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        print (logo4)
        print ('Oops Wrong input Try Again')
        sys.exit()

def coded(addd):
    for x in addd.find_all('span'):
        if (re.findall('\d+\s\d+', str(x))):
            print (x.text)

def checkcp(link):
    if 'take you through some steps to unlock your account' in str(link) or 'some steps to unlock your account' in str(link):
        print ('Your account has been locked')
        input('Press enter to back')
        menu()
    elif 'suspended your account' in str(link):
        print ('Your account has been suspended')
        input('Press enter to back')
        menu()
    elif 'Login approval needed' in str(link) or 'need to confirm that it was you' in str(link):
        print ('Your account has been checkpoint')
        input('Press enter to back')
        menu()
    elif 'Your account has been disabled' in str(link):
        print ('Your account has been disabled')
        input('Press enter to back')
        menu()
    elif '%2Fcheckpoint%2F' in str(link):
        print ('Your account has been checkpoint')
    elif 'The password you entered was incorrect' in str(link) or 'Enter a valid password and try again' in str(link):
        print ('Your password wrong')
        input('Press enter to back')
        menu()
    else:
        pass

def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies={'cookie':cookie})
            pra = BeautifulSoup(req.content,'html.parser')
            checkcp(pra)
            if '/login.php?next=' in str(pra):
                print ('Maybe your account cp or lock login your account in your kiwi browser if get login success then take new cookie from kiwi browser and try again')
                input('Press enter to back')
                menu()
            elif 'facebook.com/zero/toggle/nux/' in str(pra):
                print ('Cokie not accept first login account in your kiwi browser and get new cookie from kiwi browser and try again')
                input('Press enter to back')
                menu()
            else:
                pass
            for y in pra.find_all("a",href=True):
                if '/zero/optin/write/?action=cancel' in str(y):
                    ref=y.get('href')
                    try:
                        aj=BeautifulSoup(xyz.get('https://x.facebook.com'+ref, cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(aj)
                    except requests.exceptions.SSLError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    except requests.exceptions.ConnectionError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    for x in aj.find_all('form', {'method': 'post'}):
                        if '/zero/optin/write/?action=confirm' in str(x):
                            link=x.get('action')
                            use=re.findall('data-sigil="touchable" type="submit" value="(.*?)"', str(x))
                            for t in use:
                                use1=t
                            dog={}
                            for z in x('input'):
                                dog.update({z.get("name"):z.get("value")})
                            dog.update({'submit': use1})
                            aa=BeautifulSoup(xyz.post('https://x.facebook.com'+link, data=dog, cookies={'cookie': cookie}).text, 'html.parser')
                            req = xyz.get('https://mbasic.facebook.com/language/',cookies={'cookie':cookie})
                            pra = BeautifulSoup(req.content,'html.parser')
                            checkcp(pra)
            for x in pra.find_all('form',{'method':'post'}):
                if 'English (US)' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "English (US)"}
                    url = 'https://mbasic.facebook.com' + x['action']
                    exe = xyz.post(url,data=bahasa,cookies={'cookie':cookie})
    except Exception as e:
        pass

def tfa():
    os.system('clear')
    print (logo4)
    print ('\033[0;97mExample email==password==cookie')
    user=input('paste: ')
    if user == '':
        menu()
    try:
        email=user.split('==')[0]
        pw=user.split('==')[1]
        cok=user.split('==')[2]
    except:
        print ('put right method of email password cookie')
        time.sleep(3)
        tfa()
    email = email
    pw = pw
    coki=cok.replace(' ', '')
    cokie = coki+';'
    try:
        datr=cokie.split('datr=')[1].split(';')[0]
        fr=cokie.split('fr=')[1].split(';')[0]
        c_user=cokie.split('c_user=')[1].split(';')[0]
        xs=cokie.split('xs=')[1].split(';')[0]
        cokiee='datr='+datr+';'+'fr='+fr+';'+'c_user='+c_user+';'+'xs='+xs+';'
    except:
        try:
            datr=cokie.split('datr=')[1].split(';')[0]
            c_user=cokie.split('c_user=')[1].split(';')[0]
            xs=cokie.split('xs=')[1].split(';')[0]
            cokiee='datr='+datr+';'+'c_user='+c_user+';'+'xs='+xs+';'
        except:
            print ('Cookie not accept')
            exit()
    cookie=cokiee
    language(cookie)
    try:
        try:
            a=ses.get('https://x.facebook.com/security/2fac/setup/intro/metadata/?source=1&paipv=0', cookies={'cookie': cookie})
            bc=BeautifulSoup(a.text, 'html.parser')
            checkcp(bc)
            if '/login.php?next=' in str(bc):
                print ('Maybe your account cp or lock login your account in your kiwi browser if get login success then take new cookie from kiwi browser and try again')
                input('Press enter to back')
                menu()
            elif 'facebook.com/zero/toggle/nux/' in str(bc):
                print ('Cokie not accept first login account in your kiwi browser and get new cookie from kiwi browser and try again')
                input('Press enter to back')
                menu()
            else:
                pass
        except requests.exceptions.SSLError:
            os.system('clear')
            print (logo4)
            print ('internet problem')
            time.sleep(3)
            menu()
        except requests.exceptions.ConnectionError:
            os.system('clear')
            print (logo4)
            print ('internet problem')
            time.sleep(3)
            menu()
        for y in bc.find_all("a",href=True):
            if '/zero/optin/write/?action=cancel' in str(y):
                ref=y.get('href')
                try:
                    aj=BeautifulSoup(ses.get('https://x.facebook.com'+ref, cookies={'cookie': cookie}).text, 'html.parser')
                    checkcp(aj)
                except requests.exceptions.SSLError:
                    os.system('clear')
                    print (logo4)
                    print ('internet problem')
                    time.sleep(3)
                    menu()
                except requests.exceptions.ConnectionError:
                    os.system('clear')
                    print (logo4)
                    print ('internet problem')
                    time.sleep(3)
                    menu()
                for x in aj.find_all('form', {'method': 'post'}):
                    if '/zero/optin/write/?action=confirm' in str(x):
                        link=x.get('action')
                        use=re.findall('data-sigil="touchable" type="submit" value="(.*?)"', str(x))
                        for t in use:
                            use1=t
                        dog={}
                        for z in x('input'):
                            dog.update({z.get("name"):z.get("value")})
                        dog.update({'submit': use1})
                        aa=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dog, cookies={'cookie': cookie}).text, 'html.parser')
                        a=ses.get('https://x.facebook.com/security/2fac/setup/intro/metadata/?source=1&paipv=0', cookies={'cookie': cookie})
                        bc=BeautifulSoup(a.text, 'html.parser')
                        checkcp(bc)
    except requests.exceptions.SSLError:
        os.system('clear')
        print (logo4)
        print ('internet problem')
        time.sleep(3)
        tfa()
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (logo4)
        print ('internet problem')
        time.sleep(3)
        tfa()
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        print (logo4)
        print ('Oops Wrong input Try Again')
        sys.exit()
    except Exception as e:
        pass
    try:
        for x in bc.find_all("a",href=True):
            if '/security/2fac/setup/qrcode/generate' in str(x):
                link=x.get('href')
                try:
                    b=ses.get(link.replace('m.facebook', 'x.facebook'), cookies={'cookie': cookie})
                    bb=BeautifulSoup(b.text, 'html.parser')
                    checkcp(bb)
                except requests.exceptions.SSLError:
                    os.system('clear')
                    print (logo4)
                    print ('internet problem')
                    time.sleep(3)
                    menu()
                except requests.exceptions.ConnectionError:
                    os.system('clear')
                    print (logo4)
                    print ('internet problem')
                    time.sleep(3)
                    menu()
                for x in bb.find_all('form', {'method': 'post'}):
                    if '/password/reauth/?next=' in str(x):
                        link1=x.get('action')
                        bl=['fb_dtsg', 'jazoest']
                        data={}
                        for v in x('input'):
                            if v.get("name") in bl:
                                try:
                                    data.update({v.get("name"):v.get("value")})
                                except:
                                    pass
                        data.update({'pass': pw, 'save': re.search('type="password" /></div><input value="(.*?)"', str(b.text)).group(1)})
                        try:
                            c=BeautifulSoup(ses.post(link1.replace('m.facebook', 'x.facebook'), data=data, cookies={'cookie': cookie}).text, 'html.parser')
                            checkcp(c)
                        except requests.exceptions.SSLError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(3)
                            menu()
                        except requests.exceptions.ConnectionError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(3)
                            menu()
                        #secret=re.findall('authentication app</div><div class=".*?">(.*?)</div></div></div></td></tr></table></div></div><div><div', str(c))
                        try:
                            secret=re.findall('data-testid="key">(.*?)</div></div></div></div></div></div></div><div', str(c))
                        except:
                            print ('Password wrong')
                            exit()
                        for y in secret:
                            z=y
                        open('/sdcard/2fakey.txt', 'a').write(email+'|'+pw+'|'+z+'\n')
                        key=z.replace(' ', '')
                        a=requests.get('https://2fa.live/tok/'+key)
                        b1=a.text
                        token = re.sub('[^0-9]', '', b1)
                        gl=['fb_dtsg', 'jazoest']
                        data1={}
                        for x in c('input'):
                            if x.get("name") in gl:
                                try:
                                    data1.update({x.get("name"):x.get("value")})
                                except:
                                    pass
                        data1.update({'code': token})
                        code=BeautifulSoup(ses.post('https://x.facebook.com/security/2fac/setup/verify_code/?paipv=0', data=data1, cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(code)
                        try:
                            ad=BeautifulSoup(ses.get('https://x.facebook.com/security/2fac/factors/recovery-code/?paipv=0', cookies={'cookie': cookie}).text, 'html.parser')
                            checkcp(ad)
                        except requests.exceptions.SSLError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(3)
                            menu()
                        except requests.exceptions.ConnectionError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(1)
                            menu()
                        for x in ad.find_all('form', {'method': 'post'}):
                            if '/security/2fac/factors/recovery-code/' in str(x):
                                link=x.get('action')
                                hl=['fb_dtsg', 'jazoest']
                                submit=re.findall('data-sigil="touchable" type="submit" value="(.*?)"', str(x))
                                for y in submit:
                                    submit1=y
                                dat={}
                                for g in x('input'):
                                    if g.get("name") in hl:
                                        try:
                                            dat.update({g.get("name"):g.get("value")})
                                        except:
                                            pass
                                dat.update({"reset": "true", "submit": submit1})
                                ag=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dat, cookies={'cookie': cookie}).text, 'html.parser')
                                checkcp(ag)
                                print ('Key > '+z)
                                coded(ag)
                                print ('successfuly 2fa done')
                                input('Press enter to back')
                                menu()
                for d in bb.find_all("a",href=True):
                    if 'otpauth://totp/ID:'+email in d.get('href'):
                        secret=re.findall('data-testid="key">(.*?)</div></div></div></div></div></div></div><div', str(bb))
                        for y in secret:
                            z=y
                        open('/sdcard/2fakey.txt', 'a').write(email+'|'+pw+'|'+z+'\n')
                        key=z.replace(' ', '')
                        a=requests.get('https://2fa.live/tok/'+key)
                        b1=a.text
                        token = re.sub('[^0-9]', '', b1)
                        gl=['fb_dtsg', 'jazoest']
                        data1={}
                        for m in bb('input'):
                            if m.get("name") in gl:
                                try:
                                    data1.update({m.get("name"):m.get("value")})
                                except:
                                    pass
                        data1.update({'code': token})
                        code=BeautifulSoup(ses.post('https://x.facebook.com/security/2fac/setup/verify_code/?paipv=0', data=data1, cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(code)
                        try:
                            ad=BeautifulSoup(ses.get('https://x.facebook.com/security/2fac/factors/recovery-code/?paipv=0', cookies={'cookie': cookie}).text, 'html.parser')
                            checkcp(ad)
                        except requests.exceptions.SSLError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(3)
                            menu()
                        except requests.exceptions.ConnectionError:
                            os.system('clear')
                            print (logo4)
                            print ('internet problem')
                            time.sleep(3)
                            menu()
                        for x in ad.find_all('form', {'method': 'post'}):
                            if '/security/2fac/factors/recovery-code/' in str(x):
                                link=x.get('action')
                                hl=['fb_dtsg', 'jazoest']
                                submit=re.findall('data-sigil="touchable" type="submit" value="(.*?)"', str(x))
                                for y in submit:
                                    submit1=y
                                dat={}
                                for s in x('input'):
                                    if s.get("name") in hl:
                                        try:
                                            dat.update({s.get("name"):s.get("value")})
                                        except:
                                            pass
                                dat.update({"reset": "true", "submit": submit1})
                                ag=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dat, cookies={'cookie': cookie}).text, 'html.parser')
                                checkcp(ag)
                                print ('Key > '+z)
                                coded(ag)
                                print ('successfuly 2fa done')
                                input('press enter to back')
                                menu()
            elif '/security/2fac/factors/recovery-code/' in str(x) or '/security/2fac/setup/turn_off' in str(x):
                print ('2fa alreaf on this account')
                print ('You want recovery codes? y/n')
                yes=input('Select: ')
                if yes=='y':
                    try:
                        ad=BeautifulSoup(ses.get('https://x.facebook.com/security/2fac/factors/recovery-code/?paipv=0', cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(ad)
                    except requests.exceptions.SSLError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    except requests.exceptions.ConnectionError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    try:
                        try:
                            os.system('cat /sdcard/2fakey.txt | grep '+email+' > .key.txt')
                        except:
                            pass
                        try:
                            red=open('.key.txt', 'r').read()
                            zed=red.split('|')[2].split('\n')[0]
                        except:
                            zed='Key not found'
                        print ('Key > '+zed)
                        coded(ad)
                        print ('successfuly 2fa done')
                        input('press enter to back')
                        menu()
                    except:
                        for x in ad.find_all('form', {'method': 'post'}):
                            if '/security/2fac/factors/recovery-code/' in str(x):
                                link=x.get('action')
                                hl=['fb_dtsg', 'jazoest']
                                submit=re.findall('name="resend" type="submit" value="(.*?)"', str(x))
                                for y in submit:
                                    submit1=y
                                dat={}
                                for s in x('input'):
                                    if s.get("name") in hl:
                                        try:
                                            dat.update({s.get("name"):s.get("value")})
                                        except:
                                            pass
                                dat.update({"reset": "true", "submit": submit1})
                                ag=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dat, cookies={'cookie': cookie}).text, 'html.parser')
                                checkcp(ag)
                                try:
                                    os.system('cat /sdcard/2fakey.txt | grep '+email+' > .key.txt')
                                except:
                                    pass
                                try:
                                    red=open('.key.txt', 'r').read()
                                    zed=red.split('|')[2].split('\n')[0]
                                except:
                                    zed='Key not found'
                                print ('Key > '+zed)
                                coded(ag)
                                print ('successfuly 2fa done')
                                input('press enter to back')
                                menu()
                else:
                    menu()
        for x in bc.find_all('form', {'method': 'post'}):
            if '/password/reauth/?next=' in str(x):
                das={}
                link=x.get('action')
                print ('2fa already on this account')
                print ('You want recovery codes y/n')
                yes=input('Select: ')
                if yes=='y':
                    bl=['fb_dtsg', 'jazoest']
                    for y in x('input'):
                        if y.get("name") in bl:
                            try:
                                das.update({y.get("name"):y.get("value")})
                            except:
                                pass
                    das.update({'pass': pw, 'submit': re.search('type="password" /></div><input value="(.*?)"', str(a.text)).group(1)})
                    try:
                        c=BeautifulSoup(ses.post(link.replace('m.facebook', 'x.facebook'), data=das, cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(c)
                    except requests.exceptions.SSLError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    except requests.exceptions.ConnectionError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    try:
                        ad=BeautifulSoup(ses.get('https://x.facebook.com/security/2fac/factors/recovery-code/?paipv=0', cookies={'cookie': cookie}).text, 'html.parser')
                        checkcp(ad)
                    except requests.exceptions.SSLError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    except requests.exceptions.ConnectionError:
                        os.system('clear')
                        print (logo4)
                        print ('internet problem')
                        time.sleep(3)
                        menu()
                    try:
                        try:
                            os.system('cat /sdcard/2fakey.txt | grep '+email+' > .key.txt')
                        except:
                            pass
                        try:
                            red=open('.key.txt', 'r').read()
                            zed=red.split('|')[2].split('\n')[0]
                        except:
                            zed='Key not found'
                        print ('Key > '+zed)
                        coded(ad)
                        print ('successfuly 2fa done')
                        input('press enter to back')
                        menu()
                    except:
                        for x in ad.find_all('form', {'method': 'post'}):
                            if '/security/2fac/factors/recovery-code/' in str(x):
                                link=x.get('action')
                                hl=['fb_dtsg', 'jazoest']
                                submit=re.findall('name="resend" type="submit" value="(.*?)"', str(x))
                                for y in submit:
                                    submit1=y
                                dat={}
                                for s in x('input'):
                                    if s.get("name") in hl:
                                        try:
                                            dat.update({s.get("name"):s.get("value")})
                                        except:
                                            pass
                                dat.update({"reset": "true", "submit": submit1})
                                ag=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dat, cookies={'cookie': cookie}).text, 'html.parser')
                                checkcp(ag)
                                try:
                                    os.system('cat /sdcard/2fakey.txt | grep '+email+' > .key.txt')
                                except:
                                    pass
                                try:
                                    red=open('.key.txt', 'r').read()
                                    zed=red.split('|')[2].split('\n')[0]
                                except:
                                    zed='Key not found'
                                print ('Key > '+zed)
                                coded(ag)
                                print ('successfuly 2fa done')
                                input('press enter to back')
                                menu()
                else:
                    menu()
        print ('data not found')
        input('Press enter to back')
        menu()
    except requests.exceptions.SSLError:
        os.system('clear')
        print (logo4)
        print ('internet problem')
        time.sleep(3)
        menu()
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (logo4)
        print ('internet problem')
        time.sleep(3)
        menu()
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        print (logo4)
        print ('Oops Wrong input Try Again')
        sys.exit()
    except Exception as e:
        print ('data not found')
        input('Press enter to back')
        menu()

def change():
    os.system('clear')
    print (logo4)
    print ('~~~~~~~~~~~~~Password Change menu~~~~~~~~~~~')
    print (47*'-')
    cok=input('Paste cookie: ')
    pwold=input('Current password: ')
    pwnew=input('New password: ')
    coki=cok.replace(' ', '')
    cokie = coki+';'
    try:
        datr=cokie.split('datr=')[1].split(';')[0]
        fr=cokie.split('fr=')[1].split(';')[0]
        c_user=cokie.split('c_user=')[1].split(';')[0]
        xs=cokie.split('xs=')[1].split(';')[0]
        cokiee='datr='+datr+';'+'fr='+fr+';'+'c_user='+c_user+';'+'xs='+xs+';'
    except:
        datr=cokie.split('datr=')[1].split(';')[0]
        c_user=cokie.split('c_user=')[1].split(';')[0]
        xs=cokie.split('xs=')[1].split(';')[0]
        cokiee='datr='+datr+';'+'c_user='+c_user+';'+'xs='+xs+';'
    cookie=cokiee
    language(cookie)
    try:
        ses=requests.Session()
        ref = BeautifulSoup(ses.get("https://x.facebook.com/settings/security/password", cookies={'cookie':cookie}).text, "html.parser")
        checkcp(ref)
        if '/login.php?next=' in str(ref):
            print ('Maybe your account cp or lock login your account in your kiwi browser if get login success then take new cookie from kiwi browser and try again')
            input('Press enter to back')
            menu()
        elif 'facebook.com/zero/toggle/nux/' in str(ref):
            print ('Cokie not accept first login account in your kiwi browser and get new cookie from kiwi browser and try again')
            input('Press enter to back')
            menu()
        else:
            pass
        for y in ref.find_all("a",href=True):
            if '/zero/optin/write/?action=cancel' in str(y):
                reff=y.get('href')
                aj=BeautifulSoup(ses.get('https://x.facebook.com'+reff, cookies={'cookie':cookie}).text, 'html.parser')
                checkcp(aj)
                for x in aj.find_all('form', {'method': 'post'}):
                    if '/zero/optin/write/?action=confirm' in str(x):
                        link=x.get('action')
                        use=re.findall('data-sigil="touchable" type="submit" value="(.*?)"', str(x))
                        for t in use:
                            use1=t
                        dog={}
                        for z in x('input'):
                            dog.update({z.get("name"):z.get("value")})
                        dog.update({'submit': use1})
                        aa=BeautifulSoup(ses.post('https://x.facebook.com'+link, data=dog, cookies={'cookie':cookie}).text, 'html.parser')
                        ref = BeautifulSoup(ses.get("https://x.facebook.com/settings/security/password", cookies={'cookie':cookie}).text, "html.parser")
                        checkcp(ref)
        for x in ref.find_all("form", {"method":"post"}):
            if '/password/change/?redirect_uri=' in str(x):
                link=x.get('action')
                bl=['fb_dtsg', 'jazoest', 'password_change_session_identifier']
                submit=re.findall('data-sigil="touchable" name="save" type="submit" value="(.*?)"', str(x))
                for y in submit:
                    submit1=y
                datas={}
                for v in x('input'):
                    if v.get("name") in bl:
                        try:
                            datas.update({v.get("name"):v.get("value")})
                        except:
                            pass
                datas.update({"password_old":pwold, "password_new":pwnew, "password_confirm":pwnew, "save":submit1})
                try:
                    response = BeautifulSoup(ses.post("https://x.facebook.com"+link, data=datas, cookies={'cookie':cookie}).text, 'html.parser')
                    checkcp(response)
                except requests.exceptions.SSLError:
                    os.system('clear')
                    print (logo4)
                    print ('internet problem')
                    time.sleep(3)
                    menu()
                except requests.exceptions.ConnectionError:
                    os.system('clear')
                    print (logo4)
                    print ('internet problem')
                    time.sleep(3)
                    menu()
                for x in response.find_all('form', {'method': 'post'}):
                    if 'settings/account/password/survey/' in str(x):
                        link=x.get('action')
                        submit=re.findall('name="submit_action" type="submit" value="(.*?)"', str(x))
                        gl=['fb_dtsg', 'jazoest']
                        datt={}
                        for z in x('input'):
                            if z.get('name') in gl:
                                try:
                                    datt.update({z.get('name'):z.get('value')})
                                except:
                                    pass
                        datt.update({'session_invalidation_options': 'keep_sessions', 'submit_action': submit})
                        dov=ses.post('https://x.facebook.com'+link, data=datt, cookies={'cookie':cookie}).text
                        print ('Successfuly pass changed')
                        input('Press enter to back')
                        menu()
                print ('Maybe pass wrong or maybe account on cp or lock')
                input('Press enter to back')
                menu()
    except requests.exceptions.SSLError:
        os.system('clear')
        print (logo4)
        print ('internet problem')
        time.sleep(3)
        menu()
    except requests.exceptions.ConnectionError:
        os.system('clear')
        print (logo4)
        print ('internet problem')
        time.sleep(3)
        menu()
    except (KeyboardInterrupt, EOFError):
        os.system('clear')
        print (logo4)
        print ('Oops Wrong input Try Again')
        sys.exit()
    except Exception as e:
        print ('Maybe wrong pass or maybe account on cp or lock')
        input('Press enter to back')
        menu()

menu()

