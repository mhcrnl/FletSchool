import flet as ft

def main(page: ft.Page):
    page.title = "Calculator BMI Simplu"
    page.window_width = 400
    page.window_height = 700
    page.padding = 20
    page.bgcolor = "#f5f5f5"
    
    # Variabile
    bmi_value = 0.0
    height_cm = 170
    weight_kg = 70
    
    # Elemente UI
    result_text = ft.Text(
        "00.0",
        size=48,
        weight=ft.FontWeight.BOLD,
        color="blue"
    )
    
    category_text = ft.Text(
        "Introduceți datele",
        size=16,
        color="gray"
    )
    
    # Funcții
    def calculate_bmi(e):
        nonlocal bmi_value
        try:
            height_m = height_cm / 100
            bmi_value = weight_kg / (height_m * height_m)
            result_text.value = f"{bmi_value:.1f}"
            
            # Determină categoria
            if bmi_value < 18.5:
                category = "Subponderal"
                color = "blue"
            elif bmi_value < 25:
                category = "Normal"
                color = "green"
            elif bmi_value < 30:
                category = "Supraponderal"
                color = "orange"
            else:
                category = "Obezitate"
                color = "red"
            
            category_text.value = category
            category_text.color = color
            result_text.color = color
            
        except:
            result_text.value = "Eroare"
            category_text.value = "Verificați datele"
        
        page.update()
    
    def update_height(e):
        nonlocal height_cm
        height_cm = int(e.control.value)
        height_label.value = f"Înălțime: {height_cm} cm"
        calculate_bmi(None)
    
    def update_weight(e):
        nonlocal weight_kg
        weight_kg = int(e.control.value)
        weight_label.value = f"Greutate: {weight_kg} kg"
        calculate_bmi(None)
    
    # Slider pentru înălțime
    height_label = ft.Text(f"Înălțime: {height_cm} cm")
    height_slider = ft.Slider(
        min=100,
        max=220,
        divisions=120,
        value=height_cm,
        label="{value} cm",
        on_change=update_height
    )
    
    # Slider pentru greutate
    weight_label = ft.Text(f"Greutate: {weight_kg} kg")
    weight_slider = ft.Slider(
        min=30,
        max=200,
        divisions=170,
        value=weight_kg,
        label="{value} kg",
        on_change=update_weight
    )
    
    # Tabel categorii BMI
    bmi_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Categorie")),
            ft.DataColumn(ft.Text("BMI")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Subponderal", color="blue")),
                    ft.DataCell(ft.Text("< 18.5")),
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Normal", color="green")),
                    ft.DataCell(ft.Text("18.5 - 24.9")),
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Supraponderal", color="orange")),
                    ft.DataCell(ft.Text("25 - 29.9")),
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Obezitate", color="red")),
                    ft.DataCell(ft.Text("≥ 30")),
                ]
            ),
        ],
        border=ft.border.all(1, "lightblue"),
        border_radius=10,
    )
    
    # Layout
    page.add(
        ft.Column(
            [
                # Titlu
                ft.Text(
                    "CALCULATOR BMI",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="blue",
                    text_align=ft.TextAlign.CENTER
                ),
                
                # Rezultat
                ft.Container(
                    content=ft.Column(
                        [
                            result_text,
                            category_text,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    padding=20,
                    bgcolor="white",
                    border_radius=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Controale
                ft.Container(
                    content=ft.Column(
                        [
                            height_label,
                            height_slider,
                            ft.Divider(height=20),
                            weight_label,
                            weight_slider,
                        ]
                    ),
                    padding=20,
                    bgcolor="white",
                    border_radius=15,
                    margin=ft.margin.only(bottom=20)
                ),
                
                # Tabel
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Categorii BMI:", 
                                   size=16, 
                                   weight=ft.FontWeight.BOLD),
                            bmi_table,
                        ]
                    ),
                    padding=20,
                    bgcolor="white",
                    border_radius=15,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            spacing=10
        )
    )
    
    # Calculează la pornire
    calculate_bmi(None)

if __name__ == "__main__":
    ft.run(main)
