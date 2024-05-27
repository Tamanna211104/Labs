rate = int(input("Enter your pay rate"))
hours = int(input("Enter how many hours you worked this week"))


if hours <= 40:
    salary = rate * hours
    print(salary)
else:
    overtime = hours - 40
    newRate = rate * 1.5
    extra = overtime * newRate
    salary = (rate * 40) + extra
    print(salary)
    