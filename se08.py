count = 0
i = 3
while count < 30:
    are_primes = True
    j = 3
    while j * j <= i:
        if i % j == 0:
            are_primes = False
            break
        j += 2
    j = 3
    while j * j <= i + 2:
        if (i + 2) % j == 0:
            are_primes = False
            break
        j += 2
    if are_primes:
        print(i, i + 2)
        count += 1
    i += 2