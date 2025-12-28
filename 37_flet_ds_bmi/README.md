# 37FletDsBmi app

Iată o versiune simplificată a aplicației BMI, actualizată pentru Flet 0.80.0:

```python
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
    ft.app(target=main)
```

Sau o versiune și mai simplă, fără update automat:

```python
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
                    text="Calculează BMI",
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
    ft.app(target=main)
```

**Caracteristici versiune simplificată:**

1. **Simplu și direct** - Doar câmpuri de text și un buton
2. **Fără slider-uri complexe** - Input simplu numeric
3. **Calcul la cerere** - Doar când apăsați butonul
4. **Interface curată** - Layout minimal
5. **Compatibil cu Flet 0.80.0** - Folosește API-ul curent

**Instalare și rulare:**

```bash
pip install flet==0.80.0
python bmi_simplu.py
```

**Diferențe față de versiunea anterioară:**

1. **Slidere opționale** - Prima versiune are update automat, a doua nu
2. **Fără sistem imperial** - Doar metric
3. **Fără indicator grafic** - Doar text
4. **Fără dialog-uri complexe** - Toate informațiile sunt în pagină
5. **Cod mai scurt** - ~70 linii vs 300+ linii

Alegeți prima versiune dacă vreți update automat la glisarea sliderelor, sau a doua versiune dacă vreți cea mai simplă implementare posibilă.

## Run the app

### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://docs.flet.dev/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://docs.flet.dev/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://docs.flet.dev/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://docs.flet.dev/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://docs.flet.dev/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://docs.flet.dev/publish/windows/).