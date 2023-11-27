import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class application(App):
   def build(self):
      layout = GridLayout(cols=2)
     
      layout.add_widget(Label(text='temp in'))
      self.tinput = TextInput(multiline=False)
      layout.add_widget(self.tinput)

      layout.add_widget(Button(text = 'F to C',on_press =self.FtoC))

      layout.add_widget(Button(text = 'C to F',on_press =self.CtoF))

      self.resultLabel = Label(text='')
      layout.add_widget(self.resultLabel)
      return layout
if __name__ == '__main__':
   myApp = application()
   myApp.run()