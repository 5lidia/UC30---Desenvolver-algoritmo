temperaturas = [27,26,30,25,32,28,29,33]

soma = 0

for temperatura in temperaturas:
    soma += temperatura


media = soma / len(temperaturas)

print(f"Média da semana: {media}°C")