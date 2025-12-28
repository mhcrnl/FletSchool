import flet as ft
import time
from datetime import timedelta

def main(page: ft.Page):
    page.title = "Pomodoro Timer 🍅"
    page.window.width = 420
    page.window.height = 580
    page.window.resizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.with_opacity(0.96, ft.Colors.INDIGO_900)
    
    # Stare aplicație
    WORK_TIME = 25 * 60      # secunde
    BREAK_TIME = 5 * 60
    LONG_BREAK_TIME = 15 * 60
    
    current_time = WORK_TIME
    is_running = False
    is_work_session = True
    pomodoro_count = 0
    timer = None
    
    # Elemente UI
    time_display = ft.Text(
        value="25:00",
        size=72,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.AMBER_300,
        text_align=ft.TextAlign.CENTER
    )
    
    status_text = ft.Text(
        value="Timp de lucru! 💪",
        size=22,
        color=ft.Colors.BLUE_200,
        weight=ft.FontWeight.W_500
    )
    
    pomodoro_counter = ft.Text(
        value="Pomodoro #0",
        size=16,
        color=ft.Colors.GREY_400
    )
    
    progress_ring = ft.ProgressRing(
        value=0,
        width=220,
        height=220,
        stroke_width=12,
        color=ft.Colors.AMBER_400,
        bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.AMBER_400)
    )
    
    def format_time(seconds: int) -> str:
        td = timedelta(seconds=seconds)
        minutes, seconds = divmod(td.seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def update_display():
        time_display.value = format_time(current_time)
        progress = 1 - (current_time / (WORK_TIME if is_work_session else BREAK_TIME))
        progress_ring.value = progress if progress <= 1 else 0
        
        page.update()
    
    def timer_tick(e):
        nonlocal current_time, is_running, pomodoro_count, is_work_session
        
        if current_time > 0 and is_running:
            current_time -= 1
            update_display()
        else:
            is_running = False
            timer.cancel()
            
            # Sfârșit sesiune
            if is_work_session:
                pomodoro_count += 1
                pomodoro_counter.value = f"Pomodoro #{pomodoro_count}"
                
                if pomodoro_count % 4 == 0:
                    current_time = LONG_BREAK_TIME
                    status_text.value = "Pauză lungă! 🌿 (15 min)"
                    status_text.color = ft.Colors.GREEN_300
                else:
                    current_time = BREAK_TIME
                    status_text.value = "Pauză scurtă ☕ (5 min)"
                    status_text.color = ft.Colors.GREEN_300
                
                is_work_session = False
            else:
                current_time = WORK_TIME
                status_text.value = "Timp de lucru! 💪"
                status_text.color = ft.Colors.BLUE_200
                is_work_session = True
            
            update_display()
            page.update()
            # Sunet final (opțional - decomentează dacă ai fișiere audio)
            # page.play_sound("done.mp3")
    
    def start_pause(e):
        nonlocal is_running, timer
        
        if not is_running:
            is_running = True
            start_btn.text = "PAUZĂ"
            start_btn.color = ft.colors.AMBER_300
            start_btn.icon = ft.icons.PAUSE_CIRCLE_FILLED
            
            timer = page.run_interval(1000, timer_tick)
        else:
            is_running = False
            start_btn.text = "START"
            start_btn.color = ft.colors.GREEN_300
            start_btn.icon = ft.icons.PLAY_CIRCLE_FILLED_ROUNDED
            if timer:
                timer.cancel()
        
        page.update()
    
    def reset(e):
        nonlocal current_time, is_running, is_work_session, pomodoro_count
        
        if timer:
            timer.cancel()
            
        is_running = False
        is_work_session = True
        current_time = WORK_TIME
        pomodoro_count = 0
        
        start_btn.text = "START"
        start_btn.color = ft.Colors.GREEN_300
        start_btn.icon = ft.Icons.PLAY_CIRCLE_FILLED_ROUNDED
        
        status_text.value = "Timp de lucru! 💪"
        status_text.color = ft.Colors.BLUE_200
        pomodoro_counter.value = "Pomodoro #0"
        
        update_display()
        page.update()
    
    # Butoane
    start_btn = ft.ElevatedButton(
        "START",
        icon=ft.Icons.PLAY_CIRCLE_FILLED_ROUNDED,
        color=ft.Colors.GREEN_300,
        bgcolor=ft.Colors.with_opacity(0.25, ft.Colors.GREEN_800),
        style=ft.ButtonStyle(
            padding=ft.padding.symmetric(16, 28),
            text_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD)
        ),
        on_click=start_pause,
        width=220
    )
    
    reset_btn = ft.OutlinedButton(
        "Resetare",
        icon=ft.Icons.RESTART_ALT,
        on_click=reset,
        width=220
    )
    
    # Layout principal
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    ft.Container(height=20),
                    ft.Stack(
                        [
                            progress_ring,
                            ft.Container(
                                content=time_display,
                                alignment=ft.alignment.center,
                                width=220,
                                height=220
                            )
                        ],
                        alignment=ft.alignment.center
                    ),
                    ft.Container(height=20),
                    status_text,
                    pomodoro_counter,
                    ft.Container(height=40),
                    start_btn,
                    ft.Container(height=16),
                    reset_btn,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )
    
    update_display()


ft.run(main)
# ft.app(target=main, view=ft.WEB_BROWSER)   # dacă vrei să rulezi în browser
