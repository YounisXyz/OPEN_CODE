import random
fban = random.choice(["FB4A"])
facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
fbbv = str(random.randint(10000000, 66666666))
density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
width = random.choice(["720", "1080", "1280"])
height = random.choice(["720", "1080", "1280", "1440", "1920"])
#fbrv = str(random.randint(10000000, 99999999))
fbcr = random.choice(['Nepal_Telecom', 'DOCTYPE', 'MTN-CG', 'Cellcom', 'Salaam Telecom', 'BASE'])
#model = random.choice(self.models).rsplit('|')
fblc = random.choice(["en_US", "en_GB", "en_PK"])
fbbd = 'samsung'
fbpn = random.choice(["com.facebook.katana"])
fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
fbmf = 'samsung'
fbdv = random.choice(["SM-G920F", "SM-T535", "SM-T231", "SM-J320F", "GT-I9190", "GT-N7100", "SM-T561", "GT-N7100", "GT-I9500", "SM-J320F", "SM-G930F", "SM-J320F", "SM-J510FN", "GT-P5100", "SM-J320F", "SM-T531", "SPH-L720", "GT-I9500"])
user_agent= f"\033[0;32m[FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{fbdv};FBSV/{fbsv};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
print(user_agent)

    