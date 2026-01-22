
while True :
    print ("Odd/Even Number Chaker ")
    print("------------------------------------------")
    num = int(input("Enter Your Number :"))
    
    if num % 2 == 0 :
        print (f"{num} Is Even")
        choice = input (f"Do You Want To see {num} Even Number (y/n)").lower().strip()
        if choice == "y" :
          print (f"{num} Odd Numbers ")
          print ("--------------------------")
          for i in range (1,num+1) : 
            if i % 2 == 0 :
              
              print (i)
            
        elif choice == "n" :
          print ("Program End !")
          break
        else :
          print ("Invalid choice ")
    else :
        print (f"{num} Is Odd")
        choice = input (f"Do You Want To See {num} Odd Numbers (y/n)").lower().strip() 
        if choice == "y" :
          print (f"{num} Odd Numbers ")
          print ("--------------------------")
          for i in range (1,num+1) : 
            if i % 2 != 0 :
              print (i)
        elif choice == "n" :
          print ("Program End !")
          break
        else :
          print ("Invalid Choice ")
        
      
    ask = input ("Do You Want To Continue (y/n)")
    if ask != "y" :
      print ("Good Bye !")
      break
