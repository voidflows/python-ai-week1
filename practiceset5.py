# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

__dict__ = {
    "Namaste" : "Hello",
    "Pyaar" : "Love",
    "Dost" : "Friend",
    "Sundar" : "Beautiful",
    "Sapna" : "Dreams"
}
word = input("Enter the word you want the meaning of : ")
print(__dict__[word]) #__dict__["Pyaar"] = Love (Output)

# 2. Write a program to input eight numbers from the user and display all the unique numbers(once).

s=set()

n1 = int(input("Enter number 1 : "))
s.add(n1)

n2 = int(input("Enter number 2 : "))
s.add(n2)

n3 = int(input("Enter number 3 : "))
s.add(n3)

n4 = int(input("Enter number 4 : "))
s.add(n4)

n5 = int(input("Enter number 5 : "))
s.add(n5)

n6 = int(input("Enter number 6 : "))
s.add(n6)

n7 = int(input("Enter number 7 : "))
s.add(n7)

n8 = int(input("Enter number 8 : "))
s.add(n8)

print(s)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s = {18,'18'}
print(s)

# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s)) # 2

# 5. 
s = {}
#What is the type of 's'?
print(type(s)) #Empty dictionary

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

names = {}

lang1 = input("Enter language 1 : ")
name1 = input("Enter name 1 : ")
names.update({name1:lang1})

lang2 = input("Enter language 2 : ")
name2 = input("Enter name 2 : ")
names.update({name2:lang2})

lang3 = input("Enter language 3 : ")
name3 = input("Enter name 3 : ")
names.update({name3:lang3})

lang4 = input("Enter language 4 : ")
name4 = input("Enter name 4 : ")
names.update({name4:lang4})

print(names)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
#Ans = The latest value will be taken if both names are same

# 8. If languages of two friends are same; what will happen to the program in problem 6?
#Ans = Both the values will be printed

# 9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
s[4][0] = 9
#Ans = No (we cannot include list inside set and sets are immutable)