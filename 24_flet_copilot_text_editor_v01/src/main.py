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
    page.title = "Editor Markdown cu formatări"
    page.window_width = 900
    page.window_height = 700

    text_content = load_text()

    editor = ft.TextField(
        value=text_content,
        multiline=True,
        min_lines=30,
        expand=True,
        border_radius=10,
        border_color="blue",
        cursor_color="blue",
        on_change=lambda e: update_preview(),
    )

    preview = ft.Markdown(
        value=text_content,
        expand=True,
        selectable=True,
    )

    # ---------------------------
    # Funcții pentru formatări
    # ---------------------------

    def insert_at_cursor(tag):
        pos = editor.cursor_position or 0
        text = editor.value or ""

        new_text = text[:pos] + tag + text[pos:]
        editor.value = new_text
        editor.cursor_position = pos + len(tag)

        save_text(editor.value)
        update_preview()
        page.update()

    def bold(e):
        insert_at_cursor("**bold**")

    def italic(e):
        insert_at_cursor("_italic_")

    def underline(e):
        insert_at_cursor("__underline__")

    def update_preview():
        preview.value = editor.value
        save_text(editor.value)
        page.update()

    # ---------------------------
    # UI
    # ---------------------------

    toolbar = ft.Row(
        [
            ft.IconButton(icon=ft.Icons.FORMAT_BOLD, tooltip="Bold", on_click=bold),
            ft.IconButton(icon=ft.Icons.FORMAT_ITALIC, tooltip="Italic", on_click=italic),
            ft.IconButton(icon=ft.Icons.FORMAT_UNDERLINED, tooltip="Underline", on_click=underline),
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    page.add(
        ft.Text("Editor Markdown cu formatări", size=22, weight="bold"),
        toolbar,
        ft.Row(
            [
                ft.Container(editor, expand=1, padding=10),
                ft.VerticalDivider(),
                ft.Container(preview, expand=1, padding=10),
            ],
            expand=True,
        ),
    )


ft.run(main)
