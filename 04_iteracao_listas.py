# Lista de Frutas
frutas = ["laranja", "maçã", "uva", "pera", "mamão", "abacate", "amora"]

# Para percorrer uma lista e exibirapenasseus elementos,
# usamos a extrutura for..in, como já vimos no arquivo nº 02
for f in frutas:
    print(f)

print ('-' * 48)

# Imprimindo uma lista de trás pra frente: reversed()
for x in reversed(frutas):
    print(x)

    print ('-' * 48)

# No entanto, frequentemente prezisamos exibir, além do
# valor do elemento, também sua posição. Nesse caso, devemos
# usar a estrutura for..in cimbinada com as funções range() e len()
for pos in range(len(frutas)):
   # Opção_01: print(frutas[pos], ".", pos)
   # Opção_02: print("A fruta", fruta[pos], "está na posição", pos, ".")
   # Opção_03:
    print(f"A fruta {frutas[pos]} está na posição: {pos}.")

    print ('-' * 48)

# Às vezes, é necessário poercorrer a lista de trás para frente,
# mas tendo acesso também à posição dos elementos. Para isso, 
# usamos a estrutura for..in, range() com três parâmetros e len()
for i in range(len(frutas)-1, -1, -1):
    print(f"A fruta {frutas[i]} está na posição: {i}.")