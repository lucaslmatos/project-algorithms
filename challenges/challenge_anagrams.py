def is_anagram(first_string, second_string):
    first_string_sorted = custom_sort_quick(first_string.lower())
    second_string_sorted = custom_sort_quick(second_string.lower())
    if len(first_string) == 0 or len(second_string) == 0:
        return (first_string_sorted, second_string_sorted, False)
    if (first_string_sorted) == (second_string_sorted):
        return (first_string_sorted, second_string_sorted, True)
    return (first_string_sorted, second_string_sorted, False)


def custom_sort_quick(input_string):

    char_list = list(input_string)
    length = len(char_list)
    quicksort(char_list, 0, length - 1)
    sorted_string = ''.join(char_list)
    return sorted_string


def partition(list, low_index, high_index):
    pivot = list[high_index]
    i = low_index - 1
    for j in range(low_index, high_index):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[high_index] = list[high_index], list[i + 1]
    return i + 1


def quicksort(list, low_index, high_index):
    if low_index < high_index:
        pi = partition(list, low_index, high_index)
        quicksort(list, low_index, pi - 1)
        quicksort(list, pi + 1, high_index)
