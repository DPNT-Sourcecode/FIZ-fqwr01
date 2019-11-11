# noinspection PyUnusedLocal
def fizz_buzz(number):
    if 1 <= number <= 9999:
        if (number % 3 == 0 and number % 5 == 0) or ('3' in str(number) and '5' in str(number)):
            return 'fizz buzz'
        elif number % 3 == 0 or '3' in str(number):
            return 'fizz'
        elif number % 5 == 0 or '5' in str(number):
            return 'buzz'
        else:
            return number
    # raise NotImplementedError()


