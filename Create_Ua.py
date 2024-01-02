#this tool Creat By MR NAIB 
#FOLLOW ME ON GITHUB : Mafyia313
#Enjoy The Best UA Creat Tool 
#This script is Very easy to modified


import random
import time

# Customize the lists with your desired values
FBAV_OPTIONS = ["", "YZWSES93", "4Q095MQG", "A1XDL5U4"]
DENSITY_OPTIONS = ["1.5", "2.0", "2.5", "3.0"]
WIDTH_OPTIONS = [720, 1080, 1440, 1920, 2560]
HEIGHT_OPTIONS = [1280, 1920, 2560, 3840, 4096]
FBLC_OPTIONS = ["fr_FR", "en_US", "es_ES", "de_DE", "it_IT", "ru_RU", "zh_CN", "ja_JP"]
FBDV_OPTIONS = ["SM-N980BDS", "SM-G970F", "iPhone12,8", "HTC_U11", "Pixel_5", "Redmi_Note_9","SM-N980BDS", "SM-G970F", "iPhone12,8", "HTC_U11", "Pixel_5", "Redmi_Note_9",
    "Galaxy_S21", "OnePlus_9", "Mi_11", "Poco_F3", "Xperia_1_III", "Mate_40_Pro",
    "Moto_G60", "ZenFone_8", "Vivo_X60_Pro", "Nokia_X20", "Pixel_6", "Galaxy_S22",
    "iPhone13,1", "Redmi_10", "Xperia_5_III", "OnePlus_9T", "Mi_11T_Pro", "Realme_GT",
    "Xiaomi_Mi_12", "Oppo_F19", "LG_G9", "Sony_Xperia_10_IV", "Nokia_9_3", "OnePlus_10",
    "Vivo_V21", "Xiaomi_Mi_11X", "Motorola_Moto_G100", "HTC_Desire_21", "Realme_X9",
    "Nokia_X60", "Samsung_Galaxy_A32", "OnePlus_Nord_CE", "Sony_Xperia_1_IV", "Xiaomi_Mi_12T",
    "Oppo_Reno_6", "Motorola_Moto_E7", "LG_Wing", "HTC_U20", "Realme_X7", "Nokia_X70",
    "Vivo_Y53s", "Xiaomi_Mi_Mix_4", "Samsung_Galaxy_F42", "OnePlus_Nord_N10", "Sony_Xperia_5_IV",
    "Xiaomi_Mi_12S", "Oppo_Reno_7", "Motorola_Moto_G200", "LG_Velvet", "HTC_Drive_7", "Realme_X8",
    "Nokia_X80", "Vivo_Y73s", "Xiaomi_Mi_Mix_5", "Samsung_Galaxy_A42", "OnePlus_Nord_N100",
    "Sony_Xperia_5A", "Xiaomi_Mi_12R", "Oppo_Reno_8", "Motorola_Moto_G300", "LG_Q6", "HTC_Drive_8",
    "Realme_X9 Pro", "Nokia_X90", "Vivo_Y93s", "Xiaomi_Mi_Mix_6", "Samsung_Galaxy_F52",
    "OnePlus_Nord_N200", "Sony_Xperia_5B", "Xiaomi_Mi_12T Pro", "Oppo_Reno_9", "Motorola_Moto_G400",
    "LG_Q7", "HTC_Drive_9", "Realme_X10", "Nokia_X100", "Vivo_Y95s", "Xiaomi_Mi_Mix_7",
    "Samsung_Galaxy_A52", "OnePlus_Nord_N300", "Sony_Xperia_5C", "Xiaomi_Mi_12U",
    "Oppo_Reno_10", "Motorola_Moto_G500", "LG_Q8", "HTC_Drive_10", "Realme_X11", "Nokia_X110",
    "Vivo_Y100s", "Xiaomi_Mi_Mix_8", "Samsung_Galaxy_F62", "OnePlus_Nord_N400", "Sony_Xperia_5D",
    "Xiaomi_Mi_12V", "Oppo_Reno_11", "Motorola_Moto_G600", "LG_Q9", "HTC_Drive_11", "Realme_X12",
    "Nokia_X120", "Vivo_Y110s", "Xiaomi_Mi_Mix_9", "Samsung_Galaxy_A62", "OnePlus_Nord_N500",
    "Sony_Xperia_5E", "Xiaomi_Mi_12W", "Oppo_Reno_12", "Motorola_Moto_G700", "LG_Q10",
    "HTC_Drive_12", "Realme_X13", "Nokia_X130", "Vivo_Y120s", "Xiaomi_Mi_Mix_10",
    "Samsung_Galaxy_F72", "OnePlus_Nord_N600", "Sony_Xperia_5F", "Xiaomi_Mi_12X",
    "Oppo_Reno_13", "Motorola_Moto_G800", "LG_Q11", "HTC_Drive_13", "Realme_X14", "Nokia_X140",
    "Vivo_Y130s", "Xiaomi_Mi_Mix_11", "Samsung_Galaxy_A72", "OnePlus_Nord_N700",
    "Sony_Xperia_5G", "Xiaomi_Mi_12Y", "Oppo_Reno_14", "Motorola_Moto_G900", "LG_Q12",
    "HTC_Drive_14", "Realme_X15", "Nokia_X150", "Vivo_Y140s", "Xiaomi_Mi_Mix_12",
    "Samsung_Galaxy_F82", "OnePlus_Nord_N800", "Sony_Xperia_5H", "Xiaomi_Mi_12Z",
    "Oppo_Reno_15", "Motorola_Moto_G1000", "LG_Q13", "HTC_Drive_15", "Realme_X16",
    "Nokia_X160", "Vivo_Y150s", "Xiaomi_Mi_Mix_13", "Samsung_Galaxy_A82", "OnePlus_Nord_N900",
    "Sony_Xperia_5I", "Xiaomi_Mi_12ZA", "Oppo_Reno_16", "Motorola_Moto_G1100", "LG_Q14",
    "HTC_Drive_16", "Realme_X17", "Nokia_X170", "Vivo_Y160s", "Xiaomi_Mi_Mix_14",
    "Samsung_Galaxy_F92", "OnePlus_Nord_N1000", "Sony_Xperia_5J", "Xiaomi_Mi_12ZB",
    "Oppo_Reno_17", "Motorola_Moto_G1200", "LG_Q15"]
