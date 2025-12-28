import flet as ft
import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def main(page: ft.Page):
    page.title = "ToDo App - Flet"
    page.window_width = 400
    page.window_height = 600

    tasks = load_tasks()

    task_input = ft.TextField(
        hint_text="Adaugă un task...",
        expand=True
    )

    task_list = ft.Column(expand=True, scroll="auto")

    def refresh_list():
        task_list.controls.clear()
        for i, task in enumerate(tasks):
            task_list.controls.append(
                ft.Row(
                    [
                        ft.Checkbox(
                            value=task["done"],
                            label=task["title"],
                            on_change=lambda e, index=i: toggle_task(index),
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color="red",
                            on_click=lambda e, index=i: delete_task(index),
                        )
                    ]
                )
            )
        page.update()

    def add_task(e):
        title = task_input.value.strip()
        if title:
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
            task_input.value = ""
            refresh_list()

    def toggle_task(index):
        tasks[index]["done"] = not tasks[index]["done"]
        save_tasks(tasks)
        refresh_list()

    def delete_task(index):
        tasks.pop(index)
        save_tasks(tasks)
        refresh_list()

    add_button = ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color="blue",
        on_click=add_task
    )

    page.add(
        ft.Row([task_input, add_button]),
        task_list
    )

    refresh_list()


ft.run(main)
