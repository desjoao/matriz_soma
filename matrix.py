matriz = []
soma = 0

for i in range(3):
    matriz.append([])
    for c in range(3):
        matriz[i].append([])
        
for i in range(3):
    for c in range(3):
        matriz[i][c] = int(input('Insira um valor: '))
        soma+=float(matriz[i][c])
print(matriz)
print(f'Soma = {soma}')
