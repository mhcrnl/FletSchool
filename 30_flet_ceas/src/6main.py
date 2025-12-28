import flet as ft
import asyncio

POMODORO_TIME = 25 * 60   # 25 minute
BREAK_TIME = 5 * 60       # 5 minute

async def main(page: ft.Page):
    page.title = "Pomodoro Timer"
    page.theme_mode = "dark"
    page.window_width = 400
    page.window_height = 300

    time_left = POMODORO_TIME
    running = False
    on_break = False

    timer_text = ft.Text("25:00", size=60, weight="bold")

    # ---------------------------
    # Actualizare afișaj timp
    # ---------------------------
    def format_time(seconds):
        m = seconds // 60
        s = seconds % 60
        return f"{m:02d}:{s:02d}"

    # ---------------------------
    # Timer asincron
    # ---------------------------
    async def run_timer():
        nonlocal time_left, running, on_break

        while running and time_left > 0:
            await asyncio.sleep(1)
            time_left -= 1
            timer_text.value = format_time(time_left)
            await page.update_async()

        # Când se termină Pomodoro
        if running and time_left == 0:
            running = False
            if not on_break:
                # Trecem la pauză
                on_break = True
                time_left = BREAK_TIME
                timer_text.value = format_time(time_left)
                await page.update_async()

    # ---------------------------
    # Butoane
    # ---------------------------
    def start_timer(e):
        nonlocal running
        if not running:
            running = True
            asyncio.create_task(run_timer())

    def pause_timer(e):
        nonlocal running
        running = False

    def reset_timer(e):
        nonlocal running, time_left, on_break
        running = False
        on_break = False
        time_left = POMODORO_TIME
        timer_text.value = "25:00"
        page.update()

    # ---------------------------
    # UI Layout
    # ---------------------------
    page.add(
        ft.Column(
            [
                ft.Text("Pomodoro Timer", size=30, weight="bold"),
                timer_text,
                ft.Row(
                    [
                        ft.ElevatedButton("Start", on_click=start_timer),
                        ft.ElevatedButton("Pauză", on_click=pause_timer),
                        ft.ElevatedButton("Reset", on_click=reset_timer),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

ft.run(main)
