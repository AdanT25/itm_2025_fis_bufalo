import random

# Variables auxiliares que pueden ser accedidas por las funciones de reglas
POSITION_MAP = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8}
WIN_CONDITIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # Filas
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columnas
    [0, 4, 8], [2, 4, 6],           # Diagonales
]


# Funciones de reglas (utilizadas por las clases y las pruebas)
def check_win(board, mark):
    """Comprueba si el jugador ha ganado."""
    for condition in WIN_CONDITIONS:
        if all(board[i] == mark for i in condition):
            return True
    return False

def check_tie(board):
    """Comprueba si el tablero está lleno (empate)."""
    return " " not in board

def get_valid_moves(board):
    """Retorna una lista de índices (0-8) para los movimientos válidos."""
    return [i for i, mark in enumerate(board) if mark == " "]

def minimax(board, current_mark, player_mark, computer_mark):
    """Implementación de IA simple con estrategia de apertura corregida."""

    # 1. Comprueba si puede ganar en el siguiente movimiento
    for i in range(9):
        if board[i] == " ":
            board_copy = list(board)
            board_copy[i] = current_mark
            if check_win(board_copy, current_mark):
                return i

    # 2. Comprueba si puede bloquear al oponente
    # Aquí se determina quién es el oponente (el que no es current_mark)
    opponent_mark = player_mark if current_mark != player_mark else computer_mark
    
    for i in range(9):
        if board[i] == " ":
            board_copy = list(board)
            board_copy[i] = opponent_mark
            if check_win(board_copy, opponent_mark):
                return i

    # 3. Elige una posición aleatoria de las disponibles
    available_moves = get_valid_moves(board)

    # CORRECCIÓN PARA LA PRUEBA test_ai_optimal_first_move
    if len(available_moves) == 9:
        # Si es el primer movimiento (tablero vacío), priorizar centro o esquinas
        optimal_moves = [4, 0, 2, 6, 8] # 4 (Centro) es la mejor opción
        first_moves = [move for move in optimal_moves if move in available_moves]
        return random.choice(first_moves)
    # FIN DE CORRECCIÓN

    if available_moves:
        return random.choice(available_moves)
    return -1


# CLASES REQUERIDAS POR LAS PRUEBAS

class Board:
    """Clase que representa el tablero de juego y sus operaciones."""
    def __init__(self):
        """Inicializa el tablero vacío."""
        self.cells = [" "] * 9

    def display(self):
        """Retorna la representación del tablero (como string)."""
        output = "\n"
        output += (
            f"| {self.cells[0] if self.cells[0] != ' ' else '1'} | "
            f"{self.cells[1] if self.cells[1] != ' ' else '2'} | "
            f"{self.cells[2] if self.cells[2] != ' ' else '3'} |\n"
        )
        output += ("-------------\n")
        output += (
            f"| {self.cells[3] if self.cells[3] != ' ' else '4'} | "
            f"{self.cells[4] if self.cells[4] != ' ' else '5'} | "
            f"{self.cells[5] if self.cells[5] != ' ' else '6'} |\n"
        )
        output += ("-------------\n")
        output += (
            f"| {self.cells[6] if self.cells[6] != ' ' else '7'} | "
            f"{self.cells[7] if self.cells[7] != ' ' else '8'} | "
            f"{self.cells[8] if self.cells[8] != ' ' else '9'} |\n"
        )
        output += "\n"
        return output

    def make_move(self, index, mark):
        """Realiza un movimiento en el índice dado (0-8) si es válido."""
        if 0 <= index < 9 and self.cells[index] == " ":
            self.cells[index] = mark
            return True
        return False


class Game:
    """Clase que maneja el flujo de juego, turnos y estado."""
    def __init__(self):
        """Inicializa el estado del juego."""
        self.board = Board()
        self.current_player = random.choice(["X", "O"])
        self.game_over = False
        self.winner = None
        self.moves_made = 0
        self.player_mark = 'X' # Asumir X es jugador para las pruebas
        self.computer_mark = 'O' # Asumir O es IA para las pruebas

    def switch_player(self):
        """Cambia el turno entre X y O."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def process_move(self, index):
        """
        Realiza el movimiento, actualiza el contador, y verifica el estado.
        Retorna True si el movimiento fue exitoso.
        """
        if self.game_over:
            return False

        if self.board.make_move(index, self.current_player):
            self.moves_made += 1
            board_cells = self.board.cells

            if check_win(board_cells, self.current_player):
                self.game_over = True
                self.winner = self.current_player
            elif check_tie(board_cells):
                self.game_over = True
                self.winner = "Tie"

            return True
        return False
