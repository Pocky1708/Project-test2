from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

class TestingApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_file("main.kv")

class ABCWin(ScreenManager):
    pass

class Window_test(Screen):
    def wow(self):
        self.ids.text_show.text = self.ids.name.text
if __name__ == "__main__":
    TestingApp().run()