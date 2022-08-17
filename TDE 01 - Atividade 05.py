precoProduto = float(input("Digite o preço do produto:  "))

semJuros = precoProduto / 2

aVista = precoProduto - (precoProduto * 0.05)

comJuros = ((precoProduto * 0.05) + precoProduto) / 3

print("O valor à vista, com 5% de desconto, fica:  R$", aVista)

print("O valor de cada parcela, sendo parcelado em 2x sem juros, é de :  R$", semJuros)

print("E o valor das parcelas, sendo parcelado em 3x com juros, será:  R$", comJuros)