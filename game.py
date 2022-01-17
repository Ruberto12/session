def game():
    from random import randint
    print('Сейчас вы начнете играть в игру *камень-ножницы-бумага*')
    print('если вы хотите использовать камень ножницы или бумагу, то напишите в диалоговое окно: "rock, scissors, paper" соответственно')
    player_sign = None
    while player_sign != 'stop':
        player_sign = input('')
        a = randint(1, 3)
        if a == 1:
            pc_sign = 'rock'
        elif a == 2:
            pc_sign = 'scissors'
        else:
            pc_sign = 'paper'
        if pc_sign == player_sign:
            print('У компьютера тоже', pc_sign, 'НИЧЬЯ')
        elif pc_sign == 'rock' and player_sign == 'scissors':
            print('У компьютера', pc_sign, 'ПОРАЖЕНИЕ')
        elif pc_sign == 'paper' and player_sign == 'scissors':
            print('У компьютера', pc_sign, 'ПОБЕДА')
        elif pc_sign == 'scissors' and player_sign == 'rock':
            print('У компьютера', pc_sign, 'ПОБЕДА')
        elif pc_sign == 'rock' and player_sign == 'paper':
            print('У компьютера', pc_sign, 'ПОБЕДА')
        elif pc_sign == 'scissors' and player_sign == 'paper':
            print('У компьютера', pc_sign, 'ПОРАЖЕНИЕ')
        elif pc_sign == 'paper' and player_sign == 'rock':
            print('У компьютера', pc_sign, 'ПОРАЖЕНИЕ')
        else:
            print('Вы завершили игру или ввели неверное значение')
    print('ИГРА ОКОНЧЕНА')
game()