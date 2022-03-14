from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.theming import ThemeManager

# global variables
username = ""
password = ""
email = ""
first_name = ""
last_name = ""
full_name = ""
school = ""
subject = ""
extracurricular = ""
about_me = ""

class Login(MDScreen):

    class LoginLabel(MDRelativeLayout):
        pass

    class UsernameTextField(MDRelativeLayout):
        text = StringProperty()
        hint_text = StringProperty()

        def set_username(self, x):
            global username
            username = x

    class PasswordTextField(MDRelativeLayout):
        text = StringProperty("")
        hint_text = StringProperty()

        def set_password(self, x):
            global password
            password = x

    class ContinueButton(MDRelativeLayout):
        text = StringProperty()

        def get_username(self):
            global username
            return username

        def get_password(self):
            global password
            return password

        def get_email(self):
            global email
            return email

        def get_first_name(self):
            global first_name
            return first_name

        def get_last_name(self):
            global last_name
            return last_name

        def get_school(self):
            global school
            return school

        def get_subject(self):
            global subject
            return subject

        def get_extracurricular(self):
            global extracurricular
            return extracurricular


class CreateAccountp1(MDScreen):

    class CreateAccountLabel(MDRelativeLayout):
        pass

    class EmailTextField(MDRelativeLayout):
        text = StringProperty()
        hint_text = StringProperty()

        def set_email(self, x):
            global email
            email = x

class CreateAccountp2(MDScreen):
    pass
    class FirstNameTextField(MDRelativeLayout):
        text = StringProperty()
        hint_text = StringProperty()
        icon_right = StringProperty()

        def set_first_name(self, x):
            global first_name
            first_name = x

    class LastNameTextField(MDRelativeLayout):
        text = StringProperty()
        hint_text = StringProperty()
        icon_right = StringProperty()

        def set_last_name(self, x):
            global last_name
            last_name = x

    class SchoolTextField(MDRelativeLayout):
        text = StringProperty()
        hint_text = StringProperty()
        icon_right = StringProperty()
        def set_school(self, x):
            global school
            school = x

    class SubjectTextField(MDRelativeLayout):
        text = StringProperty()
        hint_text = StringProperty()
        icon_right = StringProperty()

        def set_subject(self, x):
            global subject
            subject = x

    class ExtracurricularTextField(MDRelativeLayout):
        text = StringProperty()
        hint_text = StringProperty()
        icon_right = StringProperty()

        def set_extracurricular(self, x):
            global extracurricular
            extracurricular = x

    class AboutMeTextField(MDRelativeLayout):
        text = StringProperty()
        hint_text = StringProperty()
        icon_right = StringProperty()

        def set_about_me(self, x):
            global about_me
            about_me = x


class Profile(MDScreen):
    pass


class BackButton(MDRelativeLayout):
    page = StringProperty()


class ScreenManager(MDScreen):
    pass


class Teach4Me(MDApp):
    theme_cls = ThemeManager()
    screenList = ["Login", "CreateAccountp1", "CreateAccountp2", "Profile"]

    def build(self):
        return

    def callback(self, screen):
        global username, email, password, first_name, last_name, full_name, school, subject, extracurricular, about_me
        full_name = first_name + " " + last_name
        currentScreen = self.root.current
        if screen is None:
            return
        if screen == self.screenList[-1] or currentScreen == self.screenList[self.screenList.index(screen) - 1]:
            self.root.transition.direction = "left"
        else:
            self.root.transition.direction = "right"
        self.root.current = screen
        if self.root.current == self.screenList[-1]:
            profile_screen = self.root.get_screen(self.root.current)
            profile_screen.ids['usernamelabel'].text = username
            profile_screen.ids['schoollabel'].text = "Teaches at " + school
            profile_screen.ids['schoollabel'].font_size = 15
            profile_screen.ids['subjectlabel'].text = "Teaches " + subject
            profile_screen.ids['subjectlabel'].font_size = 15
            profile_screen.ids['extralabel'].text = "Inolved in " + extracurricular
            profile_screen.ids['extralabel'].font_size = 15
            if about_me == "":
                profile_screen.ids['aboutme'].text = "No description"
            else:
                profile_screen.ids['aboutme'].text = about_me
                profile_screen.ids['aboutme'].font_style = "Body1"
                profile_screen.ids['aboutme'].font_size = 15
                profile_screen.ids['aboutme'].pos_hint = {"center_y": .52}
            profile_screen.ids['namelabel'].text = full_name
            profile_screen.ids['namelabel'].font_size = 16
            profile_screen.ids['email'].text = email
            profile_screen.ids['email'].font_size = 16
            profile_screen.ids['password'].text = password
            profile_screen.ids['password'].font_size = 16


Window.size = (425, 750)
Teach4Me().run()