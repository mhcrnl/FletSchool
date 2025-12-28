# 40FletKimiBmi app

Below is a minimal, self-contained BMI calculator written with Flet.  
Save it as `bmi_flet.py` and run:

```bash
pip install flet
python bmi_flet.py
```

A native window will open; type your height (cm) and weight (kg) and press “Calculează”.

```python
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
            rezultat.color = ft.colors.BLUE_GREY_900
        except ValueError:
            rezultat.value = "Introdu valori numerice!"
            rezultat.color = ft.colors.RED
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
    ft.app(target=main)
```

Enjoy your tiny desktop BMI app!

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