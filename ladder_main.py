
import random
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


def printLayout(n, arr):
    for i in range(n):
        print(f"{i + 1}", end = ' ')
    print("")
    for i in range(10):
        for j in range(n * 2):
            print(arr[i][j], end = '')
        print("")
    for i in range(n):
        print(f"{i + 1}", end = ' ')
    print("")

def printLogo():
    clear_screen()
    print(" _           _     _")
    print("| | __ _  __| | __| | ___ _ __")
    print("| |/ _` |/ _` |/ _` |/ _ ⧵ '__|")
    print("| | (_| | (_| | (_| |  __/ |")
    print("|_|⧵__,_|⧵__,_|⧵__,_|⧵___|_|")
    print("")

@choice
def ladder_main():
    printLogo()
    player_mode = input("[1. 게임 플레이] [2. 메인 화면]\n선택지를 입력: ")
    while player_mode != "1" and player_mode != "2":
        printLogo()
        print("잘못 입력하셨습니다. 다시 입력해 주세요.")
        player_mode = input("[1. 게임 플레이] [2. 메인 화면]\n선택지를 입력: ")
    else:
        if player_mode == "1":
            clear_screen()
            ladder()
            return 0
        elif player_mode == "2":
            return 1
            
def ladder():
    printLogo()
    n = input("사람의 수를 적어주세요: ")
    while True:
        try:
            n = int(n)
            break
        except BaseException:
            printLogo()
            n = input("숫자로 입력하세요.")
    printLogo()
    arr = [[0] * n * 2 for i in range(10)] #arr[10][2 * n]
    for i in range(10):
        for j in range(n * 2):
            if j % 2:
                arr[i][j] = " "
            else:
                arr[i][j] = "|"
    for i in range(1, 2 * n - 1, 2):
        for j in range(2):
            y = random.randrange(0, 10)
            while True:
                if i == 1:
                    if arr[y][i + 2] == '-':
                        y = random.randrange(0, 10)
                    else:
                        break
                elif i == 2 * n - 2:
                    if arr[y][i - 2] == '-':
                        y = random.randrange(0, 10)
                    else:
                        break
                else:
                    if arr[y][i + 2] == '-':
                        y = random.randrange(0, 10)
                    elif arr[y][i - 2] == '-':
                        y = random.randrange(0, 10)
                    else:
                        break
            arr[y][i] = "-"
    printLayout(n, arr)
    temp = []
    done = False
    while not done:
        ch = input("모든 결과를 한번에 보시려면 0, 스킵하시려면 -1, 그렇지 않으면 원하는 결과의 숫자를 입력하세요: ")
        while ch not in [str(i - 1) for i in range(int(n + 2))]:
            print("다시 입력하세요.")
            ch = input("모든 결과를 한번에 보시려면 0, 스킵하시려면 -1, 그렇지 않으면 원하는 결과의 숫자를 입력하세요: ")
        if ch == "0":
            for i in range(0, 2 * n, 2):
                x = i
                y = 0
                while True:
                    if x == 0:
                        if arr[y + 1][x + 1] == '-':
                            x += 2
                        y += 1
                    elif x == 2 * n - 2:
                        if arr[y + 1][x - 1] == '-':
                            x -= 2
                        y += 1
                    else:
                        if arr[y + 1][x - 1] == '-':
                            x -= 2
                        elif arr[y + 1][x + 1] == '-':
                            x += 2
                        y += 1
                    if y == 9:
                        print(f"{i // 2 + 1}의 목적지: {x // 2 + 1}")
                        break
            done = True
        elif ch == "-1":
            return 0
        else:
            x = (int(ch) - 1) * 2
            y = 0
            while True:
                if x == 0:
                    if arr[y + 1][x + 1] == '-':
                        x += 2
                    y += 1
                elif x == 2 * n - 2:
                    if arr[y + 1][x - 1] == '-':
                        x -= 2
                    y += 1
                else:
                    if arr[y + 1][x - 1] == '-':
                        x -= 2
                    elif arr[y + 1][x + 1] == '-':
                        x += 2
                    y += 1
                if y == 9:
                    print(f"{int(ch)}의 목적지: {x // 2 + 1}")
                    break
            temp.append(ch)
            temp.sort()
            if temp == [str(i + 1) for i in range(int(n))]:
                done = True
            
if __name__ == "__main__":
    ladder_main()
