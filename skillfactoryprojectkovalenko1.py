def print_board(board):
    # Печатаем верхнюю шапку с номерами столбцов
    print("  0 1 2")
    for i, row in enumerate(board):
        # Печатаем номер строки и содержимое через пробел
        print(f"{i} {' '.join(row)}")

def check_winner(board):
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '-':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '-':
            return board[0][i]
    
    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return board[0][2]
    
    return None

def is_full(board):
    return all(cell != '-' for row in board for cell in row)

def main():
    # Создаем пустое поле
    board = [['-' for _ in range(3)] for _ in range(3)]
    current_player = 'x'
    
    print("--- Крестики-нолики 3x3 ---")
    
    while True:
        print_board(board)
        
        try:
            print(f"\nХод игрока '{current_player}'")
            row = int(input("Введите номер строки (0-2): "))
            col = int(input("Введите номер столбца (0-2): "))
            
            if board[row][col] != '-':
                print("Эта клетка уже занята! Попробуй еще раз.")
                continue
        except (ValueError, IndexError):
            print("Ошибка! Введи число от 0 до 2.")
            continue
            
        board[row][col] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"\nПоздравляем! Победил игрок '{winner}'!")
            break
            
        if is_full(board):
            print_board(board)
            print("\nНичья!")
            break
            
        # Меняем игрока
        current_player = 'o' if current_player == 'x' else 'x'

if name == "main":
    main()