def add(x, y):
    print(x + y)


def substract(x, y):
    print(x - y)


def multiply(x, y):
    print(x * y)


def divide(x, y):
    print(x / y)


print("Introduce first number")
a = int(input())
print("Introduce second number")
b = int(input())

print("Please, choise an option: \n1.Add \n2.Substract \n3.Multiply \n4.Divide")


num = int(input())
options = {1: add(a, b),
           2: substract(a, b),
           3: multiply(a, b),
           4: divide(a, b)
           }

#options[num]()
