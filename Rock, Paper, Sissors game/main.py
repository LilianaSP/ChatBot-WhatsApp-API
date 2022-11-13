from time import time
import os
import time
import sys
from ai import AI
from game import Game


os.system("clear")  # For clearing the screen

moves = ['Rock', 'Paper', 'Scissors']

ai = AI()
game = Game()


def make_move():

    selected_move = input("Enter your move (Rock, Paper, Scissors): ").title()
    if selected_move not in moves:
        print("Invalid move")
        time.sleep(0.3)
        return make_move()
    return selected_move


def gameloop():
    # We create the counter for the number of games played and games won
    games_played = 0
    games_won = 0
    games_lost = 0
    games_tied = 0

    player_move = make_move()
    print(f"Your move is: {player_move}")
    ai_move = ai.make_move(moves)
    print(f"AI move is: {ai_move}")

    winner = game.select_winner(player_move=player_move, ai_move=ai_move)

    # Each time the loop executes we add 1 to the games played counter
    games_played = games_played + 1
    if winner == 1:
        should_play = input(
            "You won!\nWould you like to play again?\n(yes or no): ")
        games_won = games_won + 1
    elif winner == -1:
        should_play = input(
            "You lost!\nWould you like to play again?\n(yes or no): ")
        games_lost = games_lost + 1
    else:
        should_play = input(
            "Tie!\nWould you like to play again?\n(yes or no): ")
        games_tied = games_tied + 1

    if should_play != "yes":
        print("Thanks for playing!\n")
        time.sleep(0.3)
        print(f"Games played: {games_played}")
        print(f"Games won: {games_won}")
        print(f"Games lost: {games_lost}")
        print(f"Games tied: {games_tied}")
        sys.exit()
        # we clear the screen
    os.system("clear")
    gameloop()


gameloop()
