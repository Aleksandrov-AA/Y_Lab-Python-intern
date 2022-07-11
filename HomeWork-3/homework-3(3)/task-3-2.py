import time


if __name__ == '__main__':
    def dfDecorator(callCount = 1, startSleepTime = 2, factor = 3, borderSleepTime = 4):
        def funcDecorator(func):
            def wrapper():
                t = startSleepTime
                print(f'Кол-во запусков = {callCount}')
                print('Начало работы')
                for i in range(1, callCount + 1):
                    time.sleep(t)
                    funcResult = func()
                    if t % 10 == 1 and t % 100 != 11:
                        sec = "секунда"
                    elif t % 10 in [2, 3, 4] and t % 100 not in [12, 13, 14]:
                        sec = "секунды"
                    else:
                        sec = "секунд"
                    print(f'Запуск номер {i}. Ожидание: {t} {sec}. Результат декорируемой функций = {funcResult}')
                    t = t * 2 ** factor if t * 2 ** factor < borderSleepTime else borderSleepTime
                    print('Конец работы')
            return wrapper
        return funcDecorator


    @dfDecorator(callCount = 5, startSleepTime = 2, factor = 2, borderSleepTime = 50)
    def function():
        return 'Функция отработала'
