M = float(input('Enter mark: '))
SUM_M = 0
SUM_C = 0
while M > 0 : 
    C = int(input('Enter credit: '))
    SUM_M += M*C
    SUM_C += C
    M = float(input('Enter mark: '))
AVG = SUM_M/SUM_C
print('Averege is : ', AVG)