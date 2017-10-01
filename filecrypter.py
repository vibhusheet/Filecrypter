'''
Generic command line Filecrypter in python
Imported libraries
sys:- For system operations like I/O
uuid:- For generating random key
getopt:- For command line arguments
hashlib:- For sha256 hash encryption

'''
import sys, uuid, getopt, hashlib

#Imports a file, returns text as a string
def get(file_name):
	lines = list(open(file_name,"r").readlines())
	text = ""
	for i in lines:
		text += i
	return text

#Writes text in a truncated file
def set(file_name, text):
	fp = open(file_name,"w")
	fp.truncate()
	fp.write(text)

#Used to generate a SHA256 hash using a key
def hash(key):
	key1 = key.encode('utf-8')
	return ((hashlib.sha256(key1)).hexdigest())

#Used to check if the file has already been encrypted and verifies the key
def check(text, key):
		x = ""
		y = hash(key)
		lines = text.split("\n")
		length = len(lines)
		if(lines[0]==y):
			for i in range(1, length-1):
					x = x+ lines[i]+"\n"
			x = x + lines[length-1]
			return x, 1
		return text, 0

#used to generate a random key
def random():
	return(str(uuid.uuid4()))

#bitwise XOR of characters of key and text to encrypt/decrypt
def crypt(pre_text, key):
	post_text = ""
	counter = 0
	try:
		for i in pre_text:
			xbyte = ord(i) ^ ord(key[j])
			counter += 1
			counter = counter % len(k)
			post_text += (chr(xbyte))
	finally:
 		return (post_text)

def main(argv):
	input_file = ''
	output_file = ''
	key = ''
	flag1 = 0
	flag2 = 0
	flag3 = 0
	try:
		opts, args = getopt.getopt(argv, "hi:o:k:", ["-i","-o","-k"])
	except getopt.GetoptError:
		print("Usage: test.py -i <input_file> -o <output_file> -k <key_for_encryption>")
		sys.exit(0)
	for opt, arg in opts:
		if opt in ("-h", "-help"):
			print("Usage: test.py -i <input_file> -o <output_file> -k <key_for_encryption>\ndefault action without -i : takes input in the terminal\ndefault action without -o : displays output in terminal\ndefault action without -k : generates random key, which has to be inputed at the time of decryption\n")
			sys.exit(1)
		elif opt in ('-i', "--inputfile"):
			flag1 = 1
			input_file = arg
		elif opt in ('-o', "--outputfile"):
			flag2 = 1
			output_file = arg
		elif opt in ("-k", "--key"):
			flag3 = 1
			key = arg
	if flag3==0:
		key = random()
		print("Random Key generated *(save for decryption)* :", key)
	else:
		print("Key:", key)
	if flag1==1:
		print("Input file:", input_file)
		fpi = get(input_file)
		fp1, y = check(fpi, key)
		s1 = crypt(fp1, key)
		if y==0:
			s1 = hash(key)+"\n"+s1
		if flag2 == 1:
			print("Output file:", output_file)
			set(output_file, s1)
		else:
			print("Output\n"+s1)
	else:
		text = input("no Input file:\nenter text to encrypt:\n")
		s1 = hash(key)+"\n"+crypt(text,key)
		if flag2 == 1:
			set(output_file, s1)
		else:
			print("Output\n"+s1)

if __name__ == "__main__":
	main(sys.argv[1:])
