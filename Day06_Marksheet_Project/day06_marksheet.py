import time 
# Mark Sheet
def mark_sheet() :
    for i in range(3,0,-1) :
      print (f"Wate Your Marksheet Almost Ready {i}")
      time.sleep(2)
      
    print (f"\n\nStudent Name : {name.capitalize()}")
    print("--------------------------")
    print ("MARK SHEET")
    print("--------------------------")
    print (f"SUBJECT : {subject_1}-----MARKS : {marks_1}")
    print (f"SUBJECT : {subject_2}-----MARKS : {marks_2}")
    print (f"SUBJECT : {subject_3}-----MARKS : {marks_3}")
    print (f"--------------------------------------------------")
    print (f"                          TOTAL : {total_marks}")
    print (f"                          AVERAGE : {ave}")
    if ave >= 80 :
                        print (f"Grade -- A") 
    elif ave >= 60 :
                        print (f"Grade -- B")
    elif ave >= 40 :
                        print (f"Grade -- C")
        
    else :
                        print (f"Faill !")
                        print ("You Can Do It")

    
    
print ("------------------------")
print("Welcome Back")
print ("------------------------")
while True :
    name = input ("Enter The Student Name :")
    
    subject_1 = input("Enter First Subject Name :")
    marks_1 = int(input("Enter The Marks :"))
    
    subject_2 = input("Enter Secound Subject Name :")
    marks_2 = int(input("Enter The Marks :"))
    
    subject_3 = input("Enter Thard Subject Name :")
    marks_3 = int(input("Enter The Marks :"))
    
    total_marks = marks_1 + marks_2+ marks_3
    ave = total_marks/2
    if ave >= 80 :
        print (f"Grade -- A")
        show_mark_sheet = input("Do You Want To See Your Mark Sheet (y/n) :").lower().strip()
        if show_mark_sheet == "y" :
          mark_sheet()
        elif show_mark_sheet == "n" :
          print ("Good Bye !")
        else :
          print ("Invalid Choice ")
    elif ave >= 60 :
        print (f"Grade -- B")
        show_mark_sheet = input("Do You Want To See Your Mark Sheet (y/n) :").lower().strip()
        if show_mark_sheet == "y" :
          mark_sheet()
        elif show_mark_sheet == "n" :
          print ("Good Bye !")
        else :
          print ("Invalid Choice ")
    elif ave >= 40 :
        print (f"Grade -- C")
        show_mark_sheet = input("Do You Want To See Your Mark Sheet (y/n) :").lower().strip()
        if show_mark_sheet == "y" :
          mark_sheet()
        elif show_mark_sheet == "n" :
          print ("Good Bye !")
        else :
          print ("Invalid Choice ")
    else :
        print (f"Faill !")
        show_mark_sheet = input("Do You Want To See Your Mark Sheet (y/n) :").lower().strip()
        if show_mark_sheet == "y" :
          mark_sheet()
        elif show_mark_sheet == "n" :
          print ("Good Bye !")
        else :
          print ("Invalid Choice ")
    end = input("Do You Want To Continue (y/n)")
    if end != "y" :
      print("Program End !")
      break
    
