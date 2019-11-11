# noinspection PyUnusedLocal
def fizz_buzz(number):
    if 1 <= number <= 9999:
        if number > 10 and len(set(str(number))) == 1:
            if number % 2 != 0:
                fake_deluxe = 'fake deluxe'
            if number % 3 == 0 or '3' in str(number):
                return 'fizz buzz deluxe' if number % 5 == 0 or '5' in str(number) else 'fizz deluxe'
            elif number % 5 == 0 or '5' in str(number):
                return 'fizz buzz deluxe' if number % 3 == 0 or '3' in str(number) else 'buzz deluxe'
            else:
                return 'deluxe'
        else:
            if number % 3 == 0 or '3' in str(number):
                return 'fizz buzz' if number % 5 == 0 or '5' in str(number) else 'fizz'
            elif number % 5 == 0 or '5' in str(number):
                return 'fizz buzz' if number % 3 == 0 or '3' in str(number) else 'buzz'
            else:
                return number
    # raise NotImplementedError()
