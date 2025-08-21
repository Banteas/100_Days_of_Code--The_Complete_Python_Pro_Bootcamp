print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(f"Child tickets are ${bill}.")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}.")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}.")
    want_photo = input("Do you want to get a photo?: (y/n) ")
    if want_photo == "y":
        bill += 3
        print(f"Your ticket including a memory photo, will be ${bill}")
    else:
        print(f"Your ticket without a memory photo, will be ${bill}")



else:
    print("Sorry you have to grow taller before you can ride.")
