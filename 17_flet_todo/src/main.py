import flet as ft
import sqlite3

# --- 1. CONFIGURARE BAZĂ DE DATE ---
def init_db():
    # check_same_thread=False este necesar pentru aplicații web/desktop multi-thread
    conn = sqlite3.connect("tasks_database.db", check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            status INTEGER
        )
    """)
    conn.commit()
    return conn

# --- 2. CLASA PENTRU UN SINGUR TASK ---
class Task(ft.Column):
    def __init__(self, task_id, task_name, task_status, task_delete, task_status_change, task_update_name):
        super().__init__()
        self.task_id = task_id
        self.task_delete = task_delete
        self.task_status_change = task_status_change
        self.task_update_name = task_update_name

        # Vederea principală: Checkbox + Butoane Edit/Delete
        self.display_task = ft.Checkbox(
            value=True if task_status == 1 else False, 
            label=task_name, 
            on_change=self.status_changed, 
            expand=True
        )
        self.edit_name = ft.TextField(expand=True)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(ft.icons.CREATE_OUTLINED, on_click=self.edit_clicked),
                        ft.IconButton(ft.icons.DELETE_OUTLINE, icon_color="red", on_click=self.delete_clicked),
                    ],
                ),
            ],
        )

        # Vederea pentru editare (ascunsă implicit)
        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                ft.IconButton(icon=ft.icons.DONE_OUTLINE_OUTLINED, icon_color="green", on_click=self.save_clicked),
            ],
        )

        self.controls = [self.display_view, self.edit_view]

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_view.visible = True
        self.edit_view.visible = False
        self.task_update_name(self) # Salvează în DB
        self.update()

    def status_changed(self, e):
        self.task_status_change(self) # Actualizează status în DB

    def delete_clicked(self, e):
        self.task_delete(self)

# --- 3. CLASA PRINCIPALĂ A APLICAȚIEI ---
class TodoApp(ft.Column):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
        self.new_task = ft.TextField(hint_text="Ce ai de făcut?", expand=True, on_submit=self.add_clicked)
        self.tasks = ft.Column()

        # Filtrele de stare (Sintaxa pentru Flet >= 0.21.0)
        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
        )
        self.filter.tabs = [
            ft.Tab(label="Toate"),
            ft.Tab(label="Active"),
            ft.Tab(label="Finalizate"),
        ]

        self.width = 450
        self.controls = [
            ft.Text(value="Planificator Task-uri", style=ft.TextThemeStyle.HEADLINE_MEDIUM, weight=ft.FontWeight.BOLD),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                ],
            ),
            self.filter,
            self.tasks,
        ]
        self.load_tasks_from_db()

    def load_tasks_from_db(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, status FROM tasks")
        for row in cursor.fetchall():
            task = Task(row[0], row[1], row[2], self.task_delete, self.task_status_change, self.task_update_name)
            self.tasks.controls.append(task)
        self.update_filter()

    def add_clicked(self, e):
        if self.new_task.value:
            # Salvare în SQLite
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO tasks (name, status) VALUES (?, ?)", (self.new_task.value, 0))
            self.conn.commit()
            new_id = cursor.lastrowid
            
            # Adăugare în interfață
            task = Task(new_id, self.new_task.value, 0, self.task_delete, self.task_status_change, self.task_update_name)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.new_task.focus()
            self.update_filter()

    def task_delete(self, task):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task.task_id,))
        self.conn.commit()
        self.tasks.controls.remove(task)
        self.update()

    def task_status_change(self, task):
        status = 1 if task.display_task.value else 0
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task.task_id))
        self.conn.commit()
        self.update_filter()

    def task_update_name(self, task):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tasks SET name = ? WHERE id = ?", (task.display_task.label, task.task_id))
        self.conn.commit()

    def tabs_changed(self, e):
        self.update_filter()

    def update_filter(self):
        status_filter = self.filter.tabs[self.filter.selected_index].label
        for task in self.tasks.controls:
            task.visible = (
                status_filter == "Toate"
                or (status_filter == "Active" and not task.display_task.value)
                or (status_filter == "Finalizate" and task.display_task.value)
            )
        self.update()

# --- 4. LANSAREA APLICAȚIEI ---
def main(page: ft.Page):
    page.title = "To-Do Avansat"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    # Inițializăm DB și aplicația
    db_conn = init_db()
    app = TodoApp(db_conn)
    
    page.add(app)

if __name__ == "__main__":
    ft.run(main)
