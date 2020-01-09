from os import system
from time import sleep
from random import randint

# store
products = {}
with open('store.csv') as file:
    file.readline()
    for line in file:
        lst = line.rstrip().split(';')
        products[lst[0]] = int(lst[1])
print(products)

# zarabotki
zarabotki = {}
with open('zarabotki.csv') as file:
    file.readline()
    for line in file:
        work_list = line.rstrip().split(";")
        money = work_list[1]
        if money.isdigit():
            money = int(money)
        else:
            money = money.split(" - ")
            money[0] = int(money[0])
            money[1] = int(money[1])

        things = work_list[2].split(", ")
        if things[0] == '':
            things.pop()

        time = float(work_list[3])

        work_dict = {
            "money": money,
            'things': things,
            'time': time
        }
        zarabotki[work_list[0]] = work_dict


COUNT_OF_PLAYERS = int(input("Сколько бомжей симулировать?: "))
bomji = []

for i in range(COUNT_OF_PLAYERS):
    name = input("Введите имя вашего персонажа: ")
    bomj = {
        "name": name,
        "money": 10,
        "satiety": 5,
        "staff": ["шапка", "штаны"]
    }
    bomji.append(bomj)


while True:
    for player in bomji:
        system('cls')
        print("----= Main menu =-----\n"
              f"День начался для {player['name']}!\n"
              f"Ваши деньги: {player['money']}\n"
              f"Ваши вещи: {player['staff']}\n"
              "1 - магазин\n"
              "2 - на заработки\n"
              "3 - побиться с соседом\n"
              "4 - пропустить ход\n"
              "5 - выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            system('cls')
            print("Магазин:")

            keys = list(products.keys())
            for i in range(len(products)):
                product = keys[i]
                print(f"{i + 1} - {product} ({products[product]} грн)")
            choice = int(input("Ваш выбор: "))

            if 1 <= choice <= len(products):
                product = keys[choice - 1]
                if player['money'] >= products[product]:
                    player['money'] -= products[product]
                    player['staff'].append(product)
                    input("Вы приобрели " + product)

                else:
                    input("Не хватает!")


        elif choice == "2":
            system('cls')
            i = 1
            for work_name in zarabotki:
                money = zarabotki[work_name]['money']
                if type(money) == list:
                    money = f"{money[0]} - {money[1]}"

                string = f"{i} - {work_name} ({money} грн)"
                things = zarabotki[work_name]['things']
                if len(things) != 0:
                    string += f" (нужны {', '.join(things)})"
                print(string)
                i += 1

            choice = int(input("Ваш выбор: "))

            if not (1 <= choice <= len(zarabotki)):
                input("Вы ввели неправильное число!")
                continue


            player_work = list(zarabotki.keys())[choice - 1]  # "работать грузчиком"
            work_staff = zarabotki[player_work]['things']
            player_staff = player['staff']

            result = True
            for thing in work_staff:
                if thing not in player_staff:
                    result = False
                    break

            if result:
                print(f"Идет работа... {player_work}")
                sleep(zarabotki[player_work]['time'])
                money_up = zarabotki[player_work]['money']
                if type(money_up) == list:
                    money_up = randint(money_up[0], money_up[1])

                player['money'] += money_up
                input(f'Работа окончена! Вы заработали {money_up}')


            else:
                input("У вас нехватает вещей :(")




        elif choice == "3":
            pass

        elif choice == "4":
            print("Пропущено")

        elif choice == "5":
            exit()
