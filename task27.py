in_stock = input("In stock (True/False): ") == "True"
on_delivery = input("On delivery (True/False): ") == "True"
result = in_stock or on_delivery
print(result)
