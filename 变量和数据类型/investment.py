amount = float(input("Enter amount:"))
inrate = float(input("Enter interest rate:"))
period = int(input("Enter period:"))
value = 0
year = 1
print("Year and value respectively are:")
while year <= period:
 value = amount + (inrate * amount)
 print("Year {} Rs. {:.2f}" .format(year,value))
 amount = value
 year = year +1
