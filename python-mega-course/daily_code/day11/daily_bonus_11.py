"""
we want to create a function, that intakes a list of numbers from a file and then gives
the average of these numbers as the output
"""
list_of_nums = [1, 2, 3, 4, 5, 6]

def list_average(num_list):

    average_local = sum(num_list)/len(num_list)
    return average_local

average = list_average(list_of_nums)
print(average)

