import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class application(App):
   def build(self):
      layout = GridLayout(cols=2)
      layoutext = 0
      self.layoutext = layoutext
      layout.add_widget(Label(text = str(layoutext)))
      return layout
   def on_touch_up(self):
      self.layoutext = self.layoutext + 1
      print(self.layoutext)
      


if __name__ == "__main__":
    myApp = application()
    myApp.run()
