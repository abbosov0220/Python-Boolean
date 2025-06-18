logged_in = input("Logged in (True/False): ") == "True"
session_time = int(input("Enter session time: "))
result = not logged_in or session_time == 0
print(result)
