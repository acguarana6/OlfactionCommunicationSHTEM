from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from firebase import Firebase
import csv

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

class MainApp(App):
    def build(self):
        layout = BoxLayout(spacing=10, orientation='vertical')

        downloadbutton = Button(text='Press to Process Data',
                        size_hint=(.2, .2),
                        pos_hint={'center_x': .5, 'center_y': .5})
        downloadbutton.bind(on_press=self.on_press_downloadbutton)

        layout.add_widget(downloadbutton)

        return layout

    def on_press_downloadbutton(self, instance):
        print('You pressed the download button!')

        #create a csv file with all of the values from the firebase database
        allsmells = db.child("smells").get()
        smelldict = allsmells.val()
        with open('finalsmelllist.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["alcohol", "ethanol", "name"])
            for key in smelldict:
                alcohol = db.child("smells").child(key).child("alcohol").get().val()
                ethanol = db.child("smells").child(key).child("ethanol").get().val()
                name = db.child("smells").child(key).child("name").get().val()
                writer.writerow([alcohol, ethanol, name])
        print("Finished writing csv file.")
        
        #open finalsmelllist.csv, read what has been written, print the averages
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
            print('average alcohol value = ' + str(alcoholcount / counter))
            print('average ethanol value = ' + str(ethanolcount / counter))
        
        if alcoholcount / counter < 10.0:
            data = {"finalsmell": 1}
            db.push(data)
        else:
            data = {"finalsmell": 2}
            db.child("final results").push(data)
        print("Data sent, all complete!")
        

if __name__ == '__main__':
    app = MainApp()
    app.run()