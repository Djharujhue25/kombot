#!/usr/bin/python3
# Sptty Chan
# Open Source Code
import os,requests,json,random

# CLEAR

def clear():
	os.system("clear")

# BANNER

def banner():
	print("""
╭━━╮╭━━━┳━━━━╮
┃╭╮┃┃╭━╮┃╭╮╭╮┃
┃╰╯╰┫┃╱┃┣╯┃┃╰╯
┃╭━╮┃┃╱┃┃╱┃┃ 🄰🅄🅃🄷🄾🅁 : Farel Hekel
┃╰━╯┃╰━╯┃╱┃┃ 🄶🄸🅃🄷🅄🄱 : Github.com/Farel-Hekel
╰━━━┻━━━╯╱╰╯ 🄵🄱     : Facebook.com/1801249672""")

# LOGIN

def log():
	clear()
	banner()
	os.system("rm -rf bokep.json")
	print("\n--------------------------------------------------")
	bos = input("\n[=] Masukan Token : ")
	try:
		cok = requests.get("https://graph.facebook.com/me?access_token="+bos)
		y = json.loads(cok.text)
		nama = y["name"]
		mek = open("tokek.json","w")
		mek.write(bos)
		mek.close()
		zex = open("bokep.json","w")
		zex.write(bos)
		zex.close()
		print("[=] Login Berhasil")
		menu()
	except KeyError:
		print("[=] Token Kadaluarsa")
		log()

# MENU

def menu():
	clear()
	banner()
	os.system("rm -rf id.json kom.json")
	try:
		token = open("tokek.json","r").read()
		cok = requests.get("https://graph.facebook.com/me?access_token="+token)
		y = json.loads(cok.text)
		nama = y["name"]
	except (KeyError,IOError):
		print("[=] Login Dulu")
		log()
	print("\n--------------------------------------------------")
	print("\n[1] Bot Komentar")
	print("[2] Tambahkan Token")
	print("[0] Log Out")
	pilih()

# PILIH MENU

def pilih():
	sc = input("\n[=] Pilih : ")
	if sc=="":
		pilih()
	elif sc=="1":
		komen()
	elif sc=="2":
		tok = input("\n[=] Masukan Token : ")
		cs = open("bokep.json","a")
		cs.write(","+tok)
		cs.close()
		print("[=] Token Ditambahkan")
		input("[=] Kembali")
		menu()
	elif sc=="0":
		os.system("rm -rf tokek.json bokep.json")
		print("[=] Terimakasih Sudah Menggunakan SC Saya.!!!")
		exit()
	else:
		pilih()

# KOMEN

def komen():
	os.system("rm -rf id.json kom.json")
	try:
		token = open("tokek.json","r").read()
		cok = requests.get("https://graph.facebook.com/me?access_token="+token)
		y = json.loads(cok.text)
		nama = y["name"]
	except (KeyError,IOError):
		print("[=] Login Dulu")
		log()
	ki = input("\n[=] Masukan ID Postingan Publik : ")
	v = open("id.json","w")
	v.write(ki)
	v.close()
	print("\n[=] Masukan Teks Komentar...")
	print("[=] Gunakan Koma (,) Untuk Komentar Random")
	print("[=] Contoh : Kucing Kontol,Muka Lu Kayak Kontol,Bangsat")
	ka = input("[=] Komentar : ")
	w = open("kom.json","w")
	w.write(ka)
	w.close()
	say = open("id.json","r").read()
	soy = open("kom.json","r").read()
	soyy = soy.split(",")
	bc = open("bokep.json","r").read()
	gi = bc.split(",")
	bb = int(input("[=] Masukan Jumlah Komentar : "))
	print("\n[=] Mulai...")
	for k in range(bb):
		k +=1
		bo = random.choice(gi)
		id = say
		ko = random.choice(soyy)
		yt = requests.post("https://graph.facebook.com/"+id+"/comments/?message="+ko+"&access_token="+bo)
		bh = json.loads(yt.text)
		if "id" in bh:
			print("[=] Komentar Ke %s Berhasil Dikirim" %(k))
		if "error" in bh:
			print("[=] Komentar Ke %s Gagal Dikirim" %(k))
	print("[=] Selesai")
	input("[=] Kembali")
	menu()
menu()
