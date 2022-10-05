n = int(input())
for k in range(n):
    for i in range(k + 3):
        for j in range(4 * n + 1):
            if 2 * n - (k + i) <= j and j <= 2 * n + (k + i):
                print('#', end='')
            else:
                print(' ', end='')
        print()