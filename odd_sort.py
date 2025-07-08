#sort only odd numbers in list on the same positions
def sort_array(source_array):
    indexes = []
    numbers = []
    for el in enumerate(source_array):
        if el[1]%2:
            indexes.append(el[0])
            numbers.append(el[1])
    numbers.sort()
    for i in range(len(numbers)):
        source_array[indexes[i]] = numbers[i]
    return source_array


list2 = [7,43,8,12,3,3,57,35,22,34,6,1,85,45,76]

print(sort_array(list2))