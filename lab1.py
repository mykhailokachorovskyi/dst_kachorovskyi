import math
import datetime
###################
print('Hello world!')
name = input('What is your name? Print here: ')
print('Hello ' + name + '!')
print('Your name has', len(name), 'letters.')
birth_date_string = input('Please, enter your birth date in format (YYYY.MM.DD): ')
year, month, day = map(int, birth_date_string.split('.'))
birth_date = datetime.date(year, month, day)
now = datetime.date.today()
age_days = now - birth_date
age_years = int(age_days.days/365)
print('Today is', now , ',your age is', age_years, 'years (', age_days, ')')
