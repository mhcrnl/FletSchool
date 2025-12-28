# 20FletGeminiTodo app

![imagine](/home/mhcrnl/Desktop/Decembrie_2025/FletSchool/20_flet_gemini_todo/img/img.png)

Îmi cer scuze, ai perfectă dreptate! Aceasta este o eroare comună: în versiunile recente de Flet, atributul corect este **`page.client_storage`**, dar uneori apar confuzii dacă mediul de execuție nu este inițializat corect sau dacă se folosește o sintaxă ușor diferită în funcție de versiune.

Totuși, dacă primești eroarea că atributul nu există, este posibil să fie o problemă de context. O alternativă mult mai robustă și vizibilă pentru stocarea datelor (și care funcționează garantat) este utilizarea **`page.session`** pentru durata sesiunii sau, pentru salvare permanentă, scrierea într-un fișier **JSON local**.

Iată versiunea corectată care folosește un fișier JSON pentru a stoca datele, astfel încât să eviți orice eroare de tip "attribute error":

### Codul Corectat (cu salvare în fișier JSON)

```python
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
                    ft.icons.DELETE_OUTLINE, 
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
            ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked)
        ]),
        tasks_view
    )

    load_tasks()

ft.app(target=main)
```

---

### De ce această metodă este mai sigură?

1. **Independență**: Nu depinde de setările browserului sau ale sistemului de stocare intern al Flet care uneori poate fi restrictiv pe anumite sisteme de operare.
2. **Transparență**: Vei vedea un fișier `todo_data.json` apărând în același folder cu scriptul tău. Poți chiar să îl deschizi și să editezi manual sarcinile dacă dorești.
3. **Portabilitate**: Dacă muți folderul aplicației, iei și datele cu tine.

### Cum să verifici versiunea de Flet

Dacă totuși vrei să folosești `client_storage`, asigură-te că ai ultima versiune rulând:

```bash
pip install flet --upgrade
```

Dorești să adăugăm și o funcție de **editare** a sarcinilor deja create (dacă ai scris ceva greșit)?

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