def change_field(func):# применения не нашёл, но хотя бы попробовал
    def wrapper(list1, list2):
        print('---------------')
        func(list1, list2)
        print('---------------')
    return wrapper


@change_field
def print_field(list1, list2):
    field = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    for i, e in enumerate(field):
        for j, ee in enumerate(e):
            for k in range(len(list1)):
                if str(list1[k]) in ee:
                    field[i][j] = 'X'
            for k in range(len(list2)):
                if str(list2[k]) in ee:
                    field[i][j] = 'O'

    for row in field:
        print(row)
    return field


def check_win(list_1, list_2, count):
    win_comb = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'], ['1', '5', '9'], ['3', '5', '7']]
    print(list_1, list_2, sep='\n')

    if count % 2 == 1:
        list_ = list_1
        player = 'X'
    else:
        list_ = list_2
        player = 'O'

    if sorted(list_)[:3] in win_comb:
        return f'{player} победил'
    elif len(list_) > 3:
        for i in range(len(win_comb)):
            c = list(set(list_) & set(win_comb[i]))
            if len(c) == 3:
                return f'{player} победил'


def create_players():
    player_x = str(input('X Введите Ваш никнейм: '))
    player_o = str(input('O Введите Ваш никнейм: '))
    print(f'{player_x} играет за X и ходит первым')
    print(f'{player_o} играет за O и ходит вторым')
    return player_x, player_o


def is_correct(value, list1, list2):
    if value.isdigit() and int(value) in range(1, 10) and value not in list1 and value not in list2:
        return value
    else:
        while not (value.isdigit() and int(value) in range(1, 10) and value not in list1 and value not in list2):
            print('Введите что-нибудь другое.')
            value = input()
            continue
        return value


def game():
    create_players()
    print('Игра началась!')
    x_list, o_list = [], []
    counter = 0
    win = False

    while not win:
        print_field(x_list, o_list)
        counter += 1
        if counter % 2 == 1:
            x_move = is_correct(input('Ход X: '), x_list, o_list)
            x_list.append(x_move)
        else:
            o_move = is_correct(input('Ход O: '),x_list ,o_list)
            o_list.append(o_move)
        if counter > 4:
            tmp = check_win(x_list, o_list, counter)
            if tmp:
                print_field(x_list, o_list)
                print(tmp)
                win = True
                break
        if counter == 9:
            print_field(x_list, o_list)
            print("Ничья!")
            break

        continue
    return x_move, o_move, x_list, o_list


while True:
    game()
    print('Напишите "yes", если хотите сыграть ещё раз. Enter - выйти.')
    answer = input()
    if answer == 'yes':
        game()
    else:
        quit()
