from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, IconLeftWidget, IconRightWidget, ThreeLineAvatarIconListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField
from plugins.database_manager import DatabaseManager


class StudentRecords(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.doj_field = None
        self.name_field = None
        self.clss_field = None
        self.dialog = None
        self.db_manager = DatabaseManager()
        self.database = "tuition.db"

        scroll = ScrollView()
        self.list_view = MDList()
        scroll.add_widget(self.list_view)
        self.add_widget(scroll)
        self.load_students()

    def load_students(self):
        self.list_view.clear_widgets()
        students = self.db_manager.execute_query(self.database, "SELECT * FROM students")

        for id_no, name, doj, clss in students.itertuples(index=False):
            list_item = ThreeLineAvatarIconListItem(text=name,
                                                    secondary_text=f"class {clss}",
                                                    tertiary_text=str(doj))
            edit_btn = IconLeftWidget(icon="file-document-edit")
            edit_btn.bind(on_release=lambda btn, self_id=id_no, self_name=name, self_doj=doj, self_class=clss:
                self.dialog_edit(self_id, self_name, self_doj, self_class))
            list_item.add_widget(edit_btn)

            delete_btn = IconRightWidget(icon="delete")
            delete_btn.bind(
                on_release=lambda btn, self_id=id_no, self_name=name: self.dialog_delete(self_id, self_name))
            list_item.add_widget(delete_btn)
            self.list_view.add_widget(list_item)

    def dialog_edit(self, id_no=None, name='', doj='', clss='', new_student=False):
        # for creating class attributes
        for var, value in [('name', name), ('doj', doj), ('clss', clss)]:
            setattr(self, f"{var}_field",
                    MDTextField(text=str(value),
                                hint_text=f"Enter {var}",
                                size_hint_y=None,
                                height=50)
                    )
        contents = MDBoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=self.name_field.height + self.clss_field.height + self.doj_field.height + 20
        )
        contents.add_widget(self.name_field)
        contents.add_widget(self.clss_field)
        contents.add_widget(self.doj_field)

        self.dialog = MDDialog(
            title="Student Editor",
            type="custom",
            content_cls=contents,
            size_hint_y=None,
            buttons=[
                MDRaisedButton(text="Discard", on_release=lambda x: self.dialog.dismiss()),
                MDRaisedButton(text="Save", on_release=lambda x: self.database_editor(id_no, new_student))
            ])
        self.dialog.open()

    def dialog_delete(self, id_no, name):
        self.dialog = MDDialog(
            title="Confirm Delete",
            text=f"Are you sure you want to delete entry named {name}?",
            buttons=[
                MDRaisedButton(text="No", on_release=lambda x: self.dialog.dismiss()),
                MDRaisedButton(text="Yes", on_release=lambda x: self.database_editor(id_no, deletion=True))
            ]
        )
        self.dialog.open()

    def database_editor(self, id_no=None, new_student=False, deletion=False):
        name = self.name_field.text
        clss = self.clss_field.text
        doj = self.doj_field.text

        if new_student:
            query = f"""INSERT INTO students (name, class, date_joined) VALUES
            ('{name}', '{clss}', '{doj}');"""
        elif deletion:
            query = f"DELETE FROM students WHERE id={id_no}"
        else:
            query = f"UPDATE students SET name='{name}', date_joined='{doj}', class='{clss}' WHERE id={id_no}"

        self.db_manager.execute_query(self.database, query, command="commit")

        self.dialog.dismiss()
        self.load_students()  # Refresh list after update
