# 16FletTodo app

Aceasta este o versiune avansată a aplicației tale. Am adăugat un sistem de filtrare (Toate / Active / Finalizate) și posibilitatea de a edita un task existent direct în listă.

Iată codul actualizat:

```python
import flet as ft

class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="Ce ai de făcut?", expand=True, on_submit=self.add_clicked)
        self.tasks = ft.Column()

        # Filtrele de stare
        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="Toate"), ft.Tab(text="Active"), ft.Tab(text="Finalizate")],
        )

        self.width = 450
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                ],
            ),
            self.filter,
            self.tasks,
        ]

    def add_clicked(self, e):
        if self.new_task.value:
            task = Task(self.new_task.value, self.task_delete, self.update_filter)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def tabs_changed(self, e):
        self.update_filter()

    def update_filter(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == "Toate"
                or (status == "Active" and not task.display_task.value)
                or (status == "Finalizate" and task.display_task.value)
            )
        self.update()

class Task(ft.Column):
    def __init__(self, task_name, task_delete, task_status_change):
        super().__init__()
        self.task_name = task_name
        self.task_delete = task_delete
        self.task_status_change = task_status_change

        # Vederea principală (Check + Text + Edit/Delete)
        self.display_task = ft.Checkbox(value=False, label=self.task_name, on_change=self.status_changed, expand=True)
        self.edit_name = ft.TextField(expand=True)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(ft.icons.CREATE_OUTLINED, on_click=self.edit_clicked),
                        ft.IconButton(ft.icons.DELETE_OUTLINE, icon_color="red", on_click=self.delete_clicked),
                    ],
                ),
            ],
        )

        # Vederea pentru editare (ascunsă implicit)
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(icon=ft.icons.DONE_OUTLINE_OUTLINED, icon_color="green", on_click=self.save_clicked),
            ],
        )

        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.task_status_change()

    def delete_clicked(self, e):
        self.task_delete(self)

def main(page: ft.Page):
    page.title = "To-Do List Avansat"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    app = TodoApp()
    page.add(app)

ft.app(target=main)

```

---

### Ce am adăugat nou:

1. **Sistem de Clase**: Am separat aplicația în clase (`TodoApp` și `Task`) pentru a gestiona mai ușor logica fiecărui element.
2. **Funcția de Editare**:
* Fiecare task are acum două "fețe": `display_view` (cum arată în listă) și `edit_view` (un câmp de text care apare doar când apeși pe iconița de creion).
* Când salvezi, textul checkbox-ului se actualizează cu noua valoare.


3. **Filtrare (Tabs)**:
* Am adăugat un meniu de selecție (Toate, Active, Finalizate).
* Funcția `update_filter` parcurge toate task-urile și le ascunde sau le afișează în funcție de starea checkbox-ului lor.


4. **Interactivitate**: Filtrul se actualizează automat chiar și atunci când bifezi un task ca fiind gata în timp ce ești în tab-ul "Active".

Dorești să adăugăm și o bază de date locală (SQLite) pentru ca task-urile să nu se șteargă atunci când închizi aplicația?
## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://docs.flet.dev/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://docs.flet.dev/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://docs.flet.dev/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://docs.flet.dev/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://docs.flet.dev/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://docs.flet.dev/publish/windows/).