import os


class EmployeeApplication:
    def __init__(self):
        self.EMPLOYEE_DIR = "saikiran"
        self.EMPLOYEE_FILE = os.path.join(self.EMPLOYEE_DIR, "employee.txt")

    def validate_name(self, name):
        if not all(char.isalpha() or char.isspace() for char in name):
            raise ValueError("Name must contain only alphabets and spaces.")
        return ' '.join(word.capitalize() for word in name.split())

    def validate_age(self, age):
        age = int(age)
        if age < 18 or age > 60:
            raise ValueError("Age must be between 18 and 60.")
        return age

    def get_designation_salary(self):
        roles = {"Programmer": 25000, "Manager": 20000, "Tester": 15000}
        designation = input("Enter designation (Programmer / Manager / Tester): ").capitalize()
        if designation not in roles:
            raise ValueError("Invalid designation.")
        return designation, roles[designation]

    def ensure_directory(self):
        if not os.path.exists(self.EMPLOYEE_DIR):
            os.makedirs(self.EMPLOYEE_DIR)

    def save_employee(self, name, age, designation, salary):
        self.ensure_directory()
        with open(self.EMPLOYEE_FILE, "a") as f:
            f.write(f"{name},{age},{designation},{salary}\n")

    def display_employees(self):
        if not os.path.exists(self.EMPLOYEE_FILE):
            print("No employee records found.")
            return
        with open(self.EMPLOYEE_FILE, "r") as f:
            for line in f:
                name, age, designation, salary = line.strip().split(",")
                print(f"Name: {name}, Age: {age}, Designation: {designation}, Salary: {salary}")

    def raise_salary(self):
        if not os.path.exists(self.EMPLOYEE_FILE):
            print("No employee records found.")
            return
        name_to_update = input("Enter name of the employee: ").capitalize()
        
        while True:
            try:
                percent = float(input("Enter percent hike (max 30): "))
                if percent < 0 or percent > 30:
                    print("Error: Hike must be between 0 and 30.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid number.")
                continue

        updated = False
        lines = []
        with open(self.EMPLOYEE_FILE, "r") as f:
            for line in f:
                name, age, designation, salary = line.strip().split(",")
                if name.lower() == name_to_update.lower():
                    new_salary = int(int(salary) * (1 + percent / 100))
                    lines.append(f"{name},{age},{designation},{new_salary}\n")
                    updated = True
                else:
                    lines.append(line)

        if updated:
            with open(self.EMPLOYEE_FILE, "w") as f:
                f.writelines(lines)
            print(f"Salary updated for {name_to_update}.")
        else:
            print(f"Employee '{name_to_update}' not found.")

    def create_employee(self):
        while True:
            try:
                name = self.validate_name(input("Enter your name: "))
                age = self.validate_age(input("Enter your age: "))
                designation, salary = self.get_designation_salary()
            except ValueError as e:
                print("Input error:", e)
                continue

            choice = input("Continue? (Y/N): ").strip().upper()
            if choice == "Y":
                self.save_employee(name, age, designation, salary)
                print("Employee saved successfully.\n")
            elif choice == "N":
                self.save_employee(name, age, designation, salary)
                print("Employee Details:")
                print(f"Name: {name}, Age: {age}, Designation: {designation}, Salary: {salary}")
                print("Employee saved successfully.\n")
                break
            else:
                print("Invalid input. Going back to main menu.")
                break

    def run(self):
        while True:
            print("\n===== ATM EMPLOYEE APPLICATION =====")
            print("1. Create Employee")
            print("2. Display Employees")
            print("3. Raise Salary")
            print("4. Exit")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
                continue

            if choice == 1:
                self.create_employee()
            elif choice == 2:
                self.display_employees()
            elif choice == 3:
                self.raise_salary()
            elif choice == 4:
                print("Thanks for using this application!")
                break
            else:
                print("Invalid choice. Try again.")


def main():
    app = EmployeeApplication()
    app.run()


if __name__ == "__main__":
    main()