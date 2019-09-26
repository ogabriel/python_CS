num = int(input('Digite um numero: '))
begin = int(input('Digite o numero de inicio da tabuada: '))
end = int(input('Digite o numero do fim da tabuada: '))

for n in range(begin, end + 1):
    result = num * n
    print("{0} X {1} = {2}".format(n, num, result))

