# посчитать количество каждой из букв в строке

def strcounter(s):
    symbols_counter = {}
    for symbol in s:
        symbols_counter[symbol] = symbols_counter.get(symbol, 0) + 1

    return symbols_counter


for key, value in strcounter('aaaabbbbbuuuudsfsfsdf').items():
    print(f'{key}: {value}')
