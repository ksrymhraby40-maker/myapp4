from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # ساخت یک چیدمان عمودی
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # ساخت یک متن
        self.label = Label(text="سلام! این اولین اپ من است.", font_size='20sp')
        
        # ساخت یک دکمه
        btn = Button(text="من را کلیک کن!", font_size='20sp', size_hint=(1, 0.5))
        
        # اتصال دکمه به یک تابع
        btn.bind(on_press=self.on_button_click)
        
        # اضافه کردن متن و دکمه به صفحه
        layout.add_widget(self.label)
        layout.add_widget(btn)
        
        return layout

    def on_button_click(self, instance):
        self.label.text = "دکمه کلیک شد! عالیه."

if __name__ == '__main__':
    MyApp().run()