# Count down
def countDown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return list

print(countDown(5))

# Print and return
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1, 2]))

# First plus length
def first_plus_length(list):
    list = list[0] + len(list)
    return list

print(first_plus_length([1, 2, 3, 4, 5]))

# Values greater than second
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    for i in list:
        if i > list[1]:
            new_list.append(i)
    return new_list

print(values_greater_than_second([5, 2, 3, 1, 4]))
print(values_greater_than_second([3]))

# This length, that value
def length_and_value(size, value):
    list = []
    for i in range(0, size):
        list.append(value)
    return list

print(length_and_value(4, 7))
print(length_and_value(6, 2))