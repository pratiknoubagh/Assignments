def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string


input_str = input("Enter a string")
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)