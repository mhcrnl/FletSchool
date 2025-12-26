# 15FletTodo app

Salut! Flet este un framework excelent pentru a construi interfețe grafice rapid în Python, deoarece se bazează pe Flutter, dar nu necesită cunoștințe de Dart.

Iată un cod complet și simplu pentru o aplicație **To-Do** care permite adăugarea și ștergerea task-urilor:

```python
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
                alignment=ft.MainAxisAlignment.BETWEEN,
                controls=[
                    ft.Checkbox(label=new_task.value),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINE,
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
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked),
                    ],
                ),
                tasks_list,
            ],
        )
    )

# Rularea aplicației
ft.app(target=main)

```

---

### Cum funcționează codul:

1. **Structura Paginii**: Folosim `ft.Column` pentru a alinia elementele pe verticală și `ft.Row` pentru a pune câmpul de text lângă butonul de adăugare.
2. **Input (new_task)**: Este un `TextField` unde utilizatorul scrie numele task-ului. Am adăugat `on_submit`, deci poți apăsa și tasta **Enter** pentru a adăuga.
3. **Gestionarea Task-urilor**:
* Fiecare task este un `ft.Row` care conține un `Checkbox` (pentru a bifa când e gata) și un `IconButton` (pentru ștergere).
* Folosim o listă numită `tasks_list` (care este un `ft.Column`) pentru a stoca aceste rânduri.


4. **Ștergerea**: Funcția `delete_task` primește referința întregului rând și îl elimină din coloana principală, apoi face `page.update()` pentru a reflecta schimbarea.

### Cum rulezi aplicația?

1. Instalează flet dacă nu l-ai instalat deja: `pip install flet`.
2. Salvează codul într-un fișier (ex: `todo.py`).
3. Rulează-l cu comanda: `python todo.py`.

Ți-ar plăcea să adăugăm și o funcție de **editare** a task-urilor existente sau o opțiune de a filtra task-urile finalizate?

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