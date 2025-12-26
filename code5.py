num = int(input("Enter a number: "))
temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    sum += (temp % 10) ** digits
    temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
