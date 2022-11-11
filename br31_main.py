
import os

from platform   import system as system_name 

def clear_screen(): 
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    os.system(command)

def choice(func):
    def wrapper():
        func()
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
    print(" _            _____ _")
    print("| |__  _ __  |___ // |")
    print("| '_ ⧵| '__|   |_ ⧵| |")
    print("| |_) | |     ___) | |")
    print("|_.__/|_|    |____/|_|")
    print("")
    
@choice
def br31_main():
    now = 0
    printLogo()
    player_mode = input("[1. 게임 플레이] [2. 메인 화면]\n선택지를 입력: ")
    while player_mode != "1" and player_mode != "2":
        clear_screen()
        printLogo()
        print("잘못 입력하셨습니다. 다시 입력해 주세요.")
        player_mode = input("[1. 게임 플레이] [2. 메인 화면]\n선택지를 입력: ")
    else:
        if player_mode == "1":
            clear_screen()
            br31()
            return 0
        elif player_mode == "2":
            return 1

now = 0

def br31():
    global now
    printLogo()
    ch = input("플레이어 수를 입력하세요: ")
    while True:
        try:
            ch = int(ch)
            break
        except BaseException:
            printLogo()
            ch = input("플레이어 수를 숫자로 입력하세요: ")
    while True:
        for i in range(ch):
            printLogo()
            print(f"현재 숫자: {now}")
            num = input(f"플레이어{i + 1}, 1 ~ 3을 입력하세요: ")
            while True:
                try:
                    num = int(num)
                    if not(1 <= num and num <= 3):
                        num = input("1 ~ 3을 입력하세요: ")
                    else:
                        break
                except BaseException:
                    ch = input("숫자로 입력하세요: ")
            now += num
            if now >= 31:
                print(f"진 플레이어: {i + 1}")
                break
        if now >= 31:
            break
    now = 0
        
if __name__ == "__main__":
    br31_main()
