# 26FletFlashcardV1 app

Perfect, Mihai — hai să ducem Flashcard App-ul la nivelul următor și să adăugăm un **mod Quiz cu scor**, complet funcțional, integrat în aplicație.

Îți ofer **codul complet**, actualizat, cu:

### ✔ Modul QUIZ:

- întrebări afișate una câte una
- răspuns introdus de utilizator
- verificare corect/greșit
- scor final
- buton „Începe quiz”
- quiz-ul folosește cardurile existente

### ✔ Totul integrat în aplicația Flashcard existentă

---

# 🧩 **COD COMPLET – Flashcard App + QUIZ MODE**

```python
import flet as ft
import json
import os
import random

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
    page.title = "Flashcard App cu Quiz"
    page.window_width = 900
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

    # Elemente QUIZ
    quiz_question = ft.Text("", size=22, weight="bold")
    quiz_answer_input = ft.TextField(label="Răspunsul tău")
    quiz_feedback = ft.Text("", size=18)
    quiz_score_text = ft.Text("", size=18, weight="bold")

    quiz_panel = ft.Column(
        [
            ft.Text("Mod Quiz", size=22, weight="bold"),
            quiz_question,
            quiz_answer_input,
            ft.ElevatedButton("Trimite răspuns", on_click=lambda e: check_answer()),
            quiz_feedback,
            quiz_score_text,
        ],
        visible=False,
        expand=True,
    )

    # Variabile QUIZ
    quiz_cards = []
    quiz_index = 0
    quiz_score = 0

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
    # QUIZ MODE
    # ---------------------------

    def start_quiz(e):
        nonlocal quiz_cards, quiz_index, quiz_score

        if not cards:
            quiz_feedback.value = "Nu există carduri pentru quiz."
            page.update()
            return

        quiz_cards = cards.copy()
        random.shuffle(quiz_cards)
        quiz_index = 0
        quiz_score = 0

        quiz_panel.visible = True
        show_question()
        page.update()

    def show_question():
        if quiz_index >= len(quiz_cards):
            quiz_question.value = "Quiz terminat!"
            quiz_feedback.value = ""
            quiz_score_text.value = f"Scor final: {quiz_score} / {len(quiz_cards)}"
            quiz_answer_input.visible = False
            page.update()
            return

        quiz_question.value = quiz_cards[quiz_index]["question"]
        quiz_answer_input.value = ""
        quiz_feedback.value = ""
        quiz_score_text.value = f"Scor: {quiz_score}"
        page.update()

    def check_answer():
        nonlocal quiz_index, quiz_score

        if quiz_index >= len(quiz_cards):
            return

        user_answer = quiz_answer_input.value.strip().lower()
        correct_answer = quiz_cards[quiz_index]["answer"].strip().lower()

        if user_answer == correct_answer:
            quiz_feedback.value = "✔ Corect!"
            quiz_score += 1
        else:
            quiz_feedback.value = f"✘ Greșit! Răspuns corect: {correct_answer}"

        quiz_index += 1
        show_question()

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
                            ft.Divider(),
                            ft.ElevatedButton("Începe Quiz", on_click=start_quiz),
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
                    ),
                    expand=True,
                    padding=20,
                ),
                ft.VerticalDivider(),
                ft.Container(
                    quiz_panel,
                    width=300,
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

# 🎉 **Ce ai acum în aplicație**

### 🧠 Modul QUIZ complet:

- întrebări randomizate
- input pentru răspuns
- verificare corect/greșit
- scor live
- scor final
- afișare progres

### 📝 Flashcard App complet:

- creare carduri
- listă carduri
- flip întrebare/răspuns
- salvare JSON

---

Dacă vrei, pot să adaug:

- **mod „multiple choice”**
- **timer pentru fiecare întrebare**
- **statistici de învățare (acuratețe, timp mediu)**
- **categorii de carduri**
- **dark mode**

Spune-mi ce vrei să construim mai departe.

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