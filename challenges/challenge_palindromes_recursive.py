def is_palindrome_recursive(word, low_index, high_index):
    if high_index == -1:
        return False
    if word[low_index] != word[high_index]:
        return False
    if ((low_index == high_index) or (high_index - low_index) == 1):
        return True
    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
