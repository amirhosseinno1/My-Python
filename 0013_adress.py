#A simple database
# A dictionary with person names as keys. Each person is represented as another dictionary with the keys 'phone' and 'addr' refering to their phone number and address, respectively
people = {
  'Alice' : {
     'phone': '2341', 
     'addr' :  'Foo drive 23'
    }, 
  'beth':{
     'phone' : '9102', 
     'addr': 'bar street 42'
    }, 
  'Cecil':{
     'phone' : '3158', 
     'addr' : 'Baz avenue 90'
    }
}
#Descriptive labels for the phone number and address. this will be used when printing the output
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
#Only try to print information if the name is valid key in our dictionary :
if name in people : print ("%s's %s is %s." 
     %(name,  labels[key], people[name][key]))

