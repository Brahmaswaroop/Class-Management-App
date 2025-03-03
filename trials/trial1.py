from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivy.lang import Builder

KV = '''
MDNavigationLayout:

    MDScreenManager:

        MDScreen:
            name: "home"
            
            MDBoxLayout:
                orientation: "vertical"

                MDTopAppBar:
                    title: "Home"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]

                MDLabel:
                    text: "Welcome!"
                    halign: "center"

    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 0, 0, 0) 
        MDBoxLayout:
            orientation: "vertical"
            spacing: "8dp"
            padding: "8dp"

            MDLabel:
                text: "Menu"
                theme_text_color: "Primary"

            MDFlatButton:
                text: "Option 1"
                on_release: nav_drawer.set_state("close")

            MDFlatButton:
                text: "Option 2"
                on_release: nav_drawer.set_state("close")
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
