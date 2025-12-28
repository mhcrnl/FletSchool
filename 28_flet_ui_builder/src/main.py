import flet as ft

def main(page: ft.Page):
    page.title = "Flet UI Builder"
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

    selected_control = None

    # Funcție pentru selectarea unui control
    def select_control(ctrl):
        nonlocal selected_control
        selected_control = ctrl
        inspector.controls = [
            ft.Text("Inspector", size=20, weight="bold"),
            ft.TextField(
                label="Text",
                value=getattr(ctrl, "value", ""),
                on_change=lambda e: update_property("value", e.control.value),
            ),
        ]
        page.update()

    # Actualizare proprietăți
    def update_property(prop, value):
        if selected_control:
            setattr(selected_control, prop, value)
            page.update()

    # Adăugare componentă în canvas
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

    # Panou stânga – lista de componente
    palette = ft.Column(
        [
            ft.Text("Componente", size=20, weight="bold"),
            *[
                ft.ElevatedButton(comp, data=comp, on_click=add_component)
                for comp in components
            ],
        ],
        width=200,
    )

    # Layout final
    page.add(
        ft.Row(
            [
                palette,
                ft.VerticalDivider(),
                ft.Container(canvas, expand=True, padding=10),
                ft.VerticalDivider(),
                ft.Container(inspector, width=300, padding=10),
            ],
            expand=True,
        )
    )

ft.run(main)
