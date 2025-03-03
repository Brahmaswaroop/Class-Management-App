from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen:

    MDCard:
        size_hint: None, None
        size: "300dp", "180dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 8
        radius: [15,]
        md_bg_color: 0.2, 0.2, 0.2, 1

        BoxLayout:
            orientation: "vertical"
            padding: "10dp"
            spacing: "10dp"

            MDIcon:
                icon: "account"
                halign: "center"
                size_hint_y: None
                height: "50dp"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDLabel:
                text: "User Profile"
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1

            MDRaisedButton:
                text: "View Profile"
                pos_hint: {"center_x": 0.5}
                on_release: app.on_button_press()
"""

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_button_press(self):
        print("Profile button clicked!")

TestApp().run()
