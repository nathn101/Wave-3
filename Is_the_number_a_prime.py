def prime_determination():
    inp = int(input("Enter a number: "))

    prime_factors = []

    divisor = 2

    if inp >= divisor:
        while inp >= divisor:
            if inp % divisor == 0:
                prime_factors.append(divisor)
                inp  = inp // divisor
            else:
                divisor += 1
    elif inp == 1:
        prime_factors.append(1)

    if len(prime_factors) == 1:
        print("Number is prime")
    elif len(prime_factors) > 1:
        print("Number is not prime")

prime_determination()