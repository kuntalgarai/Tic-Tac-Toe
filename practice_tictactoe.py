def printboard(xState,zState):
    print(f"0 | 1 | 2 ")
    print(f"--|---|---")
    print(f"4 | 5 | 6 ")
    print(f"--|---|---")
    print(f"7 | 8 | 9 ")

if __name__ == "__main__":
    xState = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]
    zState = [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ]
    turn = 1 # 1 for x and 0 for O
    print("Welcome to Tic Tac Toe")
    while(True):
        printboard(xState,zState)
        if(turn == 1):
            print("X's Chance:")
            value= int(input("Please enter a value :"))
            xState[value] = 1
        else:
            print("X's Chance:")
            value= int(input("Please enter a value :"))
            zState[value] = 1
        break
    