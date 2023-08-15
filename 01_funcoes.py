
# Função para calcular IMC de uma pessoa
def calc_imc(peso, altura):
    return peso / altura ** 2

# p = 95
# a = 1.82
# imc = calc_imc(p, a)

# print(imc)

print (calc_imc(85, 1.72))

#################################################

from math import pi

def calc_area(base, altura, tipo):

    if tipo == "R":                        #Retangulo
        resultado = base * altura     
    elif tipo == "T":                      #Triangulo
        resultado = base * altura / 2
    elif tipo == "E":                      #Elipse
        resultado = (base/2) * (altura/2) * pi
    else:                                  # Tipo inválido ou desconhecido
        resultado = None

    return resultado

print("Retangulo 20x30:", calc_area(20, 30, "R"))
print("Triangulo 45x32:", calc_area(45, 32, "T"))
print("Elipse 10x15:", calc_area(10, 15, "E"))
print("Desconhecido 12x16:", calc_area(12, 16, "X"))