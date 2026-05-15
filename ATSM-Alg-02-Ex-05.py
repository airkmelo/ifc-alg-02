#lesgofive_05

x = 50
y = 25
z = 10
m = 5
l = 1

tr = int(input("Insira o valor: "))


if 0 <= tr <= 99 :

    p50 = (tr//x)
    p25 = (tr%x)//y
    p10 = ((tr%x)%y)//z
    p5  = (((tr%x)%y)%z)//m
    p1  = ((((tr%x)%y)%z)%m)//l

    print("É necessária", p50,"moeda de", p50*50,"centavos")
    print("São necessárias", p25, "moedas de", p25*25, "centavos")
    print("São necessárias", p10,"moedas de", p10* 10, "centavos")
    print("São necessárias", p5,"moedas de", p5*5, "centavos")
    print("São necessárias", p1,"moedas de 1 centavo")
else    :

    print("Valor não válido")