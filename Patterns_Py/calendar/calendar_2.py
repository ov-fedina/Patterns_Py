# Python code to demonstrate the working of
# calendar() function to print calendar

# importing calendar module
# for calendar operations
import calendar

# using calendar to print calendar of year
# prints calendar of 2022
print ("The calendar of year 2022 is : ")
print (calendar.calendar(2022))

#or
#print ("The calendar of year 2022 is : ")
#print (calendar.calendar(2022, 2, 2, 6, 3))
# The above function returns the calendar for the whole year for the year specified as an argument.
# The following arguments are passed to this function: year (yyyy),
# date column width (w), number of rows per week (l),
# number of spaces between the month column (c), number of columns (m).
