import random


def play_game(min_number, max_number, max_attempts, starting_capital):
    capital = starting_capital
    attempts = 0
    random_number = random.randint(min_number, max_number)

    while attempts < max_attempts and capital > 0:
        try:
            print(f"\nУ вас {capital} единиц капитала.")
            bet = int(input(f"Сделайте ставку (целое число от {min_number} до {max_number}): "))
            if bet < min_number or bet > max_number:
                print(f"Ваша ставка должна быть в диапазоне от {min_number} до {max_number}. Попробуйте снова.")
                continue
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        attempts += 1

        if bet == random_number:
            print(f"Поздравляем! Вы угадали число {random_number}. Удваиваете свою ставку!")
            capital += bet
        else:
            print(f"Вы не угадали. Загаданное число было {random_number}.")
            capital -= bet

        if capital <= 0:
            print("У вас закончились деньги! Игра окончена.")
            break

        if attempts < max_attempts:
            random_number = random.randint(min_number, max_number)

    if capital > 0:
        print(f"\nПоздравляем! Игра завершена. У вас {capital} единиц капитала.")
    else:
        print("\nИгра окончена. Вы проиграли все деньги.")
