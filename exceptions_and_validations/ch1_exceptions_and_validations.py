#---------------------MODULE 3-------------------------------------------

#----------------chapter 1: exceptions and validations-------------------

#-------------------task 1----------------------------------------------

e = "anything wrong"
try:
    f = open("testfile.txt")
    s1 = not_exists
except Exception as e:
    print(e)
    