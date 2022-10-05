n = int(input())
count = 0
for i in range(n, 2 * n + 1):
    is_prime = True
    if i != 2 and i % 2 == 0:
        is_prime = False
    j = 3
    while j * j <= n:
        if i % j == 0:
            is_prime = False
            break
        j += 2
    if is_prime:
        count += 1
print(count)