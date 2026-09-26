import random
import json


class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.level = 1
        self.experience = 0
        self.health = 100
        self.mana = 100

    def show_info(self):
        print("\n=== Информация о персонаже ===")
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Уровень:", self.level)
        print("Опыт:", self.experience)
        print("Здоровье:", self.health)
        print("Мана:", self.mana)

    def level_up(self):
        self.level += 1
        self.experience = 0

        print("\n", self.name, "повысил уровень!")
        print("Новый уровень:", self.level)

    def train(self):
        xp = random.randint(10, 30)
        self.experience += xp

        print("\n", self.name, "тренируется!")
        print("Получено опыта:", xp)
        print("Опыт:", self.experience)

        if self.experience >= 100:
            self.level_up()

    def fight(self, enemy):
        damage = random.randint(10, 20)
        enemy.health -= damage

        mana_spent = random.randint(5, 15)
        self.mana -= mana_spent

        print("\n", self.name, "атакует", enemy.name)
        print(enemy.name, "получил урон:", damage)
        print(enemy.name, "Здоровье:", enemy.health)
        print(self.name, "потратил маны:", mana_spent)
        print(self.name, "Мана:", self.mana)

        if enemy.health <= 0:
            print(enemy.name, "побежден!")
            enemy.health = 100


# Создаём персонажей
characters = [
    Character("Rudeus", 14),
    Character("Eris", 15),
    Character("Roxy", 43)
]

# Создаём врага
hitogami = Character("Man God", 1000)


while True:
    print("\n=== Six-Faced World RPG ===")
    print("1. Создать персонажа")
    print("2. Посмотреть персонажа")
    print("3. Тренироваться")
    print("4. Сражаться")
    print("5. Сохранить игру")
    print("6. Загрузить игру")
    print("0. Выйти")

    choice = input("Выберите действие: ")

    # ВЫХОД
    if choice == "0":
        print("\nИгра завершена.")
        break

    # СОЗДАНИЕ ПЕРСОНАЖА
    elif choice == "1":
        name = input("Введите имя: ")
        age = int(input("Введите возраст: "))

        new_character = Character(name, age)
        characters.append(new_character)

        print("\nПерсонаж создан!")
        new_character.show_info()

    # ПРОСМОТР ПЕРСОНАЖА
    elif choice == "2":
        print("\n=== Персонажи ===")

        for i, character in enumerate(characters, start=1):
            print(i, ".", character.name)

        character_choice = int(input("Ваш выбор: "))

        if 1 <= character_choice <= len(characters):
            characters[character_choice - 1].show_info()
        else:
            print("Такого персонажа нет.")

    # ТРЕНИРОВКА
    elif choice == "3":
        print("\n=== Выберите персонажа ===")

        for i, character in enumerate(characters, start=1):
            print(i, ".", character.name)

        character_choice = int(input("Ваш выбор: "))

        if 1 <= character_choice <= len(characters):
            characters[character_choice - 1].train()
        else:
            print("Такого персонажа нет.")

    # СРАЖЕНИЕ
    elif choice == "4":
        print("\n=== Выберите персонажа ===")

        for i, character in enumerate(characters, start=1):
            print(i, ".", character.name)

        character_choice = int(input("Ваш выбор: "))

        if 1 <= character_choice <= len(characters):
            player = characters[character_choice - 1]

            print("\n=== Выберите противника ===")
            print("99. Man God")

            rival_choice = input("Ваш выбор: ")

            if rival_choice == "99":
                player.fight(hitogami)
            else:
                print("Такого противника нет.")
        else:
            print("Такого персонажа нет.")

    # СОХРАНЕНИЕ
    elif choice == "5":
        data = []

        for character in characters:
            data.append({
                "name": character.name,
                "age": character.age,
                "level": character.level,
                "experience": character.experience,
                "health": character.health,
                "mana": character.mana
            })

        with open("save.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("\nИгра сохранена!")

    # ЗАГРУЗКА
    elif choice == "6":
        try:
            with open("save.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            characters = []

            for character_data in data:
                character = Character(
                    character_data["name"],
                    character_data["age"]
                )

                character.level = character_data["level"]
                character.experience = character_data["experience"]
                character.health = character_data["health"]
                character.mana = character_data["mana"]

                characters.append(character)

            print("\nИгра загружена!")

        except FileNotFoundError:
            print("\nФайл сохранения не найден.")

    else:
        print("\nТакого пункта меню нет.")