
import os
import random

arr = [["*","*","*"],
       ["*","*","*"],
       ["*","*","*"]]

def printLogo():
    os.system('cls')
    print(" _   _      _             _ ")
    print("| |_(_) ___| |_ ____  ___| |_ ____   ___ ")
    print("| __| |/ __| __/ _  |/ __| __/  _ ＼/ _ ＼")
    print("| |_| | (__| || (_| | (__| | | (_) || __/")
    print("＼__|_|＼__|＼_＼___|＼__|＼_＼____/＼___|")
    print("")

def printLayout():
    printLogo()
    print("+---+---+---+")
    for i in range(0, 3):
        print("|", end = '')
        for j in range(0, 3):
            print(f" {arr[i][j]} ", end = '|')
        print("\n+---+---+---+")
    print("")

def isLine():
    global cnt1, cnt2
    if cnt1 == 3:
        return 1
    elif cnt2 == 3:
        return 2
    else:
        cnt1 = 0
        cnt2 = 0

def isEnd():
    global cnt1, cnt2
    cnt1 = 0
    cnt2 = 0
    for i in range(0, 3):
        if arr[i][i] == 1:
            cnt1 += 1
        elif arr[i][i] == 2:
            cnt2 += 1
        else:
            pass
    if isLine():
        return isLine()
    for i in range(0, 3):
        if arr[i][2 - i] == 1:
            cnt1 += 1
        elif arr[i][2 - i] == 2:
            cnt2 += 1
        else:
            pass
    if isLine():
        return isLine()
    for i in range(0, 3):
        for j in range(0, 3):
            if arr[i][j] == 1:
                cnt1 += 1
            elif arr[i][j] == 2:
                cnt2 += 1
            else:
                pass
        if isLine():
            return isLine()
    for i in range(0, 3):
        for j in range(0, 3):
            if arr[j][i] == 1:
                cnt1 += 1
            elif arr[j][i] == 2:
                cnt2 += 1
            else:
                pass
        if isLine():
            return isLine()
    return 0

def isFull():
    fcnt = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if arr[i][j] != "*":
                fcnt += 1
    if fcnt == 9:
        return 1
    return 0

def computer():
    x = random.randrange(0, 3)
    y = random.randrange(0, 3)
    while (arr[x][y] == 1 or arr[x][y] == 2) :
        x = random.randrange(0, 3)
        y = random.randrange(0, 3)
        if isFull():
            return 0
    arr[x][y] = 2

def clear():
    for i in range(0, 3):
        for j in range(0, 3):
            arr[i][j] = "*"

def tictac_1p():
    while True:
        printLayout()
        p = input("놓을 곳의 좌표를 i j형식으로 적으세요: ")
        while True:
            try:
                x = int(p.split(" ")[0]) - 1
                y = int(p.split(" ")[1]) - 1
                while (arr[x][y] == 1 or arr[x][y] == 2):
                    p = input("이미 1 또는 2가 있습니다. 놓을 곳의 좌표를 i j형식으로 적으세요: ")
                    x = int(p.split(" ")[0]) - 1
                    y = int(p.split(" ")[1]) - 1
                break 
            except BaseException:
                p = input("오류: 숫자가 아니거나 범위를 벗어남, 다시 적어주세요: ")
        x = int(p.split(" ")[0]) - 1
        y = int(p.split(" ")[1]) - 1
        arr[x][y] = 1
        computer()
        if isFull() and not isEnd():
            printLayout()
            print("무승부")
            clear()
            return 0
        elif isEnd():
            printLayout()
            print(f"게임 끝 승자: {isEnd()}")
            clear()
            return 0
        else:
            pass

def tictac_2p():
    while True:
        for i in range(0, 2):
            printLayout()
            p = input(f"플레이어 {i + 1}, 놓을 곳의 좌표를 i j형식으로 적으세요: ")
            while True:
                try:
                    x = int(p.split(" ")[0]) - 1
                    y = int(p.split(" ")[1]) - 1
                    while (arr[x][y] == 1 or arr[x][y] == 2):
                        p = input("이미 1 또는 2가 있습니다. 놓을 곳의 좌표를 i j형식으로 적으세요: ")
                        x = int(p.split(" ")[0]) - 1
                        y = int(p.split(" ")[1]) - 1
                    break 
                except BaseException:
                    p = input("오류: 숫자가 아니거나 범위를 벗어남, 다시 적어주세요: ")       
            x = int(p.split(" ")[0]) - 1
            y = int(p.split(" ")[1]) - 1
            arr[x][y] = i + 1
            if isFull() and not isEnd():
                printLayout()
                print("무승부")
                clear()
                return 0
            elif isEnd():
                printLayout()
                print(f"게임 끝 승자: {isEnd()}")
                clear()
                return 0
            else:
                pass

def choice(func):
    def wrapper():
        if func():
            os.system('cls')
            return 0
        ch = input('[1. 다시 시작] [2. 메인 메뉴로]\n선택지를 입력: ')
        while ch != '1' and ch != '2':
            print('다시 입력하세요.')
            ch = input('[1. 다시 시작] [2. 메인 메뉴로]\n선택지를 입력: ')
        else:
            if ch == '1':
                os.system('cls')
                @choice
                def func1():
                    func()
                return func1()
            else:
                os.system('cls')
    return wrapper

@choice
def tictac_main():
    while(True):
        printLogo()
        player_mode = input("[1. 싱글플레이] [2. 멀티 플레이] [3. 메인 화면]\n선택지를 입력: ")
        while player_mode != "1" and player_mode != "2" and player_mode != "3":
            printLogo()
            print("잘못 입력하셨습니다. 다시 입력해 주세요.")
            player_mode = input("[1. 싱글플레이] [2. 멀티 플레이] [3. 메인 화면]\n선택지를 입력: ")
        else:
            if player_mode == "1":
                print("[싱글 플레이]")
                tictac_1p()
                break
            elif player_mode == "2":
                print("[멀티 플레이]")
                tictac_2p()
                break
            elif player_mode == "3":
                return 1
            

if __name__ == "__main__":
    tictac_main()
