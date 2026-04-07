
def sum(a, b, c):
    return a+b+c

def print_board(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|--")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight} ")
    
def checkwin(xState, zState):
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for wins in win:
        if (sum(xState[wins[0]], xState[wins[1]], xState[wins[2]]) == 3):
            print("Hurray! X has won the game.")
            return 1
        if (sum(zState[wins[0]], zState[wins[1]], zState[wins[2]]) == 3):
            print("Hurray! O has won the game.")
            return 0

    return -1

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0,]
    turn = 1 # 1 for player x and 0 for z
    
    print("Welcome to Tic Tac Toe game")
    while(True):
        print_board(xState, zState)
        if(turn == 1):
            print("X's Chance")
            value = int(input("Enter a value: " ))
            xState[value] = 1
        else:
            print("O's Chance")
            value = int(input("Enter a value: " ))
            zState[value] = 1
        
        cwin= checkwin(xState, zState)
        if(cwin != -1):
            print("Game Over")
            break
        turn = 1 - turn

        
    