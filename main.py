import flet as ft
import time
def main(page: ft.Page):
    page.title = "First App!"
    page.theme_mode = ft.ThemeMode.DARK
    text_hello = ft.Text(value="Hello, World!")
    text_hello.value = 'Привет, Geeks'
    # text_button = ft.TextButton('send', icon=ft.Icons.SEND)
    def on_click_func(_):
        print(name_input.value)
        name_input.label = 'Успешно'
        name_input.value = f'{time.ctime()}: Привет, {name_input.value}!'
    
        # pass

    name_input = ft.TextField(label='Введите имя')
    elevted_button = ft.ElevatedButton('send', icon=ft.Icons.SEND, color=ft.Colors.YELLOW, icon_color=ft.Colors.GREEN, on_click=on_click_func)
   
    # icon_button = ft.IconButton(icon=ft.Icons.SEND, icon_color=ft.Colors.RED_500)
    page.add(text_hello, elevted_button, name_input)

# ft.app(main)
ft.app(main, view=ft.AppView.WEB_BROWSER)