from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.theming import ThemeManager


class UsernameTextField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class PasswordTextField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class ContinueButton(MDRelativeLayout):
   pass


class CreateAccountButton(MDRelativeLayout):
   def on_press(self):
       print("account created")


class EmailTextField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class AccountTextField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()


class Myapp(MDApp):
    theme_cls = ThemeManager()
    screenList = ["Login", "CreateAccountp1", "CreateAccountp2"]

    def build(self):
        return

    def callback(self, screen):
        currentScreen = self.root.current
        if screen is None:
            return
        if screen == self.screenList[-1] or currentScreen == self.screenList[self.screenList.index(screen) - 1]:
            self.root.transition.direction = "left"
        else:
            self.root.transition.direction = "right"
        self.root.current = screen


Window.size = (425, 750)
Myapp().run()

#
# from kivy.lang import Builder
# from kivy.properties import StringProperty
# from kivy.uix.screenmanager import Screen
#
# from kivymd.icon_definitions import md_icons
# from kivymd.app import MDApp
# from kivymd.uix.list import OneLineIconListItem
#
#
# Builder.load_string(
#     '''
# #:import images_path kivymd.images_path
#
#
# <CustomOneLineIconListItem>
#
#     IconLeftWidget:
#         icon: root.icon
#
#
# <PreviousMDIcons>
#
#     MDBoxLayout:
#         orientation: 'vertical'
#         spacing: dp(10)
#         padding: dp(20)
#
#         MDBoxLayout:
#             adaptive_height: True
#
#             MDIconButton:
#                 icon: 'magnify'
#
#             MDTextField:
#                 id: search_field
#                 hint_text: 'Search icon'
#                 on_text: root.set_list_md_icons(self.text, True)
#
#         RecycleView:
#             id: rv
#             key_viewclass: 'viewclass'
#             key_size: 'height'
#
#             RecycleBoxLayout:
#                 padding: dp(10)
#                 default_size: None, dp(48)
#                 default_size_hint: 1, None
#                 size_hint_y: None
#                 height: self.minimum_height
#                 orientation: 'vertical'
# '''
# )
#
#
# class CustomOneLineIconListItem(OneLineIconListItem):
#     icon = StringProperty()
#
#
# class PreviousMDIcons(Screen):
#
#     def set_list_md_icons(self, text="", search=False):
#         '''Builds a list of icons for the screen MDIcons.'''
#
#         def add_icon_item(name_icon):
#             self.ids.rv.data.append(
#                 {
#                     "viewclass": "CustomOneLineIconListItem",
#                     "icon": name_icon,
#                     "text": name_icon,
#                     "callback": lambda x: x,
#                 }
#             )
#
#         self.ids.rv.data = []
#         for name_icon in md_icons.keys():
#             if search:
#                 if text in name_icon:
#                     add_icon_item(name_icon)
#             else:
#                 add_icon_item(name_icon)
#
#
# class MainApp(MDApp):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.screen = PreviousMDIcons()
#
#     def build(self):
#         return self.screen
#
#     def on_start(self):
#         self.screen.set_list_md_icons()
#
#
# MainApp().run()