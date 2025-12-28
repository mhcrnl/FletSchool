# bmi_flet.py
import flet as ft

def main(page: ft.Page):
    page.title = "BMI Calculator"
    page.window_width = 320
    page.window_height = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def calculeaza(e):
        try:
            h = float(inaltime.value) / 100          # cm → m
            w = float(greutate.value)
            bmi = round(w / (h * h), 1)
            categorie = ""
            if bmi < 18.5:
                categorie = "Subponderal"
            elif bmi < 25:
                categorie = "Normal"
            elif bmi < 30:
                categorie = "Supraponderal"
            else:
                categorie = "Obez"

            rezultat.value = f"BMI: {bmi}  –  {categorie}"
            rezultat.color = ft.Colors.BLUE_GREY_900
        except ValueError:
            rezultat.value = "Introdu valori numerice!"
            rezultat.color = ft.Colors.RED
        page.update()

    inaltime = ft.TextField(label="Înălțime (cm)", width=220, text_align=ft.TextAlign.CENTER)
    greutate = ft.TextField(label="Greutate (kg)", width=220, text_align=ft.TextAlign.CENTER)
    btn        = ft.ElevatedButton("Calculează", on_click=calculeaza)
    rezultat   = ft.Text(size=18, weight=ft.FontWeight.BOLD)

    card = ft.Card(
        content=ft.Container(
            padding=20,
            content=ft.Column(
                [
                    ft.Text("Calculator BMI", size=24, weight=ft.FontWeight.BOLD),
                    inaltime,
                    greutate,
                    btn,
                    rezultat,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
            ),
        )
    )

    page.add(card)

if __name__ == "__main__":
    ft.run(main)
