def is_anagram(first_string, second_string):
    first_string_sorted = custom_sort(first_string.lower())
    second_string_sorted = custom_sort(second_string.lower())
    if len(first_string) == 0 or len(second_string) == 0:
        return (first_string_sorted, second_string_sorted, False)
    if (first_string_sorted) == (second_string_sorted):
        return (first_string_sorted, second_string_sorted, True)
    return (first_string_sorted, second_string_sorted, False)


def custom_sort(input_string):

    char_list = list(input_string)
    length = len(char_list)
    quicksort(char_list, 0, length - 1)
    sorted_string = ''.join(char_list)
    return sorted_string


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
