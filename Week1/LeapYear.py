year = int(input("Enter an Year: "))
if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
    print("The Entered Year is a Leap Year",year)
else:
    print("The Entered Year is not a Leap Year",year)
    
