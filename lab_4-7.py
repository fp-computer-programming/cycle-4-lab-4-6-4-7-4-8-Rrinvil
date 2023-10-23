# Input: a list of numbers
numbers = [1, 2, 3, 4, 5]


num_string = ' '.join(map(str, numbers))


print("Numbers as a single string with spaces:", num_string)


numbers_list = [int(num) for num in num_string.split()]
smallest_num = min(numbers_list)
largest_num = max(numbers_list)


print("The smallest number given was", smallest_num)
print("The largest number given was", largest_num)


product = smallest_num * largest_num


print("The product of the two numbers extracted was", product)
