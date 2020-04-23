#1) Create a function that adds all numbers together
def my_add(n):
    if n==0:
        return 0
    else:
        return n + my_add(n-1)

print(my_add(4))

#2) Create a function for factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))