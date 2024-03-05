import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
visualfleechance = 'n/a'
visualcatchchance = 'n/a'
currentpokemon = 'n/a'
class application(App):
   def build(self):
      global visualfleechance
      global visualcatchchance
      layout = GridLayout()
      self.fleechance = Label(text = 'flee chance = ' + visualfleechance)
      self.catchchance = Label(text = 'catch chance = ' + visualcatchchance)
      self.encounter = Button(text = 'click here to encounter',on_press = self.encounter)
      layout.add_widget(self.fleechance)
      layout.add_widget(self.encounter)
      layout.add_widget(self.catchchance)
   def encounter(self):
      global visualcatchchance
      global visualfleechance
      global currentpokemon
      if currentpokemon != 'n/a':
         self.layoutext = 'A wild rattata appeared!'
         self.encounter.text = str(self.layoutext)
         visualfleechance.text = 'medium'
         self.fleechance.text = visualfleechance
         visualcatchchance = 'high'
         self.catchchance.text = visualcatchchance
      