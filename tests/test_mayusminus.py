from click.testing import CliRunner
from bufalo.modulos.mayusminus import mayusminus

def test_convertir_mayus() -> None:
    """Prueba que convierte el texto a mayúsculas."""
    runner = CliRunner()
    # Para poder invocar el comando mayuscula con agumento de string
    result = runner.invoke(mayusminus, ["mayuscula", "ola de saludo"])
    assert result.exit_code == 0
    assert "OLA DE SALUDO" in result.output

def test_convertir_minus() -> None:
    """Prueba que convierte el texto a minúsculas"""
    runner = CliRunner()
    # Para poder invocar ahora el comando munuscula con argumento un string
    result = runner.invoke(mayusminus,["minuscula", "OLA DE SALUDO"])
    assert result.exit_code == 0
    assert "ola de saludo" in result.output