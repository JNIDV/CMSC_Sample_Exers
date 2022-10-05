L = int(input())
W = int(input())
for i in range(L):
    for j in range(W):
        if i == 0 or i == L - 1 or j == 0 or j == W - 1:
            print('#', end='')
        else:
            print(' ', end='')
    print()