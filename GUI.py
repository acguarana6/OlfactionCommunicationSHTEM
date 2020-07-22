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
import csv

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
        Window.clearcolor = (1, 1, 1, 1)
        boxlayout = BoxLayout(orientation='vertical')

        label = Label(text='DATA SENDER APP',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .85}, color=[0, 0, 1, 1], font_size=70)

        layout = FloatLayout(size=(300, 300))
        button = Button( text='START FETCHING DATA', size_hint=(.5, .15), pos_hint={"center_x": 0.5, "center_y": 0.65})
        layout.add_widget(button)
        button.bind(on_press=self.on_press_button)
        layout.add_widget(label);

        self.progresslabel = Label(text='On standby',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .53}, color=[0, 0, 1, 1], font_size=30)

        label2 = Label(text='CURRENT DATA:',
                      size_hint=(.5, .5),
                      color=[0, 0, 1, 1],
                      pos_hint={'center_x': .5, 'center_y': .375}, font_size=60)
        layout.add_widget(label2);
        layout.add_widget(self.progresslabel);

        dropdown = DropDown(size_hint=(.5, .5))
        btn1 = Button(text='AVERAGED DATA', size_hint_y=None, height=44)
        btn2 = Button(text='RAW DATA', size_hint_y=None,  height=44)
        btn1.bind(on_release=lambda btn: dropdown.select(btn1.text))
        btn2.bind(on_release=lambda btn: dropdown.select(btn2.text))
        dropdown.add_widget(btn1)
        dropdown.add_widget(btn2)
        mainbutton = Button(text='Data View', size_hint_x = 0.4, size_hint_y = 0.1, pos_hint={'center_x': 0.5, 'center_y': 0.25})
        mainbutton.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        layout.add_widget(mainbutton);

        gridlayout = GridLayout(cols=2, row_force_default=True, row_default_height=100, size_hint_x = 0.7, pos_hint={'center_x': 0.5, 'center_y': 0.25})
        gridlayout.add_widget(Button(text='COMPOUND', size_hint_x=None, width=200))
        gridlayout.add_widget(Button(text='VALUE'))
       
        self.alcoholSol = TextInput(
            halign="left", font_size=55, hint_text='Alcohol value'
        )
        
        #gridlayout.add_widget(Button(text='200'))
        
        self.ethanolSol = TextInput(
            halign="left", font_size=55, hint_text='Ethanol value'
        )
        
        gridlayout.add_widget(Button(text='ETHANOL', size_hint_x=None, width=200))
        gridlayout.add_widget(self.ethanolSol)
        gridlayout.add_widget(Button(text='ALCOHOL', size_hint_x=None, width=200))
        gridlayout.add_widget(self.alcoholSol)
        
        #gridlayout.add_widget(Button(text='200'))
        
        boxlayout.add_widget(layout)
        boxlayout.add_widget(gridlayout)



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
                writer.writerow(["alcohol", "ethanol", "name"])
                for key in smelldict:
                    alcohol = db.child("smells").child(key).child("alcohol").get().val()
                    ethanol = db.child("smells").child(key).child("ethanol").get().val()
                    name = db.child("smells").child(key).child("name").get().val()
                    writer.writerow([alcohol, ethanol, name])
            print("Finished writing csv file.")
            
            self.progresslabel.text = 'Data fetched! CSV generated in folder.'
            
            with open('finalsmelllist.csv', 'r') as file:
                reader = csv.reader(file)
                counter = 0.0
                alcoholcount = 0.0
                ethanolcount = 0.0
                for row in reader:
                    if counter != 0.0:
                        alcoholcount = alcoholcount + float(row[0])
                        ethanolcount = ethanolcount + float(row[1])
                    counter = counter + 1.0
            self.alcoholSol.text = str(alcoholcount / counter)
            self.ethanolSol.text = str(ethanolcount / counter)
            
            self.progresslabel.text = 'Data fetched! CSV generated in folder. Values updated.'

            instance.text = "Push to Database"
        if button_text == "Push to Database":
            db = firebase.database()
            b = db.child("toUser")
            data = {"alcohol": self.alcoholSol.text,"ethanol": self.ethanolSol.text,"name": "test" }
            b.push(data)
            self.progresslabel.text = 'Data sent!'
            instance.text = "START FETCHING DATA"


if __name__ == '__main__':
    app = MainApp()
    app.run()
