userpass= {'ali': 1122 ,  'hossein':7788 , 'morad':7987}
users= userpass.keys()
user=input("enter a user :" )
user = user.lower()
if user in users :
    print("%s's password is %s"% (user , userpass.pop(user)))
else:
    print('user not defind')
