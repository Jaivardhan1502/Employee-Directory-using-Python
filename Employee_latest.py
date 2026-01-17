  # Enhanced Employee Directory System with Display All Employees

# Initialize employee records with Indian names
employee_records = {
    201: {'info': (201, 'Amit'), 'department': 'HR', 'skills': {'Communication', 'Recruitment'}},
    202: {'info': (202, 'Priya'), 'department': 'Engineering', 'skills': {'Python', 'Machine Learning'}},
    203: {'info': (203, 'Rahul'), 'department': 'Engineering', 'skills': {'Java', 'System Design'}},
    204: {'info': (204, 'Neha'), 'department': 'Marketing', 'skills': {'SEO', 'Content Writing'}},
    205: {'info': (205, 'Vikram'), 'department': 'Engineering', 'skills': {'Python', 'DevOps'}},
    206: {'info': (206, 'Sneha'), 'department': 'Sales', 'skills': {'Negotiation', 'Presentation'}},
}

# Function to search employees by skill
def search_by_skill(skill):
    result = []
    for record in employee_records.values():
        if skill in record['skills']:
            result.append(record['info'])
    return result

# Function to search employees by department
def search_by_department(department):
    result = []
    for record in employee_records.values():
        if record['department'].lower() == department.lower():
            result.append(record['info'])
    return result

# Function to display employee info (basic)
def display_employees(employee_list):
    if not employee_list:
        print("No employees found.")
    else:
        print("\n--- Employee List ---")
        for emp in employee_list:
            print(f"ID: {emp[0]}, Name: {emp[1]}")
        print("---------------------")

# Function to display all employees with details
def display_all_employees():
    if not employee_records:
        print("No employee records available.")
    else:
        print("\n=== All Employee Records ===")
        for record in employee_records.values():
            emp_id, name = record['info']
            department = record['department']
            skills = ', '.join(record['skills'])
            print(f"ID: {emp_id}, Name: {name}, Department: {department}, Skills: {skills}")
        print("=============================")

# Function to add a new employee
def add_employee():
    try:
        emp_id = int(input("Enter new employee ID: "))
        if emp_id in employee_records:
            print("Employee ID already exists!")
            return

        name = input("Enter employee name: ")
        department = input("Enter department: ")
        skills_input = input("Enter skills (comma separated): ")
        skills_set = set(skill.strip() for skill in skills_input.split(','))

        employee_records[emp_id] = {
            'info': (emp_id, name),
            'department': department,
            'skills': skills_set
        }

        print(f"Employee {name} added successfully!")

    except ValueError:
        print("Invalid input. Please enter correct values.")

# Function to display menu
def show_menu():
    print("\n=== Employee Directory Menu ===")
    print("1. Search by Skill")
    print("2. Search by Department")
    print("3. Add New Employee")
    print("4. Display All Employees")
    print("5. Exit")
    print("===============================")

# Main program loop
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            skill = input("Enter skill to search: ")
            employees = search_by_skill(skill)
            display_employees(employees)

        elif choice == '2':
            department = input("Enter department to search: ")
            employees = search_by_department(department)
            display_employees(employees)

        elif choice == '3':
            add_employee()

        elif choice == '4':
            display_all_employees()

        elif choice == '5':
            print("Exiting Employee Directory. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

# Run the program
if __name__ == "__main__":
    main()
