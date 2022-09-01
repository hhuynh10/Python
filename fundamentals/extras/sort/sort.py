list = [4, 1, 7, 3, 9, 12, 0]

def sort_list(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1-j):
            if list[i] > list[i +1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

print(sort_list(list))
