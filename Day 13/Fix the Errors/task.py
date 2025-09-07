
while True:
    try:
        age = int(input("How old are you?"))
        break
    except ValueError:
        print("You have typed an invalid number, please try again.")


if age > 18:
    print(f"You can drive at age {age}.")
