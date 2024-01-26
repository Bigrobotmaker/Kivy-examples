import random
import kivy
import time
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock
WIDTH = 4
HEIGHT = 5
class application(App):
    def revealingbutton(Button):
        button
class Revealingbutton(Button):
     def __init__(self,row,col,parent):
          super()__init__():
          self.row = row
class buttongrid(GridLayout):
        def __init__(self):
             super().__init__()
             layout = GridLayout(5)
             self.values = ([0]*WIDTH for i in range(HEIGHT))
        def __build__(self):
             super().build():
             self.buttons =[[0]* WIDTH for i in range(HEIGHT)]
             for row in range(HEIGHT):
                  for col in range(WIDTH):
                       currentbutton = Revealingbutton




if __name__ == "__main__":
    myApp = application()
    myApp.run()
