import flet as ft

def main(page: ft.Page):
    # Setările paginii
    page.title = "Aplicație To-Do"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # Funcția de adăugare task
    def add_clicked(e):
        if not new_task.value:
            new_task.error_text = "Te rog scrie un task"
            page.update()
        else:
            new_task.error_text = None
            # Creăm un rând nou pentru task cu un buton de ștergere
            task_view = ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Checkbox(label=new_task.value),
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        icon_color="red",
                        on_click=lambda _: delete_task(task_view)
                    )
                ]
            )
            tasks_list.controls.append(task_view)
            new_task.value = ""
            new_task.focus()
            page.update()

    # Funcția de ștergere task
    def delete_task(task):
        tasks_list.controls.remove(task)
        page.update()

    # Elemente UI
    new_task = ft.TextField(hint_text="Ce ai de făcut?", expand=True, on_submit=add_clicked)
    tasks_list = ft.Column()

    # Layout-ul aplicației
    page.add(
        ft.Column(
            width=400,
            controls=[
                ft.Row(
                    controls=[
                        new_task,
                        ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked),
                    ],
                ),
                tasks_list,
            ],
        )
    )

# Rularea aplicației
ft.run(main)
