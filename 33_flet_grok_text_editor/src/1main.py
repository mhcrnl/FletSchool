import flet as ft

def main(page: ft.Page):
    page.title = "Text Editor Minimal"
    
    editor = ft.TextField(
        multiline=True,
        min_lines=20,
        expand=True,
        border=ft.InputBorder.NONE,
        text_style=ft.TextStyle(font_family="Consolas", size=15)
    )
    
    filename = ft.TextField(
        value="nota-mea",
        label="Nume fișier",
        suffix=ft.Text(".txt", color=ft.Colors.GREY_500),
        width=300
    )
    
    def save(e):
        try:
            with open(f"{filename.value}.txt", "w", encoding="utf-8") as f:
                f.write(editor.value)
            page.show_snack_bar(ft.SnackBar(ft.Text("Salvat ✓")))
        except Exception as ex:
            page.show_snack_bar(ft.SnackBar(ft.Text(f"Eroare: {ex}")))
    
    page.add(
        ft.Row([filename, ft.ElevatedButton("Salvează", on_click=save)]),
        ft.Container(editor, expand=True, padding=10, border=ft.border.all(1, ft.Colors.GREY_800))
    )

ft.run(main)
