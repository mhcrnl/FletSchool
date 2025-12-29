'''
In this section, we will learn to create a simple Hello World program in Flet framework.
'''

# importing the library
import flet as ft
import sys

# defining main function
def main(page: ft.Page):

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
    
    def toggle_theme():
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    text = ft.Text(value="Hello, Anurag!", color="red")
    close_button = ft.ElevatedButton( "Închide aplicația", icon=ft.Icons.CLOSE, on_click=lambda e: page.window_close() )
    close_sys = ft.ElevatedButton("CloseSYS", icon=ft.Icons.EXIT_TO_APP, on_click=lambda e: page.window_destroy())
    close = ft.ElevatedButton("Close", on_click=lambda e: sys.exit())
    
    page.controls.append(text)
    page.add(close_button)
    page.add(close_sys)
    page.add(close)
    page.update()

# starting the app
# ft.app(target=main)
ft.run(main)

# for running it in web browser
'''
ft.app(target=main, view=ft.WEB_BROWSER)
'''

'''
Note: 

(i) When running Flet app in the browser a new user session is started for every opened tab or page.
(ii) When running as a desktop app there is only one session created.
'''
