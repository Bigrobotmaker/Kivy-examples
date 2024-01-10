import random
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock
#try: separate reveal and hide to make delay work
clicky = 0
last_num = 0
completed = 0
class application(App):
   def build(self):
      taken = []
      gen = 0
      layout = GridLayout(cols=4)
      self.card1 = Button(text = 'click here!',on_press = self.revealed1)
      self.card2 = Button(text = 'click here!',on_press = self.revealed1)
      self.card3 = Button(text = 'click here!',on_press = self.revealed2)
      self.card4 = Button(text = 'click here!',on_press = self.revealed2)
      self.card5 = Button(text = 'click here!',on_press = self.revealed3)
      self.card6 = Button(text = 'click here!',on_press = self.revealed3)
      self.card7 = Button(text = 'click here!',on_press = self.revealed4)
      self.card8 = Button(text = 'click here!',on_press = self.revealed4)
      self.card9 = Button(text = 'click here!',on_press = self.revealed5)
      self.card10 = Button(text = 'click here!',on_press = self.revealed5)
      self.card11 = Button(text = 'click here!',on_press = self.revealed6)
      self.card12 = Button(text = 'click here!',on_press = self.revealed6)
      self.card13 = Button(text = 'click here!',on_press = self.revealed7)
      self.card14 = Button(text = 'click here!',on_press = self.revealed7)
      self.card15 = Button(text = 'click here!',on_press = self.revealed8)
      self.card16 = Button(text = 'click here!',on_press = self.revealed8)
      for i in range(16):
         while (gen in taken or gen == 0) and len(taken) < 16:
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
   def revealed1(self,instance):
      global clicky
      global last_num
      global completed
      if completed == 8: return
      self.layoutext = 1
      instance.text = str(self.layoutext)
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         instance.text = str(self.layoutext)
         if last_num == 2:
            self.layoutext = "click here!"
            self.card3.text = str(self.layoutext)
            self.card4.text = str(self.layoutext)
         if last_num == 3:
            self.layoutext = "click here!"
            self.card5.text = str(self.layoutext)
            self.card6.text = str(self.layoutext)
         if last_num == 4:
            self.layoutext = "click here!"
            self.card7.text = str(self.layoutext)
            self.card8.text = str(self.layoutext)
         if last_num == 5:
            self.layoutext = "click here!"
            self.card9.text = str(self.layoutext)
            self.card10.text = str(self.layoutext)
         if last_num == 6:
            self.layoutext = "click here!"
            self.card11.text = str(self.layoutext)
            self.card12.text = str(self.layoutext)
         if last_num == 7:
            self.layoutext = "click here!"
            self.card13.text = str(self.layoutext)
            self.card14.text = str(self.layoutext)
         if last_num == 8:
            self.layoutext = "click here!"
            self.card15.text = str(self.layoutext)
            self.card16.text = str(self.layoutext)
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
         completed += 1
         if completed == 8:
            print('you win!')
      if clicky == 1:
         last_num = 1
   def revealed2(self,instance):
      global clicky
      global last_num
      global completed
      if completed == 8: return
      self.layoutext = 2
      instance.text = str(self.layoutext)
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         instance.text = str(self.layoutext)
         clicky = 0
         
         if last_num == 1:
            self.layoutext = "click here!"
            self.card1.text = str(self.layoutext)
            self.card2.text = str(self.layoutext)
         if last_num == 3:
            self.layoutext = "click here!"
            self.card5.text = str(self.layoutext)
            self.card6.text = str(self.layoutext)
         if last_num == 4:
            self.layoutext = "click here!"
            self.card7.text = str(self.layoutext)
            self.card8.text = str(self.layoutext)
         if last_num == 5:
            self.layoutext = "click here!"
            self.card9.text = str(self.layoutext)
            self.card10.text = str(self.layoutext)
         if last_num == 6:
            self.layoutext = "click here!"
            self.card11.text = str(self.layoutext)
            self.card12.text = str(self.layoutext)
         if last_num == 7:
            self.layoutext = "click here!"
            self.card13.text = str(self.layoutext)
            self.card14.text = str(self.layoutext)
         if last_num == 8:
            self.layoutext = "click here!"
            self.card15.text = str(self.layoutext)
            self.card16.text = str(self.layoutext)
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
         completed += 1
         if completed == 8:
            print('you win!')
      if clicky == 1:
         last_num = 2
   def revealed3(self,instance):
      global clicky
      global last_num
      global completed
      if completed == 8: return
      self.layoutext = 3
      instance.text = str(self.layoutext)
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         instance.text = str(self.layoutext)
         if last_num == 1:
            self.layoutext = "click here!"
            self.card1.text = str(self.layoutext)
            self.card2.text = str(self.layoutext)
         if last_num == 2:
            self.layoutext = "click here!"
            self.card3.text = str(self.layoutext)
            self.card4.text = str(self.layoutext)
         if last_num == 4:
            self.layoutext = "click here!"
            self.card7.text = str(self.layoutext)
            self.card8.text = str(self.layoutext)
         if last_num == 5:
            self.layoutext = "click here!"
            self.card9.text = str(self.layoutext)
            self.card10.text = str(self.layoutext)
         if last_num == 6:
            self.layoutext = "click here!"
            self.card11.text = str(self.layoutext)
            self.card12.text = str(self.layoutext)
         if last_num == 7:
            self.layoutext = "click here!"
            self.card13.text = str(self.layoutext)
            self.card14.text = str(self.layoutext)
         if last_num == 8:
            self.layoutext = "click here!"
            self.card15.text = str(self.layoutext)
            self.card16.text = str(self.layoutext)
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
         completed += 1
         if completed == 8:
            print('you win!')
      if clicky == 1:
         last_num = 3
   def revealed4(self,instance):
      global clicky
      global last_num
      global completed
      if completed == 8: return
      self.layoutext = 4
      instance.text = str(self.layoutext)
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         instance.text = str(self.layoutext)
         if last_num == 1:
            self.layoutext = "click here!"
            self.card1.text = str(self.layoutext)
            self.card2.text = str(self.layoutext)
         if last_num == 3:
            self.layoutext = "click here!"
            self.card5.text = str(self.layoutext)
            self.card6.text = str(self.layoutext)
         if last_num == 2:
            self.layoutext = "click here!"
            self.card3.text = str(self.layoutext)
            self.card4.text = str(self.layoutext)
         if last_num == 5:
            self.layoutext = "click here!"
            self.card9.text = str(self.layoutext)
            self.card10.text = str(self.layoutext)
         if last_num == 6:
            self.layoutext = "click here!"
            self.card11.text = str(self.layoutext)
            self.card12.text = str(self.layoutext)
         if last_num == 7:
            self.layoutext = "click here!"
            self.card13.text = str(self.layoutext)
            self.card14.text = str(self.layoutext)
         if last_num == 8:
            self.layoutext = "click here!"
            self.card15.text = str(self.layoutext)
            self.card16.text = str(self.layoutext)
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
         completed += 1
         if completed == 8:
            print('you win!')
      if clicky == 1:
         last_num = 4
   def revealed5(self,instance):
      global clicky
      global last_num
      global completed
      if completed == 8: return
      self.layoutext = 5
      instance.text = str(self.layoutext)
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         instance.text = str(self.layoutext)
         if last_num == 1:
            self.layoutext = "click here!"
            self.card1.text = str(self.layoutext)
            self.card2.text = str(self.layoutext)
         if last_num == 3:
            self.layoutext = "click here!"
            self.card5.text = str(self.layoutext)
            self.card6.text = str(self.layoutext)
         if last_num == 4:
            self.layoutext = "click here!"
            self.card7.text = str(self.layoutext)
            self.card8.text = str(self.layoutext)
         if last_num == 2:
            self.layoutext = "click here!"
            self.card3.text = str(self.layoutext)
            self.card4.text = str(self.layoutext)
         if last_num == 6:
            self.layoutext = "click here!"
            self.card11.text = str(self.layoutext)
            self.card12.text = str(self.layoutext)
         if last_num == 7:
            self.layoutext = "click here!"
            self.card13.text = str(self.layoutext)
            self.card14.text = str(self.layoutext)
         if last_num == 8:
            self.layoutext = "click here!"
            self.card15.text = str(self.layoutext)
            self.card16.text = str(self.layoutext)
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
         completed += 1
         if completed == 8:
            print('you win!')
      if clicky == 1:
         last_num = 5
   def revealed6(self,instance):
      global clicky
      global last_num
      global completed
      if completed == 8: return
      self.layoutext = 6
      instance.text = str(self.layoutext)
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         instance.text = str(self.layoutext)
         if last_num == 1:
            self.layoutext = "click here!"
            self.card1.text = str(self.layoutext)
            self.card2.text = str(self.layoutext)
         if last_num == 3:
            self.layoutext = "click here!"
            self.card5.text = str(self.layoutext)
            self.card6.text = str(self.layoutext)
         if last_num == 4:
            self.layoutext = "click here!"
            self.card7.text = str(self.layoutext)
            self.card8.text = str(self.layoutext)
         if last_num == 5:
            self.layoutext = "click here!"
            self.card9.text = str(self.layoutext)
            self.card10.text = str(self.layoutext)
         if last_num == 2:
            self.layoutext = "click here!"
            self.card3.text = str(self.layoutext)
            self.card4.text = str(self.layoutext)
         if last_num == 7:
            self.layoutext = "click here!"
            self.card13.text = str(self.layoutext)
            self.card14.text = str(self.layoutext)
         if last_num == 8:
            self.layoutext = "click here!"
            self.card15.text = str(self.layoutext)
            self.card16.text = str(self.layoutext)
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
         completed += 1
         if completed == 8:
            print('you win!')
      if clicky == 1:
         last_num = 6
   def revealed7(self,instance):
      global clicky
      global last_num
      global completed
      if completed == 8: return
      self.layoutext = 7
      instance.text = str(self.layoutext)
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         instance.text = str(self.layoutext)
         if last_num == 1:

            self.layoutext = "click here!"
            self.card1.text = str(self.layoutext)
            self.card2.text = str(self.layoutext)
         if last_num == 3:
            self.layoutext = "click here!"
            self.card5.text = str(self.layoutext)
            self.card6.text = str(self.layoutext)
         if last_num == 4:
            self.layoutext = "click here!"
            self.card7.text = str(self.layoutext)
            self.card8.text = str(self.layoutext)
         if last_num == 5:
            self.layoutext = "click here!"
            self.card9.text = str(self.layoutext)
            self.card10.text = str(self.layoutext)
         if last_num == 6:
            self.layoutext = "click here!"
            self.card11.text = str(self.layoutext)
            self.card12.text = str(self.layoutext)
         if last_num == 2:
            self.layoutext = "click here!"
            self.card3.text = str(self.layoutext)
            self.card4.text = str(self.layoutext)
         if last_num == 8:
            self.layoutext = "click here!"
            self.card15.text = str(self.layoutext)
            self.card16.text = str(self.layoutext)
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
         completed += 1
         if completed == 8:
            print('you win!')
      if clicky == 1:
         last_num = 7
   def revealed8(self,instance):
      global clicky
      global last_num
      global completed
      if completed == 8: return
      self.layoutext = 8
      instance.text = str(self.layoutext)
      clicky += 1
      if clicky == 2 and self.layoutext != last_num:
         self.layoutext = "click here!"
         instance.text = str(self.layoutext)
         if last_num == 1:
            self.layoutext = "click here!"
            self.card1.text = str(self.layoutext)
            self.card2.text = str(self.layoutext)
         if last_num == 3:
            self.layoutext = "click here!"
            self.card5.text = str(self.layoutext)
            self.card6.text = str(self.layoutext)
         if last_num == 4:
            self.layoutext = "click here!"
            self.card7.text = str(self.layoutext)
            self.card8.text = str(self.layoutext)
         if last_num == 5:
            self.layoutext = "click here!"
            self.card9.text = str(self.layoutext)
            self.card10.text = str(self.layoutext)
         if last_num == 6:
            self.layoutext = "click here!"
            self.card11.text = str(self.layoutext)
            self.card12.text = str(self.layoutext)
         if last_num == 7:
            self.layoutext = "click here!"
            self.card13.text = str(self.layoutext)
            self.card14.text = str(self.layoutext)
         if last_num == 2:
            self.layoutext = "click here!"
            self.card3.text = str(self.layoutext)
            self.card4.text = str(self.layoutext)
         clicky = 0
         last_num = 0
      if clicky == 2 and last_num == self.layoutext:
         clicky = 0
         last_num = 0
         completed += 1
         if completed == 8:
            print('you win!')
      if clicky == 1:
         last_num = 8
if __name__ == "__main__":
    myApp = application()
    myApp.run()