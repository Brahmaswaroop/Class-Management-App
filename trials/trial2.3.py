from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton

class TestApp(MDApp):
    def build(self):
        return MDBoxLayout(
            MDCard(
                radius=[16, 16, 16, 16],
                size_hint=(1, None),
                height=50,
                md_bg_color=(0, 0.5, 1, 1),
                padding=10,
                on_release=lambda x: print("Email button clicked"),
                children=[
                    MDIconButton(icon="email", theme_text_color="Custom", text_color=(1, 1, 1, 1)),
                    MDLabel(text="Email", theme_text_color="Custom", text_color=(1, 1, 1, 1))
                ]
            ),
            orientation="vertical",
            spacing=20,
            padding=20
        )

TestApp().run()
