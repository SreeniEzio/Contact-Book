from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import mainScreen
from backend import Backend

class DisplayContact(Screen):
    Builder.load_file('.\DisplayContact.kv')
    db = Backend()
    
    def on_enter(self):
        try:
            ID = mainScreen.contactID[-1]
            self.display(ID)
        except Exception:
            pass
        
        
    def display(self, id):
        data = self.db.fetch(id)[0]
        self.ids.name.text = f"Name:         {data['name']}"
        self.ids.email.text = f"E-Mail:       {data['email']}"
        self.ids.address.text = f"Address:      {data['address']}"
        self.ids.phone.text = f"Phone Number: {data['phone']}"
        
    