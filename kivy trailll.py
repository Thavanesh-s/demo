import kivy

kivy.require('2.0.0')  # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    # initialize indefinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGrid, self).__init__(**kwargs)
        # set cols
        self.cols = 2

        # name-add widget
        self.add_widget(Label(text="name:"))
        # add input
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        # food - add widget
        self.add_widget(Label(text="favourite food"))
        # add input
        self.food = TextInput(multiline=False)
        self.add_widget(self.food)

        # color - add widget
        self.add_widget(Label(text="color"))
        # add input
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        #create submit button
        self.submit = Button(text = "submit", font_size = 32)
        #bind
        self.submit.bind(on_press  = self.press)
        self.add_widget(self.submit)
    def press(self, instance):
        name = self.name.text
        pizza =self.food.text
        color =self.color.text

        #print(f"helli {name} you like {pizza}pizza and your favourite color in {color}!!")
        # print it to screen
        self.add_widget(Label(text = f"helli {name} you like {pizza} food, and your favourite color in {color}!!"))
        self.name.text = ""
        self.food.text = ""
        self.color.text = ""
class MyApp(App):

    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
