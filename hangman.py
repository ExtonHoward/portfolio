import random

def hangman():
    words = ("python","jumble","difficult","answer","hangman","saxophone","celebrated")
    word = random.choice(words)
    wrong = 0
    stages = ["",
              "__________     ",
              "|          |   ",
              "|          |   ",
              "|          0    ",
              "|         /|\   ",
              "|         / \   ",
              "|               ",
              ]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg).lower()

        if char in remaining_letters:
            cind = remaining_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = '$'

        else:
            wrong += 1
            e = wrong + 1
            print("\n".join(stages[0:e]))

        print((" ".join(board)))

        if "_" not in board:
            print("You win!")
            print("The word was", " ".join(board))
            win = True
            break

        if not win:
            if wrong == len(stages) - 1:
                print("You lose. The answer was {}.".format(word))


hangman()
