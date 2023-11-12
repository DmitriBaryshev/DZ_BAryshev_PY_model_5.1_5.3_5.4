def l(string):
    string = string.lower()
    char_count = {}
    for char in string:
        if char.isalnum():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    repeated_chars = [char for char, count in char_count.items() if count > 1]
    return len(repeated_chars)

# Примеры использования
print(l("abcde"))
print(l("aabbcde"))
print(l("aabBcde"))
print(l("indivisibility"))
print(l("Indivisibilities"))
print(l("aA11"))
print(l("ABBA"))