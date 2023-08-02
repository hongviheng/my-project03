def find_max(lst):
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value

numbers = [3, 8, 2, 10, 5]
max_num = find_max(numbers)
print("The maximum value is:", max_num)
