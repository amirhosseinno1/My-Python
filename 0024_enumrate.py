names= ['ali','reza','alireza','amir','amirali','hossein']
print(names)
for str in names:
    if 'ali' in str:
        ind= names.index(str)
        names[ind] = '[cleaned]'
print(names)

names= ['ali','reza','alireza','amir','amirali','hossein']
for index , string in enumerate(names):
    if 'ali' in string:
        names[index] = '[removed]'
print (names)