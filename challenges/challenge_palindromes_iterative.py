def is_palindrome_iterative(word):
    size = len(word)
    palindrome = True
    if size == 0:
        return False
    for index in range(size):
        if word[index] != word[(size - 1) - index]:
            palindrome = False
            break
    return palindrome
