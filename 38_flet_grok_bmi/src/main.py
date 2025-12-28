import flet as ft

def main(page: ft.Page):
    page.title = "Calculator BMI"
    page.window.width = 420
    page.window.height = 520
    page.window.resizable = False
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20

    # Câmpuri de introducere
    greutate = ft.TextField(
        label="Greutate (kg)",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=280,
        autofocus=True
    )

    inaltime = ft.TextField(
        label="Înălțime (cm)",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=280
    )

    # Rezultat
    rezultat = ft.Text(
        "Introduceți valorile și apăsați Calculare",
        size=16,
        text_align=ft.TextAlign.CENTER,
        color=ft.Colors.GREY_400
    )

    categorie = ft.Text(
        "",
        size=18,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    def calcul_bmi(e):
        try:
            kg = float(greutate.value)
            cm = float(inaltime.value)

            if kg <= 0 or cm <= 0:
                rezultat.value = "Valorile trebuie să fie pozitive!"
                categorie.value = ""
                page.update()
                return

            m = cm / 100
            bmi = kg / (m * m)
            
            # Formatare cu 1 zecimală
            bmi_text = f"{bmi:.1f}"

            # Determinarea categoriei
            if bmi < 18.5:
                cat = "Subponderal"
                culoare = ft.Colors.BLUE_300
            elif bmi < 25:
                cat = "Normoponderal"
                culoare = ft.Colors.GREEN_400
            elif bmi < 30:
                cat = "Supraponderal"
                culoare = ft.Colors.ORANGE_400
            else:
                cat = "Obezitate"
                culoare = ft.Colors.RED_400

            rezultat.value = f"BMI = {bmi_text}"
            rezultat.color = ft.Colors.WHITE

            categorie.value = cat
            categorie.color = culoare

        except ValueError:
            rezultat.value = "Introduceți doar numere valide!"
            rezultat.color = ft.Colors.RED_300
            categorie.value = ""

        page.update()

    def reset(e):
        greutate.value = ""
        inaltime.value = ""
        rezultat.value = "Introduceți valorile și apăsați Calculare"
        rezultat.color = ft.Colors.GREY_400
        categorie.value = ""
        page.update()

    # Butoane
    btn_calculeaza = ft.ElevatedButton(
        "Calculează BMI",
        on_click=calcul_bmi,
        width=280,
        height=48,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_700,
            color=ft.Colors.WHITE
        )
    )

    btn_reset = ft.TextButton(
        "Resetare",
        on_click=reset,
        style=ft.ButtonStyle(color=ft.Colors.GREY_400)
    )

    # Interfață
    page.add(
        ft.Container(height=20),
        ft.Text("Calculator IMC / BMI", size=28, weight=ft.FontWeight.BOLD),
        ft.Container(height=30),
        
        greutate,
        ft.Container(height=16),
        inaltime,
        
        ft.Container(height=30),
        btn_calculeaza,
        ft.Container(height=12),
        btn_reset,
        
        ft.Container(height=40),
        rezultat,
        ft.Container(height=8),
        categorie,
        
        ft.Container(height=20),
        ft.Text(
            "Clasificare (OMS):\n"
            "Sub 18.5 → Subponderal\n"
            "18.5–24.9 → Normal\n"
            "25–29.9 → Supraponderal\n"
            "30+ → Obezitate",
            size=12,
            color=ft.Colors.GREY_500,
            text_align=ft.TextAlign.CENTER
        )
    )

ft.run(main)
