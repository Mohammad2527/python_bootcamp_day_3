# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆


if (year % 4 == 0):
  if (year % 100 != 0 ):
     print ("Leap year.")
  elif (year % 100 == 0) and (year % 400 != 0):
    print("Not Leap year.")
  elif (year % 100 == 0) and (year % 400 == 0):
    print("Leap year.")
else:
    print("Not leap year")