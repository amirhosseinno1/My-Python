#print a formatted price list with a given width 
width = int(input('please enter width: '))
price_width = 10
item_width = width - price_width
header_format = '%-*s%*s'
format = '%-*s%*.2f'
print('='*width)
print(header_format %(item_width, 'Item' ,  price_width ,  'Price') )
print('-'*width)
print(format % (item_width, 'apples',price_width,0.4  )) 
print(format % (item_width, 'pears',price_width, 0.5 )) 
print(format % (item_width, 'melon',price_width, 1.92 )) 
print(format % (item_width, 'water melon',price_width,8 )) 
print(format % (item_width, 'grape',price_width, 12 )) 
print('='*width)
