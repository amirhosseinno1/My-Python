from math import sqrt , ceil
N = int(input('Enter number : '))
UP = ceil(sqrt(N))
#flag = 0
for m in range(2,UP+1) : 
    if N%m == 0:
        #flag = 1
        print( '%i Is not prime'%N) 
        break
else:
     print('%i Is prime'%N)
