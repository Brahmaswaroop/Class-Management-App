from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton

class TestApp(MDApp):
    def build(self):
        return MDFillRoundFlatIconButton(
            text="Like",
            icon="thumb-up",
            size_hint=(0.4, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            line_width=20
        )

TestApp().run()
