#billiejeansmjtiene_10

mat = int(input("Insira o número de matrícula:"))

aa = mat // 10000
s = (mat % 10000)//1000

print(f"Aluno do ano {aa:02d} e semestre {s:02d}")