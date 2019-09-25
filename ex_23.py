num = int(input("Insira um número: "))

def prime(num):
    aux = num
    while(aux > 2):
        aux -= 1
        if num % aux == 0:
            return False
    return True

def not_prime():
    print("Ñ é primo")

def is_prime():
    print("Primo")

if(num == 2):
    is_prime()
elif(num % 2 == 0):
    not_prime()
elif(prime(num)):
    is_prime()
else:
    not_prime()
