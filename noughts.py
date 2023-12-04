import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class application(App):
   def build(self):
      self.n = 'nought'
      layout = GridLayout(cols=5)
      for i in range(25):
        layout.add_widget(Button(text = '',on_press = self.handle_click))
      return layout
   def handle_click(self, instance):
      print(self.n)
      if self.n == 'nought':
         instance.text = 'O'
         self.n = 'cross'
      if self.n == 'cross':
         instance.text = 'X'
         self.n = 'nought'
if __name__ == "__main__":
    myApp = application()
    myApp.run()