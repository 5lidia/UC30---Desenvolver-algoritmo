def calculadora():
    while True:
        print("Calculadora")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Fechando a calculadora")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Tente novamente")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Digite valores numéricos válidos")
            continue

        if opcao == "1":
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")

        elif opcao == "2":
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")

        elif opcao == "3":
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")

        elif opcao == "4":
            if num2 == 0:
                print("Não é permitido")
            else:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")


calculadora()