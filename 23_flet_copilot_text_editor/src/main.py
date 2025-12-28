import flet as ft
import os

FILE_PATH = "document.txt"


def load_text():
    if not os.path.exists(FILE_PATH):
        return ""
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def save_text(content):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main(page: ft.Page):
    page.title = "Editor de text cu formatări"
    page.window_width = 700
    page.window_height = 800

    text_content = load_text()

    editor = ft.TextField(
        value=text_content,
        multiline=True,
        min_lines=30,
        expand=True,
        on_change=lambda e: save_text(editor.value),
        border_radius=10,
        border_color="blue",
        cursor_color="blue",
    )

    # ---------------------------
    # Funcții pentru formatări
    # ---------------------------

    def insert_format(tag_start, tag_end):
        """Inserează tag-uri în jurul selecției."""
        text = editor.value
        sel_start = editor.selection_start
        sel_end = editor.selection_end

        if sel_start == sel_end:
            # fără selecție → inserează tag-uri goale
            new_text = text[:sel_start] + tag_start + tag_end + text[sel_start:]
            editor.value = new_text
            editor.selection_start = editor.selection_end = sel_start + len(tag_start)
        else:
            # cu selecție → înconjoară textul selectat
            selected = text[sel_start:sel_end]
            new_text = (
                text[:sel_start]
                + tag_start
                + selected
                + tag_end
                + text[sel_end:]
            )
            editor.value = new_text
            editor.selection_start = sel_start
            editor.selection_end = sel_end + len(tag_start) + len(tag_end)

        save_text(editor.value)
        page.update()

    def bold(e):
        insert_format("**", "**")

    def italic(e):
        insert_format("_", "_")

    def underline(e):
        insert_format("__", "__")

    # ---------------------------
    # UI
    # ---------------------------

    toolbar = ft.Row(
        [
            ft.ElevatedButton("Bold", icon=ft.Icons.FORMAT_BOLD, on_click=bold),
            ft.ElevatedButton("Italic", icon=ft.Icons.FORMAT_ITALIC, on_click=italic),
            ft.ElevatedButton("Underline", icon=ft.Icons.FORMAT_UNDERLINED, on_click=underline),
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    save_button = ft.ElevatedButton(
        "Salvează manual",
        icon=ft.Icons.SAVE,
        on_click=lambda e: save_text(editor.value),
    )

    page.add(
        ft.Text("Editor de text cu formatări (Markdown-like)", size=22, weight="bold"),
        toolbar,
        editor,
        save_button
    )


ft.run(main)
