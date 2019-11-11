# noinspection PyUnusedLocal
def fizz_buzz(number):
    if 1 <= number <= 9999:
        if number % 3 == 0 or '3' in str(number):
            return 'fizz buzz' if number % 5 == 0 or '5' in str(number) else 'fizz'
        if number % 5 == 0 or '5' in str(number):
            return 'fizz buzz' if number % 3 == 0 or '3' in str(number) else 'buzz'
    # raise NotImplementedError()



