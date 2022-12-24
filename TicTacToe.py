board=[' ' for x in range (10)]

def insertLetter(letter, pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==' '

def printBoard(board):
    print('   |   |')
    print(' '+board[1]+' | '+board[2]+' | '+board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[4]+' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |')
    
def isWinner(bo, le):
    return (bo[7]==le and bo[8]==le and bo[9]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[1]==le and bo[2]==le and bo[3]==le) or (bo[1]==le and bo[4]==le and bo[7]==le) or (bo[2]==le and bo[5]==le and bo[8]==le) or (bo[3]==le and bo[6]==le and bo[9]==le) or (bo[1]==le and bo[5]==le and bo[9]==le) or (bo[3]==le and bo[5]==le and bo[7]==le)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'x\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move <10 :
                if spaceIsFree(move):
                    run = False
                    insertLetter('x', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please enter number within range!')
        except ValueError:
            print('Please type a number!')

def compMove():
    cornersOpen = []
    edgesOpen = []
    
    possibleMoves=[x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    
    for let in ['o', 'x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    if (board[3]== 'x' and board[7]=='x' and board[5]=='o') or (board[1]=='x' and board[9]=='x' and board[5]=='o') :
        for i in possibleMoves:
            if i in [2,4,6,8]:
                edgesOpen.append(i)
            if len(edgesOpen) > 0:
                move = selectRandom(edgesOpen)
                return move
                break
    if (board[8]== 'x' and board[4]=='x' and board[1]==' ' and board[9]==' ' and board[7]==' ' ):
        move = 7
        return move
    if (board[8]== 'x' and board[6]=='x' and board[7]==' ' and board[9]==' ' and board[3]==' ' ):
        move = 9
        return move
    if (board[2]== 'x' and board[6]=='x' and board[1]==' ' and board[9]==' ' and board[3]==' ' ):
        move = 3
        return move
    if (board[2]== 'x' and board[4]=='x' and board[7]==' ' and board[1]==' ' and board[3]==' ' ):
        move = 1
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    
    return move 

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def playAgain():
    while True :
        playGame=input("Would you like to play another round? (Yes/No) : ")
        if playGame.lower() == "no" :
            print("Okay, bye!")
            return False
        elif playGame.lower() == "yes" :
            return True
        else:
            print("Please enter a (Yes/No) answer.")
        

def main():
    print("Welcome to tic tac toe!")
    printBoard(board)
    while not isBoardFull(board) :
        if not (isWinner(board, 'o')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, o\'s won that time!')
            break
        if not (isWinner(board, 'x')):
            move = compMove()
            if move == 0:
                print('Tie game')
            else:
                insertLetter('o', move)
                print ('Computer placed an \'o\' in position', move , ':')
            compMove()
            printBoard(board)
        else:
            print('x\'s won this time. Good job!')
            break
        if isBoardFull(board):
            print('Tie game!')
            break
another_round=True
while another_round:
    main()
    another_round=playAgain()
    board=[' ' for x in range (10)]
