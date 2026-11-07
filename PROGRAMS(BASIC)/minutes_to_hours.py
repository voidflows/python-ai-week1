minutes = int(input("Enter number in minutes : "))
hours = minutes // 60 # // = floor divison
seconds = minutes % 60  # % = modulus or finding remainder
print(f"{minutes} = {hours} hours {seconds} sec") # f"" = formatted string