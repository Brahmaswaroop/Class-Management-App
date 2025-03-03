from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from datetime import datetime, timedelta

KV = """
<CalendarScreen>:

    MDBoxLayout:
        orientation: "vertical"
        padding: 5
        
        MDBoxLayout:
            id: header
            size_hint_y: 0.1
            
            MDFlatButton:
                text: "<"
                font_size: 26
                size_hint_x: 0.2
                pos_hint: {"center_y": 0.5}
                on_release: root.change_month(-1)
            
            MDLabel:
                id: month_label
                halign: "center"
                font_size: 21
                size_hint_x: 0.6
                
            MDFlatButton:
                text: ">"
                font_size: 26
                size_hint_x: 0.2
                pos_hint: {"center_y": 0.5}
                on_release: root.change_month(1)
    
        MDBoxLayout:
            id: days_container
            orientation: "vertical"
"""

Builder.load_string(KV)

class CalendarScreen(MDFloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.month_label = None
        self.days_container = None
        self.current_date = datetime.now()

    def on_kv_post(self, base_widget):
        self.month_label = self.ids.month_label
        self.days_container = self.ids.days_container
        self.update_calendar()

    def update_calendar(self):
        self.month_label.text = self.current_date.strftime("%B %Y")
        self.days_container.clear_widgets()

        week_layout = MDBoxLayout(size_hint_y=0.1, pos_hint={"center_x": 0.5})
        for i, day in enumerate(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]):
            week_layout.add_widget(MDLabel(
                text=day,
                halign="center",
                size_hint_x=(1/7),
            ))
        self.days_container.add_widget(week_layout)

        # First day of the month
        first_day_of_month = self.current_date.replace(day=1)
        start_day = (first_day_of_month.weekday() + 1) % 7
        days_in_month = (self.current_date.replace(month=(self.current_date.month % 12)+1, day=1)-timedelta(days=1)).day

        # Days grid in FloatLayout
        days_layout = MDFloatLayout(size_hint_y=0.5)
        for i in range(start_day):
            days_layout.add_widget(MDLabel(size_hint=(1/7, 0.1)))  # Empty days before the first of the month

        for day in range(1, days_in_month + 1):
            btn = MDFlatButton(
                text=str(day),
                size_hint=(1/7, 0.1),
                pos_hint={"center_x": ((start_day+day-1) % 7 * (1/7))+0.07, "top": 1-(start_day+day-1)//7 * (1/6)}
            )
            btn.bind(on_release=self.on_date_selected)
            days_layout.add_widget(btn)
        self.days_container.add_widget(days_layout)

    def change_month(self, direction):
        new_month = (self.current_date.month - 1 + direction) % 12 + 1
        new_year = self.current_date.year + ((self.current_date.month - 1 + direction) // 12)
        self.current_date = self.current_date.replace(year=new_year, month=new_month, day=1)
        self.update_calendar()

    def on_date_selected(self, instance):
        print(f"Selected date: {instance.text} {self.current_date.strftime('%B %Y')}")

# class CalendarApp(MDApp):
#     def build(self):
#         return CalendarScreen()
#
# CalendarApp().run()
