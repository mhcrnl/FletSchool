import flet as ft

def main(page: ft.Page):
    page.title = "PassGen Pro"
    page.theme_mode = ft.ThemeMode.LIGHT
    
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
        page.dialog = about_dialog
        about_dialog.open = True
        page.update()

    # 3. Integrarea în AppBar
    page.appbar = ft.AppBar(
        title=ft.Text("Password Generator"),
        bgcolor=ft.Colors.SURFACE,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        "Despre", 
                        icon=ft.Icons.INFO_OUTLINE, 
                        on_click=lambda e: open(about_dialog)  # Aici legăm funcția de deschidere
                    ),
                    ft.PopupMenuItem("Setări", icon=ft.Icons.SETTINGS),
                ]
            ),
        ],
    )

    page.add(ft.Text("Conținutul principal al aplicației..."))
    page.add(ft.ElevatedButton("Open dialog", on_click=lambda e: page.open(about_dialog))),

ft.run(main)
