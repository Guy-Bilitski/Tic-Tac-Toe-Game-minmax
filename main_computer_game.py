from random import choice
from game_board import *

RESUME_GAME = ["y", "yes", "yeah"]
END_GAME = ["no", "n", "exit"]
SHOW_SCORES = ["ShowScores", "showscores", "showScores", "Showscores"]


def main():
    ok_game, ok_games = True, True
    print("\nWelcome to tic tac toe game!\n")
    sleep(1)
    print("We count your score in the game,\n2 points for a win, 1 point for a tie")
    print("You can see your score anytime by typing 'ShowScores'")
    user1_name = input("Please enter your name\n")
    computer_name = "Computer"
    game_board = GameBoard(user1_name, computer_name)
    print("Use these numbers to mark the board:")
    print(game_board.describe_board())
    sleep(1)
    game_board.set_random_starter()
    sleep(1)
    print()
    print(game_board.show_board())
    print("I am randomly choosing who starts")
    sleep(1)
    print(game_board.get_starting_player()["name"], "start!")
    sleep(1)
    now_turn = game_board.get_starting_player()

    while ok_games:
        while ok_game:
            if now_turn["name"] != "Computer":
                position = input(now_turn["name"] + " enter your position")
                while position in SHOW_SCORES:
                    game_score = game_board.get_scores()
                    print(now_turn["name"], "score is: ", game_score[0], "Computer score is: ", game_score[1])
                    sleep(1)
                    position = input(now_turn["name"] + " enter your position")
                if game_board.valid_number(position):
                    if game_board.user_move(now_turn, position):
                        now_turn = game_board.switch_user(now_turn)
                    else:
                        break
                else:
                    continue

            else:
                if game_board.computer_move(now_turn):
                    now_turn = game_board.switch_user(now_turn)
                else:
                    break

        sleep(1)

        not_restart_or_end = True

        while not_restart_or_end:
            play_again = input("Do you want to play again? (y/n)")
            if play_again in SHOW_SCORES:
                game_score = game_board.get_scores()
                print(now_turn["name"], "score is: ", game_score[0], "Computer score is: ", game_score[1])
                sleep(1)
                continue

            if play_again in RESUME_GAME:
                print("Great! let's play again!\nRemember that you can see your score anytime by typing ShowScores")
                game_board.restart_game()
                now_turn = game_board.get_starting_player()
                break

            elif play_again in END_GAME:
                print("ok, bye bye")
                ok_games = False
                break

            else:
                print("I couldn't understand your decision, please try again")


if __name__ == '__main__':
    main()
