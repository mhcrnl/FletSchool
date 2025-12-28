'''
In this section, we will learn to create a simple Hello World program in Flet framework.
'''

# importing the library
import flet as ft
import sys

# defining main function
def main(page: ft.Page):
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
