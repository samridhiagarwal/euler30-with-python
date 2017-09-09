def power_of_digits(n, exp = 5):
    Sum = 0
    while n > 0:
       Sum += (n % 10)**exp
       n //= 10
    return Sum

total = 0
for i in range(2, 10**6):
    if power_of_digits(i) == i:
        total += i
print(total)
