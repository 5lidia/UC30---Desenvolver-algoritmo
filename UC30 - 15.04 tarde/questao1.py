def media_aluno():
    notas = []
    
    print("Cálculo de Média")
    
    for i in range(1, 4):
        try:
            nota = float(input(f"Digite a nota {i}: "))
            notas.append(nota)
            
        except ValueError:
            print("Erro: As notas devem ser numéricas. Encerrando execução.")
            return 

    media = sum(notas) / len(notas)
    print(f"Média final: {media:.2f}")

media_aluno()