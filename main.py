from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, SlideTransition

from backend import Backend
from mainScreen import MainScreen
from AddContactsScreen import AddContact
from EditContact import EditContactScreen
from DisplayContactScreen import DisplayContact

Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')
Config.set('graphics', 'resizable', False)

class ContactBookApp(MDApp):
    def build(self):
        #self.theme_cls.primary_palette = "Teal"
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MainScreen(name='mainScreen'))
        sm.add_widget(AddContact(name='contact'))
        sm.add_widget(DisplayContact(name='display_contact'))
        sm.add_widget(EditContactScreen(name='edit_contact'))
        return sm
        #return Contact()
    
    def on_start(self):
        self.backend = Backend()

ContactBookApp().run()
