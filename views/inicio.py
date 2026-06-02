import flet as ft
from views.menu import MenuView

def InicioView(page):

    page.clean()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "PAEC CETIS 61",
                    size=35,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE
                ),

                ft.Text(
                    """
¡Qué gusto tenerte aquí!

Este espacio está pensado para ti, para que descubras cómo pequeños cambios en tu alimentación, actividad física y descanso pueden mejorar tu salud y rendimiento académico.

Recuerda: tu salud es tu mejor herramienta para alcanzar tus metas.
                    """,
                    size=18,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER
                ),

                ft.Button(
                    "Entrar",
                    on_click=lambda e: MenuView(page)
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

    page.update()