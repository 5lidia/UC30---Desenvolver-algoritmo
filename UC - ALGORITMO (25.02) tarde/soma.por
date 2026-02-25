programa{
    funcao inicio() {
        inteiro n, soma, i

        soma = 0

        escreva("Digite um número: ")
        leia(n)

        para(i = 1; i <= n; i++) {
            soma = soma + 1
        }
        escreva("Soma = ", soma)
    }
}