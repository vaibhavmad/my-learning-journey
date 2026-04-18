list_num = [1, 2, 3, 4, 5, 6, 7, 8]

def sum_even(list_arg):
    sum_of_even = sum(arg for arg in list_arg if arg % 2 == 0)
    return sum_of_even

result = sum_even(list_num)
print(result)