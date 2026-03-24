import flet as ft
import time
def main(page: ft.Page):
    page.title = "First App!"
    page.theme_mode = ft.ThemeMode.DARK
    text_hello = ft.Text(value="Hello, World!")
    
    history = []
    history_column = ft.Column()
  
    def on_click_func(_):
        if name_input.value:
            greeting = f'Hello {name_input.value}'

            history.append(greeting)  # добавили в историю
            history_column.controls.append(ft.Text(greeting))  # добавили в UI

            text_hello.value = greeting
            text_hello.color = None
        else:
            text_hello.color = ft.Colors.RED
            text_hello.value = 'Введите корректное имя!'

        page.update()

    def delete_last(_):
        if history:
            history.pop()
            history_column.controls.pop()
        else:
            text_hello.value = "История пуста!"
            text_hello.color = ft.Colors.RED
        page.update()

    name_input = ft.TextField(
        label='Введите имя',
        expand=True,
        on_submit=on_click_func
    )
    elevated_button = ft.ElevatedButton(
        'Send',
        icon=ft.Icons.SEND,
        on_click=on_click_func
    )
    delete_button = ft.ElevatedButton(
        "Удалить последнее",
        icon=ft.Icons.DELETE,
        on_click=delete_last,
    )
    def edit_theme(_):
        page.theme_mode = (
            ft.ThemeMode.LIGHT
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        # if page.theme_mode == ft.ThemeMode.DARK:
        #     page.theme_mode = ft.ThemeMode.LIGHT
        # else:
        #     page.theme_mode = ft.ThemeMode.DARK
        page.update()
    
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=edit_theme)
    main_objects = ft.Row([name_input, elevated_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    # icon_button = ft.IconButton(icon=ft.Icons.SEND, icon_color=ft.Colors.RED_500)
    page.add(text_hello, main_objects, delete_button, history_column)

# ft.app(main)
ft.app(main, view=ft.AppView.WEB_BROWSER)