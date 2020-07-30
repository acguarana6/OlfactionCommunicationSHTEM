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
import time

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
        chosenKeyInd = 0
        
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

        self.alcoholSol = TextInput(
            halign="left", font_size=55, hint_text='Alcohol value'
        )

        #gridlayout.add_widget(Button(text='200'))

        self.hySulSol = TextInput(
            halign="left", font_size=55, hint_text='Hydrogen Sulfide value'
        )
        
        self.ammoniaSol = TextInput(
            halign="left", font_size=55, hint_text='Ammonia value'
        )
        
        self.formalSol = TextInput(
            halign="left", font_size=55, hint_text='Formaldehyde value'
        )
        
        gridlayout.add_widget(Button(text='ALCOHOL', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]))
        gridlayout.add_widget(self.alcoholSol)
        
        gridlayout.add_widget(Button(text='AMMONIA', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]))
        gridlayout.add_widget(self.ammoniaSol)
        
        gridlayout.add_widget(Button(text='FORMALDEHYDE', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]))
        gridlayout.add_widget(self.formalSol)
        
        gridlayout.add_widget(Button(text='HYDROGEN SULFIDE', size_hint_x=None, width=350,background_color=[0, 0, 1, 1]))
        gridlayout.add_widget(self.hySulSol)

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

            self.progresslabel.text = 'Fetching data...'
            #create a csv file with all of the values from the firebase database

            db = firebase.database()
            a = db.child("smells")
            smelldict = a.get().val()
            print(smelldict)
            with open('finalsmelllist.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["alcohol", "ammonia", "formaldehyde", "hydrogen sulfide"])
                for key in smelldict:
                    alcohol = db.child("smells").child(key).child("alcohol").get().val()
                    ammonia = db.child("smells").child(key).child("ammonia").get().val()
                    formal = db.child("smells").child(key).child("formaldehyde").get().val()
                    hySul = db.child("smells").child(key).child("hydrogen sulfide").get().val()
                    writer.writerow([alcohol, ammonia, formal, hySul])
            print("Finished writing csv file.")

            self.progresslabel.text = 'Data fetched! CSV generated in folder.'


            with open('finalsmelllist.csv', 'r') as file:
                reader = csv.reader(file)
                counter = 0.0
                alcoholcount = 0.0
                ammoniacount = 0.0
                formalcount = 0.0
                hysulcount = 0.0
                for row in reader:
                    if counter != 0.0:
                        alcoholcount = alcoholcount + float(row[0])
                        ammoniacount = ammoniacount + float(row[1])
                        formalcount = formalcount + float(row[2])
                        hysulcount = hysulcount + float(row[3])
                    counter = counter + 1.0
            self.alcoholSol.text = str(alcoholcount / counter)
            self.ammoniaSol.text = str(ammoniacount / counter)
            self.formalSol.text = str(formalcount / counter)
            self.hySulSol.text = str(hysulcount / counter)

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
                    chosenKeyInd = 0
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
                    self.progresslabel.text = "No Signal Found"
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

            #Algorithm goes here

            #data = {"alcohol": self.alcoholSol.text,"ethanol": self.ethanolSol.text,"name": "test" }
            data = 3
            b.child("finalint").set(data)
            self.progresslabel.text = 'Data sent!'
            instance.text = "START FETCHING DATA"
    def swap_label(self, progText):
        self.progresslabel.text = progText
        print(progText)
    def chooseSignal(self, instance):
        
        self.chosenKeyInd = instance.thisKeyInd
        
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
