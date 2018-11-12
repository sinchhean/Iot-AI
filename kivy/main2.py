from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Line

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class Main_Screen(Screen):
    pass


class Input_Number_Inch_Screen(Screen):
    pass


class Input_Screen(Screen):
    pass


class Screen_Management(ScreenManager):
    pass


presentation = Builder.load_file("formain2.kv")


class Screen3App(App):

    def build(self):
        return presentation


if __name__ == "__main__":
    Screen3App().run()