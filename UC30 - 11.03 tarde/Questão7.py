senha = input ("Digite a senha: ")

temsenha = any(caractere.idigit() for caractere in senha )

if len(senha) >= 8 and temsenha:
    print("Senha válida")
else:
    print("Senha inválida")