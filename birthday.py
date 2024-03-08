# Given your birthday, in the format "DD-MM-YYYY", write a function that calculates how
# many days have passed since your birthday (without counting the days in your birth year
# and the current year, so just whole years).
# The function takes your birthday as a parameter in string format.
# Do not import anything, use only what we learned in class

def days_since_birthday(birthday, current_year):
    birth_year = int(birthday.split("-")[2])

    full_years = current_year - birth_year - 1

    def is_leap(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    leap_years = sum(is_leap(year) for year in range(birth_year + 1, current_year))

    days = full_years * 365 + leap_years

    return days


print(days_since_birthday("13-04-2004", 2024))
