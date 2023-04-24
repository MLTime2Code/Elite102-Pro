
import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'example', password = 'SQL1Sh4rd2USE*')

cursor = connection.cursor()


testQuery = ("SELECT * FROM user_table")

 

cursor.execute(testQuery)

 

for item in cursor:

    print(item)

 

cursor.close()

connection.close()


def home():
  
  print('Welcome!')
  print()
  print('1--Log In')
  print('2--Create an account')
  print('3--Exit')
  print()
  print(choice)
  choice = input('What would you like to do?')
  #if I put the choice here, error appears
  #if choice is place outside of fucntion, choice is asked then the menu appears and no matter the choice, it will not function as expected
  
  if choice == 1:
     print('Please input your username and PIN')
     print('Usernam: ')
     print('PIN: ')
  elif choice == 2:
     print('A username and PIN will be randomly generated for you.')
  elif choice == 3:
     exit()
  else:
     print('1,2, & 3 are your only options. Try again.')
     return home


home()

def menu():
    print('1--Check Balance')
    print('2--Deposit')
    print('3--Withdraw')
    print()
    print(decision)
    decision = input('What would you like to do?')
    if decision == 1:
       print()#return balance
    elif decision == 2:
       print()#return deposit
    elif decision == 3:
       print()#return
    else:
       print('1,2, & 3 are your only options. Try again.')
       
    


#def balance():
  #retrieve info from SQL??
  #shows balance
  #only option is to exit and return to menu

#def deposit():
  #asks for user input on money
  #user can only add positive whole numbers (for simplicity)
  #cannot exceed 9999
  #exit option to return to menu


#def withdraw():
  #asks for user input
  #deciding between only allowing positive whole numbers that will convert to negative(if that is possible)
  #OR allowing only negative digits (user will have to manually put the - along with their number)
  


