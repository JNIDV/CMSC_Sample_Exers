n = int(input())
is_prime = True
if n != 2 and n % 2 == 0:
    is_prime = False
i = 3
while i * i <= n:
    if n % i == 0:
        is_prime = False
        break
    i += 2
if is_prime:
    print(n, "is prime.")
else:
    print(n, "is composite.")