import flet as ft

def main(page: ft.Page):
    page.title = "Prueba"

    txt = ft.Text(
        "Hola Mundo",
        size=30,
        color=ft.Colors.WHITE
    )

    page.add(txt)

ft.app(target=main)