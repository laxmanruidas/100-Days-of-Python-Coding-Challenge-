 # what is my project today '
# Day 3 - Number Guessing Game 
# Computer vs Human 
# This is my Day 3 project of 100 Days of Python Challenge
from random import randint
 # ----
print("------------------------------------------------------------------------")
print("Welcome To Computer vs Human Number Guessing Funy Game :")
print("------------------------------------------------------------------------")

# Game Lavel
print ("1. Easy -- (1,15)")
print ("2. Medium -- (1,30)")
print ("3. Hard -- (1,50)")
print ("4. Exit")
choice = int(input("Which game mode do you want to play (1,2,3) : "))

# Easy Lavel
if choice == 1 :
    attempts = 0
    computer = randint(1,15)
    while True :
      human = int(input("Guess The Number :"))
      attempts += 1
      if computer == human :
        print("Correct Answer ")
        print(f"You hit the at {attempts} Times")
        break
      elif human > computer :
        print("HINT :- Too High")
      elif human < computer :
        print("HINT :- Too Low")
      else :
        print ("Invalid")

 
# Medium Lavel
elif choice == 2 :
    attempts = 0
    computer = randint(1,30)
    while True :
      human = int(input("Guess The Number :"))
      attempts += 1
      if computer == human :
        print("Correct Answer ")
        print(f"You hit the at {attempts} Times")
        break
      elif human > computer :
        print("HINT :- Too High")
      elif human < computer :
        print("HINT :- Too Low")
      else :
        print ("Invalid")
#  Hard Level
elif choice == 3 :
    computer = randint(1,50)
    attempts = 0
    while True :
      print ("Computer - 1 to 50")
      human = int(input("Guess The Number :"))
      attempts += 1
      if computer == human :
        print("Correct Answe ")
        print(f"You hit the at {attempts} Times")
        break
      elif human > computer :
        print("HINT :- Too High")
      elif computer < human :
        print("HINT :- Too Low")
      else :
        print ("Invalid")
elif choice == 4 :
    print ("Program End !")
    
else :
    print("Invalid choice")
