import kivy
import random

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from firebase import Firebase

config = {
  "apiKey": "AIzaSyBOcmn9KlCfw4ENV9frqO6VJMNwJKuNuvY",
  "authDomain": "olfaction-communication-shtem.firebaseapp.com",
  "databaseURL": "https://olfaction-communication-shtem.firebaseio.com",
  "storageBucket": "olfaction-communication-shtem.appspot.com",
}

firebase = Firebase(config)

class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="horizontal")
        
        control_layout = BoxLayout(orientation="vertical")
        input_layout = BoxLayout(orientation="vertical")
        fetch_layout = BoxLayout(orientation="vertical")
        
        #Control field
        
        self.solution = TextInput(
        halign="left", font_size=55, hint_text='Key input'
        )
        
        control_layout.add_widget(self.solution)
        
        buttons = [["Begin Fetching from E-Nose"], ["Send to Database"]]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    )
                button.bind(on_press=self.on_button_press)
            h_layout.add_widget(button)
            control_layout.add_widget(h_layout)
    
        
        
        
        #Input field
        

        self.ethanolSol = TextInput(
            halign="left", font_size=55, hint_text='Ethanol value'
        )

        self.alcoholSol = TextInput(
            halign="left", font_size=55, hint_text='Alcohol value'
        )


        input_layout.add_widget(self.ethanolSol)
        input_layout.add_widget(self.alcoholSol)

        buttons = [
            ["Switch to moment-to-moment view"]
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            input_layout.add_widget(h_layout)
        
        #Fetch field
        fetchKey = TextInput(
            halign="left", font_size=55, hint_text='Key input to fetch'
        )
        buttons = [
           ["Pull from Database"]
        ]
        fetch_layout.add_widget(fetchKey)
        
        main_layout.add_widget(control_layout)
        main_layout.add_widget(input_layout)
        main_layout.add_widget(fetch_layout)

        return main_layout
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "Push to Database":
    
            db = firebase.database()
            a = db.child(self.solution.text)

            data = {"Alcohol": self.alcoholSol.text, "Ethanol": self.ethanolSol.text}
            a.push(data)
    #if button_text == "Pull to Database":
            

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == '__main__':
    app = MainApp()
    app.run()
