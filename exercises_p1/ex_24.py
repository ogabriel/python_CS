num = int(input("Insira um número: "))

def next_prime(aux):
    found = False
    while(not found):
        aux += 1
        found = prime(aux)
    return aux

def prime(num):
    aux = num
    while(aux > 2):
        aux -= 1
        if num % aux == 0:
            return False
    return True

aux = 1

for n in range(num):
    aux = next_prime(aux)

    print(aux)
