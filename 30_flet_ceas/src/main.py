import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Ceas digital"
    page.window_width = 400
    page.window_height = 200
    page.theme_mode = "dark"

    # Textul ce va afișa ora
    clock_text = ft.Text(
        "00:00:00",
        size=50,
        weight="bold",
        text_align="center",
        expand=True,
    )

    # Funcția asincronă care actualizează ora
    async def update_clock():
        while True:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            clock_text.value = now
            page.update()
            await page.sleep(1)

    # Layout
    page.add(
        ft.Column(
            [
                ft.Text("Ceas digital", size=25, weight="bold"),
                clock_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

    # Pornim ceasul
    page.run_task(update_clock)

ft.run(main)
