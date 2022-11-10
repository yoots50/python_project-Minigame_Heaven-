import os
import sys
from tictac_main import tictac_main
from ladder_main import ladder_main
from br31_main import br31_main
from closeNumber_main import closeNumber_main
from omok_main import omok_main
from connect4_main import connect4_main

while True:
    print(" __  __ _       _")
    print("|  ⧵/  (_)_ __ (_) __ _  __ _ _ __ ___   ___")
    print("| |⧵/| | | '_ ⧵| |/ _` |/ _` | '_ ` _ ⧵ / _ ⧵")
    print("| |  | | | | | | | (_| | (_| | | | | | |  __/")
    print("|_|  |_|_|_| |_|_|⧵__, |⧵__,_|_| |_| |_|⧵___|")
    print("                  |___/")
    print(" _   _")
    print("| | | | ___  __ ___   _____ _ __")
    print("| |_| |/ _ ⧵/ _` ⧵ ⧵ / / _ ⧵ '_ ⧵")
    print("|  _  |  __/ (_| |⧵ V /  __/ | | |")
    print("|_| |_|⧵___|⧵__,_| ⧵_/ ⧵___|_| |_|")
    print("----------안녕하세요! 미니게임 천국입니다.----------")
    print("플레이 하실 게임을 골라주세요!")
    game_type = int(input("[1. Tic tac toe] [2. 배스킨 라벤스 31] [3. 가까운 숫자 말하기] [4. 사다리타기] [5. 오목] [6. Connect4] [0. 종료]: "))
    game_type_list = [1, 2, 3, 4, 5, 6, 0]

    while True:
        if game_type not in game_type_list:
            print("올바르게 입력하여 주세요. \n")
            game_type = int(input("[1. Tic tac toe] [2. 배스킨 라벤스 31] [3. 가까운 숫자 말하기] [4. 사다리타기] [5. 오목] [6. Connect4] [0. 종료]: "))
        else:
            break
    match game_type:
        case 1:
            tictac_main()
        case 2:
            br31_main()
        case 3:
            closeNumber_main()
        case 4:
            ladder_main()
        case 5:
            omok_main()
        case 6:
            connect4_main()
        case 0:
            sys.exit()



