text = input('Введите строку: ')

char_indexes = [pos for pos, char in enumerate(text) if char == 'h']

start = char_indexes[0]
end = char_indexes[len(char_indexes) - 1] - 1

print('Развернутая последовательность между первым и последним h:', text[end:start:-1])