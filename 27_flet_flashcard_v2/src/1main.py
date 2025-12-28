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
    page.title = "Flashcard App cu Quiz și Timer"
    page.window_width = 1000
    page.window_height = 650

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

    # QUIZ UI
    quiz_question = ft.Text("", size=22, weight="bold")
    quiz_answer_input = ft.TextField(label="Răspunsul tău")
    quiz_feedback = ft.Text("", size=18)
    quiz_score_text = ft.Text("", size=18, weight="bold")
    quiz_timer_text = ft.Text("Timp rămas: 10 secunde", size=18, weight="bold")

    quiz_panel = ft.Column(
        [
            ft.Text("Mod Quiz", size=22, weight="bold"),
            quiz_question,
            quiz_timer_text,
            quiz_answer_input,
            ft.ElevatedButton("Trimite răspuns", on_click=lambda e: check_answer()),
            quiz_feedback,
            quiz_score_text,
        ],
        visible=False,
        expand=True,
    )

    # ---------------------------
    # VARIABILE QUIZ
    # ---------------------------

    quiz_cards = []
    quiz_index = 0
    quiz_score = 0
    quiz_time_left = 10
    quiz_timer_running = False

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
    # TIMER ASINCRON
    # ---------------------------

    async def quiz_tick():
        nonlocal quiz_time_left, quiz_timer_running, quiz_index, quiz_score

        while quiz_timer_running and quiz_time_left > 0:
            await page.sleep(1)
            quiz_time_left -= 1
            quiz_timer_text.value = f"Timp rămas: {quiz_time_left} secunde"
            page.update()

        # dacă timpul a expirat
        if quiz_timer_running and quiz_time_left <= 0:
            quiz_feedback.value = "⏳ Timpul a expirat!"
            quiz_timer_running = False
            quiz_index += 1
            show_question()
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
        nonlocal quiz_time_left, quiz_timer_running

        if quiz_index >= len(quiz_cards):
            quiz_question.value = "Quiz terminat!"
            quiz_feedback.value = ""
            quiz_score_text.value = f"Scor final: {quiz_score} / {len(quiz_cards)}"
            quiz_answer_input.visible = False
            quiz_timer_text.value = ""
            page.update()
            return

        quiz_question.value = quiz_cards[quiz_index]["question"]
        quiz_answer_input.value = ""
        quiz_feedback.value = ""
        quiz_score_text.value = f"Scor: {quiz_score}"

        # resetăm timerul
        quiz_time_left = 10
        quiz_timer_text.value = f"Timp rămas: {quiz_time_left} secunde"
        quiz_timer_running = True

        # pornim timerul
        page.run_task(quiz_tick)

        page.update()

    def check_answer():
        nonlocal quiz_index, quiz_score, quiz_timer_running

        quiz_timer_running = False  # oprim timerul

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


ft.run(main)
