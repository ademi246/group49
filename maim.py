from decouple import config
import logic

def maim():

    min_number = config( 'min_number', cast=int)
    max_number = config('max_number', cast=int)
    max_attempts = config( 'max_attempts', cast=int)
    starting_capital = config('starting_capital', cast=int)



    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Диапазон чисел: от {min_number} до {max_number}")
    print(f"Количество попыток: {max_attempts}")
    print(f"Ваш начальный капитал: {starting_capital}")

    logic.play_game(min_number, max_number, max_attempts, starting_capital )
maim()

