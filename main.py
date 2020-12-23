from os.path import abspath
from faker import Faker
from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.list import (
    IRightBody,
    IRightBodyTouch,
    OneLineAvatarIconListItem,
    ThreeLineAvatarIconListItem,
)
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.card import MDCard

faker = Faker("pt_BR")

produtos = [
    {
        "nome": "Arroz",
        "preco": 25.99,
        "icon": "cookie",
        "desc": faker.sentence(),
    },
    {
        "nome": "Feijão",
        "preco": 2.99,
        "icon": "cart",
        "desc": faker.sentence(),
    },
    {
        "nome": "Macarrão",
        "preco": 2.99,
        "icon": "chef-hat",
        "desc": faker.sentence(),
    },
    {"nome": "Ovo", "preco": 2.99, "icon": "stove", "desc": faker.sentence()},
    {
        "nome": "Batata",
        "preco": 2.99,
        "icon": "stove",
        "desc": faker.sentence(),
    },
    {
        "nome": "Cernoura",
        "preco": 2.99,
        "icon": "cookie",
        "desc": faker.sentence(),
    },
    {
        "nome": "Brocolis",
        "preco": 2.99,
        "icon": "cookie",
        "desc": faker.sentence(),
    },
    {
        "nome": "Batata doce",
        "preco": 2.99,
        "icon": "cookie",
        "desc": faker.sentence(),
    },
    {
        "nome": "Azeitona",
        "preco": 2.99,
        "icon": "cookie",
        "desc": faker.sentence(),
    },
    {
        "nome": "Açucar",
        "preco": 2.99,
        "icon": "cookie",
        "desc": faker.sentence(),
    },
]

kv = abspath("./main.kv")


class ListItemWithCheckbox(ThreeLineAvatarIconListItem):
    icon = StringProperty("android")

    def on_checkbox_active(self, checkbox, value):
        if value:
            self.get_root_window().children[0].get_screen("compras").compras.append(
                (self.text, self.tertiary_text)
            )
        else:
            self.get_root_window().children[0].get_screen("compras").compras.remove(
                (self.text, self.tertiary_text)
            )

    def on_release(self):
        self.get_root_window().children[0].get_screen("loja").children[
            0
        ].disabled = True
        self.get_root_window().children[0].get_screen("loja").add_widget(
            MyCard(nome=self.text, desc=self.secondary_text, preco=self.tertiary_text)
        )


class ListItemWithLabel(OneLineAvatarIconListItem):
    icon = StringProperty("plus")
    preco = StringProperty()


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    ...


class RightLabel(IRightBody, MDLabel):
    ...


class LojaScreen(MDScreen):
    lista_de_produtos = ObjectProperty()


class ComprasScreen(MDScreen):
    lista_de_compras = ObjectProperty()
    compras = ListProperty()

    def on_compras(self, instance, value):
        self.lista_de_compras.clear_widgets()
        print(self.compras)
        for compra in self.compras:
            self.lista_de_compras.add_widget(
                ListItemWithLabel(text=compra[0], preco=str(compra[1]))
            )


class Manager(ScreenManager):
    ...


class MyCard(MDCard):
    nome = StringProperty()
    preco = StringProperty()
    desc = StringProperty()
    card = ObjectProperty()

    def __init__(self, nome, preco, desc, **kwargs):
        super().__init__(**kwargs)
        self.nome = nome
        self.preco = str(preco)
        self.desc = desc

    def add_to_cart(self, *args):
        self.get_root_window().children[0].get_screen("compras").compras.append(
            (self.nome, self.preco)
        )


class LojinhaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "200"
        return Builder.load_file(kv)

    def on_start(self):
        for produto in produtos:
            self.root.get_screen("loja").lista_de_produtos.add_widget(
                ListItemWithCheckbox(
                    text=produto["nome"],
                    secondary_text=produto["desc"],
                    tertiary_text=str(produto["preco"]),
                    icon=produto["icon"],
                )
            )

    def compras(self):
        self.root.current = "compras"

    def back(self):
        self.root.current = "loja"

    def color(self):
        style = self.theme_cls.theme_style
        if style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def quit_card(self, instance):
        self.root.current_screen.children[1].disabled = False
        self.root.current_screen.remove_widget(instance)


LojinhaApp().run()
