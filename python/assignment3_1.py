shrs = 40#input("Enter hours: ")
srate = 140#input("Enter rate: ")

ihrs = float(shrs)
irate = float(srate)

if ihrs > 40:
    ohrs = ihrs - 40
else:
    ohrs = 0

#calculate rate with overtime
pay = ((ihrs - ohrs) * irate) + (ohrs * irate * 1.5)

#print the pay
print(pay)
