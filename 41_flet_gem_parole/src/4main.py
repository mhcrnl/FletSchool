import flet as ft

def main(page: ft.Page):
    page.title = "PassGen Pro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 500

    # --- 1. DEFINIREA DIALOGULUI ---
    # Creăm obiectul dialog, dar nu îl afișăm încă
    about_dialog = ft.AlertDialog(
        title=ft.Text("Despre Aplicație"),
        content=ft.Text("Creat cu Flet versiunea 2024.\nVersiune Pro 1.0"),
        actions=[
            ft.TextButton("Ok", on_click=lambda e: close_dlg(e))
        ],
    )

    # --- 2. FUNCȚIILE DE CONTROL ---
    def close_dlg(e):
        about_dialog.open = False  # Închidem dialogul
        page.update()

    def open_about(e):
        page.dialog = about_dialog # Îi spunem paginii ce dialog să folosească
        about_dialog.open = True    # Îl activăm
        page.update()               # Forțăm redesenarea interfeței

    # --- 3. CONFIGURARE APPBAR ---
    page.appbar = ft.AppBar(
        title=ft.Text("Password Generator"),
        bgcolor=ft.Colors.SURFACE,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        "Despre", 
                        icon=ft.Icons.INFO_OUTLINE, 
                        on_click=open_about # Legăm funcția aici
                    ),
                ]
            ),
        ],
    )

    # --- 4. CONȚINUT PAGINĂ ---
    page.add(
        ft.Column([
            ft.Text("Aplicația este gata!", size=20),
            ft.ElevatedButton("Deschide Despre", on_click=open_about) # Buton de rezervă
        ])
    )

ft.run(main)
