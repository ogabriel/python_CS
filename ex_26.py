num1 = int(input("Insira o dividendo: "))
num2 = int(input("Insira o divisor: "))

aux = num1
module = 0

while(aux > 0):
    module = aux
    aux -= num2

print(module)
