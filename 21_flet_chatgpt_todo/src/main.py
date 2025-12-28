import flet as ft

def main(page: ft.Page):
    page.title = "To-Do App 2025"
    page.bgcolor = ft.Colors.GREY_100
    page.padding = 20
    page.window.width = 460
    page.window.height = 680
    page.theme_mode = ft.ThemeMode.LIGHT

    tasks = []
    tasks_container = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, expand=True)

    total = ft.Text("0", weight=ft.FontWeight.BOLD)
    done = ft.Text("0", weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)

    def update_stats():
        total.value = str(len(tasks))
        done.value = str(sum(1 for t in tasks if t.completed))
        page.update()

    def add_task(e):
        text = new_task.value.strip()
        if not text:
            return
        task = Task(
            text=text,
            delete_callback=lambda t: (tasks.remove(t), tasks_container.controls.remove(t), update_stats()),
            on_change=update_stats
        )
        tasks.append(task)
        tasks_container.controls.append(task)
        new_task.value = ""
        update_stats()
        page.update()

    new_task = ft.TextField(
        hint_text="Ce trebuie făcut azi?",
        autofocus=True,
        on_submit=add_task,
        expand=True
    )

    page.add(
        ft.Container(
            width=500,
            padding=30,
            content=ft.Column([
                ft.Text("TO-DO APP", size=32, weight="bold", text_align=ft.TextAlign.CENTER),
                ft.Row([ft.Text("Total:"), total, ft.Text("  |  Terminate:"), done], alignment="center"),
                ft.Row([new_task, ft.ElevatedButton("Adaugă", on_click=add_task)]),
                ft.Container(height=20),
                tasks_container
            ], spacing=16, expand=True),
            bgcolor=ft.Colors.WHITE,
            border_radius=16,
            shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.BLUE_GREY_200)
        )
    )

if __name__ == "__main__":
    ft.run(main)
