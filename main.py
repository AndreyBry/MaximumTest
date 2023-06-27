# посчитать количество каждой из букв в строке

def strcounter(s):
    symbols_counter = {}
    for symbol in s:
        symbols_counter[symbol] = symbols_counter.get(symbol, 0) + 1

    return symbols_counter


for key, value in strcounter('aaaabbbbbuuuudsfsfsdf').items():
    print(f'{key}: {value}')

"""HOMEWORK"""


def palindrome(s):
    """
    Полученная на входе строка переворачивается и сравнивается с исходной,
    если они равны, то возвращается True, иначе - False
    :param s: str
    :return: True or False
    """
    return True if s == s[::-1] else False


print(palindrome('лепсспел'))
print(palindrome('helloworld'))
