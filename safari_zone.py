import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random
visualfleechance = 'n/a'
visualcatchchance = 'n/a'
currentpokemon = 'n/a'
rocks = 0
is_baited = 'false'
Pokemondata = {'nidoran':{'flee': 10,
                          'catch': 50
                         },
                'doduo': {'flee': 50,
                         'catch': 60
                         },
                'venomoth': {'flee': 30,
                             'catch': 40
                             },
                'tauros': {'flee': 55,
                            'catch': 35
                            },
                'cubone': {'flee': 15,
                            'catch': 25
                            },
                'chansey': {'flee': 65,
                             'catch': 30
                           },
                'kangaskahn': {'flee': 15,
                                'catch': 15
                              },
                'dratini': {'flee': 50,
                             'catch': 10
                             },
                'pinsir': {'flee': 45,
                            'catch': 12 
                           },
                'scyther': {'flee': 70,
                             'catch': 18
                            },
                'mew': {'flee': 25,
                         'catch': 5
                         },
                }
class application(App):
   def build(self):
      layout = GridLayout(cols = 3)
      self.fleechance = Label(text = 'flee chance = ' + visualfleechance)
      self.catchchance = Label(text = 'catch chance = ' + visualcatchchance)
      self.encounter = Button(text = 'click here to encounter',on_press = self.newpokemon)
      self.safariball = Button(text = 'throw safari ball', on_press = self.safari)
      self.rock = Button(text = 'Rock', on_press = self.rocks)
      self.bait = Button(text = 'Bait', on_press = self.berry)
      self.run = Button(text = 'run', on_press = self.leave)
      layout.add_widget(self.fleechance)
      layout.add_widget(self.encounter)
      layout.add_widget(self.catchchance)
      layout.add_widget(self.safariball)
      layout.add_widget(self.rock)
      layout.add_widget(self.bait)
      layout.add_widget(self.run)
      return layout
   def newpokemon(self,instance):
      global visualcatchchance
      global visualfleechance
      global currentpokemon
      global rocks
      global is_baited
      global currentpokemon
      if currentpokemon == 'n/a':
         a = random.randint(1,100)
         if a <= 39:
            tier = 'common'
         if a >=40 and a <= 69:
            tier = 'uncommon'
         if a >= 70 and a <= 89:
            tier = 'rare'
         if a >= 90 and a <= 99:
            tier = 'super_rare'
         if a == 100:
            tier = 'mew'
            currentpokemon = 'mew'
            pkmnfleechance = 'medium'
            pkmncatchchance = 'very low'
         if tier == 'common':
            b = random.randint(1,2)
            if b == 1:
               currentpokemon = 'nidoran'
               pkmnfleechance = 'low'
               pkmncatchchance = 'high'
            if b == 2:
               currentpokemon = 'doduo'
               pkmnfleechance = 'high'
               pkmncatchchance = 'high'
         if tier == 'uncommon':
            b = random.randint(1,2)
            if b == 1:
               currentpokemon = 'tauros'
               pkmncatchchance = 'medium'
               pkmnfleechance = 'high'
            if b == 2:
               currentpokemon = 'venomoth'
               pkmncatchchance = 'medium'
               pkmnfleechance = 'medium'
         if tier == 'rare':
            b = random.randint(1,3)
            if b == 1:
               currentpokemon = 'cubone'
               pkmncatchchance = 'medium'
               pkmnfleechance = 'low'
            if b == 2:
               currentpokemon = 'chansey'
               pkmncatchchance = 'medium'
               pkmnfleechance = 'high'
            if b == 3:
               currentpokemon = 'kangaskahn'
               pkmnfleechance = 'low'
               pkmncatchchance = 'low'
         if tier == 'super_rare':
            b = random.randint(1,3)
            if b == 1:
               currentpokemon = 'dratini'
               pkmncatchchance = 'low'
               pkmnfleechance = 'high'
            if b == 2:
               currentpokemon = 'pinsir'
               pkmncatchchance = 'low'
               pkmnfleechance = 'medium'
            if b == 3:
               currentpokemon = 'scyther'
               pkmncatchchance = 'low'
               pkmnfleechance = 'low'
         self.layoutext = 'A wild ' + currentpokemon + ' appeared!'
         self.encounter.text = str(self.layoutext)
         visualfleechance = str(pkmnfleechance)
         self.fleechance.text = 'flee chance = ' + visualfleechance
         visualcatchchance = str(pkmncatchchance)
         self.catchchance.text = 'catch chance = ' + visualcatchchance
         is_baited = 'false'
         rocks = 0
   def safari(self,instance):
      global rocks
      global is_baited
      global currentpokemon
      if currentpokemon != 'n/a':
         c = random.randint(1,100)
         odds = Pokemondata[currentpokemon]['catch']
         odds = odds + (5*rocks)
         if is_baited == 'true':
            odds = odds/2
         if c <= odds:
            print('catch success!')
            self.layoutext =  'you caught a ' + currentpokemon + '! click again to encounter another pokemon'
            self.encounter.text = self.layoutext
            currentpokemon = 'n/a'
            visualcatchchance = 'n/a'
            visualfleechance = 'n/a'
            self.catchchance.text = visualcatchchance
            self.fleechance.text = visualfleechance

         else:
            print('catch fail')
   def rocks(self,instance):
      global rocks
      if currentpokemon != 'n/a':
         rocks = rocks + 1
   def berry(self,instance):
      global is_baited
      if is_baited == 'false' and currentpokemon != 'n/a':
         is_baited = 'true'
   def leave(self,instance):
      if currentpokemon != 'n/a':
         self.layoutext =  'click again to encounter another pokemon'
         self.encounter.text = self.layoutext
         currentpokemon = 'n/a'
         visualcatchchance = 'n/a'
         visualfleechance = 'n/a'
         self.catchchance.text = visualcatchchance
         self.fleechance.text = visualfleechance
if __name__ == "__main__":
    myApp = application()
    myApp.run()