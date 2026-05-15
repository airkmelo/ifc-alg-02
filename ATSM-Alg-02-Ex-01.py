#ATSM-Alg-02-Ex-01

#laquestionenum_01

#horario_01

day1 = int(input("Informe o dia 1:"))

hr1 = int(input("Informe a hora 1:"))

min1 = int(input("Informe o minuto 1:"))

sec1 = int(input("Informe o segundo 1:"))

#horario_02

day2 = int(input("Informe o dia 2:"))

hr2 = int(input("Informe o horário 2:"))

min2 = int(input("Informe o minuto 2:"))

sec2 = int(input("Informe o segundo 2:"))

tot_h = day1*86400 + hr1*3600 + min1*60 + sec1

tot_h2 = day2*86400 + hr2*3600 + min2*60 + sec2

rest = tot_h2 - tot_h

print(f"O intervalo em segundos dos tempos dados é {rest} segundos")

