# LISTAS
# Listas são uma forma de armazenar mais de um valor em uma
# única variável. Os valores podem ser de tipos diferentes

#  Uma lista de números
valores = [2, 3, 5, 7, 9, 11]  

# Uma lista de valores de tipos variados
mix = ["batata", 1.25, "true", "tomate", 44]

# Lista de strings
legumes = ["batata", "pepino", "abobrinha", "cenoura"]

# OPERAÇÕES SOBRE LISTAS

# 1) PERCURSO: Significa percorrer a lista do primeiro ao 
#   ultimo elemento, fazendo algo com cada um deles.

# Imprimindo cada um dos elementos da lista, um por linha:
for val in valores:
    print(val)
    print("-" * 10)
    
# Imorimento o dobro de valores de cada elemento da lista:
for x in valores:
    print(x * 2)
    print("-" * 10)

# 2) INSERINDO UM NOVO ELEMENTO NO FIM DA LISTA

valores.append(13)
legumes.append("cebola")

print (valores)
print (legumes)

print("-" * 40)

# 3) INSERINDO UM NOVO ELEMENTO NO MEIO DA LISTA

legumes.insert(2, "mandioquinha")
print(legumes)
print("-" * 40)
legumes.insert(0, "beterraba")
print(legumes)
print("-" * 40)