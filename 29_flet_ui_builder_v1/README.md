# 29FletUiBuilderV1 app

Mihai, pregătește‑te — acum intrăm în zona **adevăratelor unelte profesionale**.  
Îți dau o versiune complet funcțională a UI Builder‑ului **cu generator de cod Flet**, astfel încât orice UI construit în canvas să poată fi exportat ca Python.

Asta înseamnă:

### ✔ Panou stânga – componente

### ✔ Canvas – UI construit

### ✔ Inspector – editezi proprietăți

### ✔ Generator de cod – exportă UI‑ul în Python Flet

Totul într‑un singur fișier, clar, extensibil și ușor de modificat.

---

# 🧩 **UI BUILDER COMPLET CU GENERATOR DE COD**

Acesta este un prototip complet funcțional, perfect pentru extins.

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Flet UI Builder cu Generator de Cod"
    page.window_width = 1200
    page.window_height = 700

    # Lista componentelor disponibile
    components = [
        "Text",
        "Button",
        "TextField",
        "Container",
    ]

    # Canvas-ul unde adăugăm componente
    canvas = ft.Column(expand=True, scroll="auto")

    # Inspectorul de proprietăți
    inspector = ft.Column(
        [
            ft.Text("Inspector", size=20, weight="bold"),
            ft.Text("Selectează un element pentru a-i edita proprietățile."),
        ],
        expand=True,
    )

    # Generator de cod
    code_output = ft.TextField(
        label="Cod generat",
        multiline=True,
        min_lines=20,
        expand=True,
        read_only=True,
    )

    selected_control = None

    # ---------------------------
    # Funcție pentru selectarea unui control
    # ---------------------------
    def select_control(ctrl):
        nonlocal selected_control
        selected_control = ctrl

        # Inspector simplu: editezi doar textul
        inspector.controls = [
            ft.Text("Inspector", size=20, weight="bold"),
            ft.TextField(
                label="Text",
                value=getattr(ctrl, "value", getattr(ctrl, "content", ft.Text("")).value if hasattr(ctrl, "content") else ""),
                on_change=lambda e: update_property("value", e.control.value),
            ),
        ]
        page.update()

    # ---------------------------
    # Actualizare proprietăți
    # ---------------------------
    def update_property(prop, value):
        if selected_control:
            if hasattr(selected_control, prop):
                setattr(selected_control, prop, value)
            elif hasattr(selected_control, "content") and hasattr(selected_control.content, prop):
                setattr(selected_control.content, prop, value)
            page.update()

    # ---------------------------
    # Adăugare componentă în canvas
    # ---------------------------
    def add_component(e):
        comp = e.control.data

        if comp == "Text":
            ctrl = ft.Text("Text nou", size=20)
        elif comp == "Button":
            ctrl = ft.ElevatedButton("Buton")
        elif comp == "TextField":
            ctrl = ft.TextField(label="Input")
        elif comp == "Container":
            ctrl = ft.Container(
                content=ft.Text("Container"),
                padding=10,
                bgcolor="#eeeeee",
                border_radius=5,
            )
        else:
            return

        # Fiecare control devine selectabil
        ctrl.on_click = lambda e, c=ctrl: select_control(c)

        canvas.controls.append(ctrl)
        page.update()

    # ---------------------------
    # Generator de cod
    # ---------------------------
    def generate_code(e):
        code = "import flet as ft\n\n\ndef main(page: ft.Page):\n"
        code += "    page.title = \"UI generat\"\n\n"

        for i, ctrl in enumerate(canvas.controls):
            if isinstance(ctrl, ft.Text):
                code += f"    t{i} = ft.Text('{ctrl.value}', size={ctrl.size})\n"
            elif isinstance(ctrl, ft.ElevatedButton):
                code += f"    b{i} = ft.ElevatedButton('{ctrl.text}')\n"
            elif isinstance(ctrl, ft.TextField):
                code += f"    f{i} = ft.TextField(label='{ctrl.label}')\n"
            elif isinstance(ctrl, ft.Container):
                code += f"    c{i} = ft.Container(content=ft.Text('{ctrl.content.value}'), padding={ctrl.padding})\n"

        # Adăugăm componentele în pagină
        code += "\n    page.add(\n"
        for i, ctrl in enumerate(canvas.controls):
            prefix = "t" if isinstance(ctrl, ft.Text) else \
                     "b" if isinstance(ctrl, ft.ElevatedButton) else \
                     "f" if isinstance(ctrl, ft.TextField) else \
                     "c"
            code += f"        {prefix}{i},\n"
        code += "    )\n\n\nft.app(target=main)"

        code_output.value = code
        page.update()

    # ---------------------------
    # Panou stânga – lista de componente
    # ---------------------------
    palette = ft.Column(
        [
            ft.Text("Componente", size=20, weight="bold"),
            *[
                ft.ElevatedButton(comp, data=comp, on_click=add_component)
                for comp in components
            ],
            ft.Divider(),
            ft.ElevatedButton("Generează cod", on_click=generate_code),
        ],
        width=200,
    )

    # ---------------------------
    # Layout final
    # ---------------------------
    page.add(
        ft.Row(
            [
                palette,
                ft.VerticalDivider(),
                ft.Container(canvas, expand=True, padding=10),
                ft.VerticalDivider(),
                ft.Container(inspector, width=300, padding=10),
                ft.VerticalDivider(),
                ft.Container(code_output, width=400, padding=10),
            ],
            expand=True,
        )
    )


ft.app(target=main)
```

---

# 🎉 Ce poate versiunea asta

### ✔ Construiești UI vizual

Adaugi Text, Button, TextField, Container.

### ✔ Selectezi componente și le editezi

Inspectorul permite modificarea textului.

### ✔ Generezi cod Flet real

Codul generat poate fi copiat și rulat direct.

### ✔ Structură clară și extensibilă

Poți adăuga:

- drag & drop
- layout nesting (Row/Column în interiorul altora)
- editare completă de proprietăți
- export/import proiecte

---

# 🔥 Vrei să mergem mai departe?

Pot să-ți adaug:

### ➤ Drag & Drop real în canvas

### ➤ Inspector complet (padding, margin, colors, width/height)

### ➤ Export în fișier .py

### ➤ TreeView pentru structura UI

### ➤ Preview live într-o fereastră separată

Spune-mi ce vrei să construim în continuare și îl extindem pas cu pas.

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