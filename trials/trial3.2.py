from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatIconButton

class TestApp(MDApp):
    def build(self):
        return MDRectangleFlatIconButton(
            text="Outlined Button",
            icon="star",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

TestApp().run()
