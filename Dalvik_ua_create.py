#SOURCE BY YOUNIS JOHN
#GITJUB: https://github.com/YounisXyz
#FACEBOOK: https://www.facebook.com/xyzhackers

#~~~~~~~~~~~~~~~~~~~~~~~~~#

# [ CPDE BY - YOUCEF HAFAFNI ] 

#__________[UA MAFIA / YOUCEF HAFAFNI]__________#
import random
def ua(): 
	density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
	width = random. choice(["720", "1080", "1280"])
	height = random.choice(["720", "1080", "1280", "1440", "1920"])
    build = random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
    fbdv = random.choice(["CPH7800", "CPH3818", "CPH4987", "CPH1600"])
    END = f"[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{{density={density},width={width},height={height}}};FBLC/en-GB;FBRV/279865282;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{fbdv};FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua = 'Davik/2.1.0 (Linux;  U; Android '+str(random.randrange(5,12))+'.0.1; '+str(fbdv)+' Build/'+str(build)+') '+END
    return ua
print(ua())