ano_1 = int(input('primer año '))
ano_2 = int(input('segundo año '))


for i in range(ano_1, ano_2+1):
    if not i % 10 == 0:
        continue
    if not i % 4 == 0:
        continue    
    if i % 100 != 0 or i % 400 == 0:
        print(i)
