from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None

        open_popup_btn = MDRaisedButton(
            text="Open Pop-up",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=self.show_popup
        )
        self.add_widget(open_popup_btn)

    def show_popup(self, instance):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Popup Window",
                type="custom",
                content_cls=MDScreen(),
                buttons=[
                    MDRaisedButton(text="Close", on_release=lambda x: self.dialog.dismiss())
                ],
            )
        self.dialog.open()

class MyApp(MDApp):
    def build(self):
        return MainScreen()

MyApp().run()
