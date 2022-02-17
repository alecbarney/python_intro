open_file = open('CupcakeInvoices.csv')

for row in open_file:
    print(row)

for row in open_file:
    flavor = row.split(',')
    print(flavor[2])

for row in open_file:
    value = row.split(',')
    total = int(value[3]) * float(value[4])
    print(total)


total = 0

for row in open_file:
    value = row.split(',')
    total = total+ (int(value[3]) * float(value[4]))
    
print(total)



open_file.close()
