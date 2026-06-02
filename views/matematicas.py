import flet as ft

def mostrar_matematicas(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "TEMAS SELECTOS DE MATEMÁTICAS",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/matematicas.jpg",
                    width=400
                ),

                ft.Text(
                    """
Las matemáticas ayudan a analizar datos
relacionados con la salud.

Aplicaciones:

• Cálculo del Índice de Masa Corporal (IMC).
• Estadísticas de actividad física.
• Gráficas de hábitos alimenticios.
• Porcentajes y probabilidades.

Gracias a las matemáticas podemos tomar
decisiones informadas para mejorar nuestra salud.
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