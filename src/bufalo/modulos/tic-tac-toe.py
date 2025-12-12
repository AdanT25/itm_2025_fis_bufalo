import random

board = [' '] * 9

POSITION_MAP = {
    1: 0, 2: 1, 3: 2,
    4: 3, 5: 4, 6: 5,
    7: 6, 8: 7, 9: 8
}

def display_board(current_board):
    """Muestra el tablero en la terminal con los números de posición."""
    print("\n")
    print(f"| {current_board[0] if current_board[0] != ' ' else '1'} | {current_board[1] if current_board[1] != ' ' else '2'} | {current_board[2] if current_board[2] != ' ' else '3'} |")
    print("-------------")
    print(f"| {current_board[3] if current_board[3] != ' ' else '4'} | {current_board[4] if current_board[4] != ' ' else '5'} | {current_board[5] if current_board[5] != ' ' else '6'} |")
    print("-------------")
    print(f"| {current_board[6] if current_board[6] != ' ' else '7'} | {current_board[7] if current_board[7] != ' ' else '8'} | {current_board[8] if current_board[8] != ' ' else '9'} |")
    print("\n")

def check_win(board, mark):
    """Comprueba si el jugador con la 'mark' (X o O) ha ganado."""
    
    win_conditions = [
        # Filas
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # Columnas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # Diagonales
        [0, 4, 8], [2, 4, 6]
    ]

    for condition in win_conditions:
        
        if all(board[i] == mark for i in condition):
            return True
    return False

def check_tie(board):
    """Comprueba si el tablero está lleno (empate)."""
    
    return ' ' not in board

def get_player_move(board):
    """Pide al jugador que introduzca su movimiento y lo valida."""
    while True:
        try:
           
            move = input("Elige tu movimiento (1-9): ")
            if not move: 
                continue
            position = int(move)
            
            # 1. Comprueba si la posición está dentro del rango válido
            if position not in POSITION_MAP:
                print("¡Movimiento no válido! Elige un número entre 1 y 9.")
                continue
            
            # 2. Comprueba si el espacio ya está ocupado
            index = POSITION_MAP[position]
            if board[index] == ' ':
                return index # Devuelve el índice de la lista (0-8)
            else:
                print(f"¡El espacio {position} ya está ocupado! Elige otro.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

def get_computer_move(board, computer_mark):
    """Calcula el movimiento de la computadora (simple IA)."""
    
    # Estrategia de la Computadora:
    
    # 1. Comprueba si puede ganar en el siguiente movimiento
    for i in range(9):
        if board[i] == ' ':
            board_copy = list(board)
            board_copy[i] = computer_mark
            if check_win(board_copy, computer_mark):
                return i

    # 2. Comprueba si puede bloquear al jugador
    player_mark = 'X' if computer_mark == 'O' else 'O'
    for i in range(9):
        if board[i] == ' ':
            board_copy = list(board)
            board_copy[i] = player_mark
            if check_win(board_copy, player_mark):
                return i

    # 3. Elige una posición aleatoria de las disponibles
    available_moves = [i for i, mark in enumerate(board) if mark == ' ']
    if available_moves:
        return random.choice(available_moves)
    return -1 # Debería ser un empate si llega aquí

# Función Principal del Juego

def play_game():
    """Ejecuta el ciclo principal del juego Tic Tac Toe."""
    global board
    board = [' '] * 9 # Reinicia el tablero al comienzo
    
    # Asignar símbolos
    player_mark = input("¿Quieres ser 'X' o 'O'? ").upper()
    while player_mark not in ['X', 'O']:
        print("Opción no válida. Por favor, elige 'X' o 'O'.")
        player_mark = input("¿Quieres ser 'X' o 'O'? ").upper()
        
    computer_mark = 'O' if player_mark == 'X' else 'X'
    
    print(f"\n¡Tú eres: {player_mark}! La computadora es: {computer_mark}.")
    
    # Decidir quién empieza (turno aleatorio)
    if random.choice([True, False]):
        current_turn = 'player'
        print("¡Tú empiezas primero!")
    else:
        current_turn = 'computer'
        print("¡La computadora empieza primero!")

    game_on = True
    while game_on:
        display_board(board)
        
        if current_turn == 'player':
            print("Tu turno.")
            move_index = get_player_move(board)
            board[move_index] = player_mark
            
            # Comprobar estado del juego
            if check_win(board, player_mark):
                display_board(board)
                print("¡Felicidades! ¡Has ganado!")
                game_on = False
            elif check_tie(board):
                display_board(board)
                print("¡Es un empate!")
                game_on = False
            else:
                current_turn = 'computer' # Cambiar de turno
                
        elif current_turn == 'computer':
            print("Turno de la computadora...")
            move_index = get_computer_move(board, computer_mark)
            
            # La IA devuelve -1 si no hay movimientos disponibles (empate)
            if move_index != -1: 
                board[move_index] = computer_mark
            
            # Comprobar estado del juego
            if check_win(board, computer_mark):
                display_board(board)
                print(" ¡La computadora ha ganado! ")
                game_on = False
            elif check_tie(board):
                display_board(board)
                print(" ¡Es un empate! ")
                game_on = False
            else:
                current_turn = 'player' # Cambiar de turno

# --- Ejecución del Juego ---

if __name__ == '__main__':
    print("¡Bienvenido a Tic Tac Toe (Tres en Raya) en la Terminal!")
    
    # Loop para jugar varias veces
    while True:
        play_game()
        
        # Preguntar si quiere jugar de nuevo
        play_again = input("¿Quieres jugar otra vez? (s/n): ").lower()
        if play_again != 's':
            print("¡Gracias por jugar! ¡Adiós!")
            break
        print("--- Nuevo Juego ---")