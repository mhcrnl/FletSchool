import flet as ft


def main(page: ft.Page):
    page.title = "Editor de text în Flet"
    page.theme_mode = "light"
    page.window_width = 900
    page.window_height = 600

    # Zona principală de text
    editor = ft.TextField(
        multiline=True,
        min_lines=20,
        max_lines=999,
        expand=True,
        border_radius=10,
        bgcolor=ft.Colors.WHITE,
        text_style=ft.TextStyle(size=16),
        cursor_color=ft.Colors.BLUE,
        hint_text="Scrie aici...",
    )

    status = ft.Text("", size=12, color=ft.Colors.GREY)

    # Funcții pentru butoane
    def wrap_selection(prefix: str, suffix: str):
        """Încadrează selecția cu prefix / suffix (ex: **text**)."""
        value = editor.value or ""
        sel_start = editor.selection_start or 0
        sel_end = editor.selection_end or 0

        if sel_start == sel_end:  # nimic selectat
            return

        before = value[:sel_start]
        selected = value[sel_start:sel_end]
        after = value[sel_end:]

        editor.value = before + prefix + selected + suffix + after
        # Repoziționez selecția pe noul text
        editor.selection_start = sel_start
        editor.selection_end = sel_end + len(prefix) + len(suffix)
        page.update()

    def bold_click(e):
        wrap_selection("**", "**")

    def italic_click(e):
        wrap_selection("_", "_")

    def clear_click(e):
        editor.value = ""
        status.value = "Text șters."
        page.update()

    # Salvare în fișier
    save_dialog = ft.FilePicker()
    open_dialog = ft.FilePicker()
    page.overlay.append(save_dialog)
    page.overlay.append(open_dialog)

    def save_result(e: ft.FilePickerResultEvent):
        if e.path:
            try:
                with open(e.path, "w", encoding="utf-8") as f:
                    f.write(editor.value or "")
                status.value = f"Salvat în: {e.path}"
            except Exception as ex:
                status.value = f"Eroare la salvare: {ex}"
        else:
            status.value = "Salvarea a fost anulată."
        page.update()

    def open_result(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            path = e.files[0].path
            try:
                with open(path, "r", encoding="utf-8") as f:
                    editor.value = f.read()
                status.value = f"Fișier încărcat: {path}"
            except Exception as ex:
                status.value = f"Eroare la citire: {ex}"
        else:
            status.value = "Încărcarea a fost anulată."
        page.update()

    save_dialog.on_result = save_result
    open_dialog.on_result = open_result

    def save_click(e):
        save_dialog.save_file(
            dialog_title="Salvează textul",
            file_name="text.txt",
            allowed_extensions=["txt", "md"],
        )

    def open_click(e):
        open_dialog.pick_files(
            dialog_title="Deschide fișier",
            allow_multiple=False,
            allowed_extensions=["txt", "md"],
        )

    # Toolbar
    toolbar = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.FORMAT_BOLD,
                tooltip="Bold (**text**)",
                on_click=bold_click,
            ),
            ft.IconButton(
                icon=ft.Icons.FORMAT_ITALIC,
                tooltip="Italic (_text_)",
                on_click=italic_click,
            ),
            ft.VerticalDivider(width=1),
            ft.IconButton(
                icon=ft.Icons.FOLDER_OPEN,
                tooltip="Deschide fișier",
                on_click=open_click,
            ),
            ft.IconButton(
                icon=ft.Icons.SAVE,
                tooltip="Salvează în fișier",
                on_click=save_click,
            ),
            ft.VerticalDivider(width=1),
            ft.IconButton(
                icon=ft.Icons.DELETE_OUTLINE,
                tooltip="Șterge tot textul",
                on_click=clear_click,
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
    )

    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Editor de text", size=24, weight=ft.FontWeight.BOLD),
                toolbar,
                editor,
                status,
            ],
            expand=True,
        ),
        padding=20,
    )

    page.add(container)


if __name__ == "__main__":
    ft.app(target=main)
