#!/usr/bin/python3
#-*-coding:utf-8-*-

import os,requests,sys,time

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)

def logo():
    print("""
  ___ ___   _    ___   ___ 
 |_ _| _ \ | |  / _ \ / __|
  | ||  _/ | |_| (_) | (__ 
 |___|_|   |____\___/ \___|""")

def menu():
    os.system("clear")
    logo()
    print("\n1. Track IP Kamu")
    print("2. Track IP Target")
    mn = input("\nPilih : ")
    if mn in [""]:
        jalan("\nIsi Yang Benar !")
        menu()
    elif mn in ["1","01"]:
        ipkamu()
    elif mn in ["2","02"]:
        iptarget()
    else:
        jalan("\nIsi Yang Benar !")
        menu()
    
def ipkamu():
    a = requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    try:
        bn = a["status"]
    except KeyError:
        bn = " "
    try:
        ng = a["country"]
    except KeyError:
        ng = " "
    try:
        cc = a["countryCode"]
    except KeyError:
        cc = " "
    try:
        pr = a["regionName"]
    except KeyError:
        pr = " "
    try:
        kt = a["city"]
    except KeyError:
        kt = " "
    try:
        kb = a["zip"]
    except KeyError:
        kb = " "
    try:
        tz = a["timezone"]
    except KeyError:
        tz = " "
    try:
        sp = a["isp"]
    except KeyError:
        sp = " "
    jalan("\nStatus : " + bn)
    jalan("IP Kamu : " + ip)
    jalan("Negara : " + ng)
    jalan("Kode Negara : " + cc)
    jalan("Provinsi : " + pr)
    jalan("Kota : " + kt)
    jalan("Kode Pos : " + kb)
    jalan("Zona Waktu : " + tz)
    jalan("Provider : " + sp)
    jalan("Info Lengkap : http://ip-api.com/#" + ip)
    kembali()

def iptarget():
    b = input("Masukkan IP Target : ")
    if b in [""]:
        jalan("\nIsi Yang Benar !")
        menu()
    a = requests.get("http://ip-api.com/json/"+b,headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    try:
        bn = a["status"]
    except KeyError:
        bn = " "
    try:
        ng = a["country"]
    except KeyError:
        ng = " "
    try:
        cc = a["countryCode"]
    except KeyError:
        cc = " "
    try:
        pr = a["regionName"]
    except KeyError:
        pr = " "
    try:
        kt = a["city"]
    except KeyError:
        kt = " "
    try:
        kb = a["zip"]
    except KeyError:
        kb = " "
    try:
        tz = a["timezone"]
    except KeyError:
        tz = " "
    try:
        sp = a["isp"]
    except KeyError:
        sp = " "
    jalan("\nStatus : " + bn)
    jalan("IP Target : " + ip)
    jalan("Negara : " + ng)
    jalan("Kode Negara : " + cc)
    jalan("Provinsi : " + pr)
    jalan("Kota : " + kt)
    jalan("Kode Pos : " + kb)
    jalan("Zona Waktu : " + tz)
    jalan("Provider : " + sp)
    jalan("Info Lengkap : http://ip-api.com/#" + ip)
    kembali()

def kembali():
    input("\n[ Kembali ]")
    menu()

if __name__=="__main__":
	menu()