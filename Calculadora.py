from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_string("""
<Calculadora>:
    a: _a
    b: _b
    result: _result
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, 1
            id: _screen_manager
            Screen:
                name: 'screen1'
                GridLayout:
                    cols:1
                    TextInput:
                        id: _a
                        text: ''
                    TextInput:
                        id: _b
                        text: ''
                    Label:
                        id: _result
                    Button:
                        text: 'Sumar'
                        on_press: _result.text = str(int(_a.text) + int(_b.text))
                    Button:
                        text: 'Restar'
                        on_press: _result.text = str(int(_a.text) - int(_b.text))
                    Button:
                        text: 'Multiplicar'
                        on_press: root.product(*args)
                    Button:
                        text: 'Dividir'
                        on_press: root.division(*args)

""")

class Calculadora(FloatLayout):
       def product(self, instance):
                self.result.text = str(int(self.a.text) * int(self.b.text))

       def division(self, instance):
           self.result.text = str(int(self.a.text) / int(self.b.text))

class MiApp(App):
    def build(self):
        return Calculadora()

if __name__ == '__main__':
    MiApp().run()