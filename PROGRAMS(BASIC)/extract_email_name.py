email = "i.rahulmondal07@gmail.com"
if "@" in email:
    parts = email.split("@")[0] #split divides wherever it finds the matching character
    # parts = email.split("@") = ['i.rahulmondal07', 'gmail.com'] as output
    print(parts)
else:
    print("Invalid Email")