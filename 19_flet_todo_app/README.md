# 19FletTodoApp app

Salut! Flet este o alegere excelentă pentru a construi aplicații rapid, deoarece îți permite să creezi interfețe grafice (GUI) folosind doar Python, fără să ai nevoie de HTML/CSS/JS.

Iată un exemplu complet pentru o aplicație **To-Do** modernă, care include adăugarea sarcinilor, bifarea lor și ștergerea acestora.

### Codul aplicației To-Do

```python
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
                ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked),
            ],
        ),
        tasks_view,
    )

ft.app(target=main)

```

---

### Cum funcționează?

1. **`ft.TextField`**: Este zona unde scrii sarcina. Am adăugat `on_submit`, deci poți apăsa direct *Enter* pentru a adăuga task-ul.
2. **`ft.Column` (tasks_view)**: Acesta este containerul care va ține lista de sarcini. De fiecare dată când adăugăm ceva, facem `.append()` în această listă.
3. **Stateless Update**: Flet funcționează prin actualizarea paginii. De aceea, după fiecare modificare (adăugare sau ștergere), apelăm `page.update()`.
4. **Lambda**: În butonul de ștergere, folosim `lambda _: delete_task(task_row)` pentru a trimite exact rândul respectiv către funcția de ștergere.

### Cum rulezi aplicația?

1. Instalează flet: `pip install flet`
2. Salvează codul într-un fișier (ex: `todo.py`).
3. Rulează-l: `python todo.py`

**Ți-ar plăcea să adăugăm și o funcție de salvare locală a datelor (într-o bază de date simplă sau JSON), astfel încât sarcinile să nu dispară la închiderea aplicației?**

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