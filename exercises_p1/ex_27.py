num = int(input("Insira um número: "))

reverse_num = num
aux = 0

while(aux != 0):
    reverse_num = reverse_num * 10 + aux % 10
    aux = aux / 10

if(reverse_num == num):
    print("O número digitado é palíndromo")
else:
    print("O número digotadp ñ é palíndromo")

print(reverse_num)
