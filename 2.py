
SUM = 0
fib1 = 1
fib2 = 1

while fib1 < 4000000:
    if fib1 % 2 == 0:
        SUM += fib1
    newfib = fib1 + fib2
    fib1 = fib2
    fib2 = newfib

print(SUM)
