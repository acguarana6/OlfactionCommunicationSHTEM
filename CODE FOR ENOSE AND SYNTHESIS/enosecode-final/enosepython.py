from firebase import Firebase
import csv
import serial
import time

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

arduino = serial.Serial('/dev/cu.usbmodem1411', 9600) #connect python to arduino's serial port
time.sleep(2) #give connection a minute to settle

print("Serial port connected and working")

#test code that's commented out
'''
for x in range(6):
  first = arduino.read_until(b',')
  #arduino.read(1)
  second = arduino.read_until(b',')
  #arduino.read(1)
  third = arduino.read_until(b',')
  #arduino.read(1)
  fourth = arduino.read_until()

  print(first.decode("utf-8"))
  print(second.decode("utf-8"))
  print(third.decode("utf-8"))
  print(fourth.decode("utf-8"))
'''

#create a new csv file in same folder as python script
#read data sent over serial port
#put into csv file
with open('rawdata.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(["alcohol", "ammonia", "hydrogen sulfide", "formaldehyde"])
  for x in range(5):
    first = arduino.read_until(b',')
    second = arduino.read_until(b',')
    third = arduino.read_until(b',')
    fourth = arduino.read_until()

    print(first.decode("utf-8"))
    print(second.decode("utf-8"))
    print(third.decode("utf-8"))
    print(fourth.decode("utf-8"))

    #write row in csv file
    writer.writerow([first.decode("utf-8").replace(',',''), second.decode("utf-8").replace(',',''), third.decode("utf-8").replace(',',''), fourth.decode("utf-8")])

#read csv file and put each row into json data structure
#send it up to database
with open('rawdata.csv','r') as file:
  reader = csv.reader(file)
  counter = 0
  for row in reader:
    if counter != 0:
      data = {"alcohol": float(row[0]), "ammonia": float(row[1]), "hydrogen sulfide": float(row[2]), "formaldehyde": float(row[3])}
      db.child("smells").push(data)
    counter = counter + 1

