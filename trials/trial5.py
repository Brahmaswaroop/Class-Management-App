from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDCard:
        radius: 36
        md_bg_color: "grey"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .6, .4

        FitImage:
            source: "../resources/tuition_management_system.jpg"
            pos_hint: {"top": 1}
            radius: 36
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)


Example().run()