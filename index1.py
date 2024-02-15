employee_dict = {}

while True:
    name = input("Enter employee name: ")
    if name.lower() == 'no':
        break
    salary = float(input("Enter employee salary: "))
    employee_dict[name] = salary

print("\nEmployee Data:")
print(employee_dict)