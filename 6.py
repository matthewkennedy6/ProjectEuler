
sumOfSquares = 0
sum = 0

for i in range(101):
    sumOfSquares += i * i
    sum += i

squareOfSum = sum * sum

print(str(squareOfSum - sumOfSquares))