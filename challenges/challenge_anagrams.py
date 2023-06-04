def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return first_string, second_string, False

    first_string = first_string.lower()
    second_string = second_string.lower()

    sorted_string1 = quicksort(first_string)
    sorted_string2 = quicksort(second_string)

    is_anagram = sorted_string1 == sorted_string2

    return sorted_string1, sorted_string2, is_anagram


def quicksort(string):
    char_list = list(string)

    quicksort_helper(char_list, 0, len(char_list) - 1)

    sorted_string = ''.join(char_list)

    return sorted_string


def quicksort_helper(char_list, low, high):
    if low < high:
        partition_index = partition(char_list, low, high)

        quicksort_helper(char_list, low, partition_index - 1)
        quicksort_helper(char_list, partition_index + 1, high)


def partition(char_list, low, high):
    pivot = char_list[high]
    i = low - 1

    for j in range(low, high):
        if char_list[j] <= pivot:
            i = i + 1
            char_list[i], char_list[j] = char_list[j], char_list[i]

    char_list[i + 1], char_list[high] = char_list[high], char_list[i + 1]

    return i + 1
