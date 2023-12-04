import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class application(App):
   def build(self):
#      self.grid = []
#      for i in range(6):
#         for j in range (6):
#            self.grid.append((i,j))
      self.n = 'nought'
      layout = GridLayout(cols=5)
      for i in range(25):
        layout.add_widget(Button(text = '',on_press = self.handle_click))
      return layout
   def handle_click(self, instance):
      if self.n == 'nought' and instance.text == '':
         instance.text = 'O'
         self.n = 'cross'
      elif self.n == 'cross' and instance.text == '':
         instance.text = 'X'
         self.n = 'nought'
if __name__ == "__main__":
    myApp = application()
    myApp.run()