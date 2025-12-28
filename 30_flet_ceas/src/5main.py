import flet as ft
import flet.canvas as cv
import math
import datetime
import asyncio

async def main(page: ft.Page):
    page.title = "Ceas analogic"
    page.theme_mode = "dark"
    page.window_width = 400
    page.window_height = 450

    size = 300
    center = size / 2
    radius = size / 2 - 10

    # Canvas nou (CustomPaint)
    canvas = cv.Canvas(
        shapes=[],
        width=size,
        height=size,
    )

    async def draw_clock():
        while True:
            canvas.shapes.clear()

            # Cadran
            canvas.shapes.append(
                cv.Circle(
                    center=ft.Offset(center, center),
                    radius=radius,
                    paint=cv.Paint(
                        color=ft.colors.WHITE,
                        stroke_width=4,
                        style=cv.PaintingStyle.STROKE,
                    ),
                )
            )

            # Marcaje ore
            for i in range(12):
                angle = math.radians(i * 30 - 90)
                x1 = center + math.cos(angle) * (radius - 10)
                y1 = center + math.sin(angle) * (radius - 10)
                x2 = center + math.cos(angle) * (radius - 25)
                y2 = center + math.sin(angle) * (radius - 25)

                canvas.shapes.append(
                    cv.Line(
                        p1=ft.Offset(x1, y1),
                        p2=ft.Offset(x2, y2),
                        paint=cv.Paint(color=ft.colors.WHITE, stroke_width=3),
                    )
                )

            # Ora curentă
            now = datetime.datetime.now()
            hour = now.hour % 12
            minute = now.minute
            second = now.second

            # Unghiuri
            hour_angle = math.radians((hour + minute / 60) * 30 - 90)
            minute_angle = math.radians(minute * 6 - 90)
            second_angle = math.radians(second * 6 - 90)

            # Acul orelor
            canvas.shapes.append(
                cv.Line(
                    p1=ft.Offset(center, center),
                    p2=ft.Offset(
                        center + math.cos(hour_angle) * (radius * 0.5),
                        center + math.sin(hour_angle) * (radius * 0.5),
                    ),
                    paint=cv.Paint(color=ft.colors.BLUE, stroke_width=6),
                )
            )

            # Acul minutelor
            canvas.shapes.append(
                cv.Line(
                    p1=ft.Offset(center, center),
                    p2=ft.Offset(
                        center + math.cos(minute_angle) * (radius * 0.75),
                        center + math.sin(minute_angle) * (radius * 0.75),
                    ),
                    paint=cv.Paint(color=ft.colors.GREEN, stroke_width=4),
                )
            )

            # Acul secundelor
            canvas.shapes.append(
                cv.Line(
                    p1=ft.Offset(center, center),
                    p2=ft.Offset(
                        center + math.cos(second_angle) * (radius * 0.85),
                        center + math.sin(second_angle) * (radius * 0.85),
                    ),
                    paint=cv.Paint(color=ft.colors.RED, stroke_width=2),
                )
            )

            # Punct central
            canvas.shapes.append(
                cv.Circle(
                    center=ft.Offset(center, center),
                    radius=5,
                    paint=cv.Paint(color=ft.colors.WHITE),
                )
            )

            await page.update_async()
            await asyncio.sleep(1)

    page.add(
        ft.Column(
            [
                ft.Text("Ceas analogic", size=25, weight="bold"),
                canvas,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
    )

    asyncio.create_task(draw_clock())

ft.run(main)
