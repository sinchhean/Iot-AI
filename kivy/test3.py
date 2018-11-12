from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.floatlayout import FloatLayout
from math import *
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from random import *
from kivy.uix.image import Image


import datetime

import time

Builder.load_file('fortest3.kv')


class Painter(Widget):
    
    def on_touch_down(self,touch):
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self,touch):
        touch.ud["line"].points += [touch.x, touch.y]

class Ticks(Widget):
    def __init__(self, **kwargs):
        super(Ticks, self).__init__(**kwargs)
        self.bind(pos=self.update_clock)
        self.bind(size=self.update_clock)
        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            time = datetime.datetime.now()
            Color(0.2, 0.5, 0.2)
            Line(points=[self.center_x, self.center_y, self.center_x+0.8*self.r*sin(pi/30*time.second), self.center_y+0.8*self.r*cos(pi/30*time.second)], width=1, cap="round")
            Color(0.3, 0.6, 0.3)
            Line(points=[self.center_x, self.center_y, self.center_x+0.7*self.r*sin(pi/30*time.minute), self.center_y+0.7*self.r*cos(pi/30*time.minute)], width=2, cap="round")
            Color(0.4, 0.7, 0.4)
            th = time.hour*60 + time.minute
            Line(points=[self.center_x, self.center_y, self.center_x+0.5*self.r*sin(pi/360*th), self.center_y+0.5*self.r*cos(pi/360*th)], width=3, cap="round")

class Smile(Widget):
    def __init__(self, **kwargs):
        super(Smile, self).__init__(**kwargs)
        self.bind(pos=self.theface)
        self.bind(size=self.theface)
        Clock.schedule_interval(self.theface, 1)

    def theface(self,donw, *arg):
        time = datetime.datetime.now()
        cont = time.second%2
        self.canvas.clear()
        with self.canvas:
            if cont == 1:
                Color(0.2,0.5,0.2)
                Line(points=[100,350,140,400,240,400,280,350],width=2,cap="round")
                Color(0.2,0.5,0.2)
                Line(points=[450,350,490,400,590,400,630,350],width=2,cap="round")
                Color(0.2,0.5,0.2)
                Line(points=[190,150,240,100,490,100,540,150],width=2,cap="round")
            else:
                Color(0.2,0.5,0.2)
                Line(points=[100,350,280,350],width=2,cap="round")
                Color(0.2,0.5,0.2)
                Line(points=[450,350,630,350],width=2,cap="round")
                Color(0.2,0.5,0.2)
                Line(points=[190,150,240,100,490,100,540,150],width=2,cap="round")



class AnimatingImage(Image):
    time = 0.0
    rate = 0.2
    frame = 1
    def update(self, dt):
        self.time += dt
        if (self.time > self.rate):
            self.time -= self.rate
            self.source = "atlas://invader/frame" + str(self.frame)
            self.frame = self.frame + 1
            if (self.frame > 2):
                self.frame = 1   

class AnimationScreen(Widget):

    def __init__(self, **kwargs):
        super(AnimationScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.update2, 1.0/60.0)
        
    def update2(self,dt):
        self.invader.update(dt)




        
class Animationwindow(Screen):
    pass

class turnwindow(Screen):
    pass 
            
class Mainwindow(Screen):
    pass

class facewindow(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Mainwindow(name='main'))
sm.add_widget(turnwindow(name='other'))
sm.add_widget(facewindow(name='face1'))
sm.add_widget(Animationwindow(name='ani'))

sm.current = 'face1'




class MainApp(App):    
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()