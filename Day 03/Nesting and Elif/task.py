print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?: "))
    if age < 12:
     print("You have to pay a discounted ticket of 5$")
    elif age <= 18:
        print("You have to pay a discounted ticket of 7$")
    else:
     print("You have to pay the whole ticket of 12$")
else:
    print("Sorry you have to grow taller before you can ride.")
