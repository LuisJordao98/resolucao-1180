def menorvalpos(vetor):
    menor_valor = vetor[0]
    posicao = 1
    for i in range(1, len(vetor)):
        if vetor[i] < menor_valor:
            menor_valor = vetor[i]
            posicao = i
    return menor_valor, posicao

N = int(input("Digite um numero: "))

if N <= 1 or N >= 1000:
    print("O valor deve estar entre 1 e 1000")
else:
    print("Digite os valores do vetor")
    valores = input().split()

    if len(valores) != N:
        print("A quantidade de valores fornecidos não corresponde a N.")
    else:
        vetor = [int(valor) for valor in valores]

        menor_valor, posicao = menorvalpos(vetor)

        print("Menor valor:", menor_valor)
        print("Posicao:", posicao)
