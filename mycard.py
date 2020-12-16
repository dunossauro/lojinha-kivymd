from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

# from kivy.config import Config
# Config.set("graphics", "window_state", "maximized")
# Config.set("graphics", "minimum_width", 800)
# Config.set("graphics", "minimum_height", 384)

KV = '''
<MyCard>:
    id: card
    size_hint: (0.7, 0.7)
    pos_hint: {"center_x": .5, "center_y": .5}
    orientation: 'vertical'

    MDBoxLayout:
        size_hint_y: 0.24
        padding: [25,0,25,0]
        md_bg_color: app.theme_cls.primary_color
        
        MDLabel:
            text: 'Comprar'
            font_style: 'H5'
            theme_text_color: 'Primary'
            # text_color: self.theme_cls.primary_color

        MDIconButton:
            icon: 'close'
            on_release: app.quit_card()

    FitImage:
        size_hint_y: 0.5
        source: './arroz2.jpg'
        allow_stretch: True

    BoxLayout:
        padding: [25,0,25,25]
        orientation: 'vertical'
        MDLabel:
            text: 'Arroz Agulhinha'
            font_style: 'H6'
            theme_text_color: 'Primary'
        MDLabel:
            text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut cursus, nunc id lobortis luctus, velit ante aliquam ligula, non convallis elit arcu ut nisi. Vestibulum vestibulum, sapien vitae porta gravida, sem nisi sollicitudin nunc, laoreet euismod sem leo eu sem.'
            font_style: 'Caption'
            theme_text_color: 'Secondary'
        RelativeLayout:
            MDRaisedButton:
                text: 'Adicionar 12.99'
                font_style: 'H6'
                theme_text_color: 'ContrastParentBackground'

ScreenManager:
    Screen:
        name: "tela"
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: 'mercado'
                left_action_items: [['menu', lambda x: x]]
            MDLabel:
                text: 'batata'
            MDRectangleFlatButton:
                text: 'batatinha'
                on_press: app.press()
'''


class MyCard(MDCard):
    ...


class TestCard(MDApp):
    def press(self, *args):
        self.root.current_screen.add_widget(
            MyCard()
        )


    def quit_card(self, *args):
        self.root.current_screen.remove_widget(
            self.root.current_screen.children[0]
        )

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'LightBlue'
        self.theme_cls.primary_hue = '200'
        return Builder.load_string(KV)


TestCard().run()
