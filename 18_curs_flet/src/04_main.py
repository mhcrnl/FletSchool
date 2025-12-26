import flet as ft

def main(page: ft.Page):
    page.title = "Aplicație cu Meniu"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # 1. Funcția pentru schimbarea paginilor sau acțiuni
    def menu_item_clicked(e):
        index = e.control.selected_index
        if index == 0:
            content_text.value = "Ești pe pagina Acasă"
        elif index == 1:
            content_text.value = "Ești pe pagina Setări"
        elif index == 2:
            show_help_dialog()
        
        # Închidem meniul automat după selecție
        page.drawer.open = False
        page.update()

    # 2. Funcția pentru dialogul de Help
    def show_help_dialog():
        dialog = ft.AlertDialog(
            title=ft.Text("Ajutor"),
            content=ft.Text("Aceasta este o aplicație demonstrativă Flet.\nFolosește meniul pentru navigare."),
            actions=[
                ft.TextButton("Închide", on_click=lambda e: close_dialog(dialog))
            ],
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    def close_dialog(dialog):
        dialog.open = False
        page.update()

    # 3. Definirea Meniului Lateral (Navigation Drawer)
    page.drawer = ft.NavigationDrawer(
        on_change=menu_item_clicked,
        controls=[
            ft.Container(height=12), # Spațiu sus
            ft.NavigationDrawerDestination(
                label="Acasă",
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
            ),
            ft.Divider(thickness=1), # Linie de separare
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.Icons.SETTINGS_OUTLINED),
                label="Setări",
                selected_icon=ft.Icons.SETTINGS,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.HELP_OUTLINE,
                label="Help",
                selected_icon=ft.Icons.HELP,
            ),
        ],
    )

    # 4. UI Principal
    content_text = ft.Text("Apasă pe butonul de meniu", size=20)
    
    page.appbar = ft.AppBar(
        leading=ft.IconButton(ft.Icons.MENU, on_click=lambda _: page.show_drawer()),
        title=ft.Text("Meniu Flet"),
        bgcolor=ft.Colors.SURFACE_VARIANT,
    )

    page.add(
        ft.Center(
            content=content_text
        )
    )

ft.run(main)
