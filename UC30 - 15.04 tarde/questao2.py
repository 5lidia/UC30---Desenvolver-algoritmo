def compra():
    print("Caixa de Supermercado")
    
    try:
        preco1 = float(input("Digite o preço do primeiro produto: "))
        preco2 = float(input("Digite o preço do segundo produto: "))
        
        total = preco1 + preco2
        print(f"Valor total da compra: R$ {total:.2f}")
        
    except ValueError:
        print("Erro: Os preços devem ser numéricos. Encerrando execução.")

compra()