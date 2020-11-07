'''
Preencha um dicionário com informações de 5 produtos.
- Solicite os dados ao usuário
- Utilize o nome do produto como chave e o preço como valor.
Percorra o dicionário e exiba o nome dos produtos com preço
superior a R$ 50.00

'''
produtos = {}
for a in range(5):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    produtos[nome] = preco
    
print(produtos)

print("Produtos com valor superior a 50.00: ")
for a in produtos:
    if produtos[a] > 50:
        print(a)
