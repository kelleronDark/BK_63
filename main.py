def palindrome(word):
    return True if word == word[::-1] else False
print(palindrome(input()))

"""приравнивание строки со строкой, но с обратным ходом"""