import click


@click.group()
def mayusminus() -> None:
    """Convierte texto a mayúsculas o minúsculas."""
    pass


@mayusminus.command()
@click.argument("texto", type=str)
def mayuscula(texto: str) -> None:
    """Convierte el texto a mayúsculas."""
    result = texto.upper()
    click.echo(result)


@mayusminus.command()
@click.argument("texto", type=str)
def minuscula(texto: str) -> None:
    """Convierte el texto a minúsculas."""
    result = texto.lower()
    click.echo(result)


