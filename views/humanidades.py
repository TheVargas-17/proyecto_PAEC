import flet as ft

def mostrar_humanidades(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "HUMANIDADES",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/humanidades.jpg",
                    width=400
                ),

                ft.Text(
                    """
Las humanidades promueven valores que ayudan
a mejorar la convivencia y el bienestar social.

Valores importantes:

• Respeto.
• Empatía.
• Solidaridad.
• Responsabilidad.

Estos valores contribuyen a construir
ambientes saludables dentro de la escuela,
la familia y la comunidad.
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