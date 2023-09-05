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
