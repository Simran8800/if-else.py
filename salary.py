p=int(input("enter the n"))
if p>100000:
    tax=p*15/100
if p>50000 and  p<=100000:
    tax=p*10/100
if p<=50000:
    tax=p*5/100
print(tax)