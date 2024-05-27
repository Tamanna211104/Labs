salary = int(input("What is your salary"))
service = int(input("How many years of service do you have"))

if service > 5:
    newSalary = salary * 1.5
    print(newSalary)
else: 
    print(salary)