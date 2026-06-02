import flet as ft

def mostrar_movimiento(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "MOVIMIENTO Y ESTABILIDAD",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/movimiento.jpg",
                    width=400
                ),

                ft.Text(
                    """
La actividad física es fundamental para
mantener una buena salud.

Beneficios:

• Fortalece músculos y huesos.
• Mejora la circulación.
• Reduce el estrés.
• Incrementa la energía.
• Ayuda a prevenir enfermedades.

Se recomienda realizar al menos
30 minutos de actividad física al día.
                    """,
                    size=18,
                    color=ft.Colors.WHITE
                ),

                ft.Button(
                    "Volver",
                    on_click=volver_menu
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    page.update()