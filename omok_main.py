import os

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

def printLogo():
    os.system('cls')
    print("                       _")
    print("  ___  _ __ ___   ___ | | __")
    print(" / _ ⧵| '_ ` _ ⧵ / _ ⧵| |/ /")
    print("| (_) | | | | | | (_) |   <")
    print(" ⧵___/|_| |_| |_|⧵___/|_|⧵_⧵")
    print("")
    
def printLayout(arr, n, m):
    printLogo()
    print("   ①  ②  ③  ④  ⑤  ⑥  ⑦  ⑧  ⑨  ⑩  ⑪")
    print("")
    for i in range(n):
        if i == 0:
            print("①", end = ' ')
        elif i == 2:
            print("②", end = ' ')
        elif i == 4:
            print("③", end = ' ')
        elif i == 6:
            print("④", end = ' ')
        elif i == 8:
            print("⑤", end = ' ')
        elif i == 10:
            print("⑥", end = ' ')
        elif i == 12:
            print("⑦", end = ' ')
        elif i == 14:
            print("⑧", end = ' ')
        elif i == 16:
            print("⑨", end = ' ')
        elif i == 18:
            print("⑩", end = ' ')
        elif i == 20:
            print("⑪", end = ' ')
        else:
            print("  ", end = ' ')
        for j in range(m):
            print(arr[i][j], end = "")
        print("")
    print("")

def isFull(arr, n, m):
    fcnt = 0
    for i in range(0, n, 2):
        for j in range(0, m, 2):
            if arr[i][j] == '●' or arr[i][j] == '○':
                fcnt += 1
    if fcnt == (m + 1) * (n + 1):
        return 1
    return 0

def isEnd(arr, n, m):
    for i in range(0, n, 2):
        for j in range(0, m, 2):
            if arr[i][j] == '●':
                if isLine(arr, i, j):
                    return 1
            elif arr[i][j] == '○':
                if isLine(arr, i, j):
                    return 2
    return 0

def isLine(arr, i, j):
    cnt = 0
    try:
        for k in range(2, 10, 2):
            if arr[i][j] == arr[i][j + k]:
                cnt += 1
        if cnt == 4:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 10, 2):
            if arr[i][j] == arr[i][j - k]:
                cnt += 1
        if cnt == 4:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 10, 2):
            if arr[i][j] == arr[i + k][j]:
                cnt += 1
        if cnt == 4:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 10, 2):
            if arr[i][j] == arr[i - k][j]:
                cnt += 1
        if cnt == 4:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 10, 2):
            if arr[i][j] == arr[i + k][j + k]:
                cnt += 1
        if cnt == 4:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 10, 2):
            if arr[i][j] == arr[i - k][j - k]:
                cnt += 1
        if cnt == 4:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 10, 2):
            if arr[i][j] == arr[i - k][j + k]:
                cnt += 1
        if cnt == 4:
            return 1
    except IndexError:
        pass
    cnt = 0
    try:
        for k in range(2, 10, 2):
            if arr[i][j] == arr[i + k][j - k]:
                cnt += 1
        if cnt == 4:
            return 1
    except IndexError:
        pass
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

def omok():
    #arr[n][m]
    n = 10 #세로
    m = 10 #가로
    m = 2 * m + 1
    n = 2 * n + 1
    arr = [["   "] * m for i in range(n)]
    clear(arr, n, m)
    while True:
        for i in range(0, 2):
            printLayout(arr, n, m)
            p = input(f"플레이어 {i + 1}, 놓을 곳의 좌표를 i j형식으로 적으세요: ")
            while True:
                try:
                    x = 2 * (int(p.split(" ")[0]) - 1)
                    y = 2 * (int(p.split(" ")[1]) - 1)
                    while (arr[x][y] == '●' or arr[x][y] == '○'):
                        printLayout(arr, n, m)
                        p = input("이미 1 또는 2가 있습니다. 놓을 곳의 좌표를 i j형식으로 적으세요: ")
                        x = 2 * (int(p.split(" ")[0]) - 1)
                        y = 2 * (int(p.split(" ")[1]) - 1)
                    break 
                except BaseException:
                    printLayout(arr, n, m)
                    p = input("오류: 숫자가 아니거나 범위를 벗어남, 다시 적어주세요: ")       
            x = 2 * (int(p.split(" ")[0]) - 1)
            y = 2 * (int(p.split(" ")[1]) - 1)
            if i == 0:
                arr[x][y] = '●'
                if y < 20:
                    arr[x][y + 1] = '──'
                if y > 1:
                    arr[x][y - 1] = '── '
                if arr[x][y - 2] == '●' or arr[x][y - 2] == '○':
                    arr[x][y - 1] = '─ '
            else:
                arr[x][y] = '○'
                if y < 20:
                    arr[x][y + 1] = '──'
                if y > 1:
                    arr[x][y - 1] = '── '
                if arr[x][y - 2] == '●' or arr[x][y - 2] == '○':
                    arr[x][y - 1] = '─ '
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
def omok_main():
    printLogo()
    player_mode = input("[1. 게임 플레이] [2. 메인 화면]\n선택지를 입력: ")
    while player_mode != "1" and player_mode != "2":
        printLogo()
        print("잘못 입력하셨습니다. 다시 입력해 주세요.")
        player_mode = input("[1. 게임 플레이] [2. 메인 화면]\n선택지를 입력: ")
    else:
        if player_mode == "1":
            os.system('cls')
            omok()
            return 0
        elif player_mode == "2":
            return 1
if __name__ == "__main__":
    #print("격자무늬 만드는 함수입니다.")
    #m = 10#int(input("가로 크기 입력: "))
    #n = 10#int(input("세로 크기 입력: "))
    #omok(m, n)
    omok_main()
    input()
    
