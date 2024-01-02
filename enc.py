# -*- coding: UTF-8 -*-.
##################################################################
#                             OPEN SOURCE                        #
#                                                                #                                                               
#                                                                #
#    BOLEH DI RECOD TAPI CANTUMKAN NAMA AUTHOR YA KONTOL         #
#                                                                #
#               AUTHOR > Boy Hamzah                              #
#               GITHUB   > https://github.com/BOY-H4MZ4H         #
#               FACEBOOK > https://github.com/Boy.Hamzaah        #
#               TEAM  > XNSCODE                                  #
#                                                                #
#                                                                #
##################################################################
#                JANGAN DI EDIT EDIT LAGI YA BROOO               #
##################################################################
import sys, argparse, codecs, binascii, time
from os import system, remove
from sys import argv
from random import choice, shuffle
class NamaMenurun(object):
	def __init__(self, string):
		for i in string + '\n':
			sys.stdout.write(str(i))
			sys.stdout.flush()
			time.sleep(5e-05)
class LambdaEncode:
	def __init__(self):
		self.xnscode = '# Encode Lambda Boy Hamzah\n# Follow Github Ku Dan Github Organisasi Kami Jangan Lupa Kasi Bintang Nya\n# https://github.com/BOY-H4MZ4H\n# https://github.com/XNSCODE\n\nexec((lambda __, _, : _(%s,__))("%s",__import__(\'codecs\').decode))'
		self.Eksekusi()
	def Eksekusi(self):
		system('clear')
		exec((lambda __, _, : _('# Rapbqr Ynzoqn Obl Unzmnu\n# Sbyybj Tvguho Xh Qna Tvguho Betnavfnfv Xnzv Wnatna Yhcn Xnfv Ovagnat Aln\n# uggcf://tvguho.pbz/OBL-U4ZM4U\n# uggcf://tvguho.pbz/KAFPBQR\n\nrkrp((ynzoqn __, _, : _(\'# Encode Lambda Boy Hamzah\\a# Follow Github Ku Dan Github Organisasi Kami Jangan Lupa Kasi Bintang Nya\\a# https://github.com/BOY-H4MZ4H\\a# https://github.com/XNSCODE\\a\\aexec((lambda __, _, : _(\\\'AnznZraheha("""        _______ _______ ______  ______  _______\\\\n |      |_____| |  |  | |_____] |     \\\\\\\\ |_____|\\\\n |_____ |     | |  |  | |_____] |_____/ |     |\\\\n \\\\nNH > Obl Unzmnu\\\\nTU > uggcf://tvguho.pbz/OBL-U4ZM4U\\\\nSO > uggcf://jjj.snprobbx.pbz/Obl.Unzmnnu\\\\nGZ > KAFPBQR""")\\\\n\\\',__))("rot_13",__import__(\\\'codecs\\\').decode))\',__))("ebg_13",__vzcbeg__(\'pbqrpf\').qrpbqr))',__))("rot_13",__import__('codecs').decode))
		try:
			print ("\n01.) Encode Lambda python3 Rot 13\n02.) Info Script\n00.) Keluar")
			inp = int(input("\n> "))
			if inp == 2:
				NamaMenurun("\nAuthor Script Boy Hamzah\n\nTeam XNSCODE\n\n-------------------------------------\nAngga\nYayan\nBoy Hamzah\nRizal\nM.Rizky\nDapunta\nLatip\nHan\nFallen\nIqbal\n-------------------------------------")
			elif inp == 1:
				lapis = 0
				file = input("\n[ CONTOH ] /sdcard/xnscode/file.py\n\nNama File > ")
				total = int(input("\nMau Berapa Lapis Compile.? Max 10\n\n> "))
				if ( total < 11 ):
					out = input("\nOutput > ")
					sex = open(file).read()
					boy = repr(codecs.encode(sex, 'rot_13'))
					f = open(out, 'w')
					f.write(self.xnscode % (boy, 'rot_13'))
					f.close()
					while ( total >= lapis ):
						xn = open(out).read()
						ses = repr(codecs.encode(xn, 'rot_13'))
						f = open(out, 'w')
						f.write(self.xnscode % (ses,
										 'rot_13'))
						f.close()
						print(f"\r{lapis}")
						lapis += 1
					print ("\nFile Berhasil Di Compile")
					print(f"\nNama File > {out}")
			elif inp == 0:
				exit(f'Good Bye')
			else:
				exit("\nEngkau Buta Kah Anjing")
		except (KeyboardInterrupt,EOFError):
			exit("\nSelamat Tinggal")
		except ValueError:
			exit("\nHarus Angka...")
		except FileNotFoundError:
			exit(f"\nNama File Dari > [ {file} ] Tidak Ada")
if __name__ == '__main__':
    LambdaEncode()
