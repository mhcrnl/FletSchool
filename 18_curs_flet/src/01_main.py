import flet as ft
import os

def main(page: ft.Page):

    page.title = "MY super App"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 400
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def close_app(e):
        #page.window_close()
        os._exit(0)

        
    page.add(
        
        ft.Text("Hello, Flet!", color="green"),
        ft.Button("Exit", on_click=close_app, color="red"),
        ft.Button("Buton_1", bgcolor="green",
                  url="https://docs.flet.dev/controls/button/#flet.Button",
                  on_hover="Open the Flet Site"),
        ft.Button(content="cerc",
                style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=40)),
        ft.Checkbox(),

        ft.CupertinoSlider(value=0.6),

        ft.CupertinoTimerPicker(value=1000),

        ft.FilledButton(content="Tap me"),

        ft.FilledIconButton(icon=ft.Icons.CHECK),

        ft.MenuBar(
            controls=[
                ft.SubmenuButton(
                    content=ft.Text("Submenu"),
                    controls=[
                        ft.MenuItemButton(content=ft.Text("Item 1")),
                        ft.MenuItemButton(content=ft.Text("Item 2")),
                        ft.MenuItemButton(content=ft.Text("Item 3")),
            ],
        ),
    ],
)
        
        )

    

ft.run(main)
