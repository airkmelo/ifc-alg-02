#stragniamoreotcho_08

lapa3 = int(input("Insira um outro número novamente: "))

cent = lapa3//100 
dez  = (lapa3%100)//10 
uni  = ((lapa3%100)%10)

print(cent + dez*10 + uni*100)