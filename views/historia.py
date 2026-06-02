import flet as ft

def mostrar_historia(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "CONCIENCIA HISTÓRICA III",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/historia.jpg",
                    width=400
                ),

                ft.Text(
                    """
A lo largo de la historia las sociedades
han desarrollado diferentes prácticas para
mejorar la salud y la calidad de vida.

Ejemplos:

• Campañas de vacunación.
• Mejoras en la higiene.
• Acceso a agua potable.
• Promoción del ejercicio físico.

Estos avances han contribuido a aumentar
la esperanza de vida de las personas.
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