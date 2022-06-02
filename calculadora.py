import os
import platform

from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.lang import Builder

# This is needed for supporting Windows 10 with OpenGL < v2.0
if platform.system() == "Windows":
    os.environ["KIVY_GL_BACKEND"] = "angle_sdl2"

Builder.load_file('my.kv')


class Container(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_key = "0"
    def clear(self):
        self.ids.calc_input.text = ''

    def backspace(self):
        prior = self.ids.calc_input.text 
        if prior == self.start_key or prior == "Error":
            self.ids.calc_input.text = f""
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = prior[:-1]
        
    def insert(self,text):
        prior = self.ids.calc_input.text 
        if prior == self.start_key or prior == "Error":
            self.ids.calc_input.text = f"{text}"
            return
        self.ids.calc_input.text = f"{prior}{text}"

    def math_signal(self):
        prior = self.ids.calc_input.text
        signal = "" if len(prior) <= 0 else prior[0]
        if  signal == "+":
            signal = f"-{prior[1:]}"
        elif  signal == "-":
            signal = f"+{prior[1:]}"
        else:
            signal = f"+{prior}"

        self.ids.calc_input.text = f"{signal}"

    def solve(self):
        try:
            data = self.ids.calc_input.text
            newData = ""
            for i in data:
                if i == "x":
                    i = "*"
                newData += i
            answer = eval(newData)
            self.ids.calc_input.text = f"{answer}"
        except:
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"Error"

class Calculadora(MDApp):  # NOQA: N801
    def __init__(self, **kwargs):
        super(Calculadora, self).__init__(**kwargs)
        Window.soft_input_mode = "below_target"
        self.title = "Cromo-47"

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"

        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.accent_hue = "500"

        self.theme_cls.theme_style = "Light"

    def build(self):
        return Container()
