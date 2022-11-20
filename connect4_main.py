import os

#아래의 출처에서 코드를 수정함
#출처: https://stackoverflow.com/questions/22885780/python-clear-the-screen
from platform   import system as system_name 
def clear_screen(): 
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    os.system(command)
    
def choice(func):
    def wrapper():
        if func():
            clear_screen()
            return 0
        ch = input('[1. 다시 시작] [2. 메인 메뉴로]\n선택지를 입력: ')
        while ch != '1' and ch != '2':
            print('다시 입력하세요.')
            ch = input('[1. 다시 시작] [2. 메인 메뉴로]\n선택지를 입력: ')
        else:
            if ch == '1':
                clear_screen()
                @choice
                def func1():
                    func()
                return func1()
            else:
                clear_screen()
    return wrapper

def printLogo():
    clear_screen()
    print("                                 _   _  _")
    print("  ___ ___  _ __  _ __   ___  ___| |_| || |")
    print(" / __/ _ ⧵| '_ ⧵| '_ ⧵ / _ ⧵/ __| __| || |_")
    print("| (_| (_) | | | | | | |  __/ (__| |_|__   _|")
    print(" ⧵___⧵___/|_| |_|_| |_|⧵___|⧵___|⧵__|  |_|")
    print("")

def printLayout(arr, n, m):
    printLogo()
    print("  ①  ②  ③  ④  ⑤  ⑥  ⑦")
    print("")
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end = "")
        print("")
    print("")

def isFull(arr, n, m):
    fcnt = 0
    for i in range(1, n, 2):
        for j in range(1, m, 2):
            if arr[i][j] == ' ●' or arr[i][j] == ' ○':
                fcnt += 1
    if fcnt == (m + 1) * (n + 1):
        return 1
    return 0

def isLine(arr, i, j):
    cnt = 0
    try:
        for k in range(2, 8, 2):
            if arr[i][j] == arr[i][j + k]:
                cnt += 1
        if cnt == 3:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 8, 2):
            if arr[i][j] == arr[i][j - k]:
                cnt += 1
        if cnt == 3:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 8, 2):
            if arr[i][j] == arr[i + k][j]:
                cnt += 1
        if cnt == 3:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 8, 2):
            if arr[i][j] == arr[i - k][j]:
                cnt += 1
        if cnt == 3:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 8, 2):
            if arr[i][j] == arr[i + k][j + k]:
                cnt += 1
        if cnt == 3:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 8, 2):
            if arr[i][j] == arr[i - k][j - k]:
                cnt += 1
        if cnt == 3:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 8, 2):
            if arr[i][j] == arr[i - k][j + k]:
                cnt += 1
        if cnt == 3:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 8, 2):
            if arr[i][j] == arr[i + k][j - k]:
                cnt += 1
        if cnt == 3:
            return 1
    except IndexError:
        pass
    return 0

def isEnd(arr, n, m):
    for i in range(1, n, 2):
        for j in range(1, m, 2):
            if arr[i][j] == ' ●':
                if isLine(arr, i, j):
                    return 1
            elif arr[i][j] == ' ○':
                if isLine(arr, i, j):
                    return 2
    return 0
    
def clear(arr, n, m):
    for i in range(n):
        if i % 2:
            arr[i][0] = '│'
            arr[i][m - 1] = '│'
        else:
            arr[i][0] = '├'
            arr[i][m - 1] = '┤'
        for j in range(m):
            if i % 2 and not j % 2:
                arr[i][j] = '│'
        for j in range(m):
            if not j % 2:
                arr[0][j] = '┬'
                arr[n - 1][j] = '┴'
            else:
                arr[0][j] = '───'
                arr[n - 1][j] = '───'
                if not i % 2:
                    arr[i][j] = '───'
                else:
                    if i < n - 1 and j < m - 1:
                        arr[i + 1][j + 1] = '┼'
    arr[0][0], arr[0][m - 1], arr[n - 1][0], arr[n - 1][m - 1] = '┌', '┐', '└', '┘'

def connect4():
    n = 2 * 6 + 1
    m = 2 * 7 + 1
    height = [[n - 2] * 2 for i in range(7)]
    arr = [["   "] * m for i in range(n)]
    clear(arr, n, m)
    while True:
        for i in range(0, 2):
            printLayout(arr, n, m)
            p = input(f"플레이어 {i + 1}, 놓을 곳의 위치를 적으세요: ")
            while True:
                try:
                    p = int(p)
                    while p < 1 or p > 7:
                        printLayout(arr, n, m)
                        p = input(f"놓을 곳의 위치를 1 ~ 7의 범위로 적으세요: ")
                        p = int(p)
                    while height[p - 1][i] == -1:
                        printLayout(arr, n, m)
                        p = input(f"꽉 찼습니다. 다른 숫자를 입력하세요: ")
                        p = int(p)
                    break
                except BaseException:
                    printLayout(arr, n, m)
                    p = input(f"놓을 곳의 위치를 숫자로 적으세요: ")
            y = 2 * (p - 1) + 1
            x = height[p - 1][i]
            if i == 0:
                arr[x][y] = ' ●' 
            else:
                arr[x][y] = ' ○'
            height[p - 1][0] -= 2
            height[p - 1][1] -= 2
            if isFull(arr, n, m) and not isEnd(arr, n, m):
                printLayout(arr, n, m)
                print("무승부")
                return 0
            elif isEnd(arr, n, m):
                printLayout(arr, n, m)
                print(f"게임 끝 승자: {isEnd(arr, n, m)}")
                return 0
            else:
                pass
        
@choice
def connect4_main():
    printLogo()
    player_mode = input("[1. 게임 플레이] [2. 메인 화면]\n선택지를 입력: ")
    while player_mode != "1" and player_mode != "2":
        printLogo()
        print("잘못 입력하셨습니다. 다시 입력해 주세요.")
        player_mode = input("[1. 게임 플레이] [2. 메인 화면]\n선택지를 입력: ")
    else:
        if player_mode == "1":
            clear_screen()
            connect4()
            return 0
        elif player_mode == "2":
            return 1

if __name__ == "__main__":
    connect4_main()
    input()

