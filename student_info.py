first_name = input("First name\n= ")
surname = input("Surname\n= ")
age = int(input("Age\n= "))
favourite_num = float(input("Favourite number\n= "))

print(f"UPPERCASE: Welcome, {first_name.upper()} {surname.upper()}")
print(f"TITLECASE: Welcome, {first_name.title()} {surname.title()}")
print(f"Age in months: {age*12}")
print(f"Favourite num: {round(favourite_num)}")

print(f"{type(first_name)}")
print(f"{type(surname)}")
print(f"{type(age)}")
print(f"{type(favourite_num)}")


