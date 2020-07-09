from game_board import *
from functions import *

RESUME_GAME = ["y", "yes", "yeah"]
END_GAME = ["no", "n", "exit"]
SHOW_SCORES = ["ShowScores", "showscores", "showScores", "Showscores"]


def main():
    print("\nWelcome to tic tac toe game!\n")
    print("We count your score in the game,\n2 points for a win, 1 point for a tie")
    print("You can see your score anytime by typing 'ShowScores'")
    sleep(1.5)
    user1_name = input("\nUser1 please enter your name (starts in first game, marks 'x')")
    user2_name = input("\nUser2 please enter your name")
    game_board = GameBoard(user1_name, user2_name)
    ok_games = True
    ok = True
    now_turn = game_board.get_starting_player()
    print("Use these numbers to mark the board:")
    print(game_board.describe_board())
    sleep(1)

    while ok_games:
        print(game_board.show_board())
        while ok:
            position = input(now_turn["name"] + " enter your position")
            while position in SHOW_SCORES:
                game_score = game_board.get_scores()
                print(game_board.get_user1()["name"], "score is: ", game_score[0],
                      game_board.get_user2()["name"], "score is: ", game_score[1])
                sleep(1)
                position = input(now_turn["name"] + " enter your position")
            if game_board.valid_number(position):
                if game_board.user_move(now_turn, position):
                    now_turn = game_board.switch_user(now_turn)
                    continue
                else:
                    break
            else:
                continue

        sleep(1)
        not_restart_or_end = True

        while not_restart_or_end:
            play_again = input("Do you want to play again? (y/n)")
            if play_again in SHOW_SCORES:
                game_score = game_board.get_scores()
                print(game_board.get_user1()["name"], "score is: ", game_score[0],
                      game_board.get_user2()["name"], "score is: ", game_score[1])
                sleep(1)
                continue

            if play_again in RESUME_GAME:
                print("Great! let's play again!\nRemember that you can see your score anytime by typing ShowScores")
                game_board.clean_board()
                starter = input("Who wants to start now?")

                while starter != game_board.get_user1()["name"] and starter != game_board.get_user2()["name"]:
                    print("Sorry, the users names are: ",
                          game_board.get_user1()["name"], ",", game_board.get_user2()["name"])
                    sleep(1)
                    starter = input("Who wants to start now?")

                if starter != game_board.get_starting_player()["name"]:
                    game_board.set_starter(game_board.switch_user(game_board.get_starting_player()))

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

