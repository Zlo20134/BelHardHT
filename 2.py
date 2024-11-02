def count_char(STR_VAL):
    char_count = {}
    for char in STR_VAL:
        if char.isalpha():  # Проверяем, является ли символ буквой
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

STR_VAL = 'python is the fastest-growing major programming language'
print(count_char(STR_VAL) )
