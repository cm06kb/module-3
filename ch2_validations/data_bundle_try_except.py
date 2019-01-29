# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:52:48 2018
@author: Kate Sorotos
"""

"""ch02_Data Bundle Purchase_validation"""


import time 

def passwordCheck(truePasscode, balance):
    count = 3
    while True:
        try:
            while count > 0:
                password_attempt = int(input('Please enter your password: '))
                if password_attempt != truePasscode:
                    count = count -1
                    print(str('Password incorrect - You have ' + str(count) + ' attempts left'))
                elif password_attempt == truePasscode:
                    print('Password OK')
                    DataBundlePurchase(truePasscode, balance)
            break
        except ValueError:
            print('Error: please make your choice by entering a number')
    print('Transaction cancelled - You have used up all of your attempts')
    


def DataBundlePurchase(truePasscode, balance):
        time.sleep(1)
        
        print('\nTo request your balance enter "1"')
        print('To purchase data enter "2"')
        print('To top up your account enter "3"')
        
        time.sleep(1)
        
        transactionType = 0
        while True:
            try:
                while transactionType < 1 or transactionType > 3:
                    transactionType = int(input('Please enter your choice: '))
                break
            except ValueError:
                print('Error: please make your choice by entering a number')
                
        print()
        
        if transactionType == 1:
            print('Your balance is: £{}'.format(balance))
            
            print('Would you like another service? ')
            print('Type "y" for yes or "n" for no ')
            restart_option(truePasscode, balance)
            
        
        elif transactionType == 2:
            checkNumber(truePasscode, balance)
        elif transactionType == 3:
            topUp(truePasscode, balance)
        
def restart_option(truePasscode, balance):
    restart = ""
    while True:
        try:
            while restart != 'y' or restart != 'n':
                restart = input('Please enter your choice: ')
                if restart == 'y':
                    DataBundlePurchase(truePasscode, balance)
                elif restart == 'n':
                    print('Thanks, have a nice day!')
                else: 
                    print('Please make a valid response to continue')
                    restart_option(truePasscode, balance)
            break
        except ValueError:
            print('Error: please make your choice by entering "y" or "n"')  
    
        
        
                    
def retryPassword(truePasscode, balance):
    print('Type "y" for yes or "n" for no')
    retry = input().lower()
    if retry == 'y':
        DataBundlePurchase(truePasscode, balance)
    else:
        print('Thanks, have a nice day!')
    
    
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
    
def checkNumber(truePasscode, balance):
    phone_number = '1' 
    phone_number_2 = '2'
    while True:
        try:
            while phone_number != phone_number_2:
                phone_number = int(input('Please enter your phone number to proceed: '))
                phone_number_2 =  int(input('Please re-enter your phone number: ')) 
                if phone_number != phone_number_2:
                    print('Error - The numbers you have entered do not match.')
                    checkNumber(truePasscode, balance)
                elif phone_number == phone_number_2:
                    dataAmount(truePasscode, balance)
            break
        except ValueError:
            print('Error - Please type a number to continue')



def dataAmount(truePasscode, balance):
    max = 100.00
    print('>>The maximum amount you are able to top up by is £100')
    print('>>Your top-up amount must be a multiple of 5')
    print()
    time.sleep(1)
    print('You have £' + str(balance) + ' remaining in your balance. \nHow much money would you like to top up by? ')
    money = 1
    new_balance = round(balance - money,2)
    
    while True:
        try:
            while money > 0:
                money = int(input())
                if money > max:
                    print('I\'m afraid you are only able to top up by £100 or less')
                    time.sleep(1)
                    print('Transaction cancelled')
                elif money > balance:
                    print('Amount greater than available balance.')
                    time.sleep(1)
                    print('Transaction cancelled')
                elif money %5!=0:
                    print('Your top-up amount must be a multiple of 5.')
                elif money == int(money/5)*5:
                    print('Thanks for your purchase. You now have £' + str(new_balance) + ' left in your account.')
                    time.sleep(1)
                    print('Would you like another service? ')
                    print('Type "y" for yes or "n" for no')
                    restart = input().lower()
                    if restart == 'y':
                        DataBundlePurchase(truePasscode, balance)
                    else:
                        print('Thanks, have a nice day!')
            break
        except ValueError:
            print('Error - Please enter a numerical value to continue.')
            dataAmount(truePasscode, balance)

        
    
def topUp(truePasscode, balance):
    print('\nYour current balance is £' + str(balance))
    time.sleep(1)
    amount = 1
    balance = balance + amount
    while True: 
        try:
            while amount > 0:
                amount = int(input('How much would you like to top-up by today? £ '))
                print('You have topped up your account by £' + str(amount) + '\nYour balance is now £' + str(balance)) 
                time.sleep(1)
                print('\nWould you like another service? ')
                print('Type "y" for yes or "n" for no')
                restart = input().lower()
                if restart == 'y':
                    DataBundlePurchase(truePasscode, balance)
                else:
                    print('Thanks, have a nice day!')
        except ValueError:
            print('Error - Please enter a numerical value to continue.')
            topUp(truePasscode, balance)
    
passwordCheck(1234, 34.55)
