vetor = [0] * 5

for i in range(5):
    vetor[i] = float(input(f"Digite o elemento {i + 1}: "))

soma = sum(vetor)

print("A soma dos elementos do vetor é:", soma)
