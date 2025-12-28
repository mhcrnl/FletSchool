# 35FletGemBmi app



Crearea unui calculator de **BMI (Indice de Masă Corporală)** în Flet este un proiect excelent pentru a învăța cum să preiei date de la utilizator și să oferi feedback vizual instantaneu.

Iată o implementare modernă care folosește glisoare (`Sliders`) pentru o experiență de utilizare mai fluidă:

Python

```
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
            category.color = ft.colors.BLUE_400
        elif 18.5 <= bmi_value < 25:
            category.value = "Greutate Normală"
            category.color = ft.colors.GREEN_400
        elif 25 <= bmi_value < 30:
            category.value = "Supraponderal"
            category.color = ft.colors.ORANGE_400
        else:
            category.value = "Obezitate"
            category.color = ft.colors.RED_400

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
            italic=True, size=12, text_align=ft.TextAlign.CENTER, color=ft.colors.GREY_600
        )
    )

    # Calcul inițial la deschidere
    calculate_bmi(None)

ft.app(target=main)
```

---

### De ce am ales acest design?

1. **Interactivitate (`on_change`)**: Spre deosebire de formularele clasice unde trebuie să apeși un buton "Calculează", aici rezultatul se actualizează instantaneu pe măsură ce miști glisiera.

2. **Feedback Vizual**: Textul își schimbă culoarea (albastru, verde, roșu) pentru a indica starea de sănătate, ceea ce face aplicația mult mai intuitivă.

3. **Matematică simplă**: Folosim formula standard $BMI = \frac{\text{greutate (kg)}}{\text{înălțime (m)}^2}$.

### Ce am folosit din Flet:

- **`ft.Slider`**: Perfect pentru a limita inputul utilizatorului la valori rezonabile și pentru a evita erorile de tastare.

- **`ft.Divider`**: Pentru a crea spațiu vizual între secțiunile de input și cele de rezultat.

- **`ft.Text`**: Am folosit diferite grosimi de font (`FontWeight`) pentru a crea o ierarhie vizuală clară.

**Ai vrea să adăugăm și o funcție de "Istoric", care să salveze ultimele 5 calcule într-o listă jos în pagină?**

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