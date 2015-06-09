#Crappy Bitcoin Cryptolocker example 
Please dont use this. This is only a proof of concept and should NOT be used by anyone.

#Usage
This, if the correct modules and python are installed on the users computer, is a fully working cryptolocker example.

#How
The program will encrypt the users directory on the users machine, with a key unknown to the user.

Due to the key technically being stored in RAM it will be lost if the user tampers with the program, for example turning off the machine or exiting the program. As the key only exists as a variable in the program it is nearly impossible for the user to obtain it.

The program then creates a bitcoin wallet with the blockchain api and tells the user to send 0.001 btc there. When the BTC is sent it will be forwarded to a personal wallet. When the BTC is detected as being sent a request will be sent to a personal server where it will be logged in a database.

Every 100s the program checks the database to see if BTC has been sent, if it has the program will decrypt the files. 
Otherwise the program will exit after 3 hours and the key (therefore the files) will be lost.

#Testing

If you want to use this yourself to test it you should first create a virtual windows machine to test it in.
Then you need to:

Clone the repository

		$ git clone https://github.com/basilthebeagles/pythonCryptolockerExample.git
	
Install the PyCrypto binaries 

Widnows:[here](http://www.voidspace.org.uk/python/modules.shtml#pycrypto)
Linux/Mac: [here](https://www.dlitz.net/software/pycrypto/)

Install requests via pip:

		$ pip install requests
	
or navigate to the requests folder in the newly cloned repository and run:

		setup.py bdist_wininst

and then run the newly created .exe in the dist directory of the requests directory.	

Run the program, the password is "basil".		

#TODO

I can not find a way to generate a 256bit (or 32 byte) key in python so the program uses a set key. This is obviously very vunerable Also if I found a way to stop the Windows processes so I could encrypt files in use it would be "nice".   		
	
	


