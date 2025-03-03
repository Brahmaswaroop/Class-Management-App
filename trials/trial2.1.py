from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen:

    MDCard:
        size_hint: None, None
        size: "280dp", "120dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 5
        radius: [12,]
        on_release: app.card_clicked()

        BoxLayout:
            orientation: "horizontal"
            spacing: "10dp"
            padding: "10dp"

            MDIcon:
                icon: "email"
                theme_text_color: "Custom"
                text_color: 0, 0, 1, 1
                size_hint: None, None
                size: "48dp", "48dp"

            MDLabel:
                text: "Click me!"
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1
                valign: "center"
"""

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def card_clicked(self):
        print("Card clicked!")

TestApp().run()
