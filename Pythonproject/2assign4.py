def find_largest_element(numbers):
    if len(numbers) == 0:
        return None

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    return largest

# Example usage
number_enter = input("Enter list of numbers")
largest_number = find_largest_element(number_enter)
print("Largest element:", largest_number)