import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.properties import NumericProperty

class clickyclack(Button):
    def toggle(root):
        if root.count%2 == 0:
            root.count += 1
        else:
            root.count == 0
class clackyclick(Button):
    def toggle(root):
        if root.count%2 != 0:
            root.count += 1
        else:
            root.count == 0
class numbox(BoxLayout):
    score = NumericProperty()
    count = NumericProperty()
class clickinatorapp(App):

    def build(self):
        return numbox()
if __name__ == '__main__':
    clickinatorapp().run()
