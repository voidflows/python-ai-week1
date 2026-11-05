# Dictionary = Key-Value pairs.Unordered,mutable,no duplicate keys,index based.Denoted by {}

student = {
    "name" : "Rahul",
    "Age" : 26
}
print(student.items()) #items() = Returns all key-value pairs
print(student.get("Age")) #get() = Gets the value for a key
print(student.keys()) #keys() = Returns all keys
print(student.values()) #values() = Returns all values
print(student.pop("Age")) #pop() = Removes a key and returns its value
print(student.popitem()) #popitem() = Removes and returns the last inserted pair
student.update({"Profession" : "IT"}) #update() = Adds or updates key-value pairs
print(student)

new_student = student.copy() #copy() = creates a copy
new_student = {"name" : "Trisha"}
print(new_student)

students = {"name": "Rahul"}

students.setdefault("age", 25)
students.setdefault("name", "Amit")

print(students)