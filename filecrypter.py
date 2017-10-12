'''
Generic command line Filecrypter in python
Imported libraries
sys:- For system operations like I/O
uuid:- For generating random key
getopt:- For command line arguments
hashlib:- For sha256 hash encryption
'''

import sys
import uuid
import getopt
import hashlib


def get_text(file_name):
    """gets contents of a file and returns text as a string"""
    lines = list(open(file_name, "r").readlines())
    text = ""
    for i in lines:
        text += i
        return text


def set_text(to_file, text, file_name=""):
    """Writes a file with text"""
    if to_file:
        output_file = open(file_name, "w")
        output_file.truncate()
        output_file .write(text)
        print("Output file: ", file_name)
    else:
        print("Output: \n", text)


def gen_hash(key):
    """Generate a SHA256 hash using a key"""
    key = key.encode('utf-8')
    return (hashlib.sha256(key)).hexdigest()


def check(text, key):
    """Check if file already encrypted with key"""
    key = hash(key)
    lines = text.split("\n")
    length = len(lines)
    if lines[0] == key:
        text = ""
        for i in range(1, length-1):
            text = text + lines[i]+"\n"
        text = text + lines[length-1]
        return text, 1
    return text, 0


def random():
    """used to generate a random key"""
    key = str(uuid.uuid4())
    print("Random Key generated (*save for decryption*) :", key)
    return key


def crypt(pre_text, key):
    """Bitwise XOR of key and text to en/decrypt"""
    post_text = ""
    counter = 0
    try:
        for i in pre_text:
            xbyte = ord(i) ^ ord(key[counter])
            counter = counter + 1
            counter = counter % len(key)
            post_text = post_text + chr(xbyte)
    except Exception as ex:
        print("Exception occured: "+ex)
    return post_text


def main(argv):
    input_file = ''
    output_file = ''
    key = ''
    flag1 = 0
    flag2 = 0
    flag3 = 0
    try:
        opts = getopt.getopt(argv, "hi:o:k:", ["-i", "-o", "-k"])
    except getopt.GetoptError:
        print("""Usage: test.py - i <input_file> - o <output_file>
              - k <key_for_encryption>""")
        sys.exit(0)
    for opt, arg in opts:
        if opt in ("- h", "-help"):
            print("""Usage: test.py - i <input_file> - o <output_file>
                  - k <key_for_encryption>\ndefault action without
                  - i: input in the terminal\ndefault action
                  without - o: displays output in terminal\n
                  default action without - k: generates random
                  key, which is used at the time of decryption\n""")
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
    if flag3 == 0:
        key = random()
    else:
        print("Key:", key)
    if flag1 == 1:
        print("Input file:", input_file)
        fpi = get_text(input_file)
        fp1, decrypt_flag = check(fpi, key)
        crypted_text = crypt(fp1, key)
        if decrypt_flag == 0:
            crypted_text = gen_hash(key)+"\n"+crypted_text
    else:
        text = input("No Input file detected:\nenter text to en/decrypt:\n")
        crypted_text = gen_hash(key)+"\n"+crypt(text, key)
    set_text(flag2, crypted_text, output_file)


if __name__ == "__main__":
    main(sys.argv[1:])
