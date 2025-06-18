pin = input("Enter PIN: ")
correct_pin = input("Enter correct PIN: ")
result = pin != correct_pin or len(pin) != 4
print(result)
