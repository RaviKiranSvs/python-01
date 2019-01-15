file = r"location/transaction.log"

input = []

with open(file) as f:
    f = f.readlines()

for line in f:
    input.append(line)
    
sum = 0

for i in input:
    type = i[0]
    amount = int(i[2:])
    if  type == 'D':
        sum += amount
    elif type == 'W':
        sum -= amount

print sum
