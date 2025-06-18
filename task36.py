auto_update = input("Auto update (True/False): ") == "True"
mode = input("Enter mode: ")
result = auto_update and mode == "light"
print(result)
