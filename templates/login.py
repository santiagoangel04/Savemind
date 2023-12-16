import flet as ft


def main(page:ft.Page):
    container = ft.Container(
        border= 20,
        width=400,
        gradient= ft.LinearGradient([
            ft.colors.PURPLE,
            ft.colors.PINK,
            ft.colors.RED
        ])
    )
    page.bgcolor = ft.colors.BLACK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(container) #agregar el elemento a la pantalla

ft.app(target = main)#para que se ejecute como una aplicacion web
