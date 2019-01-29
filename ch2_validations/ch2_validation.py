#--------------chapter 2 : validation -----------------------------------





#-----------------------task 1------------------------------------------------

#print ("What’s your age?")
#Age = input()
#Age = input("What’s your age? ")
#
#
##-----------------------task 2------------------------------------------------
#
#print ("What’s your age?")
#age = int(input())
#type(age)
#Option = input("Please input yes or no ").lower()
#
#
##-----------------------task 3------------------------------------------------
#
#def create_password():
#    password = input("please enter a password, this must be more than 6 characters but less than 12: ")
#    check_password_len(password)
#
#def check_password_len(password):  
#    if len(password) in range(6, 12):
#        print("thank you")
#    else:
#        print("I'm sorry, that password is not between 6-12 digits long, try again")
#        create_password()
#
#create_password()
#
##------------------task 4----------------------------------------------
#
##print("***choice***")
##print("1. Display my name")
##print("2.Display my age")
##print("2.Display my city")
##choice = 0
##choice = int(input("what is your choice? "))
##
##while choice<1 or choice> 3:
##    choice = int(input("what is your choice? "))
##
##if choice==1:
##    print("ms wu")
##elif choice == 2:
##    print("5 years old")
##elif choice == 3:
##    print("London")
#
##---------------------task 5---------------------------------------------
#    
##we can use a try/exception block to handle incorrect data type input/
#
#print("***choice***")
#print("1. Display my name")
#print("2.Display my age")
#print("2.Display my city")
#choice = 0
#
#
#while True:
#    try:
#        while choice<1 or choice> 3:
#            choice = int(input("what is your choice? "))
#        break  
#    except ValueError:
#        print("please type a number!")
#    
#if choice==1:
#    print("ms wu")
#elif choice == 2:
#    print("5 years old")
#elif choice == 3:
#    print("London")

#-------Task 7: OOP and Validation------------------------------------


#class Spam(object):
#    def __init__(self, description, value):
#         if not description or value <=0:
#             raise ValueError
#         self.description = description
#         self.value = value
#
#
#s = Spam('s', 5)
#t = Spam("t", -1)
#
#
#print(s.value)
#print(t.value)


#-------Task 8: OOP and Validation------------------------------------

#can achieve the same using an assert keyword


class Spam(object):
    def __init__(self, description, value):
        assert description != ""
        assert value >0
        self.description = description
        self.value = value

s = Spam('s', 5)
t = Spam("t", -1)


print(s.value)
print(t.value)




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    