# Day 5 Project - Contact Book Management System
# empty dictnory
contacts = {}
# main menu
def options() :
    print ("------Contac Book Menu ------")
    print ("1.Add Contact ")
    print ("2.show Contact ")
    print ("3.Search Contac By Name ")
    print ("4.Exit ")
    print (" Choice (1-4)")

while True :
      options ()
      choice = input("Enter Your Choice :").lower().strip()

# Add New contact
      if choice == "1" :
          name = input("Enter Name :")

          if name in contacts :
              print(" Contact already exasits")


          else :
              phone = input("Enter Mobile  :").strip()
              email = input("Enter Email :").strip()
              contacts[name] = {
                  "phone" : phone,
                  "email" : email
              }
              print ("Contact save succesfuly")

# Show All Contact
      elif choice == "2" :
          if not contacts :
              print ("not contacts available")
          else :
              for name,info in contacts.items() :
                  print ('All Contacts ')
                  print (f"Name : {name.title()}")
                  print (f"Phone : {info['phone']}")
                  print (f"Email : {info['email']}")

# search contact by name
      elif choice == "3" :
          search_name = input("Enter name to search :").lower().strip()

          if search_name in contacts :
              info = contacts[search_name] 
              print ("contac found")
              print (f"Name : {search_name.title()}")
              print (f"Phone : {info['phone']}")
              print (f"Email : {info['email']}")
          else :
              print ("contacts not found")

# Exit 
      elif choice == "4" :
          print ("Program End !")
          print ("Good Bye ")
          break
# Invalid Coice 
      else :
          print ("invalid choice ")



