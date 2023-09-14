def find_prime_factors(number):
    prime_factors = []
    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1

    return prime_factors


num = int(input("Enter a number"))
factors = find_prime_factors(num)
print("Prime factors of", num, "are:", factors)