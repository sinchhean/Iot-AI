# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import pigpio
from kivy.properties import StringProperty
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path




setted = False
PI = ""




popup1 = Popup(title="error",
    content=Label(text="please input the right IP address"),
    size_hint=(None, None), size=(400, 400))
popup2 = Popup(title="sucess",
    content=Label(text="successfully connected"),
    size_hint=(None, None), size=(400, 400))
class Container(GridLayout):
    
    def ip_input(self):
        global setted
        global PI
        val = self.ids.ipinput.text
        self.ids.whatisit.text = str(val)
        try: 
            PI = pigpio.pi(val)
            PI.set_mode(17, pigpio.OUTPUT)
            PI.set_mode(6, pigpio.OUTPUT)
            PI.set_mode(27, pigpio.OUTPUT)
            PI.set_mode(22, pigpio.OUTPUT)
            setted = True
            print("ok")
            popup2.open()
            PI.write(17, 0)
            PI.write(6, 0)
            PI.write(27, 0)
            PI.write(22, 0)
        except:
            print("error")
            setted = False
            popup1.open()

    def move_forward(self):
        if(setted == True):
            #forward()
            PI.write(17,0)
            PI.write(6,1)
            PI.write(27, 1)
            PI.write(22, 0)
        else:
            popup1.open()


    def move_backward(self):

        if(setted== True):
            #backward()
            PI.write(17, 1)
            PI.write(6, 0)
            PI.write(27, 0)
            PI.write(22, 1)
        else:
            popup1.open()


    def turn_right(self):
        if(setted== True):
            #turnright()
            PI.write(17, 1)
            PI.write(6, 0)
            PI.write(27, 1)
            PI.write(22, 0)
        else:
            popup1.open()

    def turn_left(self):
        if(setted== True):
            #turnleft()
            PI.write(17, 0)
            PI.write(6, 1)
            PI.write(27, 0)
            PI.write(22, 1)
        else:
            popup1.open()
        
    def stop_it(self):
        if(setted== True):
            #stop()
            PI.write(17, 0)
            PI.write(6, 0)
            PI.write(27, 0)
            PI.write(22, 0)
        else:
            popup1.open()

class MainApp(App):
    def build(self):
        self.title = 'Awesome app!!!'
        return Container()

if __name__ == "__main__":
    app = MainApp()
    app.run()