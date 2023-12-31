import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

#class application(App):
#   def build(self):
#       layout = BoxLayout(orientation='horizontal')
#       layout.add_widget(Label(text='press it-->'))
#       layout.add_widget(Label(text='you know you want to-->'))
#       layout.add_widget(Button(text='THE BUTTON!'))
#       layout.add_widget(Button(text='THE (other) BUTTON!'))
#       return layout


#if __name__ == '__main__':
#   myApp = application()
#   myApp.run()

class application(App):
   def build(self):
      layout = GridLayout(cols=2)
     
      layout.add_widget(Label(text='First Number'))
      self.firstNumberInput = TextInput(multiline=False)
      layout.add_widget(self.firstNumberInput)

      layout.add_widget(Label(text='Second Number'))
      self.secondNumberInput = TextInput(multiline=False)
      layout.add_widget(self.secondNumberInput)

      self.calculateButton = Button(text = 'multiply',on_press = self.handle_click)
      layout.add_widget(self.calculateButton)
      self.resultLabel = Label(text='')
      layout.add_widget(self.resultLabel)

      self.calculateButton = Button(text = 'add',on_press = self.handle_click2)
      layout.add_widget(self.calculateButton)
      self.resultLabel = Label(text='')
      layout.add_widget(self.resultLabel)
      
      self.calculateButton = Button(text = 'subtract',on_press = self.handle_click3)
      layout.add_widget(self.calculateButton)
      self.resultLabel = Label(text='')
      layout.add_widget(self.resultLabel)

      self.calculateButton = Button(text = 'divide',on_press = self.handle_click4)
      layout.add_widget(self.calculateButton)
      self.resultLabel = Label(text='')
      layout.add_widget(self.resultLabel)
      return layout

   def handle_click(self, instance):
      try:
         result = self.get_first_number() * self.get_second_number()
         self.resultLabel.text = 'Result: ' + str(result )
      except:
         self.resultLabel.text = 'there was an error'

   def handle_click2(self, instance):
      try:
         result = self.get_first_number() + self.get_second_number()
         self.resultLabel.text = 'Result: ' + str(result )
      except:
         self.resultLabel.text = 'there was an error'
   
   def handle_click3(self, instance):
      try:
         result = self.get_first_number() - self.get_second_number()
         self.resultLabel.text = 'Result: ' + str(result )
      except:
         self.resultLabel.text = 'there was an error'
   
   def handle_click4(self, instance):
      try:
            if self.get_second_number() == 0:
               self.resultLabel.text = 'error, division by 0'
            else:
               result = self.get_first_number() // self.get_second_number()
               self.resultLabel.text = 'Result: ' + str(result )
      except:
         self.resultLabel.text = 'there was an error'


   def get_first_number(self):
         return int(self.firstNumberInput.text)
   
   def get_second_number(self):
      return int(self.secondNumberInput.text)
if __name__ == '__main__':
   myApp = application()
   myApp.run()
