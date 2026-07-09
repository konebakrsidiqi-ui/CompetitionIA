from kivy.app import App
from kivy.uix.label import Label

class MonApp(App):
    def build(self):
        return Label(text="Bonjour !\nCompétition ChatGPT vs Gemini")

MonApp().run()
