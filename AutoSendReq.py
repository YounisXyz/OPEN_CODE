import os, requests, re, time, sys
 
def logo():
    print("\n\x1b[1;97m\n\t\n        d8888b. .d8888. d8b   db\n        88  `8D 88'  YP 888o  88\n    \x1b[1;95m    88oooY' `8bo.   88V8o 88\n        88~~~b.   `Y8b. 88 V8o88\n   \x1b[1;97m     88   8D db   8D 88  V888\n        Y8888P' `8888Y' VP   V8P\n-------------------------------------------\n => Author  :  BILAL KHAN\n => Github  :  https://github.com/BIL4L-KH4N\n => Tools   :  Auto Friend Requests\n-------------------------------------------")
    
def file():
    os.system('clear')
    logo()
    print("         \x1b[1;97m    Put File Path")
    print('-------------------------------------------')
    fil = input(' [+] File : ')
    print('\x1b[1;97m-------------------------------------------')
    return open(fil,'r').read().splitlines()
 
 
def req(idx,cookies,fb_dtsg,j2,uid):
    #print(ids)
    try:
        headers = {'authority': 'web.facebook.com','accept': '*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https://web.facebook.com','referer': 'https://web.facebook.com/','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"','sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Linux"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36','viewport-width': '980','x-asbd-id': '129477','x-fb-friendly-name': 'FriendingCometFriendRequestSendMutation','x-fb-lsd': '_HXdQr8kHu0XQKU7XKSGvZ',}        
        data = {
            'av': uid,
            '__user': uid,
            '__a': '1',
            '__req': '2v',
            '__hs': '',
            'dpr': '1',
            '__ccg': 'GOOD',
            '__rev': '',
            '__s': '',
            '__hsi': '',
            '__dyn': '',
            '__csr': '',
            '__comet_req': '15',
            'fb_dtsg': fb_dtsg,
            'jazoest': j2,
            'lsd': '',
            '__spin_r': '',
            '__spin_b': '',
            '__spin_t': '',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1687455775544,420893,190055527696468,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,unexpected,1687455771503,169129,391724414624676,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1687455767259,87694,391724414624676,","friend_requestee_ids":["'+idx+'"],"refs":[null],"source":"profile_button","warn_ack_for_ids":[],"actor_id":"'+uid+'","client_mutation_id":"3"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '6355998154485513',
        }
        post = requests.post('https://web.facebook.com/api/graphql/', cookies=cookies, headers=headers, data=data)
        result = 'success'
    except:
       result = 'Error'
    return result
        
        
 
os.system('clear')
logo()
try:
    print("      \x1b[1;97m       Put Your Cookies")
    print('-------------------------------------------')
    cookie = input(" [+] Cookies : ")
    cookies = {'cookie' : cookie}
    uid = cookie.split('c_user=')[1].split(';')[0]
    res = requests.get('https://m.facebook.com/', cookies=cookies).text
    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(res)).group(1)
    j2 = re.search('name="jazoest" value="(.*?)"', str(res)).group(1)
    print('-------------------------------------------')
    print(' [+] Successfully activated as \x1b[1;92m'+uid+' \x1b[1;97m:) ')
    print('-------------------------------------------');time.sleep(2)
    try:
        filee = file()
    except Exception as e:
        print(e)
        os.sys.exit()
    try:
        for idz in filee:
            try:
                idx,names = idz.split('|')
            except:
                idx = idz
            #print(idx)
            opp = req(idx,cookies,fb_dtsg,j2,uid)
            if 'success' in opp:
                print('  \x1b[1;97m>> Sending Request To : \x1b[1;92m'+idx)
                print('\x1b[1;97m-------------------------------------------')
            else:
                print('  \x1b[1;91m>> Cookie Or Link Invalid .....! ')
                print('\x1b[1;97m-------------------------------------------')
        os.sys.exit()
        
    except Exception as e:
        print(e)
        os.sys.exit()
    
except Exception as e:
    print(e)
 