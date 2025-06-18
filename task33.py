logged_in = input("Is logged in (True/False): ") == "True"
is_admin = input("Is admin (True/False): ") == "True"
result = logged_in and not is_admin
print(result)
