import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class application(App):
   def build(self):
      self.num = 1
      layout = GridLayout(cols=2)
      layout.add_widget(Button(text = '+',on_press = self.add))
      self.number = Label(text = str(self.num))
      layout.add_widget(self.number)
      layout.add_widget(Button(text = '-',on_press  = self.subtract))
      return layout
   def add(self,instance):
      self.num = self.num + 1
      self.number.text = str(self.num)
   def subtract(self,instance):
      self.num = self.num - 1
      self.number.text = str(self.num)
      
if __name__ == '__main__':
   myApp = application()
   myApp.run()