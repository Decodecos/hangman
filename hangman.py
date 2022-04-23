#
def hangman(word):
    wrong = 0
    stages = ["",
              "______     ",
              "|          ",
              "|     |    ",
              "|     O    ",
              "|    /|\   ",
              "|    / \   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Input a charactor "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        print(" ".join(rletters))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! Answer is {}.".format(word))

hangman("abcdefghijklm")
