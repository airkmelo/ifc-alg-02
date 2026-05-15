#ATSM-Alg-02-Ex-02

#horario em segundos

tm = int(input("Infome seu tempo em segundos: "))

d = tm // 86400

hh = (tm - d*86400) //3600

mm = (tm - d*86400 - hh*3600) // 60

ss = (tm - d*86400 - hh* 3600 - mm*60) // 1

print(f"D:{d:02d} HH:{hh:02d} MM:{mm:02d} SS:{ss:02d}")
