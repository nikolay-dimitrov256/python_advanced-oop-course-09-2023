import tkinter as tk
from tkinter import ttk, messagebox

app_config = {
    'board': [[' '] * 3 for _ in range(3)],
    'sign': 'X',
    'X': '',
    'O': ''
}


def won_by_rows(board):
    return any([len(set(row)) == 1 and row[0] != ' ' for row in board])


def won_by_columns(board):
    return any([len(set(row)) == 1 and row[1] != ' ' for row in
                [[board[row_i][col_i] for row_i in range(3)] for col_i in range(3)]])


def won_by_diagonals(board):
    return any((len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != ' ',
                len(set([board[i][3 - (i + 1)] for i in range(3)])) == 1 and board[0][-1] != ' '))


def game_won_check(board):
    return any([won_by_rows(board), won_by_columns(board), won_by_diagonals(board)])


def draw_by_rows(board):
    return all(['X' in row and 'O' in row for row in board])


def draw_by_columns(board):
    return all(['X' in row and 'O' in row for row in
                [[board[row_i][col_i] for row_i in range(3)] for col_i in range(3)]])


def draw_by_diagonals(board):
    primary_diagonal = [board[row][row] for row in range(3)]
    secondary_diagonal = [board[row][3 - (row + 1)] for row in range(3)]
    return (('X' in primary_diagonal and 'O' in primary_diagonal)
            and ('X' in secondary_diagonal and 'O' in secondary_diagonal))


def draw_check(board):
    return all([draw_by_rows(board), draw_by_columns(board), draw_by_diagonals(board)])


def clear_widgets(window):
    for item in window.pack_slaves():
        item.destroy()


def win(window):
    window.destroy()
    messagebox.showinfo(title='Win!', message=f'{app_config[app_config["sign"]]} wins!')


def draw(window):
    window.destroy()
    messagebox.showinfo(title='Draw!', message='Draw!')


def render_board(window):
    entry = ttk.Entry(window, width=30, foreground='green')
    entry.pack()
    entry.insert(0, f'{app_config[app_config["sign"]]}, please mark a square.')
    entry['state'] = 'readonly'

    button_frame = tk.Frame(window)

    for row in range(3):
        for col in range(3):
            ttk.Button(button_frame,
                       command=lambda r=row, c=col: press_button(window, r, c),
                       text=app_config['board'][row][col],
                       width=3).grid(row=row, column=col, padx=5, pady=5)

    button_frame.pack()


def press_button(window, row, col):
    if app_config['board'][row][col] != ' ':
        return None

    app_config['board'][row][col] = app_config['sign']

    if game_won_check(app_config['board']):
        win(window)
        return None

    elif draw_check(app_config['board']):
        draw(window)
        return None

    app_config['sign'] = 'O' if app_config['sign'] == 'X' else 'X'

    clear_widgets(window)

    render_board(window)


def initial_screen(window: tk.Tk):
    ttk.Label(window, text='First player name:', foreground='green').pack()
    first_player = ttk.Entry(window)
    first_player.pack()

    first_player_sign = tk.StringVar(window)
    first_player_sign.set('X')
    ttk.Label(window, text='Player one, please chose a sign:', foreground='green').pack()
    ttk.Radiobutton(window, variable=first_player_sign, value='X', text='X').pack()
    ttk.Radiobutton(window, variable=first_player_sign, value='O', text='O').pack()

    ttk.Label(window, text='Second player name:', foreground='green').pack()
    second_player = ttk.Entry(window)
    second_player.pack()

    ttk.Button(window,
               text='Enter',
               command=lambda: play_game(window, first_player.get(), second_player.get(), first_player_sign)).pack()


def play_game(window: tk.Tk, first_player: str, second_player: str, first_player_sign):
    app_config['sign'] = first_player_sign.get()
    app_config['X'] = first_player if app_config['sign'] == 'X' else second_player
    app_config['O'] = second_player if app_config['sign'] == 'X' else first_player

    clear_widgets(window)

    render_board(window)


root = tk.Tk()
root.title('Tic Tac Toe')
root.geometry('200x200')

initial_screen(root)

root.mainloop()
