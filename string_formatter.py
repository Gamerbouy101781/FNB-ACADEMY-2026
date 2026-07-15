first_name = input("Enter first name\n= ").strip()
last_name = input("Enter last name\n= ").strip()
bio = input("Insert bio\n= ").strip()

print("==========================================================================")
username = f"{first_name[0].lower()}{last_name.lower()}"
print(f"username: {username}")

full_name = f"fullname: {first_name.title()} {last_name.title()}"
print(full_name)
print("==========================================================================")

print(f"Bio: {bio}")
print(f"Number of characters: {len(bio)}")
print(f"updated bio: {bio.replace("I am", "I'm")}")

print("==========================================================================")




