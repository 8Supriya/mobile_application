from db_connector import insert_item_details, insert_user_details
from Item_details import ItemDetails


def mechant_service(user_id):
    print('================================')
    print('Merchant Page')
    print('================================')
    heading='=============================================\nenter your choice:\n1. Create item \n2. View item \n3. View order list \n4. Accept \n5. logout \n============================================= \n'
    int_value=''
    while int_value!=1 and int_value!=2 and int_value!=3 and int_value!=4 and int_value!=5:
        result=input(heading)
        try:
            int_value=int(result)
            if int_value==1:
                create_item(user_id)
                int_value=''
            elif int_value==2:
                print('view item')
                int_value=''
            elif int_value==3:
                print('View order list')
                int_value=''
            elif int_value==4:
                print('Accept')
                int_value=''
            elif int_value==5:
                print('logout successfully')
                return    
        except Exception as e:
            print(e)
            print('\n\ninvalid input')  

def create_item(user_id):
    flag=False
    while flag==False:
        product_name=input('Enter the name of the product : ')
        flag=validate_product_name(product_name)
    
    flag=False
    while flag==False:
        price=input('Enter the price : ')
        flag=validate_product_price(price)

    flag=False
    while flag==False:
        qty=input('Enter the qty : ')
        flag=validate_product_quantity(qty)   


    item_detail=ItemDetails(product_name,price,qty,user_id) 
    insert_item_details(item_detail)    
    print('successfully created')
 

def validate_product_name(name):
    if name.isalpha():
        if len(name) > 3 and len(name) <=10:
             return True
        else:
          print('name should be more than 3 and less than 10 letters') 
          return False   
    else:
        print("name should contain only alphanumeric")
        return False               

def validate_product_price(price):
    if price.isnumeric():
             return True
    else:
     print("price should contain only numeric")
     return False  

def validate_product_quantity(qty):
    if qty.isnumeric():
             return True
    else:
     print("qty should contain only numeric")
     return False  
