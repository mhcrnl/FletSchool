import flet as ft
import datetime

async def main(page: ft.Page):
    page.title = "Ceas digital"
    page.window_width = 400
    page.window_height = 200
    page.theme_mode = "dark"

    clock_text = ft.Text(
        "00:00:00",
        size=50,
        weight="bold",
        text_align="center",
        expand=True,
    )

    async def update_clock():
        while True:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            clock_text.value = now
            await page.update_async()
            await page.sleep(1)

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

    page.run_task(update_clock)

ft.run(main)
