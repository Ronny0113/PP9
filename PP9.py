import logging as log
import random
log.basicConfig(filename="game.log", level=log.INFO, format='%(asctime)s %(levelname)s: %(message)s')
txt1 = "Введите максимальное число N: "
txt2 = "Введите количество попыток: "
txt3 = "Введите вашу догадку: "


def input_check(txt):  # функция-обработчик ошибок ввода
    while True:
        try:
            a = int(input(txt))
            if a <= 0:
                print("Введите натуральное число!")
                log.error("Incorrect number")
            else:
                log.info(f"User input {a}")
                return a
        except ValueError:
            print("Некоректное значение, попробуйте ещё раз")
            log.error("ValuerError")


log.info("--Program started--")
n = input_check(txt1)
k = input_check(txt2)
log.info(f"{n} numbers, {k} attempts")
answer = random.randint(1, n)  # программа рандомно выбирает ответ из выбранного диапазона
log.info(f"Answer is {answer}")

for i in range(k):  # сама игра
    attempt = input_check(txt3)
    log.info(f"Try {i + 1}: {attempt}")
    if attempt == answer:
        if i == 1:
            print("Вы победили со 2-ой попытки!")
            log.info("Victory")
            break
        else:
            print(f"Вы победили с {i + 1}-ой попытки!")
            log.info("Victory")
            break
    elif attempt < answer:
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")
    if i == k - 1:
        print("Попытки закончились, вы проиграли :(")
        log.info("Defeat, out of attempts")

print("Спасибо за игру")
log.info("--Program finished--")
