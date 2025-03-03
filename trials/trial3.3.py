from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.label import MDLabel

class IconTextButton(MDBoxLayout):
    def __init__(self, text, icon, **kwargs):
        super().__init__(spacing=10, adaptive_size=True, **kwargs, size_hint=(1,1))

        self.add_widget(MDIconButton(icon=icon, theme_text_color="Custom", text_color=(0,0,0,1)))
        self.add_widget(MDLabel(text=text, theme_text_color="Custom", text_color=(0,0,0,1)))

class TestApp(MDApp):
    def build(self):
        button = MDRaisedButton(md_bg_color=(0, 0.5, 1, 1), size_hint=(0.2,0.1), pos_hint={"x":0.5, "y":0.5})
        button.add_widget(IconTextButton("Send Email", "email"))  # Custom layout inside button
        return button

TestApp().run()
