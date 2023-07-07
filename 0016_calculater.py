a=float( input('enter first num:' ))
b=float( input('enter second num:' ))
op= input('enter oprator: ')
c = a+b
if op == '+' :
    print('%f %s %f = %f' %(a, op,b ,c ))
elif op == '*' :
    c = a*b
    print('%f %s %f = %f' %(a, op,b ,c ))

elif op == '/' :
    c = a/b
    print('%f %s %f = %f' %(a, op,b ,c ))

elif op == '-' :
    c = a-b
    print('%f %s %f = %f' %(a, op,b ,c ))
else:
    print('erorr')
