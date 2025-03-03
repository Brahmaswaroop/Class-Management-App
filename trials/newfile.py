from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker

KV = '''
MDScreen:

    MDTextField:
        id: date_field
        mode: "rectangle"
        hint_text: "Select a date"
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint_x: .6
        readonly: True
        icon_right: "calendar"
        on_focus: if self.focus: app.show_date_picker()

'''


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.set_date)
        date_dialog.open()

    def set_date(self, instance, value, date_range):
        self.root.ids.date_field.text = str(value)


Example().run()