FBSV_OPTIONS = ["11", "12", "13", "14", "15", "16", "17"]
FBOP_OPTIONS = ["4", "5", "6", "7", "8"]
FBCA_OPTIONS = ["arm64-v8a", "armeabi-v7a", "x86", "x86_64", "armeabi"]

def generate_user_agent():
    fban_fbaa = random.choice(["FBAN", "FB4A"])
    fbav = random.choice(FBAV_OPTIONS)
    fbbv = random.randint(100000000, 999999999)
    density = random.choice(DENSITY_OPTIONS)
    width = random.choice(WIDTH_OPTIONS)
    height = random.choice(HEIGHT_OPTIONS)
    fbdm = f"/*{{density={density},width={width},height={height}}}"
    fblc = random.choice(FBLC_OPTIONS)
    fbrv = random.randint(100000000, 999999999)
    fbcr = random.choice(["OPPO", "TECNO", "Realme", "Sony", "LG", "Nokia"])
    fbmf = random.choice(["VIVO", "Apple", "Xiaomi", "OnePlus", "Motorola"])
    fbbd = random.choice([    "Samsung", "Huawei", "iPhone", "Google", "ASUS", "Sony", "LG", "Xiaomi", "Motorola",
    "Nokia", "Lenovo", "BlackBerry", "Oppo", "Vivo", "Realme", "OnePlus", "HTC",
    "ZTE", "Meizu", "Infinix", "Tecno", "Xolo", "Micromax", "Honor", "Sharp", "Lenovo",
    "Panasonic", "Asus", "Lava", "Gionee", "HMD_Global", "Honor", "LeEco", "Lenovo",
    "Micromax", "Nubia", "Oppo", "Panasonic", "Realme", "Sharp", "Sony", "Vivo",
    "Xiaomi", "Motorola", "Nokia", "Blackberry", "Google", "HTC", "LG", "Lenovo",
    "OnePlus", "Realme", "Sony", "Vivo", "ZTE", "Alcatel", "Amazon", "Blackview",
    "Blu", "Cubot", "Elephone", "Gigaset", "Hisense", "Infinix", "Karbonn", "Kazam",
    "Kyocera", "Lephone", "Medion", "Meizu", "Micromax", "Nextbit", "Nubia", "NuVision",
    "Obi", "Onida", "Oppo", "Palm", "Parla", "Poco", "Razer", "Realme", "Sanyo", "Spice",
    "Tecno", "Verykool", "Vivo", "Wiko", "Xolo", "YU", "Zebra", "ZTE", "ZUK",
    "QMobile", "Haier", "Tecno", "itel", "Telenor", "Nokia", "Infinix", "Motorola",
    "OPhone", "Rivo", "VGO Tel", "G'Five", "Megagate", "Club Mobile", "Voice Mobile",
    "Calme", "GFive", "HTC", "Honor", "LG", "Meizu", "OnePlus", "Oppo", "Realme", "Sony",
    "Vivo", "Xiaomi", "ZTE"])
    fbpn = "com.facebook.katana"
    fbdv = random.choice(FBDV_OPTIONS)
    fbsv = random.choice(FBSV_OPTIONS)
    fbop = random.choice(FBOP_OPTIONS)
    fbca = random.choice(FBCA_OPTIONS)
    fbss = random.choice([random.randint(10, 20), ""])

    user_agent = f"[{fban_fbaa}/;FBAV/{fbav};FBBV/{fbbv};FBAN/{fban_fbaa};FBAV/{fbav};FBBV/{fbbv};FBDM/{fbdm};FBLC/{fblc};FBRV/{fbrv};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{fbdv};FBSV/{fbsv};FBOP/{fbop};FBCA/{fbca};FBSS/{fbss};]"

    return user_agent

def generate_user_agents(count):
    user_agents = [generate_user_agent() for _ in range(count)]
    return user_agents

def main():
	# ASCII logo
    print("""
       _    _         
 | |  | |  /\    
 | |  | | /  \   
 | |  | |/ /\ \  
 | |__| / ____ \ 
  \____/_/    \_\                                  
  \033[0;34m This tool Created By  √  Mr Naib
  \033[0;34m Use this tool and get √ UA
  \033[0;34m Fcabeook Name : MR NAIB
  \033[0;34m Github : Mafyia313
 ________________________________,,,________________________,


    """)
    
    num_user_agents = int(input("\033[1;33m How many user agents do you want to create? "))
    user_agents = generate_user_agents(num_user_agents)
    print("\033[0;31m Generating User Agents loading..")
    time.sleep(8)
    

    print("\033[0;32m Generated User Agents:")
    for idx, user_agent in enumerate(user_agents, start=1):
        print(f"User Agent { idx}: {user_agent}")

if __name__ == "__main__":
    main()
