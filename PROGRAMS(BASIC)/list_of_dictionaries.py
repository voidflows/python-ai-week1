# A list can hold multiple dictionaries. Syntax = [{},{},...]

students = [{
    "name" : "Rahul",
    "marks" : 90,
    "skills" : ["Python","SQL"]
},
{"name" : "Trisha",
 "marks" : 95,
 "skills" : ["Economics","Finance"]
}]

#Accessing values
print(students[0]) # students[0] = Select the first dictionary in the list.
print(students[0]["name"]) # students[0]["name"] = Inside that dictionary, read the value of the name key.
print(students[0]["skills"][1]) # students[0]["skills"][1] = First dictionary → skills list → second item (Java).

#Loop through every dictionary
for student in students:
    print(student["name"] , student["marks"])

# Rule: in checks list elements, but checks dictionary keys (not values). For dictionary values, use .values().




