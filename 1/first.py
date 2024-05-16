# CALCULATION OF AGE FROM THE BIRTH YEAR PROG

import datetime  # this module provides the recent date and time

current_year = datetime.datetime.now().year  # getting the current year
birth_year = int(input("Enter your birth year : "))

age = current_year - birth_year
print(age)
