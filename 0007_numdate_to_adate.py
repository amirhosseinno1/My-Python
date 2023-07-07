#print out a date, given year , month and day as numbers
months = ['january', 'February', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'desember']
#A list with one ending for each number from 1 to 31
endings = ['st', 'nd', 'rd']+17*['th']+['st', 'nd', 'rd']+7*['th']
year = (input('year: '))
month = (input('month(1-12): '))
day=(input('day(1-31):'))
month_number = int(month)
day_number= int(day)
#remember to subtract 1 from month and day to get a correct index
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]
print(month_name + " " +ordinal + " " + year)
