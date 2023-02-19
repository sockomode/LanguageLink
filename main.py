from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import NoTransition
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.icon_definitions import md_icons
from kivymd.uix.floatlayout import MDFloatLayout

import functions
import Profile

Window.size = (310, 580)

Builder.load_file('kv/basicpages.kv')
Builder.load_file('kv/loginpage.kv')



class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class LoginPage(Screen):
    pass

class BrowsePage(Screen):
    pass

class ProfileCard(MDFloatLayout, FakeRectangularElevationBehavior):
    pass
class ProfilePage(Screen):
    pass

class ConnectionsPage(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Cyan"

        functions.fill()
        myprof = Profile.Profile("Brandon", ["German"], "Chinese", "US", "bxu@gmail.com", "teehee", 12, 1231231234)
        prof = functions.profToList(myprof)
        prof2 = myprof.getProf()

        sm = MyScreenManager(transition=NoTransition())
        sm.add_widget(BrowsePage(name='browsepage'))
        sm.add_widget(ConnectionsPage(name='connectionspage'))
        sm.add_widget(ProfilePage(name='profilepage'))
        sm.add_widget(LoginPage(name='loginpage'))

        sm.current = 'loginpage'

        return sm


    def attempt_login(self, username, password):
        print('Username input:', username.text)
        print('Password input:', password.text)

        # username and password check
        self.root.current = 'browsepage'

    def switch_screen(self, screen_name):
        self.root.current = screen_name

    def give_like(self):
        Profile.likeProfile(self)


MainApp().run()
