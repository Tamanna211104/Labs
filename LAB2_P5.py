quantity = int(input("How many units do you have?"))
cost = quantity * 100

if cost > 1000:
    newCost = cost *.90
    print(newCost)
else: 
    print(cost)