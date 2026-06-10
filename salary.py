try:
    monthly_salary = float(input("Enter your monthly salary: "))
    if (monthly_salary < 0):
        raise ValueError("Salary cannot be negative.")
    annual_salary = monthly_salary * 12
    print("Your annual salary is: ₹{:.2f}".format(annual_salary))   
except ValueError:
    print("Invalid input. Please enter a valid number for monthly salary.")