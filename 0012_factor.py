width  = 66
unit_price_width = 15
total_price_width = 20
item_width = 25
number_width=6
A=input('Enter item 1: ')
A1=int(input('Enter price: '))
A2=int(input('Enter number: '))
totalA=A1*A2 
B=input('Enter item 2: ')
B1=int(input('Enter price: '))
B2=int(input('Enter number: '))
totalB=B1*B2
C=input('Enter item 3:')
C1=int(input('Enter price: '))
C2=int(input('Enter number: '))
totalC=C1*C2
D=input('Enter item 4:')
D1=int(input('Enter price: '))
D2=int(input('Enter number: '))
totalD=D1*D2
E=input('Enter item 5: ')
E1=int(input('Enter price: '))
E2=int(input('Enter number: '))
totalE=E1*E2
F=input('Enter item 6: ')
F1=int(input('Enter price: '))
F2=int(input('Enter number: '))
totalF=F1*F2
G=input('Enter item 7: ')
G1=int(input('Enter price: '))
G2=int(input('Enter number: '))
totalG=G1*G2
H=input('Enter item 8: ')
H1=int(input('Enter price: '))
H2=int(input('Enter number: '))
totalH=H1*H2
print('='*width)
fotmat='%-*s%-*s%-*s%*s'
Org_format='%-*s%-*i%-*i%*i'
print(fotmat % (item_width, 'Item',unit_price_width, 'Unit price',number_width, 'Number' , total_price_width,'Total price'  ))
print('-'*width)
print( Org_format % (item_width, A,unit_price_width, A1,number_width, A2, total_price_width,totalA ))
print( Org_format % (item_width, B,unit_price_width, B1,number_width, B2, total_price_width,totalB ))
print( Org_format % (item_width, C,unit_price_width, C1,number_width, C2, total_price_width,totalC))
print( Org_format % (item_width,D,unit_price_width, D1,number_width, D2, total_price_width,totalD ))
print( Org_format % (item_width, E,unit_price_width, E1,number_width, E2, total_price_width,totalE ))
print( Org_format % (item_width, F,unit_price_width, F1,number_width, F2, total_price_width,totalF ))
print( Org_format % (item_width, G,unit_price_width, G1,number_width,G2, total_price_width,totalG ))
print( Org_format % (item_width, H,unit_price_width, H1,number_width, H2, total_price_width,totalH ))
print('-'*width)
sum=totalA+totalB+totalC+totalD+totalE+totalF+totalG+totalH
print('%-*s%*i'%(46,'sum' , 20,sum ))
print('='*width)
