def leap(year):
    if (year % 4==0 & year%400==0):
      print("Leap Year")
    else:
      print("no")

year=int(input("Year: "))
leap(year)
