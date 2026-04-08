def transporte(passagem, dias):
    total = 0 

    for i in range(dias):
        total += passagem * 2

    print(f"Gasto total do mês: R${total}")