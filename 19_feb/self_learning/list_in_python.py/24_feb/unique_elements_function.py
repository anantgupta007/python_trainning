# unique_elements_function.py

def unique_elements(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique

numbers = list(map(int, input().split()))
result = unique_elements(numbers)

print(*result)