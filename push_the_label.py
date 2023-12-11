import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class application(App):
   def build(self):
      layout = GridLayout(cols=2)
      layoutext = 0
      self.layoutext = layoutext
      self.drlabel = Label(text = str(layoutext),on_touch_up = self.addup)
      layout.add_widget(self.drlabel)
      return layout
   def addup(self,instance,left):
      self.layoutext = self.layoutext + 1
      self.drlabel.text = str(self.layoutext)
      


if __name__ == "__main__":
    myApp = application()
    myApp.run()
