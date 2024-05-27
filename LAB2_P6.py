grade = int(input("Enter your grade to recieve your mark"))

if grade < 25:
    print("F")
elif 25 <= grade < 45:
    print("E")
elif 45 <= grade < 50:
    print("D")
elif 50 <= grade < 60:
    print("C")
elif 60 <= grade < 80:
    print("B")
else: 
    print("A")