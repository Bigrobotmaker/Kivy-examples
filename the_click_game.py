import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty

class clickyclack(Button):
    def toggle(self):
        global time
        if time == 0: return
        if self.parent.count%2 == 0:
            self.parent.count += 1
        else:
            self.parent.count = 0
class clackyclick(Button):
    def toggle(self):
        global time
        if time == 0: return
        if self.parent.count%2 != 0:
            self.parent.count += 1
        else:
            self.parent.count = 0
class numbox(BoxLayout):
    count = NumericProperty()
    time = NumericProperty(20)

    def __init__(self):
        super().__init__()
        Clock.schedule_interval(self.second_pass, 1)
    def second_pass(self, dt):
        global time
        if self.time > 0:
            self.time -= 1
    
    Clock.schedule_interval(second_pass, 1)
class clickinatorapp(App):

    def build(self):
        global time
        time = 20
        return numbox()
if __name__ == '__main__':
    clickinatorapp().run()
