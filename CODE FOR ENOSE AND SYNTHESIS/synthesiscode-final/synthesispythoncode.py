import serial
import time
from firebase import Firebase

config = {
  "apiKey": "AIzaSyCO-aIknTFTNbpgsZeTH6kLPSti0TdrKEE",
    "authDomain": "testerdatabase-dd943.firebaseapp.com",
    "databaseURL": "https://testerdatabase-dd943.firebaseio.com",
    "projectId": "testerdatabase-dd943",
    "storageBucket": "testerdatabase-dd943.appspot.com",
    "messagingSenderId": "770490613537",
    "appId": "1:770490613537:web:7ea990b9b2e787e4cd0860",
    "measurementId": "G-FFV7N1EB5G"
}

firebase = Firebase(config)
db = firebase.database()

arduino = serial.Serial('/dev/cu.usbmodem1411', 9600) #connect python to the arduino's serial port
time.sleep(2)

print("Serial port connected and working")

#random key is no longer coming from the arduino 
#you will have to enter your ready key below and send it out.
'''
randomBytes = arduino.read_until()
encoding = 'utf-8'
randomKey = randomBytes.decode(encoding)
randomKey = randomKey.strip()
'''
randomKey = "enterrandomkeyhere" #enter in your ready key
print(randomKey)
db.child("Signal").child("key").set(randomKey)

time.sleep(10)

all_user_ids = db.shallow().get().val()
keys = list(all_user_ids)
while(randomKey not in keys):
  all_user_ids = db.shallow().get().val()
  keys = list(all_user_ids)

finalint = db.child(randomKey).child("finalint").get().val()
arduino.write([finalint]) #need to figure out how to properly encode the final int coming from firebase
print(finalint)
