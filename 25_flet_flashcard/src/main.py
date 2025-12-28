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


ft.run(main)
