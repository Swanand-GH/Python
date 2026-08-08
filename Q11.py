#11. Add a new key-value pair to a dictionary, modify an existing value, and access a specific key
#Given Input: student = {"name": "Alice", "age": 20, "grade": "B"}


student = {"name": "Alice", "age": 20, "grade": "B"}

student["city"] = "New York"
print("After adding city:", student)

student["grade"] = "A"
print("After modifying grade:", student)

print("Student name:", student["name"])
