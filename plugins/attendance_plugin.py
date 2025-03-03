from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.pickers import MDDatePicker

from plugins.database_manager import DatabaseManager


class DateSelector(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.date_field = MDTextField(
            mode="rectangle",
            hint_text="Select a date",
            size_hint_x=0.6,
            readonly=True,
            icon_right="calendar"
        )
        self.date_field.bind(focus=self.on_focus)
        self.add_widget(self.date_field)

    def on_focus(self, instance, value):
        if value:
            self.show_date_picker()

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.set_date)
        date_dialog.open()

    def set_date(self, instance, value, date_range):
        self.date_field.text = str(value)


class AttendanceBook(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", size_hint_y=None, **kwargs)
        self.bind(minimum_height=self.setter("height"))
        self.db = DatabaseManager()
        self.student_attendance = {}
        students = self.db.execute_query("tuition.db", "SELECT id, name FROM students")
        for id_no, name in students.itertuples(index=False):
            self.student_attendance[str(id_no)] = 1
            button = MDRaisedButton(
                id=str(id_no),
                text=name,
                md_bg_color=(17 / 255, 191 / 255, 40 / 255, 1),
            )
            button.bind(on_release=self.mark_absent)
            self.add_widget(button)

    def mark_absent(self, instance):
        if instance.md_bg_color == (17 / 255, 191 / 255, 40 / 255, 1):
            self.student_attendance[instance.id] = 0
            instance.md_bg_color = (196 / 255, 12 / 255, 12 / 255, 1)
        else:
            self.student_attendance[instance.id] = 1
            instance.md_bg_color = (17 / 255, 191 / 255, 40 / 255, 1)

# class ExampleApp(MDApp):
#     def build(self):
#         return DateSelector()
# ExampleApp().run()
