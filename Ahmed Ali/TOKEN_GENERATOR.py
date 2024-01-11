##FULL CREDIT - TechQaiser
##Owner's github : https://github.com/techqaiser
import os,requests,re
try:
	from bs4 import BeautifulSoup as bs
except:
	os.system('pip install bs4')
cooke = input(' cookie : ')
cookie = {'Cookie': cooke}
xyz = requests.session()
data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
req = xyz.post('https://graph.facebook.com/v16.0/device/login/', data=data).json()
cd = req['code']
ucd = req['user_code']
url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038' % (
    cd)
req = bs(xyz.get('https://mbasic.facebook.com/device', cookies=cookie).content, 'html.parser')
raq = req.find('form', {'method': 'post'})
dat = {'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
        'fb_dtsg': re.search('name="fb_dtsg" type="hidden" value="(.*?)"', str(req)).group(1), 'qr': '0',
        'user_code': ucd}
rel = 'https://mbasic.facebook.com' + raq['action']
pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
dat = {}
raq = pos.find('form', {'method': 'post'})
for x in raq('input', {'value': True}):
    try:
        if x['name'] == '__CANCEL__':
            pass
        else:
            dat.update({x['name']: x['value']})
    except Exception as e:
        pass
rel = 'https://mbasic.facebook.com' + raq['action']
pos = bs(xyz.post(rel, data=dat, cookies=cookie).content, 'html.parser')
req = xyz.get(url, cookies=cookie).json()
if 'access_token' in req:
    print('\033[1;36m Token ' + req['access_token'])
    exit()
else:
    exit('\033[1;31m Invalid COokie Or Something WEnt WRong')
