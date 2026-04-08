def controle_financeiro(mesada, gastos):
    total = 0

    for gasto in gastos:
        total += gasto

    if total > mesada:
        print(f"prejuízo de R${total - mesada }")
        
    else: 
        print(f"Sobrou R${mesada - total}")