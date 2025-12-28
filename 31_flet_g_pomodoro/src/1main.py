import flet as ft
import threading
import time

class PomodoroTimer:
    def __init__(self):
        # Timpi în secunde
        self.work_time = 25 * 60  # 25 minute
        self.short_break = 5 * 60  # 5 minute
        self.long_break = 15 * 60  # 15 minute
        self.current_time = self.work_time
        self.is_running = False
        self.is_work_session = True
        self.session_count = 0
        self.timer_thread = None

class PomodoroApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Pomodoro Timer"
        self.page.window_width = 400
        self.page.window_height = 600
        self.page.bgcolor = ft.Colors.BLUE_GREY_900
        
        self.timer = PomodoroTimer()
        
        # Stiluri
        self.primary_color = ft.Colors.RED_400
        self.secondary_color = ft.Colors.GREEN_400
        self.text_color = ft.Colors.WHITE
        
        # Elemente UI
        self.create_ui()
        self.update_display()
    
    def create_ui(self):
        """Crează interfața grafică"""
        # Titlu
        self.title = ft.Text(
            "POMODORO TIMER",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=self.primary_color
        )
        
        # Timer display
        self.time_display = ft.Text(
            "25:00",
            size=72,
            weight=ft.FontWeight.BOLD,
            color=self.text_color
        )
        
        # Status indicator
        self.status_text = ft.Text(
            "Sesiune de Lucru",
            size=20,
            color=self.secondary_color
        )
        
        # Contor sesiuni
        self.session_counter = ft.Text(
            "Sesiuni completate: 0",
            size=16,
            color=ft.Colors.GREY_300
        )
        
        # Butoane de control
        self.start_button = ft.ElevatedButton(
            "START",
            icon=ft.Icons.PLAY_ARROW,
            bgcolor=self.primary_color,
            color=ft.Colors.WHITE,
            on_click=self.start_timer
        )
        
        self.pause_button = ft.ElevatedButton(
            "PAUZĂ",
            icon=ft.Icons.PAUSE,
            bgcolor=ft.Colors.AMBER,
            color=ft.Colors.WHITE,
            on_click=self.pause_timer,
            disabled=True
        )
        
        self.reset_button = ft.ElevatedButton(
            "RESET",
            icon=ft.Icons.REFRESH,
            bgcolor=ft.Colors.BLUE_GREY_700,
            color=ft.Colors.WHITE,
            on_click=self.reset_timer
        )
        
        # Setări timpi
        self.work_slider = ft.Slider(
            min=1,
            max=60,
            divisions=59,
            label="Lucru: {value} min",
            value=25,
            active_color=self.primary_color,
            on_change=self.update_work_time
        )
        
        self.short_break_slider = ft.Slider(
            min=1,
            max=30,
            divisions=29,
            label="Pauză scurtă: {value} min",
            value=5,
            active_color=self.secondary_color,
            on_change=self.update_short_break
        )
        
        self.long_break_slider = ft.Slider(
            min=5,
            max=30,
            divisions=25,
            label="Pauză lungă: {value} min",
            value=15,
            active_color=ft.Colors.BLUE_400,
            on_change=self.update_long_break
        )
        
        # Layout principal
        controls = ft.Column(
            controls=[
                self.title,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                self.time_display,
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                self.status_text,
                self.session_counter,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                ft.Row(
                    controls=[self.start_button, self.pause_button, self.reset_button],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                ft.Divider(height=30, color=ft.Colors.GREY_700),
                ft.Text("SETĂRI TIMPI", size=18, color=ft.Colors.GREY_300),
                self.work_slider,
                self.short_break_slider,
                self.long_break_slider
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        container = ft.Container(
            content=controls,
            padding=20,
            alignment=ft.alignment.center
        )
        
        self.page.add(container)
    
    def format_time(self, seconds):
        """Formatează timpul în MM:SS"""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def update_display(self):
        """Actualizează afișajul timerului"""
        self.time_display.value = self.format_time(self.timer.current_time)
        
        if self.timer.is_work_session:
            self.status_text.value = "Sesiune de Lucru"
            self.status_text.color = self.primary_color
        else:
            if self.timer.session_count % 4 == 0:
                self.status_text.value = "Pauză Lungă"
            else:
                self.status_text.value = "Pauză Scurtă"
            self.status_text.color = self.secondary_color
        
        self.session_counter.value = f"Sesiuni completate: {self.timer.session_count}"
        
        self.page.update()
    
    def timer_loop(self):
        """Bucla principală a timerului"""
        while self.timer.is_running and self.timer.current_time > 0:
            time.sleep(1)
            self.timer.current_time -= 1
            
            # Actualizează afișajul pe thread-ul principal
            self.page.run_task(lambda: self.time_display.update())
        
        if self.timer.current_time <= 0 and self.timer.is_running:
            self.page.run_task(self.session_completed)
    
    def start_timer(self, e):
        """Pornește timerul"""
        if not self.timer.is_running:
            self.timer.is_running = True
            self.start_button.disabled = True
            self.pause_button.disabled = False
            
            # Pornește thread-ul timerului
            self.timer.timer_thread = threading.Thread(target=self.timer_loop, daemon=True)
            self.timer.timer_thread.start()
            
            self.page.update()
    
    def pause_timer(self, e):
        """Pauzează timerul"""
        self.timer.is_running = False
        self.start_button.disabled = False
        self.pause_button.disabled = True
        self.page.update()
    
    def reset_timer(self, e):
        """Resetează timerul la setările inițiale"""
        self.timer.is_running = False
        self.timer.current_time = self.timer.work_time
        self.timer.is_work_session = True
        self.start_button.disabled = False
        self.pause_button.disabled = True
        
        self.update_display()
    
    def session_completed(self):
        """Gestionează finalizarea unei sesiuni"""
        self.timer.is_running = False
        
        if self.timer.is_work_session:
            self.timer.session_count += 1
            # Verifică dacă este pauza lungă (după 4 sesiuni)
            if self.timer.session_count % 4 == 0:
                self.timer.current_time = self.timer.long_break
            else:
                self.timer.current_time = self.timer.short_break
            
            # Afișează notificare
            self.show_notification("Pauză!", "E timpul pentru o pauză!")
        else:
            self.timer.current_time = self.timer.work_time
            self.show_notification("Înapoi la lucru!", "Sesiunea de lucru a început!")
        
        self.timer.is_work_session = not self.timer.is_work_session
        self.start_button.disabled = False
        self.pause_button.disabled = True
        self.update_display()
    
    def show_notification(self, title, message):
        """Afișează o notificare"""
        dialog = ft.AlertDialog(
            title=ft.Text(title),
            content=ft.Text(message),
            actions=[
                ft.TextButton("OK", on_click=lambda e: self.close_dialog(dialog))
            ]
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def close_dialog(self, dialog):
        """Închide dialogul"""
        dialog.open = False
        self.page.update()
    
    # Funcții pentru actualizarea setărilor
    def update_work_time(self, e):
        self.timer.work_time = int(self.work_slider.value) * 60
        if self.timer.is_work_session and not self.timer.is_running:
            self.timer.current_time = self.timer.work_time
            self.update_display()
    
    def update_short_break(self, e):
        self.timer.short_break = int(self.short_break_slider.value) * 60
    
    def update_long_break(self, e):
        self.timer.long_break = int(self.long_break_slider.value) * 60

def main(page: ft.Page):
    app = PomodoroApp(page)

if __name__ == "__main__":
    ft.run(main)
