# Реалізувати алгоритм бінарного пошуку за допомогою рекурсії.
def r_binary_search(seq, left, right, target):
    if left > right:
        return 'No such value in a list'
    else:
        mid = left + (right - left) // 2
        if target > seq[mid]:
            return r_binary_search(seq, mid + 1, right, target)
        if target < seq[mid]:
            return r_binary_search(seq, left, mid - 1, target)
        else:
            return f'Value\'s index is {mid}'


if __name__ == '__main__':
    l = [1, 5, 7, 17, 23, 67, 105]
    print(r_binary_search(l, 0, len(l) - 1, 23))
