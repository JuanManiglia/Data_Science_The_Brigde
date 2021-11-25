import random
print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
aleatorios = [random.randint(0,1000) for i in range(n)]
print(aleatorios)
a_less_num = []
num = int(input('numero maximo:'))
for i in aleatorios:
    if i < num:
        a_less_num.append(i)
print(a_less_num)