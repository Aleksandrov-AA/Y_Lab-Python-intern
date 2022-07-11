if __name__ == '__main__':

    dictionary = dict()

    def funcDecorator(func):
        def wrapper(number):
            if not dictionary.get(number):
                dictionary[number] = func(number)
            return dictionary[number]
        return wrapper

    @funcDecorator
    def multiplier(number: int):
        return number * 2