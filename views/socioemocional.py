import flet as ft

def mostrar_socioemocional(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "SOCIOEMOCIONAL",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/socioemocional.jpg",
                    width=400
                ),

                ft.Text(
                    """
La salud socioemocional es la capacidad de reconocer,
comprender y controlar nuestras emociones.

Beneficios:

• Mejor autoestima.
• Menor estrés.
• Mejor comunicación.
• Relaciones saludables.
• Mejor rendimiento académico.

Consejos:

• Expresa tus emociones.
• Habla con personas de confianza.
• Practica actividades relajantes.
• Mantén una actitud positiva.
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