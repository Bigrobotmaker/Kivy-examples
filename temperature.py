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
   def FtoC(self,instance):
      try:
         self.resultLabel.text = (int(self.tinput.text)-32)//1.8
      except:
         self.resultLabel.text = 'an error was encountered, please check your input'
   
   def CtoF(self,instance):
      try:
         self.resultLabel.text = (int(self.tinput.text)+32)*1.8
      except:
         self.resultLabel.text = 'an error was encountered, please check your input'
   
if __name__ == '__main__':
   myApp = application()
   myApp.run()