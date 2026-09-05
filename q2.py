# Q2 - lists, functions and .copy()

def process_list(numbers):
    new_list = numbers.copy()   # copy so the original doesn't change

    # collect the negatives first, removing while looping skips elements
    negatives = []
    for num in new_list:
        if num < 0:
            negatives.append(num)

    for num in negatives:
        new_list.remove(num)

    new_list.append(0)
    new_list.sort()
    return new_list


original = [5, -2, 8, -1, 3]
result = process_list(original)

print("Original:", original)
print("Result:", result)

# difference between = and .copy()
a = [1, 2, 3]
b = a
b.append(99)
print("using b = a :", a)

a = [1, 2, 3]
b = a.copy()
b.append(99)
print("using b = a.copy() :", a)
