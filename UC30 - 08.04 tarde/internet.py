def internet(consumo):
    total = 0

    for dia in consumo: 
        total += dia

    if total > 30:
        print("Plano excedido")
    else: 
        print("Dentro do limite")