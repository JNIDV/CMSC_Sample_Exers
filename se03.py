A = int(input())
B = int(input())
temp1 = A
temp2 = B
if temp1 < temp2:
    temp1, temp2 = temp2, temp1
remainder = temp1 % temp2
while remainder > 0:
    temp1 = temp2
    temp2 = remainder
    remainder = temp1 % temp2
print(temp2)