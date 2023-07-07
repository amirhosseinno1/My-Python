months = ['farvardin', 'ordibehesht', 'khordad', 'tir', 'mordad', 'shahrivar', 'mehr', 'aban', 'azar', 'dey', 'bahman', 'esfand']
days=['st','nd', 'rd']+17*['th']+['st','nd', 'rd']+7*['th']+['st']
year =int(input('Enter year : '))
month = int(input('Enter month : '))
day= int(input('Enter day : '))
dindex=day-1
mindex=month-1
print(day, days[dindex],' ', months[mindex],' ', year)
