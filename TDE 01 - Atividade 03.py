salarioMinimo = 1212.00

salarioFuncionario = float(input("Digite o seu salário para saber quantos salários mínimo você recebe:  "))

salarioQuantidade = salarioFuncionario / salarioMinimo

if salarioFuncionario == salarioMinimo:

    print("Você recebe exatamente um salário mínimo.")

elif salarioFuncionario < salarioMinimo:

    print("Você recebe", salarioQuantidade, "do salário mínimo.")

elif salarioFuncionario > salarioMinimo:

    print("Você recebe", salarioQuantidade, "vezes o salário mínimo!")