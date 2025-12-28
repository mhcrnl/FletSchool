import flet as ft

def main(page: ft.Page):
    page.title = "Text Editor Minimal"
    page.window.width = 700
    page.window.height = 500
    
    text_field = ft.TextField(
        multiline=True,
        min_lines=20,
        max_lines=30,
        expand=True,
        border=ft.InputBorder.NONE,
        text_style=ft.TextStyle(font_family="Consolas", size=15)
    )
    
    def save_file(e):
        if not file_name.value:
            page.show_snack_bar(ft.SnackBar(ft.Text("Scrie un nume de fișier!")))
            return
            
        try:
            with open(file_name.value + ".txt", "w", encoding="utf-8") as f:
                f.write(text_field.value)
            page.show_snack_bar(ft.SnackBar(ft.Text("Salvat! ✓")))
        except Exception as ex:
            page.show_snack_bar(ft.SnackBar(ft.Text(f"Eroare: {ex}")))
    
    file_name = ft.TextField(
        value="notite",
        width=220,
        label="Nume fișier (fără .txt)",
        suffix_text=ft.Text(".txt", color=ft.Colors.GREY_500)
    )
    
    page.add(
        ft.Row([
            file_name,
            ft.ElevatedButton("Salvează", on_click=save_file, icon=ft.Icons.SAVE)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Container(
            content=text_field,
            padding=10,
            border=ft.border.all(1, ft.Colors.GREY_800),
            expand=True
        )
    )

ft.run(main)
