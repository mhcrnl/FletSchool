import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "Password Generator"
    page.window_width = 300
    page.bgcolor="CC0000"
    
    text_field = ft.TextField(label="Parola ta", read_only=True)
    
    def generate(e):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(12))
        text_field.value = password
        page.update()

    page.add(
        ft.Text("Password Generator", size=20, weight="bold"),
        text_field,
        ft.ElevatedButton("Generează", on_click=generate),
        ft.IconButton(ft.Icons.COPY, on_click=lambda _: page.set_clipboard(text_field.value))
    )

ft.run(main)
