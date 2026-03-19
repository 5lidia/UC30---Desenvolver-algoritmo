def rank_jogador(pontos, derrotas):
    perda = derrotas * 10
    final = pontos - perda

    if final < 0:
        return "Banido"

    if final < 100:
        return "Bronze"
    if final < 300:
        return "Prata"
    if final < 600:
        return "Ouro"
    
    return "Diamante"