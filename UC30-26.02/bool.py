#resp = input("Você vai passar de ano? s/N: ")
#resultado = bool(resp)

#print("Resposta ", resp )
#print("Resultado ", resultado )

resp = input("Você vai passar de ano? s/n").strip().lower()

resultado = (resp == "s")

print("resultado ", resultado)
print(type(resultado))