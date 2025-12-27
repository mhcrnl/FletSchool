import flet as ft

def main(page: ft.Page):
    page.title = "Lista Mea To-Do"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 600

    # Funcție pentru ștergerea unei sarcini
    def delete_task(task_row):
        tasks_view.controls.remove(task_row)
        page.update()

    # Funcție pentru adăugarea unei sarcini noi
    def add_clicked(e):
        if not new_task.value:
            return
        
        # Creăm structura unei sarcini (Checkbox + Text + Buton Șterge)
        task_text = ft.Checkbox(label=new_task.value, expand=True)
        task_row = ft.Row(
            controls=[
                task_text,
                ft.IconButton(
                    icon=ft.icons.DELETE_OUTLINE,
                    icon_color="red",
                    on_click=lambda _: delete_task(task_row)
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        tasks_view.controls.append(task_row)
        new_task.value = "" # Resetăm câmpul de text
        new_task.focus()
        page.update()

    # Elemente interfață
    new_task = ft.TextField(hint_text="Ce ai de făcut azi?", expand=True, on_submit=add_clicked)
    tasks_view = ft.Column()

    # Layout-ul paginii
    page.add(
        ft.Text("To-Do List", size=30, weight=ft.FontWeight.BOLD),
        ft.Row(
            controls=[
                new_task,
                ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked),
            ],
        ),
        tasks_view,
    )

ft.run(main)
