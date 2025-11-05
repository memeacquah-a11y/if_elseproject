print ("Welcome to the rollercoaster ride. How may we be of help today!!")
height =int(input("What is your height in cm? "))
bill =0

if height >= 120:
    print("You can ride the rollercoaster")
    age= int(input("What is your age?"))
    if age <= 12:
        bill= 5
        print("Child tickets are $5.")
    elif age <= 18:
     bill = 18
     print("Please pay $18")
    elif age >= 45 and age <=55:
       print("Everything is on us.")
    else:
     bill = 25
     print("Please pay $25")

    wants_photo = input("Do you want to have a photo take? type y for Yes and n for No.")
    if wants_photo == "y":
       bill += 3
       print(f"You owe an additional $3.You're final bill is {bill}  ")
else:
     print("Sorry, you're too short for the ride")

number_to_check= int(input("What is the number you want to check?"))
if number_to_check %2 ==0:
   print("The number is even")
else:
    print("The number is odd")
print("The end")