from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
#from gpiozero import PWMOutputDevice
#from gpiozero import Motor
#from gpiozero.pins.pigpio import PiGPIOFactory
# import pigpio
from time import sleep


from os import listdir
from kivy.config import Config

#factory = PiGPIOFactory(host='192.168.11.12')
#motor = Motor(5,6)
# PI = pigpio.pi("192.168.11.12")
# PI.set_mode(5, pigpio.OUTPUT)
# PI.set_mode(6, pigpio.OUTPUT)
# Config.set('graphics', 'width', '500')
# Config.set('graphics', 'height', '500')

kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)


class AddButton(Button):
    pass


class SubtractButton(Button):
    pass


class Container(GridLayout):
    display = ObjectProperty()

    def add_one(self):
        value = "up"
        self.display.text = str(value)
       # motor.forward()
        # PI.write(5, 1)
        # PI.write(6, 0)

    def subtract_one(self):
        value = "down"
        self.display.text = str(value)
        #motor.backward()
        # PI.write(6, 1)
        # PI.write(5, 0)
        
    def stop_it(self):
        value = "stop"
        self.display.text = str(value)
        #motor.stop()
        # PI.write(5, 0)
        # PI.write(6, 0)

class MainApp(App):
    def build(self):
        self.title = 'Awesome app!!!'
        return Container()


if __name__ == "__main__":
    app = MainApp()
    app.run()