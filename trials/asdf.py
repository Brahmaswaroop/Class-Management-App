from kivymd.app import MDApp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

class ScrollableButtons(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Container for buttons
        self.box_layout = MDBoxLayout(
            orientation="vertical",
            size_hint_y=None,  # Required for scrolling
            spacing=10,
            padding=10
        )
        self.box_layout.bind(minimum_height=self.box_layout.setter("height"))

        # Add multiple buttons dynamically
        for i in range(20):  # You can change this number
            btn = MDRaisedButton(
                text=f"Button {i+1}",
                size_hint_x=0.8,
                pos_hint={"center_x": 0.5}
            )
            self.box_layout.add_widget(btn)

        self.add_widget(self.box_layout)

class ScrollApp(MDApp):
    def build(self):
        return ScrollableButtons()

ScrollApp().run()
