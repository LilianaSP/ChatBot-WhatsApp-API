

class Game:
    def select_winner(self, player_move, ai_move):
        #For winning we return 1 and for loosing we return -1
        if player_move == 'Rock' and ai_move == 'Scissors':
            return 1
        elif player_move == 'Rock' and ai_move == 'Paper':
            return -1
        elif player_move == 'Scissors' and ai_move == 'Paper':
            return 1
        elif player_move == 'Scissors' and ai_move == 'Rock':
            return -1
        elif player_move == 'Paper' and ai_move == 'Rock':
            return 1
        elif player_move == 'Paper' and ai_move == 'Scissors':
            return -1
        else:
            return 0