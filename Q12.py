#12. Remove a specific key from a dictionary, retrieve all key-value pairs,
#    and check whether a given key exists
#Given Input: car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}


car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

car.pop("color")
print("After removing color:", car)

print("All key-value pairs:", car.items())
print("All keys:", car.keys())
print("All values:", car.values())

if "model" in car:
    print("The key 'model' exists")
else:
    print("The key 'model' does not exist")
