idade = int(input("Digite a idade do seu atleta:"))

if idade < 12:
    categoria = "Infantil"
elif idade < 18:
    categoria = "Juvenil"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Sênior"