repeat = True

while repeat:
    try:
        first_number = int(input("Please enter first number: "))
        second_number = int(input("Please enter second number: "))
        operator = input("Please enter an operator [+,-,*,/]: ")

        match operator:
            case "+":
                result = first_number + second_number
            case "-":
                result = first_number - second_number
            case "*":
                result = first_number * second_number
            case "/":
                result = first_number / second_number
            case _:
                print("Please enter a valid operator.")
                continue  # go to the next loop iteration

        print(f"Your answer is: {result}")

    except ValueError:
        print("Please enter valid numbers.")
        continue
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        continue

    choice = input("Do you want to calculate more? [y]: ")
    if choice.strip().lower() != "y":
        repeat = False
        
       