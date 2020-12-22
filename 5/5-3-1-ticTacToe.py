_the_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
              'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
              'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def _print_board (_board):
    print(_board['top-L'] + '|' + _board['top-M'] + '|' + _board['top-R'])
    print('-+-+-')
    print(_board['mid-L'] + '|' + _board['mid-M'] + '|' + _board['mid-R'])
    print('-+-+-')
    print(_board['low-L'] + '|' + _board['low-M'] + '|' + _board['low-R'])

#_print_board(_the_board)

_turn = 'X'
for _i in range(9):
    _print_board(_the_board)
    print(_turn + 'の番です、どこに打つの？')
    _move = input()
    _the_board[_move] = _turn

    if _turn == 'X':
        _turn = 'O'
    else:
        _turn = 'X'

_print_board(_the_board)
