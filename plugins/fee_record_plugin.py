from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

KV = """
<StudentFeeDetails>:
    orientation: "vertical"

    MDBoxLayout:
        id: table_months
        size_hint_y: None
        height: self.minimum_height

        MDBoxLayout:
            id: table1
            orientation: "vertical"
            size_hint_x: 0.5
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)

            MDRaisedButton:
                text: "January"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}

        MDBoxLayout:
            id: table2
            orientation: "vertical"
            size_hint_x: 0.5
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)

            MDRaisedButton:
                text: "February"
                size_hint_x: 0.8
                pos_hint: {"center_x": 0.5}

    MDBoxLayout:
        id: students
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height
"""

class StudentFeeDetails(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# class MyApp(MDApp):
#     def build(self):
#         return StudentFeeDetails()
# MyApp().run()
