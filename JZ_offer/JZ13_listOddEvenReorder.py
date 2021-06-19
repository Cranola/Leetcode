'''
Problem description:
Enter an integer array and implement a function to adjust the order of the numbers
in the array so that all odd numbers are in the first half of the array, and all
even numbers are in the second half of the array, and the relative order between odd and
odd, even and even is guaranteed unchanged.
'''


# Solution1
def reorder_extra_space(array: list):
    """
    Create two extra arrays to put odd numbers and even numbers separately.
    The time Complexity is O(n).
    :param array:
    :return:
    """
    odd_array = []
    even_array = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            even_array.append(array[i])
        else:
            odd_array.append(array[i])
    return odd_array + even_array


# Solution2
def find_first_odd(array: list):
    """
    Find the first odd number in array. If there is no odd number, return None.
    :param array:
    :return:
    """
    for i in range(len(array)):
        if array[i] % 2 == 1:
            return i
    return None


def reorder_first_odd(array: list):
    """
    Find the first odd number in the list;
    Put it to the first index place and the origin numbers before it will be moved forward to the next index.
    Recursively run this operation with the new list without the first odd number mentioned above.(array[0] for now)
    :param array:
    :return:
    """
    if len(array) <= 1:
        return array
    else:
        first_odd_index = find_first_odd(array)
        if first_odd_index is None:
            return array
        else:
            pivot = array[first_odd_index]
            for i in range(first_odd_index, 0, -1):
                array[i] = array[i-1]
            array[0] = pivot
            return [array[0]] + reorder_first_odd(array[1:])


# Solution3
def reorder_bubble_sort(array: list):
    """
    Just like the bubble sort, we start from the last index of array to the second index. If array[index] is odd
    and array[index-1] is even, swap them. Recursively run this in array[1:].
    :param array:
    :return:
    """
    if len(array) <= 1:
        return array
    for i in range(len(array)-1):
        for j in range(len(array)-1, i, -1):
            if array[j] % 2 == 1 and array[j-1] % 2 == 0:
                array[j], array[j-1] = array[j-1], array[j]
    return array


if __name__ == "__main__":
    # result validation, all solutions are approved on the website
    array = [1, 2, 3, 4, 5, 6, 7]
    result_reorder_extra_space = reorder_extra_space(array)
    result_reorder_first_odd = reorder_first_odd(array)
    result_reorder_bubble_sort = reorder_bubble_sort(array)
    print("The result of solution1 is: {}" .format(result_reorder_extra_space))
    print("The result of solution2 is: {}" .format(result_reorder_first_odd))
    print("The result of solution3 is: {}" .format(result_reorder_bubble_sort))
