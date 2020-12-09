from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_hue = '200'
        
        screen = Screen()
        screen.add_widget(
            MDRaisedButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


MainApp().run()
