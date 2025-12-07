import types
from unittest.mock import patch
import click

import bufalo.cli as cli


def test_autodiscover_error():
    """
    Simula un error al importar un módulo para cubrir la excepción en autodiscover.
    El error es capturado dentro de autodiscover, asegurando que no rompa el CLI.
    """
    # Creamos un módulo falso
    fake_module = types.ModuleType("fake_module")

    # Patch para forzar que import_module lance excepción
    with patch("pkgutil.iter_modules", return_value=[(None, "fake_module", False)]), \
         patch("importlib.import_module", side_effect=Exception("Error simulado")):
        cli.autodiscover()  # No debe lanzar excepción


def test_force_cli_py_coverage():
    """
    Forzar la ejecución de main.add_command en cli.py usando un módulo falso.
    Cubre las líneas donde se agrega un click.Group al CLI principal.
    """
    # Creamos un click.Group falso con nombre para evitar error "Command has no name"
    group = click.Group(name="mock_group")  # <- importante
    group.callback = lambda: None
    group.callback.__module__ = "fake_module"  # Coincide con module.__name__

    # Creamos un módulo falso con nuestro grupo
    fake_module = types.ModuleType("fake_module")
    setattr(fake_module, "mock_group", group)

    # Guardamos los comandos actuales antes de autodiscover
    before_commands = set(cli.main.commands.keys())

    # Patch para forzar autodiscover
    with patch("pkgutil.iter_modules", return_value=[(None, "fake_module", False)]), \
         patch("importlib.import_module", return_value=fake_module):
        cli.autodiscover()

    # Verificamos que se haya agregado un nuevo comando de tipo click.Group
    new_commands = set(cli.main.commands.keys()) - before_commands
    assert any(isinstance(cli.main.commands[name], click.Group) for name in new_commands)
