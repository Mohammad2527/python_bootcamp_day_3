print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print(f"child tickets are ${bill}.")
        
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    elif age >= 45 and age <=55:
        print("Everything is going to be ok. have a free ride on us!")
        
    elif age > 18:
        bill = 12
        print(f"Adult tickets are ${bill}.")

    want_photos = input("Do you want to take photos? Y or N\n")

    if want_photos == "Y" or want_photos == "y": #or "y":
        bill += 3
    
    print (f"Your total bill is ${bill}")
#     else:
#         print (f"Your total bill is ${bill}")      
              
else:
    print("Sorry, you have to grow taller before you can ride.")


