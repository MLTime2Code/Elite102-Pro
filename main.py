
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

  if choice == 1:
     print('Please input your username and PIN')
     print('Usernam: ')
     print('PIN: ')
  elif choice == 2:
     print('A usernam and PIN will be randomly generated for you.')
  elif choice == 3:
     exit()
  else:
     print('1,2, & 3 are your only options. Try again.')
     return home




def menu():
    print('1--Check Balance')
    print('2--Deposit')
    print('3--Withdraw')
    print()
    print(decision)
    decision = input('What would you like to do?')
    
    

#def balance():

#def deposit():


#def withdraw():

