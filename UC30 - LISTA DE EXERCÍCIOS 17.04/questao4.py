def imc():
    try:
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))

        resultado = peso / (altura * altura)

        if resultado < 18.5:
            print("Magro")
        elif resultado <= 24.9:
            print("Normal")
        else:
            print("Acima do peso")

    except:
        print("Erro")

imc()