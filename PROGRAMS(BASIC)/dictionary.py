student = {
    "name" : "Rahul",
    "age" : 26,
    "city" : "Ranaghat"
}

#Accessing values
print(student["name"])

#Loop through a dictionary
for k,v in student.items():
    print(k,v)

# in checks dictionary KEYS by default.
if "name" in student:
    print(student["name"])

# Add in dictionary
student["salary"] = 50000
print(student)

# update
# student["age"] = 26