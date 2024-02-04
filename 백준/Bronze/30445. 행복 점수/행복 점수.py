from decimal import Decimal

s = input()
happy = ['H', 'A', 'P', 'Y']
sad = ['S', 'A', 'D']
ph, pg = 0, 0
for i in s:
    if i in happy:
        ph += 1
    if i in sad:
        pg += 1
if ph == pg == 0:
    print('50.00')
elif ph == 0:
    print('0.00')
else:
    H = Decimal(Decimal(ph)/Decimal(ph+pg))*100
    t1 = int(H*1000)
    t2 = int(H*100)
    if t1-10*t2 >= 5:
        t2 += 1
    print(f'{t2/100:.2f}')