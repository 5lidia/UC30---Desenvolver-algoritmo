programa {
    funcao inicio(){
        real valor, salario, prestacao
        inteiro anos, meses

        escreva("Digite o valor da casa:")
        leia(valor)

        escreva("Digite seu salário:")
        leia(salario)

        escreva("Em quantos anos você quer pagar:")
        leia(anos)

        meses = anos * 12
        prestacao = valor / meses

        escreva("O valor da prestação é ", prestacao)

        se(prestacao <= salario * 0.30) {
            escreva("Empréstimo aprovada \n")
        } senao{
            escreva("Empréstimo não aprovado \n")
        }
    }
}