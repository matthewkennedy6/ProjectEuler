import ProjectEulerTools

maxPalindrome = 0

for i in range(999,100,-1):
    for j in range(999,100,-1):
        prod = i * j
        if  maxPalindrome < prod and ProjectEulerTools.isPalindrome(str(prod)):
            maxPalindrome = prod

print(maxPalindrome)