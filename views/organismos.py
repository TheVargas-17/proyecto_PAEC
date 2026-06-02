import flet as ft

def mostrar_organismos(page, volver_menu):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "ORGANISMOS, ESTRUCTURAS Y PROCESOS",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Image(
                    src="assets/organismos.jpg",
                    width=400
                ),

                ft.Text(
                    """
El cuerpo humano necesita nutrientes,
actividad física y descanso para funcionar
correctamente.

Hábitos saludables:

• Consumir frutas y verduras.
• Beber suficiente agua.
• Dormir al menos 8 horas.
• Evitar comida chatarra en exceso.
• Realizar actividad física regularmente.

Una buena alimentación mejora la salud
y el desempeño escolar.
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