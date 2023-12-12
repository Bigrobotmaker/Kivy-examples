import random
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class application(App):
   def build(self):
      layout = GridLayout(cols=4)
      for i in range(16):
        layout.add_widget(Label(text = 'click here'), on_touch_up = self.revealed)
      return layout
   def revealed(self,instance,left):
      self.layoutext = str(self.numbr)
      clicky += 1
      if clicky == 2:
         self.layoutext = "click here!"
         clicky = 0
if __name__ == "__main__":
    myApp = application()
    myApp.run()