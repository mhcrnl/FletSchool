# 39FletClaudeBmi app

# 📊 Aplicație de Calcul BMI în Flet 0.80.0

Iată o aplicație completă de calcul al masei corporale (BMI) folosind Flet:

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Calculator BMI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.window.width = 400
    page.window.height = 600
    page.window.resizable = False

    # Funcție pentru a determina categoria BMI
    def get_bmi_category(bmi):
        if bmi < 18.5:
            return "Subponderal", ft.colors.BLUE_400
        elif 18.5 <= bmi < 25:
            return "Greutate normală", ft.colors.GREEN_400
        elif 25 <= bmi < 30:
            return "Supraponderal", ft.colors.ORANGE_400
        else:
            return "Obezitate", ft.colors.RED_400

    # Funcție pentru calculul BMI
    def calculate_bmi(e):
        try:
            weight = float(weight_field.value)
            height = float(height_field.value) / 100  # convertim cm în metri

            if weight <= 0 or height <= 0:
                result_text.value = "Introduceți valori valide!"
                result_text.color = ft.colors.RED
                result_container.visible = False
                page.update()
                return

            bmi = weight / (height ** 2)
            category, color = get_bmi_category(bmi)

            result_text.value = f"BMI: {bmi:.1f}"
            result_text.color = color
            category_text.value = category
            category_text.color = color
            result_container.visible = True

            # Actualizăm indicatorul vizual
            bmi_indicator.value = min(bmi / 40, 1)  # Normalizăm pentru progress bar

        except ValueError:
            result_text.value = "Introduceți numere valide!"
            result_text.color = ft.colors.RED
            result_container.visible = False

        page.update()

    # Funcție pentru resetare
    def reset_fields(e):
        weight_field.value = ""
        height_field.value = ""
        result_container.visible = False
        result_text.value = ""
        page.update()

    # Câmpuri de input
    weight_field = ft.TextField(
        label="Greutate (kg)",
        hint_text="Ex: 70",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=300,
        prefix_icon=ft.icons.MONITOR_WEIGHT,
    )

    height_field = ft.TextField(
        label="Înălțime (cm)",
        hint_text="Ex: 175",
        keyboard_type=ft.KeyboardType.NUMBER,
        width=300,
        prefix_icon=ft.icons.HEIGHT,
    )

    # Butoane
    calculate_button = ft.ElevatedButton(
        text="Calculează BMI",
        icon=ft.icons.CALCULATE,
        on_click=calculate_bmi,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_700,
        ),
        width=300,
    )

    reset_button = ft.TextButton(
        text="Resetează",
        icon=ft.icons.REFRESH,
        on_click=reset_fields,
        width=300,
    )

    # Rezultate
    result_text = ft.Text(
        size=30,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    category_text = ft.Text(
        size=20,
        text_align=ft.TextAlign.CENTER,
    )

    bmi_indicator = ft.ProgressBar(
        width=300,
        value=0,
        color=ft.colors.BLUE_400,
        bgcolor=ft.colors.BLUE_100,
    )

    # Container pentru rezultate
    result_container = ft.Container(
        content=ft.Column(
            [
                result_text,
                category_text,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                bmi_indicator,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.BLUE_50,
        visible=False,
    )

    # Tabel cu categorii BMI
    bmi_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Categorie", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("BMI", weight=ft.FontWeight.BOLD)),
        ],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Subponderal", color=ft.colors.BLUE_400)),
                ft.DataCell(ft.Text("< 18.5")),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Normal", color=ft.colors.GREEN_400)),
                ft.DataCell(ft.Text("18.5 - 24.9")),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Supraponderal", color=ft.colors.ORANGE_400)),
                ft.DataCell(ft.Text("25 - 29.9")),
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Obezitate", color=ft.colors.RED_400)),
                ft.DataCell(ft.Text("≥ 30")),
            ]),
        ],
        border=ft.border.all(1, ft.colors.GREY_400),
        border_radius=10,
    )

    # Layout principal
    page.add(
        ft.Column(
            [
                ft.Container(height=20),
                ft.Text(
                    "Calculator BMI",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Calculează-ți indicele de masă corporală",
                    size=14,
                    color=ft.colors.GREY_700,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Divider(height=30, color=ft.colors.TRANSPARENT),
                weight_field,
                height_field,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                calculate_button,
                reset_button,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                result_container,
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                ft.Text("Categorii BMI:", weight=ft.FontWeight.BOLD, size=16),
                bmi_table,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        )
    )

ft.app(target=main)
```

## 📋 Instalare și Rulare

**1. Instalează Flet:**

```bash
pip install flet==0.80.0
```

**2. Salvează codul într-un fișier (ex: `bmi_calculator.py`)**

**3. Rulează aplicația:**

```bash
python bmi_calculator.py
```

## ✨ Caracteristici

- **Interface intuitivă** cu design modern
- **Calcul instantaneu** al BMI
- **Categorii color-coded**: 
  - 🔵 Subponderal (< 18.5)
  - 🟢 Greutate normală (18.5-24.9)
  - 🟠 Supraponderal (25-29.9)
  - 🔴 Obezitate (≥ 30)
- **Progress bar vizual** pentru BMI
- **Tabel de referință** cu toate categoriile
- **Validare input** pentru valori corecte
- **Buton de resetare**

Aplicația este gata de folosit și complet funcțională! 🎉

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