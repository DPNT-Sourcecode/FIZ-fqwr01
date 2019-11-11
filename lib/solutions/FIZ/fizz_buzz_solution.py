# noinspection PyUnusedLocal
def fizz_buzz(number):
    if 1 <= number <= 9999:
        output = ''
        if (number % 3 == 0 and '3' in str(number)) or (number % 5 == 0 and '5' in str(number)):
            if number % 3 == 0 or '3' in str(number):
                output = 'fizz buzz deluxe' if number % 5 == 0 or '5' in str(number) else 'fizz deluxe'
            elif number % 5 == 0 or '5' in str(number):
                output = 'fizz buzz deluxe' if number % 3 == 0 or '3' in str(number) else 'buzz deluxe'
            else:
                output = 'deluxe'
        else:
            if number % 3 == 0 or '3' in str(number):
                output = 'fizz buzz' if number % 5 == 0 or '5' in str(number) else 'fizz'
            elif number % 5 == 0 or '5' in str(number):
                output = 'fizz buzz' if number % 3 == 0 or '3' in str(number) else 'buzz'
            else:
                output = number
    return output.replace('deluxe','fake deluxe') if number % 2 != 0 and isinstance(output,str) else output



