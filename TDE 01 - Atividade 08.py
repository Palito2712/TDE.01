pi = 3.14

raioCilindro = float(input("A lata de tinta custa R$50,00 e possui 5L. Qual é o raio do cilindro que será pintado?  "))

alturaCilindro = float(input("E qual é a altura?  "))

areaLateral = 2.0 * pi * raioCilindro * alturaCilindro

areaBase = pi * (raioCilindro ** 2.0)

areaTotal = areaLateral + (2.0 * areaBase)

litrosTinta = areaTotal / 3.0

quantidadeTinta = litrosTinta / 5.0

custoTinta = quantidadeTinta * 50.0

print("O valor total das tintas é: R$", custoTinta)

print("E a quantidade de latas será:  ", quantidadeTinta)