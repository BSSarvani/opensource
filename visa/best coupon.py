amount=int(input())
dis=amount//10
if dis>=100:
    bill=amount-dis
else:
    bill=amount-100
print(bill)
