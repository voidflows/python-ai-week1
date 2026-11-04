# 1. Write a python program to display a user entered name followed by Good Afternoon using input() function.

user_name = input("Enter your name : ")
print(f"Good afternoon,{user_name}")

# 2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>","Rahul").replace("<|Date|>","04/11/26"))

#3. 3. Write a program to detect double space in a string.
sentence = "Learning   Python"
print(sentence.find("  "))
print(sentence.find("Python"))

#4. Replace the double space from problem 3 with single spaces.
print(sentence.replace("  "," "))

#5. Write a program to format the following letter using escape sequence characters.
print("Dear Harry,\n\tthis python course is nice. \nThanks!")




