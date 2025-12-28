import flet as ft


def main(page: ft.Page):
    page.title = "Calculator BMI"
    page.window_width = 400
    page.window_height = 500
    page.theme_mode = "light"

    # Input-uri
    weight = ft.TextField(
        label="Greutate (kg)",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=200,
    )

    height = ft.TextField(
        label="Înălțime (cm)",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=200,
    )

    result_text = ft.Text(size=20, weight=ft.FontWeight.BOLD)

    def calc_bmi(e):
        try:
            w = float(weight.value)
            h = float(height.value) / 100  # convertim în metri

            bmi = w / (h * h)
            bmi = round(bmi, 2)

            # Interpretare BMI
            if bmi < 18.5:
                status = "Subponderal"
                color = ft.Colors.BLUE
            elif bmi < 25:
                status = "Normal"
                color = ft.Colors.GREEN
            elif bmi < 30:
                status = "Supraponderal"
                color = ft.Colors.ORANGE
            else:
                status = "Obezitate"
                color = ft.Colors.RED

            result_text.value = f"BMI: {bmi} — {status}"
            result_text.color = color

        except:
            result_text.value = "Introduceți valori valide!"
            result_text.color = ft.Colors.RED

        page.update()

    calc_button = ft.ElevatedButton(
        "Calculează BMI",
        icon=ft.Icons.CALCULATE,
        on_click=calc_bmi,
    )

    page.add(
        ft.Column(
            [
                ft.Text("Calculator BMI", size=28, weight=ft.FontWeight.BOLD),
                weight,
                height,
                calc_button,
                result_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


if __name__ == "__main__":
    ft.run(main)
