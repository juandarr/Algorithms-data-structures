### Bringing it all togheter

## Hangman the game
def hangman(word):
    wrong = 0
    stages = ["",
             "  __________      ",
             "  |        |      ",
             "  |        |      ",
             "  |        0      ",
             "  |       /|\     ",
             "  |       / \     ",
             "  |               ",
             "_oOo_            "
    ]
    for i in stages:
        print(i)
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("\nWelcome to Hangman\n")
    print('Board: '+" ".join(board))

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            indexList = []
            cind = rletters \
                .index(char)
            while cind!=None:
                indexList.append(cind)
                try:
                    cind = cind+rletters[cind+1:].index(char)+1
                except:
                    cind = None
            for i in indexList:
                board[i] = char
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
            .join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
            .join(stages[0: \
            wrong]))
        print("You lose! It was {}."
            .format(word))

with open('wordsHangman.txt','r') as f:
    s=f.read()
    sList=s.split('\n')

for i,word in enumerate(sList):
    sList[i]=word.lower()

import random

hangman(sList[random.randint(0,len(sList)-1)])
