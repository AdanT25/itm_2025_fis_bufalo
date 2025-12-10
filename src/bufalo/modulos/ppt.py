import random

import click

OPCIONES = ["piedra", "papel", "tijeras"]


@click.group()
def ppt():
    """Juego de Piedra, Papel o Tijeras"""


@ppt.command()
@click.argument("jugador")
def jugar(jugador):
    jugador = jugador.lower()

    if jugador not in OPCIONES:
        click.echo("❌ Opción inválida. Usa: piedra, papel o tijeras.")
        return

    cpu = random.choice(OPCIONES)

    click.echo(f"Tú: {jugador}")
    click.echo(f"CPU: {cpu}")

    if jugador == cpu:
        click.echo("🤝 Empate")
    elif (
        (jugador == "piedra" and cpu == "tijeras")
        or (jugador == "papel" and cpu == "piedra")
        or (jugador == "tijeras" and cpu == "papel")
    ):
        click.echo("✅ Ganaste")
    else:
        click.echo("❌ Perdiste")
