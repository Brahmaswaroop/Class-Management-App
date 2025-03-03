from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from threading import Thread
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton

from plugins.database_manager import DatabaseManager
from plugins.attendance_plugin import DateSelector, AttendanceBook
from plugins.calender_plugin import CalendarScreen
from plugins.fee_record_plugin import StudentFeeDetails
from plugins.student_records_plugin import StudentRecords

class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        image = Image(source="resources/load.gif", anim_delay=0.05)
        self.add_widget(image)

class CustomButton(MDRaisedButton):
    pass

class ClassManagerApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.go_back_list = []

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "LightBlue"
        return Builder.load_file("index.kv")

    def go_back(self):
        if self.go_back_list:
            screen_name = self.go_back_list.pop()
            self.root.current = screen_name

    def switch_screen(self, screen_name, *args):
        if self.root.has_screen(screen_name):
            self.go_back_list.append(self.root.current)
            self.root.current = screen_name
        else:
            print(f"Screen '{screen_name}' not found")

    # def on_start(self):
    #     self.root.add_widget(LoadingScreen(name="loading_screen"))
    #     self.root.current = "loading_screen"  # Show a loading screen
    #     Thread(target=self.download_db, daemon=True).start()

    def download_db(self):
        database_manager = DatabaseManager()
        database_manager.database_download()
        Clock.schedule_once(lambda dt: self.switch_screen("main_screen"))

ClassManagerApp().run()
