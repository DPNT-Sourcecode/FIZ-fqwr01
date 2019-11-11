# noinspection PyUnusedLocal
def fizz_buzz(number):
    if 1 <= number <= 9999:
        output = ''
        three_multiple = number % 3 == 0
        five_multipe = number % 5 == 0
        if (three_multiple and '3' in str(number)) or (five_multipe and '5' in str(number)):
            if three_multiple or '3' in str(number):
                output = 'fizz buzz deluxe' if five_multipe or '5' in str(number) else 'fizz deluxe'
            elif five_multipe or '5' in str(number):
                output = 'fizz buzz deluxe' if three_multiple or '3' in str(number) else 'buzz deluxe'
            else:
                output = 'deluxe'
        else:
            if three_multiple or '3' in str(number):
                output = 'fizz buzz' if five_multipe or '5' in str(number) else 'fizz'
            elif five_multipe or '5' in str(number):
                output = 'fizz buzz' if three_multiple or '3' in str(number) else 'buzz'
            else:
                output = number
    return output.replace('deluxe','fake deluxe') if number % 2 != 0 and isinstance(output,str) else output




