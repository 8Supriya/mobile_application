from merchant_service import mechant_service
from db_connector import get_user_details


"""
This Function is used to define logic function
---------
Parameter : user_id -> to be checked
---------
Logic
---------
1. Handle exceptions using try
2. read username and password
3. Get details of username and password from get_user_details
4. Read Deposit amount.withdraw amount,blance amount,amount statement and logout
5. Print exception details if the try block throws the exception

""" 
def login_func():
    try:
        user_details=''
        while user_details=='':
            username=input('enter username:')
            password=input('enter password:')
            user_details=get_user_details(username,password)
            if user_details.usertype=='MERCANT':
                mechant_service(user_details.user_id)
            else:
                print('log in as CUSTOMER')    
            print()
    except Exception as e:
        print(e)
       
