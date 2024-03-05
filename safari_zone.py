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
      layout = GridLayout(cols = 3)
      self.fleechance = Label(text = 'flee chance = ' + visualfleechance)
      self.catchchance = Label(text = 'catch chance = ' + visualcatchchance)
      self.encounter = Button(text = 'click here to encounter',on_press = self.newpokemon)
      layout.add_widget(self.fleechance)
      layout.add_widget(self.encounter)
      layout.add_widget(self.catchchance)
      return layout
   def newpokemon(self,instance):
      global visualcatchchance
      global visualfleechance
      global currentpokemon
      if currentpokemon == 'n/a':
         self.layoutext = 'A wild rattata appeared!'
         self.encounter.text = str(self.layoutext)
         visualfleechance = 'medium'
         self.fleechance.text = 'flee chance = ' + visualfleechance
         visualcatchchance = 'high'
         self.catchchance.text = 'catch chance = ' + visualcatchchance
if __name__ == "__main__":
    myApp = application()
    myApp.run()