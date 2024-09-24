vetor = [0] * 5

for i in range(5):
    vetor[i] = float(input(f"Digite o elemento {i + 1}: "))

maior = vetor[0]

for elemento in vetor:
    if elemento > maior:
        maior = elemento

print("O maior elemento do vetor é:", maior)
