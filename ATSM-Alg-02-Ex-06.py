#laquestioneses_06

lapa = int(input("Insira alguma coisa: "))

mil  = lapa//1000
cent = lapa%1000 // 100
dez  = (lapa%1000)%100 // 10
uni  = ((lapa%1000)%100)%10

print(mil, "+", cent, "+", dez, "+", uni)

print(mil + cent + dez + uni)

