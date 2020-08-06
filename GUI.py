from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from firebase import Firebase
import random
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from kivy.core.window import Window
from kivy.uix.popup import Popup
import csv

import pickle
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.cm as cm
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from scipy.stats import mode
from sklearn.metrics import accuracy_score

'''from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp'''

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

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]



class MainApp(App):
    def build(self):
        Window.size = (800, 725)
        self.chosenKeyInd = 0
        self.valArray = []
        self.smellName = "ERR"
        Window.clearcolor = (0.5, 0.5, 0.5, 0.5)
        boxlayout = BoxLayout(orientation='vertical')

        label = Label(text='DATA SENDER APP',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .85}, color=[1, 1, 1, 1], font_size=70)

        """fetchKey = TextInput(
            halign="left", font_size=55, hint_text='Key input to fetch', size_hint=(0.8, 1), pos_hint={"center_x": 0.5, "center_y": 0.65}
        )"""

        #layout = FloatLayout(size=(300, 300))
        layout = BoxLayout(orientation="vertical")
        button = Button( text='START FETCHING DATA', size_hint=(0.8, 1), pos_hint={"center_x": 0.5, "center_y": 0.65},background_color=[0, 0, 1, 1])

        layout.add_widget(label);

        #layout.add_widget(fetchKey)
        layout.add_widget(button)
        button.bind(on_press=self.on_press_button)


        self.progresslabel = Label(text='On standby',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .53}, color=[1, 1, 1, 1], font_size=30)

        label2 = Label(text='CURRENT DATA:',
                      size_hint=(.5, .5),
                      color=[1, 1, 1, 1],
                      pos_hint={'center_x': .5, 'center_y': .375}, font_size=60)
        layout.add_widget(self.progresslabel);
        layout.add_widget(label2);


