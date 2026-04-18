try:
    user_input1 = int(input("Please enter first number"))
    user_input2 = int(input("Please enter first number"))

    result = user_input1/user_input2
    print(result)
except ZeroDivisionError:
    print("You can not divide a number by 0.")
except ValueError:
    print("Please enter a valid number")
