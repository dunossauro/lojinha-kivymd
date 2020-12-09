from faker import Faker
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import (
    OneLineAvatarIconListItem,
    ThreeLineAvatarIconListItem,
    IRightBodyTouch,
    IRightBody,
)
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel


faker = Faker('pt_BR')

produtos = [
    {'nome': 'Arroz', 'preço': 25.99, 'icon': 'cookie', 'desc': faker.sentence()},
    {'nome': 'Feijão', 'preço': 2.99, 'icon': 'cart', 'desc': faker.sentence()},
    {'nome': 'Macarrão', 'preço': 2.99, 'icon': 'chef-hat', 'desc': faker.sentence()},
    {'nome': 'Ovo', 'preço': 2.99, 'icon': 'stove', 'desc': faker.sentence()},
    {'nome': 'Batata', 'preço': 2.99, 'icon': 'cookie', 'desc': faker.sentence()},
    {'nome': 'Cernoura', 'preço': 2.99, 'icon': 'cookie', 'desc': faker.sentence()},
    {'nome': 'Brocolis', 'preço': 2.99, 'icon': 'cookie', 'desc': faker.sentence()},
    {'nome': 'Batata doce', 'preço': 2.99, 'icon': 'cookie', 'desc': faker.sentence()},
    {'nome': 'Azeitona', 'preço': 2.99, 'icon': 'cookie', 'desc': faker.sentence()},
    {'nome': 'Açucar', 'preço': 2.99, 'icon': 'cookie', 'desc': faker.sentence()},
]

compras = []

kv = '''
<ListItemWithCheckbox>:

    IconLeftWidget:
        icon: root.icon

    RightCheckbox:
        on_active: root.on_checkbox_active(*args)


<ListItemWithLabel>:
    IconLeftWidget:
        icon: root.icon

    RightLabel:
        text: '1.99'


<ComprasScreen>:
    name: 'compras'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Mercado do seu Idi'
            left_action_items: [['arrow-left', lambda x: app.back()]]
        ScrollView:
            MDList:
                id: lista_de_compras

<LojaScreen>:
    name: 'loja'
    BoxLayout:
        orientation: 'vertical'
        
        MDToolbar:
            title: 'Mercado do seu Idi'
            left_action_items: [['menu', lambda x: app.back()]]
            right_action_items: [['cart', lambda x: app.compras()]]
    
        ScrollView:
            MDList:
                id: lista_de_produtos
Manager:
    LojaScreen:
    ComprasScreen:
'''


class ListItemWithCheckbox(ThreeLineAvatarIconListItem):
    icon = StringProperty("android")

    def on_checkbox_active(self, checkbox, value):
        compras.append(
            (self.text, float(self.tertiary_text))
        )

class ListItemWithLabel(OneLineAvatarIconListItem):
    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    ...



class RightLabel(IRightBody, MDLabel):
    ...

class LojaScreen(MDScreen):
    ...


class ComprasScreen(MDScreen):
    ...


class Manager(ScreenManager):
    ...


class LojinhaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.primary_hue = "200" 
        return Builder.load_string(kv)


    def on_start(self):
        for produto in produtos:
            self.root.current_screen.ids.lista_de_produtos.add_widget(
                ListItemWithCheckbox(
                    text=produto['nome'],
                    secondary_text=produto['desc'],
                    tertiary_text=str(produto['preço']),
                    icon=produto['icon']
                )
            )

    def compras(self):
        self.root.current = 'compras'
        for compra in compras:
            self.root.current_screen.ids.lista_de_compras.add_widget(
                ListItemWithLabel(text=compra[0])
            )

    def back(self):
        self.root.current = 'loja'


LojinhaApp().run()
