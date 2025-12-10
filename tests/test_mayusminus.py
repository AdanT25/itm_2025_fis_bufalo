from click.testing import CliRunner
from bufalo.modulos.mayusminus import mayusminus

def test_convertir_mayus() -> None:
    """Prueba que convierte el texto a mayúsculas."""
    runner = CliRunner()
    # Para poder invocar el comando mayuscula con agumento de string
    result = runner.invoke(mayusminus, ["mayuscula", "ola de saludo"])
    assert result.exit_code == 0
    assert "OLA DE SALUDO" in result.output

