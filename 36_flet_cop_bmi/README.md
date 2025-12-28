# 36FletCopBmi app

Perfect, Mihai — îți construiesc un **calculator BMI (Body Mass Index)** în Flet, simplu, modern și ușor de extins. Codul este complet funcțional și îl poți rula imediat.

---

# 🧮 Calculator BMI în Flet

```python
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
                color = ft.colors.BLUE
            elif bmi < 25:
                status = "Normal"
                color = ft.colors.GREEN
            elif bmi < 30:
                status = "Supraponderal"
                color = ft.colors.ORANGE
            else:
                status = "Obezitate"
                color = ft.colors.RED

            result_text.value = f"BMI: {bmi} — {status}"
            result_text.color = color

        except:
            result_text.value = "Introduceți valori valide!"
            result_text.color = ft.colors.RED

        page.update()

    calc_button = ft.ElevatedButton(
        "Calculează BMI",
        icon=ft.icons.CALCULATE,
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
    ft.app(target=main)
```

---

# 🔧 Ce poți adăuga ușor peste acest proiect

- grafic cu evoluția BMI în timp
- salvarea rezultatelor în fișier
- slider pentru greutate și înălțime
- animații la afișarea rezultatului
- teme light/dark

Dacă vrei, pot transforma acest calculator într-o aplicație completă cu istoric, grafice și UI modern.

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