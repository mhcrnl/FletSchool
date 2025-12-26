import flet as ft

def main(page: ft.Page):
	page.add(
                ft.Column([
                        ft.Text("Titlu Sus"),
                        ft.Row([
                                ft.ElevatedButton("Stanga"),
                                ft.ElevatedButton("Dreapta"),
                                ])
                        ])
                )

ft.run(main)



