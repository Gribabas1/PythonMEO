from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class TopApp(App):
    def build(self):
        self.info = Label(text='1', font_size=80)
        grid = GridLayout(cols=1)
        btn = Button(text='Плюс 1', font_size=50, background_color='cyan', on_press=self.plus)
        grid.add_widget(self.info)
        grid.add_widget(btn)
        return grid

    def plus(self, instance):
        self.info.text = str(int(self.info.text)+1)

if __name__ == "__main__":
    TopApp().run()