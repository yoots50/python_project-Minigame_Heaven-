import random
import os

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
    print("  ____ _                                        _")
    print(" / ___| | ___  ___  ___   _ __  _   _ _ __ ___ | |__   ___ _ __")
    print("| |   | |/ _ ⧵/ __|/ _ ⧵ | '_ ⧵| | | | '_ ` _ ⧵| '_ ⧵ / _ ⧵ '__|")
    print("| |___| | (_) ⧵__ ⧵  __/ | | | | |_| | | | | | | |_) |  __/ |")
    print(" ⧵____|_|⧵___/|___/⧵___| |_| |_|⧵__,_|_| |_| |_|_.__/ ⧵___|_|")
    print("")

@choice
def closeNumber_main():
    printLogo()
    close_number_mode = int(input("[1. 싱글플레이] [2. 멀티플레이] [3. 게임 설명] [4. 메인 화면]: "))
    match close_number_mode:
        case 1:
            printLogo()
            computer_number = random.randint(1, 101)
            close_number_p1_number = int(input("1 - 100 사이의 숫자를 입력하세요: "))
            close_number_computer_number = random.randint(1, 101)

            compare_number1 = abs(computer_number - close_number_p1_number)
            compare_number2 = abs(computer_number - close_number_computer_number)

            if compare_number1 > compare_number2:
                print("패배하였습니다")
            elif compare_number1 == compare_number2:
                print("비겼습니다.")
            else:
                print("승리 하였습니다!")
            print("랜덤 숫자는 %d 였고, 컴퓨터의 숫자는 %d 이였습니다." % (computer_number, close_number_computer_number))

        case 2:
            printLogo()
            computer_number = random.randint(1, 101)
            close_number_p1_number = int(input("1 - 100 사이의 숫자를 입력하세요: Player1: "))
            printLogo()
            close_number_p2_number = int(input("1 - 100 사이의 숫자를 입력하세요: Player2: "))

            compare_number1 = abs(computer_number - close_number_p1_number)
            compare_number2 = abs(computer_number - close_number_p2_number)

            if compare_number1 > compare_number2:
                print("Player 2가 승리하였습니다!")
            elif compare_number1 == compare_number2:
                print("비겼습니다.")
            else:
                print("Player 1이 승리하였습니다!")
            print("랜덤 숫자는 %d였습니다." % computer_number)

        case 3:
            print("컴퓨터가 1 - 100 사이의 랜덤 숫자를 생성하고, 플레이어들이 숫자를 입력하여 컴퓨터가 생성한 숫자랑 더 가깝게 입력한 플레이어가 승리를 합니다.  ")
            input("뒤로 돌아가려면 아무 키나 입력: ")
            closeNumber_main()
            
        case 4:
            return 1

        case _:
            printLogo()
            print("다시 입력해주세요.")
            close_number_mode = int(input("[1. 싱글플레이] [2. 멀티플레이] [3. 게임 설명] [4. 메인 화면]: "))
        

if __name__ == "__main__":
    closeNumber_main()
