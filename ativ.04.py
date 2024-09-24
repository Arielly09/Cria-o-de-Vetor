vetor = [0] * 5

for i in range(5):
    vetor[i] = float(input(f"Digite o elemento {i + 1}: "))

menor = vetor[0]

for elemento in vetor:
    if elemento < menor:
        menor = elemento

print("O menor elemento do vetor é:", menor)
