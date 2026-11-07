values = [10,20,30,40,50,50,60,70,80,80]
unique = sorted(set(values),reverse=True)

#unique = set(values)
#unique_numbers = sorted(unique,reverse = True)

if len(unique)>=2:
    print(f"Second highest = {unique[1]}")
else:
    print("No second distinct highest number")