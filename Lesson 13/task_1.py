# Write a Python program to detect the number of local variables declared in a function.
def count_var():
    """Func to count local vars"""
    a = 4
    b = 5
    c = 6
    count = 0
    for i in locals():
        count += 1
    return count - 1


print(count_var())


def count_var_2():
    """Func to count local vars v.2"""
    a = 4
    b = 5
    c = 6
    return 0


print(count_var_2.__code__.co_nlocals)
