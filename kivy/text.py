from kivy.app import App

from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label

import time

class PopupProgress():
    def __init__(self, value_init=0, value_max=1, title='', size=None, 
                 auto_close=False):
        self._auto_close = auto_close
        self._box = BoxLayout(orientation='vertical')

        if size is None:
            size_hint = (1,1)
        else:
            size_hint = (None, None)

        self.popup = Popup(title=title, 
                           content=self._box, 
                           auto_dismiss=False, 
                           size_hint=size_hint, 
                           size=tuple(size)
                           )

        # progress bar
        self._pb = ProgressBar(max=value_max, value = value_init)
        self._box.add_widget(self._pb)

        # label
        self._label = Label(text='')
        self._box.add_widget(self._label)

        # close button
        self._button = Button(text='Close', height=40, size_hint_y=None, 
                        disabled=True)
        self._button.bind(on_press=self.popup.dismiss)
        self._box.add_widget(self._button)

        self.popup.open()


    def set_value(self, value=None, message=''):
        if not value is None:
            self._pb.value = value
        self._label.text = message
        if self._pb.value_normalized>=1:
            if self._auto_close:
                self.popup.dismiss()
            else:
                self.enable_close_button()


    def enable_close_button(self):
        self._button.disabled = False

class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        button = Button(text='popup!')
        button.bind(on_press=self.func_test_pp)
        self.add_widget(button)


    def pp_update(self, *args):
        try:
            value, message = next(self.gen)
            self.pp.set_value(value, message)
            Clock.schedule_once(self.pp_update, 0.1)
        except StopIteration:
            self.pp.enable_close_button()
        except Exception as e:
            self.pp.set_value(message=str(e))
            self.pp.enable_close_button()


    def func_test_pp(self, *args):
        self.pp = PopupProgress(
                title='TestPopupProgress', 
                size=(self.width/2, self.height/3)
                )
        self.gen = self.func_test()
        Clock.schedule_once(self.pp_update, 0.1)


    def func_test(self):
        yield 0, 'Preparing...'

        allitems = 5
        for i in range(allitems):
            time.sleep(1)
            yield (i+1)/allitems, '{:d}/{:d}'.format(i+1, allitems)

        yield 1, 'Complete.'


class TestPopupProgressApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestPopupProgressApp().run()