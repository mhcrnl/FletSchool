import flet as ft

def main(page: ft.Page):
    page.title = "Calculator BMI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 550
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Funcția de calcul
    def calculate_bmi(e):
        height_m = slider_height.value / 100
        weight_kg = slider_weight.value
        
        # Formula: BMI = kg / m^2
        bmi_value = weight_kg / (height_m ** 2)
        result_text.value = f"{bmi_value:.1f}"
        
        # Determinarea categoriei și culorii
        if bmi_value < 18.5:
            category.value = "Subponderal"
            category.color = ft.Colors.BLUE_400
        elif 18.5 <= bmi_value < 25:
            category.value = "Greutate Normală"
            category.color = ft.Colors.GREEN_400
        elif 25 <= bmi_value < 30:
            category.value = "Supraponderal"
            category.color = ft.Colors.ORANGE_400
        else:
            category.value = "Obezitate"
            category.color = ft.Colors.RED_400
            
        page.update()

    # Elemente UI
    title = ft.Text("Calculator BMI", size=30, weight=ft.FontWeight.BOLD)
    
    slider_height = ft.Slider(
        min=100, max=230, divisions=130, 
        label="{value} cm", value=170, 
        on_change=calculate_bmi
    )
    
    slider_weight = ft.Slider(
        min=30, max=150, divisions=120, 
        label="{value} kg", value=70, 
        on_change=calculate_bmi
    )

    result_text = ft.Text("24.2", size=50, weight=ft.FontWeight.W_900)
    category = ft.Text("Greutate Normală", size=20, weight=ft.FontWeight.BOLD)

    # Layout-ul paginii
    page.add(
        title,
        ft.Divider(height=20, color="transparent"),
        ft.Text("Înălțime (cm):", weight=ft.FontWeight.W_500),
        slider_height,
        ft.Text("Greutate (kg):", weight=ft.FontWeight.W_500),
        slider_weight,
        ft.Divider(height=40),
        ft.Text("Scorul tău BMI:"),
        result_text,
        category,
        ft.Container(height=20),
        ft.Text(
            "BMI-ul este o măsură statistică a masei corporale a unei persoane.",
            italic=True, size=12, text_align=ft.TextAlign.CENTER, color=ft.Colors.GREY_600
        )
    )

    # Calcul inițial la deschidere
    calculate_bmi(None)

ft.run(main)
