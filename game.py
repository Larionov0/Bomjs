from os import system

# store
products = {}
with open('store.csv') as file:
    file.readline()
    for line in file:
        lst = line.rstrip().split(';')
        products[lst[0]] = int(lst[1])


with open('zarabotki.csv') as file:
    pass


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
            print("1 - собирать бутылки (3 - 15 грн)\n"
                  "2 - работать грузчиком (30 грн) (нужны тапки)\n"
                  "3 - работать менеджером (100 грн) (нужен телефон)")

        elif choice == "3":
            pass

        elif choice == "4":
            pass

        elif choice == "5":
            pass
