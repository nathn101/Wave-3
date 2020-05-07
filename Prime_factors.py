inp = int(input("Enter a number ( Greater than or equal to 2 ): "))

prime_factors = []

divisor = 2

if inp >= divisor:
    while inp >= divisor:
        if inp % divisor == 0:
            prime_factors.append(divisor)
            inp  = inp // divisor
        else:
            divisor += 1

elif inp < divisor:
    print("Incorrect input")

print(prime_factors)