#dropdown = DropDown(size_hint=(.5, .5))
#btn1 = Button(text='AVERAGED DATA', size_hint_y=None, height=44)
#btn2 = Button(text='RAW DATA', size_hint_y=None,  height=44)
#btn1.bind(on_release=lambda btn: dropdown.select(btn1.text))
#btn2.bind(on_release=lambda btn: dropdown.select(btn2.text))
#dropdown.add_widget(btn1)
#dropdown.add_widget(btn2)
#mainbutton = Button(text='Data View', size_hint_x = 0.4, size_hint_y = 0.1, pos_hint={'center_x': 0.5, 'center_y': 0.25})
        #mainbutton.bind(on_release=dropdown.open)
        #dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        #layout.add_widget(mainbutton);

        gridlayout = GridLayout(cols=2, row_force_default=True, row_default_height=100, size_hint_x = 0.8, pos_hint={'center_x': 0.5, 'center_y': 0.25})
        gridlayout.add_widget(Button(text='COMPOUND', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]) )
        gridlayout.add_widget(Button(text='VALUE' ,background_color=[0, 0, 1, 1]) )

        self.MQ136 = TextInput(
            halign="left", font_size=55, hint_text='MQ136 value'
        )

        #gridlayout.add_widget(Button(text='200'))

        self.MQ137 = TextInput(
            halign="left", font_size=55, hint_text='MQ137 value'
        )

        self.MQ3 = TextInput(
            halign="left", font_size=55, hint_text='MQ3 value'
        )

        self.MQ5 = TextInput(
            halign="left", font_size=55, hint_text='MQ5 value'
        )

        self.MQblank = TextInput(
            halign="left", font_size=55, hint_text='MQblank value'
        )
        self.MQblank2 = TextInput(
            halign="left", font_size=55, hint_text='MQblank2 value'
        )

        gridlayout.add_widget(Button(text='MQ136', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]))
        gridlayout.add_widget(self.MQ136)

        gridlayout.add_widget(Button(text='MQ137', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]))
        gridlayout.add_widget(self.MQ137)

        gridlayout.add_widget(Button(text='MQ3', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]))
        gridlayout.add_widget(self.MQ3)

        gridlayout.add_widget(Button(text='MQ5', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]))
        gridlayout.add_widget(self.MQ5)

        gridlayout.add_widget(Button(text='MQblank', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]))
        gridlayout.add_widget(self.MQblank)

        gridlayout.add_widget(Button(text='MQblank2', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]))
        gridlayout.add_widget(self.MQblank2)



        #gridlayout.add_widget(Button(text='200'))

        boxlayout.add_widget(layout)
        boxlayout.add_widget(gridlayout)

        #db = firebase.database()
        #db.child("Signal").push("")



        return boxlayout

    def on_press_button(self, instance):
        print('You pressed the button!')
        button_text = instance.text
        if button_text == 'START FETCHING DATA':
            self.valArray = []
            self.progresslabel.text = 'Fetching data...'
            #create a csv file with all of the values from the firebase database

            ref = firebase.database()
            data = ref.child("smells").get()
            key = data.val()
            print("hello")
            if(key == None):
                self.progresslabel.text = 'No data currently in database'

            else:
                db = firebase.database()
                a = db.child("smells")
                smelldict = a.get().val()
                print(smelldict)
                with open('finalsmelllist.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["MQ136", "MQ137", "MQ3", "MQ5" , "MQblank" , "MQblank2"])
                    for key in smelldict:
                        MQ136 = db.child("smells").child(key).child("MQ136").get().val()
                        MQ137 = db.child("smells").child(key).child("MQ137").get().val()
                        MQ3 = db.child("smells").child(key).child("MQ3").get().val()
                        MQ5 = db.child("smells").child(key).child("MQ5").get().val()
                        MQblank = db.child("smells").child(key).child("MQblank").get().val()
                        MQblank2 = db.child("smells").child(key).child("MQblank2").get().val()
                        writer.writerow([MQ136, MQ137, MQ3, MQ5 , MQblank , MQblank2])
                print("Finished writing csv file.")

                self.progresslabel.text = 'Data fetched! CSV generated in folder.'


                with open('finalsmelllist.csv', 'r') as file:
                    reader = csv.reader(file)
                    counter = 0.0
                    MQ136count = 0.0
                    MQ137count = 0.0
                    MQ3count = 0.0
                    MQ5count = 0.0
                    MQblankcount = 0.0
                    MQblank2count = 0.0
                    next(reader)
                    for row in reader:
                        if counter != 0.0:
                            MQ136count = MQ136count + float(row[0])
                            MQ137count = MQ137count + float(row[1])
                            MQ3count = MQ3count + float(row[2])
                            MQ5count = MQ5count + float(row[3])
                            MQblankcount = MQblankcount + float(row[4])
                            MQblank2count = MQblank2count + float(row[5])
                        counter = counter + 1.0
                self.MQ136.text = str(MQ136count / counter)
                self.MQ137.text = str(MQ137count / counter)
                self.MQ3.text = str(MQ3count / counter)
                self.MQ5.text = str(MQ5count / counter)
                self.MQblank.text = str(MQblankcount / counter)
                self.MQblank2.text = str(MQblank2count / counter)
                
                self.valArray.append(MQ3count / counter)
                self.valArray.append(MQ137count / counter)
                self.valArray.append(MQ5count / counter)
                self.valArray.append(MQblankcount / counter)
                self.valArray.append(MQblank2count / counter)
                
                print("ValArray v")
                print(self.valArray)
                
                self.progresslabel.text = 'Data fetched! CSV generated in folder. Values updated.'
                self.swap_label('Data fetched! CSV generated in folder. On standby for a signal.')

                '''print('3 seconds start')
                time.sleep(2)
                print('3 seconds are over')
                self.swap_label('On Standby. Looking for signal from synthesizer (every 2 seconds).')'''
                instance.text = "Check for Signal"

                #instance.text = "Push to Database"


        if button_text == "Check for Signal":
            x = 1
            self.progresslabel.text = 'Checking for Signal......'
            while True:
                ref = firebase.database()
                users = ref.child("Signal").get()
                key = users.val()
                #print(key)
                if(key == None):
                    self.progresslabel.text = 'On Standby. No Signal yet.'
                else:
                    db = firebase.database()
                    keyDict = firebase.database().child("Signal").get().val()
                    keyList = list(keyDict)
                    self.chosenKeyInd = 0
                    finalKey = firebase.database().child("Signal").child(keyList[0]).get().val()

                    keyCount = int(len(keyDict))
                    print(keyCount)
                    if(keyCount==1):
                        self.progresslabel.text = 'Ready to Go! Key = ' + str(finalKey)
                        instance.text = "Push to Database"
                    else:
                        content = BoxLayout(orientation="vertical")

                        for x in range(0,keyCount):
                            db = firebase.database()
                            keyDict = firebase.database().child("Signal").get().val()
                            keyList = list(keyDict)
                            thisKey = firebase.database().child("Signal").child(keyList[x]).get().val()


                            button = Button( text=str(thisKey),background_color=[0, 0, 1, 1])
                            content.add_widget(button)
                            button.thisKeyInd = x
                            button.bind(on_press=self.chooseSignal)
                            button.subInst = instance

                        self.popup = Popup(content=content, auto_dismiss=False, title = "Pick a synthesis key!", title_align = "center", )

                        # bind the on_press event of the button to the dismiss function

                        # open the popup
                        self.popup.open()
                    break
                if(x==10):
                    print('program terminated')
                    self.progresslabel.text = "No Signal Found."
                    instance.text = "Click button to check again for Signal."
                    break
                x = x+1
                print(x)
                time.sleep(2)

        if button_text == "Click button to check again for Signal.":
            x = 1
            self.progresslabel.text = 'Checking for Signal......'
            while True:
                ref = firebase.database()
                users = ref.child("Signal").get()
                key = users.val()
                #print(key)
                if(key == None):
                    self.progresslabel.text = 'On Standby. No Signal yet.'
                else:
                    db = firebase.database()
                    keyDict = firebase.database().child("Signal").get().val()
                    keyList = list(keyDict)
                    chosenKeyInd = 0
                    finalKey = firebase.database().child("Signal").child(keyList[0]).get().val()

                    keyCount = int(len(keyDict))
                    print(keyCount)
                    if(keyCount==1):
                        self.progresslabel.text = 'Ready to Go! Key = ' + str(finalKey)
                        instance.text = "Push to Database"
                        chosenKeyInd = 0
                    else:
                        content = BoxLayout(orientation="vertical")

                        for x in range(0,keyCount):
                            db = firebase.database()
                            keyDict = firebase.database().child("Signal").get().val()
                            keyList = list(keyDict)
                            thisKey = firebase.database().child("Signal").child(keyList[x]).get().val()


                            button = Button( text=str(thisKey),background_color=[0, 0, 1, 1])
                            content.add_widget(button)
                            button.thisKeyInd = x
                            button.bind(on_press=self.chooseSignal)
                            button.subInst = instance

                        self.popup = Popup(content=content, auto_dismiss=False, title = "Pick a synthesis key!", title_align = "center", )

                        # bind the on_press event of the button to the dismiss function

                        # open the popup
                        self.popup.open()
                    break
                if(x==10):
                    print('program terminated')
                    self.progresslabel.text = "No Signal Found."
                    instance.text = "Click button to check again for Signal."
                    break
                x = x+1
                print(x)
                time.sleep(2)


        if button_text == "Push to Database":
            db = firebase.database()
            keyDict = firebase.database().child("Signal").get().val()
            keyList = list(keyDict)
            finalKey = firebase.database().child("Signal").child(keyList[self.chosenKeyInd]).get().val()
            b = db.child(finalKey)

        #Algorithm goes here##---------------------------------##

            valArray = self.valArray
            
            
            '''valArray = []
            valArray.append(111)
            valArray.append(13.0)
            valArray.append(88.3)
            valArray.append(7.6)
            valArray.append(71.26)'''
            
            x = valArray[0]
            print(x)
            testAvg = x
            #testAvg = 190
            print(testAvg)
            
            meanList = [101.77966101694915, 187.50169491525423, 143.08474576271186, 111.5186440677966, 207.4237288135593, 246.92542372881357]

            dists = []
            currentLowest = 0
            for x in range(6):
                dists.append(abs(testAvg-meanList[x]))
                if(x!=0):
                    if(dists[x]<dists[currentLowest]):
                        currentLowest = x

            print(dists)
            print(currentLowest)
            if currentLowest == 0:
                print("LemonGrass")
                self.smellName = "LemonGrass"
                finalNum = 4
            if currentLowest == 1:
                print("Eucalyptus")
                self.smellName = "Eucalyptus"
                finalNum = 2
            if currentLowest == 2:
                print("Peppermint")
                self.smellName = "Peppermint"
                finalNum = 1
            if currentLowest == 3:
                print("Lavendar")
                self.smellName = "Lavendar"
                finalNum = 6
            if currentLowest == 4:
                print("TeaTree")
                self.smellName = "TeaTree"
                finalNum = 5
            if currentLowest == 5:
                print("Orange")
                self.smellName = "Orange"
                finalNum = 3
        
    #Algorithm ends here##---------------------------------##
            data = finalNum
            b.child("finalint").set(data)
            self.progresslabel.text = 'Smell classified as ' + self.smellName + '. Data sent!'
            instance.text = "START FETCHING DATA"
    def swap_label(self, progText):
        self.progresslabel.text = progText
        print(progText)
    def chooseSignal(self, instance):

#self.chosenKeyInd = instance.thisKeyInd

        db = firebase.database()
        keyDict = firebase.database().child("Signal").get().val()
        keyList = list(keyDict)
        finalKey = firebase.database().child("Signal").child(keyList[self.chosenKeyInd]).get().val()

        self.progresslabel.text = 'Ready to Go! Key = ' + str(finalKey)
        instance.subInst.text = "Push to Database"

        self.popup.dismiss()



if __name__ == '__main__':
    app = MainApp()
    app.run()

'''Key
-> eNose_to_app
    -> Key
-> App_to_User
    ->Key
-> App_to_emitter
    ->Key
'''
