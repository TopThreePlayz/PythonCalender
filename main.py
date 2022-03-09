def leap_year(y2):
    if(y2 % 4 == 0):
        if (y2 % 100 == 0):
            if (y2 % 400 != 0):
                return 0
            else:
                return 1
        else:
            return 1
    else:
        return 0
    


def days_left(d1, m1, y1):
    c = 0
    for i in range(1,m1):
         c = c + number_of_days(i, y1)
         #print(c)
         #print(i)
    if (leap_year(y1) == 0):
        return 365 - (c + d1)
    elif (leap_year(y1) == 1):
        return 366 - (c + d1)
    
    
    

def number_of_days(m, y):
    global leap
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        return 31
    elif (m == 4 or m == 6 or m == 9 or m == 11):
        return 30
    elif (m == 2 and leap_year(y) == 0):
        return 28
    elif (m == 2 and leap_year(y) == 1):
        return 29
        




print("Please enter a date")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
print("Menu")
print("1) Calculate the number of days in the given month.")
print("2) Calculate the number of days left in the given year.")
choice = int(input(""))
if (choice == 1):
    print(number_of_days(month, year))
if (choice == 2):
    print(days_left(day, month, year))
