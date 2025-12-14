"""
Pruebas unitarias para el módulo de Tic Tac Toe.

Para ejecutar estas pruebas:
    uv run pytest tests/test_tictactoe.py -v
"""

from click.testing import CliRunner

from bufalo.modulos.tictactoe import tictactoe


def test_tictactoe_help() -> None:
    """Prueba que el comando help funciona."""
    runner = CliRunner()
    result = runner.invoke(tictactoe, ["--help"])
    assert result.exit_code == 0
    assert "Tic Tac Toe" in result.output
    assert "tablero" in result.output
    assert "mover" in result.output
    assert "reiniciar" in result.output
    assert "estado" in result.output


def test_tablero_inicial() -> None:
    """Prueba que se muestra el tablero inicial vacío."""
    runner = CliRunner()
    result = runner.invoke(tictactoe, ["tablero"])

    assert result.exit_code == 0
    # El tablero inicial debe mostrar números del 1 al 9
    for i in range(1, 10):
        assert str(i) in result.output
    # Debe indicar que es turno de X
    assert "Turno de: X" in result.output


def test_mover_posicion_valida() -> None:
    """Prueba un movimiento válido."""
    runner = CliRunner()
    # Primer movimiento en posición 5 (centro)
    result = runner.invoke(tictactoe, ["mover", "5"])

    assert result.exit_code == 0
    assert "Movimiento realizado" in result.output
    assert "Turno de: O" in result.output
    assert "X" in result.output  # Debe mostrar la X en el tablero


def test_mover_posicion_invalida() -> None:
    """Prueba un movimiento en posición inválida."""
    runner = CliRunner()
    # Posición fuera de rango
    result = runner.invoke(tictactoe, ["mover", "0"])

    assert result.exit_code == 0
    assert "Posición inválida" in result.output

    # Posición mayor a 9
    result = runner.invoke(tictactoe, ["mover", "10"])
    assert "Posición inválida" in result.output


def test_mover_casilla_ocupada() -> None:
    """Prueba mover a una casilla ya ocupada."""
    runner = CliRunner()
    # Mover dos veces a la misma posición
    runner.invoke(tictactoe, ["mover", "1"])
    result = runner.invoke(tictactoe, ["mover", "1"])

    assert result.exit_code == 0
    assert "ya está ocupada" in result.output


def test_reiniciar_juego() -> None:
    """Prueba el comando reiniciar."""
    runner = CliRunner()
    # Hacer un movimiento
    runner.invoke(tictactoe, ["mover", "1"])
    # Reiniciar
    result = runner.invoke(tictactoe, ["reiniciar"])

    assert result.exit_code == 0
    assert "Juego reiniciado" in result.output
    # El tablero debe estar vacío (mostrar números)
    for i in range(1, 10):
        assert str(i) in result.output
    assert "Turno de: X" in result.output


def test_estado_inicial() -> None:
    """Prueba el comando estado al inicio."""
    runner = CliRunner()
    # Reiniciar primero para estado limpio
    runner.invoke(tictactoe, ["reiniciar"])
    result = runner.invoke(tictactoe, ["estado"])

    assert result.exit_code == 0
    assert "Jugador actual: X" in result.output
    assert "Movimientos realizados: 0" in result.output
    assert "Juego terminado: False" in result.output
    # El tablero debe mostrarse
    assert "Tablero:" in result.output


def test_victoria_horizontal() -> None:
    """Prueba una victoria horizontal (X gana)."""
    runner = CliRunner()
    runner.invoke(tictactoe, ["reiniciar"])

    # X gana en fila 1 (posiciones 1, 2, 3)
    # X:1, O:4, X:2, O:5, X:3
    runner.invoke(tictactoe, ["mover", "1"])  # X
    runner.invoke(tictactoe, ["mover", "4"])  # O
    runner.invoke(tictactoe, ["mover", "2"])  # X
    runner.invoke(tictactoe, ["mover", "5"])  # O
    result = runner.invoke(tictactoe, ["mover", "3"])  # X gana

    assert result.exit_code == 0
    assert "¡Jugador X gana!" in result.output


def test_victoria_vertical() -> None:
    """Prueba una victoria vertical (O gana)."""
    runner = CliRunner()
    runner.invoke(tictactoe, ["reiniciar"])

    # O gana en columna 3 (posiciones 3, 6, 9)
    # X:1, O:3, X:2, O:6, X:4, O:9
    runner.invoke(tictactoe, ["mover", "1"])  # X
    runner.invoke(tictactoe, ["mover", "3"])  # O
    runner.invoke(tictactoe, ["mover", "2"])  # X
    runner.invoke(tictactoe, ["mover", "6"])  # O
    runner.invoke(tictactoe, ["mover", "4"])  # X
    result = runner.invoke(tictactoe, ["mover", "9"])  # O gana

    assert result.exit_code == 0
    assert "¡Jugador O gana!" in result.output


def test_victoria_diagonal() -> None:
    """Prueba una victoria diagonal."""
    runner = CliRunner()
    runner.invoke(tictactoe, ["reiniciar"])

    # Movimientos para victoria diagonal (esquina a esquina)
    # X:1, O:2, X:5, O:3, X:9
    runner.invoke(tictactoe, ["mover", "1"])  # X
    runner.invoke(tictactoe, ["mover", "2"])  # O
    runner.invoke(tictactoe, ["mover", "5"])  # X
    runner.invoke(tictactoe, ["mover", "3"])  # O
    result = runner.invoke(tictactoe, ["mover", "9"])  # X gana

    assert result.exit_code == 0
    assert "¡Jugador X gana!" in result.output


def test_empate() -> None:
    """Prueba un juego que termina en empate."""
    runner = CliRunner()
    runner.invoke(tictactoe, ["reiniciar"])

    # Secuencia INFALIBLE de empate - probada
    # X:1, O:5, X:2, O:3, X:7, O:4, X:6, O:8, X:9
    movimientos = [1, 5, 2, 3, 7, 4, 6, 8, 9]

    for pos in movimientos:
        result = runner.invoke(tictactoe, ["mover", str(pos)])

    assert result.exit_code == 0
    assert "¡Empate!" in result.output


def test_multiples_partidas() -> None:
    """Prueba jugar múltiples partidas seguidas."""
    runner = CliRunner()

    # Primera partida
    runner.invoke(tictactoe, ["reiniciar"])
    runner.invoke(tictactoe, ["mover", "1"])
    runner.invoke(tictactoe, ["mover", "2"])

    # Segunda partida
    runner.invoke(tictactoe, ["reiniciar"])
    result = runner.invoke(tictactoe, ["tablero"])

    # El tablero debe estar vacío en la nueva partida
    for i in range(1, 10):
        assert str(i) in result.output
    assert "Turno de: X" in result.output
