#vambora_questione_04

a1 = int(input("Insira o número:"))
a2 = int(input("Insira o número:"))
a3 = int(input("Insira o número:"))

b1 = min(a1,a2,a3)

b2 = max(a1,a2,a3)

med = (a1+a2+a3) - b2 - b1

print(b1, med, b2)