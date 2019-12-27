from os import system

# store
products = {}
with open('store.csv') as file:
    file.readline()
    for line in file:
        lst = line.rstrip().split(';')
        products[lst[0]] = int(lst[1])

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

        work_dict = {
            "money": money,
            'things': things
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
              "1 - магазин\n"
              "2 - на заработки\n"
              "3 - побиться с соседом\n"
              "4 - пропустить ход\n"
              "5 - выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            pass

        elif choice == "2":
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


        elif choice == "3":
            pass

        elif choice == "4":
            pass

        elif choice == "5":
            pass
