#A simple database
people = {
  'Alice' : {
     'phone': '2341', 
     'addr' :  'Foo drive 23'
    }, 
  'Beth':{
     'phone' : '9102', 
     'addr': 'bar street 42'
    }, 
  'Cecil':{
     'phone' : '3158', 
     'addr' : 'Baz avenue 90'
    }
}
labels = {
   'phone' : 'phone number', 
   'addr' : 'address'
   }
name = input('Name:')
#are we looking for a phone number or address?
request = input ('phone number (p) or address (a)?')

#use the correct key
if request == 'p':key ='phone'
if request == 'a':key ='addr'

# Use get to provide default values:
person = people.get(name, {})
label= labels.get (key, key)
result = person.get(key, 'not available')

print ("%s's %s is %s." 
     %(name ,  label ,  result))

