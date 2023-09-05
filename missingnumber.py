def missing_number(n):
    numbers = set(n)
    length = len(n)
    output = []
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output
all_numbers = [1, 3,4, 5, 6, 7, 9, 10, 11, 14, 17, 18, 20]
print(missing_number(all_numbers))

#optimized way

def missing_numbers(nums):
    nums_set = set(nums)
    min_num, max_num = min(nums), max(nums)
    all_numbers = set(range(min_num, max_num + 1))
    missing = list(all_numbers - nums_set)
    return missing

all_numbers = [1, 3, 4, 5, 6, 7, 9, 10, 11, 14, 17, 18, 20]
print(missing_numbers(all_numbers))
