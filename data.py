# x = 3
# y = float(3)
# print(x,y)

# def bill_calculator():
#     x = int(input("How much was the bill?"))
#     y = input("How was the service?").strip().lower()
#     if y == "great":
#         print(x * 1.25)
#     elif y == "good":
#         print(x * 1.2)
#     elif y == "okay": 
#         print(x * 1.15)
#     elif y == "bad":
#         print(x)
#     else: print("ERROR")
# bill_calculator()

# values = [1,2.23,5,7,2,30,15]
# print(values)
# for i in values:
#     print(values[0])
#     print(values[6])

# x = "words are here"
# y= x.split( )
# z = y[0]
# print(y)
# print(z)

# x = input("Type Sentence here")
# print(len(x.split(" ")))

# day_of_week = input("what day is it? ")
# if day_of_week == "Friday":
#     print("correct")
# else:
#     print("incorrect")

# x = "test"
# print(f"hello {x}")

# temp = 75
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')
# else:
#     print('cold')

# def even_or_odd():
#     N = int(input("Type number here!"))
#     if N % 2 == 1:
#         print("ODD")
#     else:
#         print("EVEN")
# even_or_odd()

# def factor():
#     n = int(input("What number do you want to factor?"))
#     for i in range(1,n+1):
#         if n % i == 0:
#             print(i)
# factor()

def gcf():
    n1 = int(input("What is the first number do you want to find the GCF of?"))
    n2 = int(input("What is the second number do you want to find the GCF of?"))
    if n1 > n2:
        t = n2
    else: t = n1
    for i in range(1,t+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    print(gcd)
gcf()

# only sample function , loop, and how to access something in a list