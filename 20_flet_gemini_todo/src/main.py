import flet as ft
import json
import os

# Numele fișierului unde salvăm datele
DATA_FILE = "todo_data.json"

def main(page: ft.Page):
    page.title = "To-Do List Persistent"
    page.window_width = 400
    page.window_height = 600
    
    tasks_view = ft.Column()

    def save_tasks(e=None):
        # Colectăm datele din UI
        data = []
        for row in tasks_view.controls:
            checkbox = row.controls[0]
            data.append({"label": checkbox.label, "value": checkbox.value})
        
        # Salvăm în fișier
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
        page.update()

    def delete_task(task_row):
        tasks_view.controls.remove(task_row)
        save_tasks()
        page.update()

    def add_task_to_ui(label, checked=False):
        task_row = ft.Row(
            controls=[
                ft.Checkbox(
                    label=label, 
                    value=checked, 
                    expand=True, 
                    on_change=save_tasks # Salvează când bifezi
                ),
                ft.IconButton(
                    ft.Icons.DELETE_OUTLINE, 
                    icon_color="red", 
                    on_click=lambda _: delete_task(task_row)
                )
            ]
        )
        tasks_view.controls.append(task_row)

    def add_clicked(e):
        if not new_task.value: return
        add_task_to_ui(new_task.value)
        new_task.value = ""
        save_tasks()
        new_task.focus()
        page.update()

    # Încărcăm datele din fișier la pornire
    def load_tasks():
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                try:
                    saved_data = json.load(f)
                    for task in saved_data:
                        add_task_to_ui(task["label"], task["value"])
                except:
                    pass
        page.update()

    new_task = ft.TextField(
        hint_text="Ce planuri ai?", 
        expand=True, 
        on_submit=add_clicked
    )

    page.add(
        ft.Text("Lista mea", size=30, weight="bold"),
        ft.Row([
            new_task, 
            ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=add_clicked)
        ]),
        tasks_view
    )

    load_tasks()

ft.run(main)
