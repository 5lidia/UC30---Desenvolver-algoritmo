# Entrada
N = int(input())
R = int(input())
P = int(input())

total = N
novos = N
dias = 0

# Caso seja atingido
if total >= P:
    print(0)
else:
    while total < P:
        novos = novos * R
        total += novos
        dias += 1
    
    print(dias)