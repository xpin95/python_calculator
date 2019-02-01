result = 0
def add(x,y):
    result = x + y;
    print(result)

def substract(x,y):
    print(x - y)


def multiply(x,y):
    print(x * y)


def divide(x,y):
    print(x / y)

x = int(input())
y = int(input())

print("1:sumar")
print("2:divi")
print("escribe 3 para sustituir la clave por xxxxx...")
print("escribe 4 para separar caracteres cada 3 posiciones")

num = int(input())
options = {1: add(x,y),
           2: substract(x,y),
           3: multiply(x,y),
           4: divide(x,y)

           }

options[num]()