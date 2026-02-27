nome = input("Digite seu nome: ")
if len(nome) > 5:
    print("Seu nome é grande, ele possui mais de 20 letras")
    print(f"Ele possui {len(nome)} caracteres.")

valor = int(imput("Digite um número: "))
if valor % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")

nota = float(input("Digite sua nota"))

if nota > 10:
    print("Passou")
else:
    if nota == 7: 
        print("Pode melhorar")
    else:
        print("Recuperação")

nota = float(input("Digite sua nota"))

if nota >= 10:
    print("Passou")
elif nota == 7:
    print("Pode melhorar")
else:
    print("Recuperação")

idade = int(input("Digite a idade: "))

if idade >= 16 and idade <= 69:
    print("Faixa permitida")
else:
    print("Fora da faixa")
