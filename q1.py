# Q1 - list analyzer
# not allowed to use max, min, sum, sort or sorted here

n = int(input())
numbers = []

# reading the numbers, they can be on one line separated by spaces
while len(numbers) < n:
    for value in input().split():
        numbers.append(int(value))

largest = numbers[0]
smallest = numbers[0]
total = 0
even = 0
odd = 0

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total = total + num
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

# reverse by going from the last index backwards
reversed_list = []
i = len(numbers) - 1
while i >= 0:
    reversed_list.append(numbers[i])
    i = i - 1

print("Largest:", largest)
print("Smallest:", smallest)
print("Sum:", total)
print("Even count:", even)
print("Odd count:", odd)
print("Reversed:", *reversed_list)
