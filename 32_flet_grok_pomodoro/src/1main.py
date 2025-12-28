import flet as ft
import time

def main(page: ft.Page):
    page.title = "Pomodoro Simplu"
    page.window.width = 360
    page.window.height = 480
    page.window.resizable = False
    page.theme_mode = ft.ThemeMode.DARK
    
    seconds = 25 * 60
    running = False
    timer = None
    
    time_text = ft.Text(
        "25:00",
        size=64,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    status = ft.Text(
        "Lucru",
        size=24,
        color=ft.Colors.GREEN_300
    )
    
    def format_time(s):
        m = s // 60
        sec = s % 60
        return f"{m:02d}:{sec:02d}"
    
    def tick(e):
        nonlocal seconds
        if seconds > 0 and running:
            seconds -= 1
            time_text.value = format_time(seconds)
            page.update()
        else:
            running = False
            timer.cancel()
            status.value = "GATA!"
            status.color = ft.colors.AMBER_400
            page.update()
    
    def start_pause(e):
        nonlocal running, timer
        if not running:
            running = True
            btn.text = "Pauză"
            btn.icon = ft.Icons.PAUSE_CIRCLE
            btn.color = ft.Colors.AMBER_300
            timer = page.run_interval(1000, tick)
        else:
            running = False
            btn.text = "Start"
            btn.icon = ft.Icons.PLAY_CIRCLE
            btn.color = ft.Colors.GREEN_300
            if timer:
                timer.cancel()
        page.update()
    
    def reset(e):
        nonlocal seconds, running
        if timer:
            timer.cancel()
        running = False
        seconds = 25 * 60
        time_text.value = "25:00"
        status.value = "Lucru"
        status.color = ft.Colors.GREEN_300
        btn.text = "Start"
        btn.icon = ft.Icons.PLAY_CIRCLE
        btn.color = ft.Colors.GREEN_300
        page.update()
    
    btn = ft.ElevatedButton(
        "Start",
        icon=ft.Icons.PLAY_CIRCLE,
        color=ft.Colors.GREEN_300,
        on_click=start_pause,
        width=180,
        height=56
    )
    
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Container(height=40),
                    time_text,
                    ft.Container(height=20),
                    status,
                    ft.Container(height=60),
                    btn,
                    ft.Container(height=20),
                    ft.OutlinedButton("Reset", on_click=reset, width=180)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            expand=True,
            alignment=ft.alignment.center
        )
    )


ft.run(main)
# ft.app(target=main, view=ft.WEB_BROWSER)  # pentru browser
