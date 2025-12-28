# 25FletFlashcard app

Super, Mihai — hai să construim împreună un **Flashcard App** în Flet, unul care chiar arată bine și funcționează ca o aplicație reală. Îți dau o versiune completă, simplă, dar elegantă, pe care o poți extinde oricând cu funcții mai avansate.

Îl facem cu:

- creare carduri (întrebare + răspuns)
- listă de carduri
- modul de învățare (flip card)
- salvare locală în fișier JSON
- UI modern

Totul într-un singur fișier Python.

---

# 🧩 **FLASHCARD APP – Cod complet în Flet**

```python
import flet as ft
import json
import os

FILE_PATH = "flashcards.json"


def load_cards():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_cards(cards):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(cards, f, indent=4, ensure_ascii=False)


def main(page: ft.Page):
    page.title = "Flashcard App"
    page.window_width = 800
    page.window_height = 600

    cards = load_cards()
    selected_index = None

    # ---------------------------
    # UI COMPONENTE
    # ---------------------------

    question_field = ft.TextField(label="Întrebare", expand=True)
    answer_field = ft.TextField(label="Răspuns", expand=True)

    flashcard_display = ft.Container(
        content=ft.Text("Selectează un card sau creează unul nou", size=20),
        padding=20,
        border_radius=10,
        bgcolor="#eeeeee",
        expand=True,
    )

    card_list = ft.Column(scroll="auto", expand=True)

    # ---------------------------
    # FUNCȚII
    # ---------------------------

    def refresh_list():
        card_list.controls.clear()
        for i, card in enumerate(cards):
            card_list.controls.append(
                ft.ListTile(
                    title=ft.Text(card["question"]),
                    on_click=lambda e, index=i: select_card(index),
                )
            )
        page.update()

    def select_card(index):
        nonlocal selected_index
        selected_index = index
        q = cards[index]["question"]
        flashcard_display.content = ft.Text(q, size=22, weight="bold")
        page.update()

    def add_card(e):
        q = question_field.value.strip()
        a = answer_field.value.strip()
        if q and a:
            cards.append({"question": q, "answer": a})
            save_cards(cards)
            question_field.value = ""
            answer_field.value = ""
            refresh_list()
            page.update()

    def flip_card(e):
        if selected_index is None:
            return
        current = flashcard_display.content.value
        q = cards[selected_index]["question"]
        a = cards[selected_index]["answer"]

        if current == q:
            flashcard_display.content = ft.Text(a, size=22, italic=True)
        else:
            flashcard_display.content = ft.Text(q, size=22, weight="bold")

        page.update()

    # ---------------------------
    # LAYOUT
    # ---------------------------

    page.add(
        ft.Row(
            [
                ft.Container(
                    ft.Column(
                        [
                            ft.Text("Creează un card nou", size=18, weight="bold"),
                            question_field,
                            answer_field,
                            ft.ElevatedButton("Adaugă card", on_click=add_card),
                            ft.Divider(),
                            ft.Text("Lista cardurilor", size=18, weight="bold"),
                            card_list,
                        ],
                        expand=True,
                    ),
                    width=300,
                    padding=10,
                ),
                ft.VerticalDivider(),
                ft.Container(
                    ft.Column(
                        [
                            flashcard_display,
                            ft.ElevatedButton("Flip Card", on_click=flip_card),
                        ],
                        expand=True,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    expand=True,
                    padding=20,
                ),
            ],
            expand=True,
        )
    )

    refresh_list()


ft.app(target=main)
```

---

# 🎉 Ce poate aplicația

### ✔ Creezi carduri noi

Întrebare + răspuns → salvate automat în JSON.

### ✔ Listă de carduri

Poți selecta oricând un card din listă.

### ✔ Modul de învățare

Cardul se poate „flip-ui” între întrebare și răspuns.

### ✔ Salvare persistentă

La fiecare pornire, cardurile sunt încă acolo.

### ✔ UI modern și curat

Structurat pe două panouri: listă + card activ.

---

# Vrei să-l facem și mai tare?

Pot adăuga:

- mod „quiz” cu scor
- categorii de carduri
- export/import carduri
- animații la flip
- dark mode
- sincronizare cloud (Firebase)
- statistici de învățare

Spune-mi ce direcție vrei să urmăm și îl transformăm într-o aplicație premium.

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