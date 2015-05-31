#Crappy Cryptolocker example
Please dont attempt to use this maliciously

#Why 
I decided to create this as a terrible proof of concept of how
easy it is to hold a user to ransome.
#How
Using the python Cypto library and two functions obtained from: [here](http://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto
)a program (IE this) can be constructed that will encrypt files on the users hard drive, without giving them the key
meaning they can not decrypt the files themselves.
#Usage
Between
	 encryptionManager.manage(0, rootDirectionary, key)
and 	
	encryptionManager.manage(1, rootDirectionary, key)
anything can be inserted. Essentially the user is at the hands of whoever puts 
this on their computer.

#Saftey??
Using this program by itself, it would be very hard to actually getting a user
to run it. They would have to have python installed, their system path configured,
and the Crypto module installed. This is all before actually getting them to run it.
Also the program cant encrypt files that are in use or need admin permission. 

Unfortunately the files that the user probably holds dearest, such as documents and photos,
will probably not be in use or need administrator permission.

#Testing
I tested this in a Virtual Windows 7 machine, I think you should too. 
Unless you want all your files encrypted.

#TODO
I can not find a way to generate a 256bit (or 32 byte) key in python so the
program uses a set key.
Also if I found a way to stop the Windows processes so I could encrypt files in
use it would be "nice".
