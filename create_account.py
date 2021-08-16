
from db_connector import insert_user_details
from userdetails import UserDetails


def create_account():

    flag=False
    while flag==False:
        username=input('enter username : ')
        flag=validate_username(username)

    
    flag=False
    while flag==False:
        password=input('enter password : ')
        flag=validate_password(password)
    
    choice=''
    while choice!='1' and choice!='2':
        choice=input('Select 1 for Merchant and 2 for Customer : ')
    if choice=='1':
        usertype="MERCANT"
    else:
        usertype='CUSTOMER'


    print('===========================================================')    
    print('please confirm the details')
    print('username is {}'.format(username))
    print('password is {}'.format(password))
    print('usertype is {}'.format(usertype))
    print('=============================================================')

    result='========================================\nenter your choice:\n1. confirmation \n2. edit \n============================================= \n'
    num_value=''
    while num_value!=1 and num_value!=2:
        result2=input(result)
        try:
         num_value=int(result2)
         if num_value==1:
          user_detail= UserDetails(username,password,usertype)
          insert_user_details(user_detail)
          print('successfully created')
          
         elif num_value==2:
          print('edit your details')
          create_account()
        except:
         print('\n\ninvalid input')        
        


def validate_username(name):
    if name.isalpha():
        if len(name) > 3 and len(name) <=10:
        #  data= if_username_exist(name)
        #  if data:
        #    print('username already exist')
        #    return False
        #  else:
             return True
        else:
          print('username should be more than 3 and less than 10 letters') 
          return False   
    else:
     print("name should contain only letters")
     return False  


def validate_password(password):

    if password.isalnum() and not password.isalpha() and not password.isnumeric():
        if len(password) > 3 and len(password) <=10:
             return True
        else:
          print('passsword should be more than 3 and less than 10 letters') 
          return False   
    else:
     print("password should contain only alphanumeric")
     return False               