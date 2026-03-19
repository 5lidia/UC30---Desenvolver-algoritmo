def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"

    # verifica se tem taxa
    if saque > 1000:
        saque = saque + (saque * 0.02)

    resto = saldo - saque
    return resto