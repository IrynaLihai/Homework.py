def deleteEmployee(employees, chosen_employee):
    for i, employee in enumerate(employees):
        if employee["name"] == chosen_employee:
            employees.pop(i)
            print("Employee deleted successfully!")
            return employees
    print("Employee not found in the list.")
    return employees

def addToDict(my_dict):
    key = input("Enter category word: ")
    value = input("Enter value word: ")
    my_dict[key] = value

def deleteDict(my_dict, employees):
    key_or_employee = input("Do you want to delete a category or a profile? ")
    if key_or_employee == "category":
        key = input("Enter the category to delete: ")
        if key in my_dict:
            my_dict.pop(key)
            print("Category deleted successfully!")
        else:
            print("Category not found in the dictionary.")
    elif key_or_employee == "profile":
        chosen_employee = input("Enter the full name of the employee to delete: ")
        employees = deleteEmployee(employees, chosen_employee)
    else:
        print("Invalid choice! Try again.")
    return my_dict, employees

def searchDict(my_dict):
    searchedItem = input("Enter data for search: ")
    for key, value in my_dict.items():
        if searchedItem in key or searchedItem in value:
            print(f"Data found: {key}: {value}")
            return
    print("Data not found in the dictionary.")

def replaceDict(my_dict):
    key = input("Enter category to make changes: ")
    if key in my_dict:
        new_value = input("Enter the new value: ")
        my_dict[key] = new_value
        print("Value replaced successfully!")
    else:
        print("Category not found in the dictionary.")
    return my_dict

def action_choice(selected_employee, employees):
    while True:
        action = input("What action do you need to do with the library "
                       "(add, delete, search, replace, show dictionary with changes (enter show), "
                       "or enter stop to exit)? - ")
        if action == 'add':
            selected_employee = addToDict(selected_employee)
        elif action == 'delete':
            selected_employee, employees = deleteDict(selected_employee, employees)
        elif action == 'search':
            searchDict(selected_employee)
        elif action == 'replace':
            selected_employee = replaceDict(selected_employee)
        elif action == 'show':
            print("This is the current employees in the library:")
            for employee in employees:
                for key, value in employee.items():
                    print(f"{key}: {value}")
        elif action == 'stop':
            print("Goodbye!")
            break
        else:
            print("Invalid action! Try again!")

def menu(selected_employee):
    while True:
        choice = input("Do you still need to make changes with this person? (Enter 'yes' or 'no'): ")
        if choice == 'yes':
            action_choice(selected_employee)
        elif choice == 'no':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice! Try again!")

def employee_select(employees):
    while True:
        chosen_employee = input("With whom do you need to make changes? (Enter full name or 'stop' to stop): ")
        if chosen_employee == 'stop':
            print("Goodbye!")
            break

        selected_employee = None
        for employee in employees:
            if employee["name"] == chosen_employee:
                selected_employee = employee
                action_choice(selected_employee, employees)

        if selected_employee is None:
            print("Employee not found!")
            continue

def firm():
    dagny = {"name": "Dagny Taggart", "phone": 12343, "email": "dagnytaggart@firm.com", "position": "SEO", "room": 203,
             "skype": "dagnytaggart"}
    francisco = {"name": "Francisco d'Anconia", "phone": 34535, "email": "franciscodanconia@firm.com",
                 "position": "Manager",
                 "room": 204, "skype": "franciscodanconia"}
    john = {"name": "John Galt", "phone": 12743, "email": "johngalt@firm.com", "position": "Developer", "room": 205,
            "skype": "johngalt"}
    hank = {"name": "Hank Rearden", "phone": 17743, "email": "hankrearden@firm.com", "position": "SMM", "room": 206,
            "skype": "hankrearden"}

    employees = [dagny, francisco, john, hank]

    print("These are the current employees in the library:")
    for worker in employees:
        for key, value in worker.items():
            print(f"{key}: {value}")

    while True:
        new_old = input("Do you need to work with a new profile (add someone new)? "
                        "Enter 'yes', 'no', or 'stop' to stop: ")
        if new_old == 'stop':
            print("Goodbye!")
            break
        elif new_old == 'yes':
            new_employee = {}
            new_employee["name"] = input("Enter name: ")
            new_employee["phone"] = input("Enter phone: ")
            new_employee["email"] = input("Enter email: ")
            new_employee["position"] = input("Enter position: ")
            new_employee["room"] = input("Enter room: ")
            new_employee["skype"] = input("Enter Skype: ")
            employees.append(new_employee)
            print("New employee added successfully!")
            print("These are the current employees in the library:")
            for worker in employees:
                for key, value in worker.items():
                    print(f"{key}: {value}")
        elif new_old == 'no':
            employee_select(employees)
        else:
            print("Invalid choice! Try again.")

firm()
