grade=int(input("enter your grade: "))

if grade >= 90 and grade<100:
    print(f"{grade} equals A")
elif grade >=70 and grade <=90:
    print("B")
elif grade >=60 and grade<70:
    print("C")
elif grade >50 and grade<60:
    print("D")
elif grade>40 and grade<50:
    print("E")
elif grade >0 and grade<40:
    print("F")
else:
        print("enter grade between 0 and 100")

