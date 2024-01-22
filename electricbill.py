#Wap to calculate electric bill(accept no. of units from the user) according to the following criteria.
# ist 100unit=no charge
# next 100 unit=rs 5 per unit
# next 200 unit= rs 10 per unit

units=float(input("enter the no of units: "))
if units <=100:
    total_bill=0
elif units >100 and units<=200:
    total_bill=(units-100)*5
else:
    total_bill=100*5+(units-200)*10
print(f"total bill:{total_bill}")

    