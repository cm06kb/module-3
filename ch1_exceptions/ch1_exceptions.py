#---------------------MODULE 3-------------------------------------------

#----------------chapter 1: exceptions and validations-------------------

#-------------------task 1----------------------------------------------

try:
    f = open("testfile.txt")
    print(x)
except Exception as e:
    print(e)

#the try block above opens textfile and then prints a variable x, but the variable x has not been defined so the except block runs.
    
#--------------------task 2------------------------------------------------

try: 
    f = open("testfile.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close
    
# if no error messages are raised by the try block the else block runs.

#------------------------task 3----------------------------------------------

try:
    f = open("testfile")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("execute finaly...")

#as we have left the .txt on the filename, the except block runs, the else block does not run
#and the inally blcok will run 

try:
    f = open("testfile.txt")
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("execute finaly...")
    
#as we have added the .txt on the filename, the else block runs and the finally block runs



    