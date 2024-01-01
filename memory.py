import random
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#current plan: make 16 different labels and add in a random order
class application(App):
   def build(self):
      last_num = 0
      taken = []
      gen = 0
      layout = GridLayout(cols=4)
      self.card1 = Label(text = 'click here',on_touch_up = self.revealed1)
      self.card2 = Label(text = 'click here',on_touch_up = self.revealed1)
      self.card3 = Label(text = 'click here',on_touch_up = self.revealed2)
      self.card4 = Label(text = 'click here',on_touch_up = self.revealed2)
      self.card5 = Label(text = 'click here',on_touch_up = self.revealed3)
      self.card6 = Label(text = 'click here',on_touch_up = self.revealed3)
      self.card7 = Label(text = 'click here',on_touch_up = self.revealed4)
      self.card8 = Label(text = 'click here',on_touch_up = self.revealed4)
      self.card9 = Label(text = 'click here',on_touch_up = self.revealed5)
      self.card10 = Label(text = 'click here',on_touch_up = self.revealed5)
      self.card11 = Label(text = 'click here',on_touch_up = self.revealed6)
      self.card12 = Label(text = 'click here',on_touch_up = self.revealed6)
      self.card13 = Label(text = 'click here',on_touch_up = self.revealed7)
      self.card14 = Label(text = 'click here',on_touch_up = self.revealed7)
      self.card15 = Label(text = 'click here',on_touch_up = self.revealed8)
      self.card16 = Label(text = 'click here',on_touch_up = self.revealed8)
      for i in range(16):
         while gen in taken and len(taken) != 16:
            gen = random.randint(1,16) 
         if gen == 1:
            layout.add_widget(self.card1)
            taken.append(1)
         if gen == 2:
            layout.add_widget(self.card2)
            taken.append(2)
         if gen == 3:
            layout.add_widget(self.card3)
            taken.append(3)
         if gen == 4:
            layout.add_widget(self.card4)
            taken.append(4)
         if gen == 5:
            layout.add_widget(self.card5)
            taken.append(5)
         if gen == 6:
            layout.add_widget(self.card6)
            taken.append(6)
         if gen == 7:
            layout.add_widget(self.card7)
            taken.append(7)
         if gen == 8:
            layout.add_widget(self.card8)
            taken.append(8)
         if gen == 9:
            layout.add_widget(self.card9)
            taken.append(9)
         if gen == 10:
            layout.add_widget(self.card10)
            taken.append(10)
         if gen == 11:
            layout.add_widget(self.card11)
            taken.append(11)
         if gen == 12:
            layout.add_widget(self.card12)
            taken.append(12)
         if gen == 13:
            layout.add_widget(self.card13)
            taken.append(13)
         if gen == 14:
            layout.add_widget(self.card14)
            taken.append(14)
         if gen == 15:
            layout.add_widget(self.card15)
            taken.append(15)
         if gen == 16:
            layout.add_widget(self.card16)
            taken.append(16)
      return layout
   def revealed1(self,instance,last_num):
      self.layoutext = 1
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
         last_num = 0
      if clicky == 1:
         last_num = 1
   def revealed2(self,instance,last_num):
      self.layoutext = 2
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
      if clicky == 1:
         last_num = 2
   def revealed3(self,instance,last_num):
      self.layoutext = 3
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
      if clicky == 1:
         last_num = 3
   def revealed4(self,instance,left):
      self.layoutext = 4
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
      if clicky == 1:
         last_num = 4
   def revealed5(self,instance,left):
      self.layoutext = 5
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
      if clicky == 1:
         last_num = 5
   def revealed6(self,instance,left):
      self.layoutext = 6
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
      if clicky == 1:
         last_num = 6
   def revealed7(self,instance,left):
      self.layoutext = 7
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
      if clicky == 1:
         last_num = 7
   def revealed8(self,instance,left):
      self.layoutext = 8
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
      if clicky == 1:
         last_num = 8
if __name__ == "__main__":
    myApp = application()
    myApp.run()