import string
import secrets

length = 12
password = ""

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(length): #repeats the process 12 times
    random_character = secrets.choice(characters) #choice() = Randomly selects each characters from the loop
    password+=random_character

print(password)

