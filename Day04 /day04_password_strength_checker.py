# what is my project today 
# Day 4 - Password Strength Checker 
# small latter , capital latter, number ,special syambol
# This is my Day 4 project of 100 Days of Python Challenge

# Take inout
Password = input("Enter Your Password ")

# chake
has_upper = False
has_lower = False
has_digit = False
has_sepcial = False

special_chars = "!@#$%^&*"
# user input True/False
for ch in Password :
    if ch.isupper() :
      has_upper = True 
    elif ch.islower() :
      has_lower = True
    elif ch.isdigit() :
      has_digit = True
    elif ch in special_chars :
      has_sepcial = True

length = len(Password) # finde Password length 

# chake user input Password type

if length >= 8 and has_upper and has_lower and has_digit and has_sepcial :
    print (" Password er Strength :- STRONG")
elif length >= 6 and has_lower and has_digit :
    print (" Password er Strength :- MEDIUM")
else :
    print (" Password er Strength :- WEAK")
    
