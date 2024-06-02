month = int(input("enter month name   "))
monthlyRainfall = float(input("enter the rainfall for this month "))
if month == 1:
    monthName = "January"
elif month == 2:
    monthName = "February"
elif month == 3:
    monthName = "March"
elif month == 4:
    monthName = "April"
elif month == 5:
    monthName = "May"
elif month == 6:
    monthName = "June"
elif month == 7:
    monthName = "July"
elif month == 8:
    monthName = "August"
elif month == 9:
    monthName = "September"
elif month == 10:
    monthName = "October"
elif month == 11:
    monthName = "November"
elif month == 12:
    monthName = "December"
elif monthlyRainfall <= 10:
    print("the average rainfall is ",monthlyRainfall,"therefore it is winter")
else:
    print("the average rainfall is ",monthlyRainfall,"therefore it is summer")





