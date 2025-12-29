import flet as ft
import random
import string



def main(page: ft.Page):
    page.title = "PassGen Pro"
    page.window_width = 400
    page.window_height = 500
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # --- CONFIGURARE APPBAR ---
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.Icons.LOCK_OUTLINED),
        leading_width=40,
        title=ft.Text("Password Generator"),
        center_title=False,
        bgcolor=ft.Colors.SURFACE,
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED, on_click=lambda _: toggle_theme()),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem("Despre", icon=ft.Icons.INFO_OUTLINE, on_click=lambda e: open_about),
                    ft.PopupMenuItem("Setări", icon=ft.Icons.SETTINGS),
                ]
            ),
        ],
    )

    # 1. Definirea ferestrei de dialog "Despre"
    about_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Despre PassGen Pro"),
        content=ft.Column([
            ft.Text("Versiune: 1.0.0"),
            ft.Text("Creat cu Flet & Python"),
            ft.Text("Această aplicație generează parole sigure folosind algoritmi criptografici."),
            ft.Divider(),
            ft.Text("Autor: [Numele Tău]", size=12, italic=True)
        ], tight=True),
        actions=[
            ft.TextButton("Închide", on_click=lambda e: page.close(about_dialog))
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # 2. Funcția pentru deschiderea dialogului
    def open_about(e):
        page.open(about_dialog)

    def toggle_theme():
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    # --- LOGICĂ APLICAȚIE ---
    text_field = ft.TextField(
        label="Parola generată", 
        read_only=True, 
        text_align=ft.TextAlign.CENTER,
        text_size=20,
        border_radius=10
    )
    
    slider_len = ft.Slider(min=8, max=32, divisions=24, label="Lungime: {value}", value=12)

    def generate(e):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(int(slider_len.value)))
        text_field.value = password
        page.update()

    def copy_to_clipboard(e):
        if text_field.value:
            page.set_clipboard(text_field.value)
            page.show_snack_bar(ft.SnackBar(ft.Text("Copiat în clipboard!")))

    # --- LAYOUT ---
    page.add(
        ft.Column(
            [
                ft.Text("Alege lungimea parolei:", weight=ft.FontWeight.BOLD),
                slider_len,
                ft.Divider(height=20),
                text_field,
                ft.Row(
                    [
                        ft.ElevatedButton("Generează", icon=ft.Icons.REFRESH, on_click=generate, expand=True),
                        ft.IconButton(ft.Icons.COPY, on_click=copy_to_clipboard(text_field), tooltip="Copiază")
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.run(main)
