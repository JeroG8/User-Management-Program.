# Main
import functions as mod

print("Welcome to User Management System.\n" \
"1) Create User.\n" \
"2) Search User.\n" \
"3) Update User.\n" \
"4) Delete User.\n" \
"5) Exit Program.\n")

users = {}

while True:
    option_choosed = input("Choose an option from above: ")
    if option_choosed == "1":
        print(f"You choose option {option_choosed} Creat user.")
        doc = (input("Document: ")).strip()
        name_surname = input("Name and surname: ").strip().title()
        age = input("age: ").strip()
        sex = input("Sex (Male or female): ").strip().title()

        print(mod.create_user(users, doc, name_surname, age, sex))

    elif option_choosed == "2":
        print(f"You choose option {option_choosed} Search user.")
        doc = input("Document: ").strip()

        print(mod.search_user(users,doc))

    elif option_choosed == "3":
        print(f"You choose option {option_choosed} Update user.")
        doc = input("Document: ").strip()
        name_surname = input("New name and surname (leave empty to skip): ").strip()
        age = input("New age (leave empty to skip): ").strip()
        sex = input("Nex sex (leave empty to skip): ").strip()

        print(mod.update_user(users,doc,name_surname,age,sex))
        
    elif option_choosed == "4":
        print(f"You choose option {option_choosed} Delete user.")
        doc = input("Document: ").strip()

        print(mod.delete_user(users,doc))

    elif option_choosed == "5":
        print(f"You choose option {option_choosed} Exit program.")
        print("Goodbye!")
        break
    else:
        print("Write a number 1-5 with option you'd like to use.")