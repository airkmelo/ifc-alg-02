#daisiesjustinbiebernoves_09

dat = int(input())


ddc = dat // 10000
mmc = dat % 10000 // 100
aac = (dat%10000)%100 

 
print(f"{aac:02d}{mmc:02d}{ddc:02d}")
