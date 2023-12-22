import random
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class application(App):
   def build(self):
      available = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]
      layout = GridLayout(cols=4)
      for i in range(16):
         numb = random.choice(available)
         layout.add_widget(Label(text = 'click here'), on_touch_up = self.revealed, nmbr = numb)
         available.pop(numb)
      return layout
   def revealed(self,instance,left):
      self.layoutext = str(instance.numbr)
      storag = instance.nmbr
      clicky += 1
      if clicky == 2 and storag != instance.nmbr:
         self.layoutext = "click here!"
         clicky = 0
      if clicky == 2 and storag != instance.nmbr:
         clicky = 0
if __name__ == "__main__":
    myApp = application()
    myApp.run()