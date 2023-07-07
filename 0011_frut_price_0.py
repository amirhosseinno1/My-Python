#print a formatted price list with a given width 
width = int(input('please enter width: '))
price_width = 10
item_width = width - price_width
header_format = '%-*s%*s'
format = '%-*s%*.2f'
apple_price = float(input('enter apples price: '))
pear_price= float(input('enter pears price: '))
melon_price= float(input('enter melon price: '))
watermelon_price=float(input('enter melon price: '))
grape_price= float(input('enter grape price: '))
print('='*width)
print(header_format %(item_width, 'Item' ,  price_width ,  'Price') )
print('-'*width)
print(format % (item_width, 'apples',price_width,apple_price  )) 
print(format % (item_width, 'pears',price_width, pear_price )) 
print(format % (item_width, 'melon',price_width, melon_price)) 
print(format % (item_width, 'water melon',price_width,watermelon_price )) 
print(format % (item_width, 'grape',price_width, grape_price )) 
print('='*width)
