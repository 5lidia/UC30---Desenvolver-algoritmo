def pontuacao_total(pontos, tempo):
    # bônus ou punição
    if tempo < 30:
        pontos += 50
    elif tempo > 100:
        pontos -= 20

    # verificação final
    if pontos > 200:
        return "Recorde"
    
    return pontos