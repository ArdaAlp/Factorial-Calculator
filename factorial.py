def factorial(num):
    if (num == 0 or num == 1):
        return 1

    fact = 1
    for i in  range(1, num + 1):
        fact *= i
    
    return fact

num = int(input("Enter the number for factorial calculating: "))

if (num < 0):
    print("Please enter just natural numbers! (>= 0)")

else:
    print(f"{num}! equals: {factorial(num)}")