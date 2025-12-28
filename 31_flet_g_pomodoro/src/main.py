import flet as ft
import time
import threading

def main(page: ft.Page):
    page.title = "Pomodoro Timer"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 500
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Variabile de stare
    seconds = 25 * 60
    running = False

    def format_time(s):
        mins, secs = divmod(s, 60)
        return f"{mins:02d}:{secs:02d}"

    # Componente UI
    timer_text = ft.Text(value=format_time(seconds), size=60, weight=ft.FontWeight.BOLD)
    status_text = ft.Text(value="Focus Time!", size=20, color=ft.Colors.ORANGE_700)
    
    progress_ring = ft.ProgressRing(
        value=1.0, stroke_width=10, width=200, height=200, color=ft.Colors.ORANGE_700
    )

    def update_timer():
        nonlocal seconds, running
        while seconds > 0 and running:
            time.sleep(1)
            seconds -= 1
            timer_text.value = format_time(seconds)
            progress_ring.value = seconds / (25 * 60)
            page.update()
        
        if seconds == 0:
            status_text.value = "Pauză! Te-ai descurcat de minune."
            status_text.color = ft.Colors.GREEN
            page.update()

    def start_timer(e):
        nonlocal running
        if not running:
            running = True
            btn_start.disabled = True
            btn_pause.disabled = False
            # Rulăm timer-ul într-un thread separat pentru a nu bloca UI-ul
            threading.Thread(target=update_timer, daemon=True).start()
            page.update()

    def pause_timer(e):
        nonlocal running
        running = False
        btn_start.disabled = False
        btn_pause.disabled = True
        page.update()

    def reset_timer(e):
        nonlocal seconds, running
        running = False
        seconds = 25 * 60
        timer_text.value = format_time(seconds)
        progress_ring.value = 1.0
        status_text.value = "Focus Time!"
        btn_start.disabled = False
        btn_pause.disabled = True
        page.update()

    # Butoane
    btn_start = ft.ElevatedButton("Start", icon=ft.Icons.PLAY_ARROW, on_click=start_timer)
    btn_pause = ft.ElevatedButton("Pauză", icon=ft.Icons.PAUSE, on_click=pause_timer, disabled=True)
    btn_reset = ft.OutlinedButton("Reset", icon=ft.Icons.RESTART_ALT, on_click=reset_timer)

    # Layout
    page.add(
        status_text,
        ft.Stack(
            [
                progress_ring,
                ft.Container(content=timer_text, alignment=ft.alignment.center, width=200, height=200)
            ]
        ),
        ft.Row(
            [btn_start, btn_pause, btn_reset],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.run(main)
