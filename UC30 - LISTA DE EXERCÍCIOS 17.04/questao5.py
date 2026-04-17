convidados = ["Gaby","Erika","Bruno","JL","Ana"]

soma = 0

for convites in convidados:
    soma += 1

if soma % 2 == 0:
    print("O número de convidados é par:", soma)
else:
    print("O número de convidados é ímpar:", soma)