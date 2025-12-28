import flet as ft

def main(page: ft.Page):
    page.title = "Calculator BMI Simplificat"
    page.window_width = 350
    page.window_height = 500
    page.padding = 20
    
    # Elemente UI
    height_field = ft.TextField(
        label="Înălțime (cm)",
        value="170",
        width=200
    )
    
    weight_field = ft.TextField(
        label="Greutate (kg)",
        value="70",
        width=200
    )
    
    result_text = ft.Text(size=32, weight=ft.FontWeight.BOLD)
    category_text = ft.Text(size=16)
    
    # Funcție calcul
    def calculate_click(e):
        try:
            height = float(height_field.value)
            weight = float(weight_field.value)
            
            if height <= 0 or weight <= 0:
                raise ValueError
            
            height_m = height / 100
            bmi = weight / (height_m * height_m)
            
            result_text.value = f"BMI: {bmi:.1f}"
            
            if bmi < 18.5:
                category = "Subponderal"
                color = "blue"
            elif bmi < 25:
                category = "Normal"
                color = "green"
            elif bmi < 30:
                category = "Supraponderal"
                color = "orange"
            else:
                category = "Obezitate"
                color = "red"
            
            category_text.value = category
            category_text.color = color
            result_text.color = color
            
        except:
            result_text.value = "Date invalide!"
            category_text.value = ""
            result_text.color = "red"
        
        page.update()
    
    # Layout
    page.add(
        ft.Column(
            [
                ft.Text(
                    "BMI Calculator",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER
                ),
                
                ft.Divider(height=20),
                
                height_field,
                weight_field,
                
                ft.ElevatedButton(
                    "Calculează BMI",
                    on_click=calculate_click,
                    width=200
                ),
                
                ft.Divider(height=20),
                
                ft.Container(
                    content=ft.Column(
                        [
                            result_text,
                            category_text
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=20,
                    bgcolor="#e3f2fd",
                    border_radius=10,
                    alignment=ft.alignment.center
                ),
                
                ft.Divider(height=20),
                
                ft.Text(
                    "Categorii:\n"
                    "< 18.5 - Subponderal\n"
                    "18.5-24.9 - Normal\n"
                    "25-29.9 - Supraponderal\n"
                    "≥ 30 - Obezitate",
                    size=14
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

if __name__ == "__main__":
    ft.run(main)
