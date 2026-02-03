# Stores employee details
# Calculates salaries
# Applies deductions
# Generates payslips
# Produces payroll reports

#importing employee details
import csv

employee_details = []

with open("employee_details.csv", newline = '') as details:
    reader = csv.DictReader(details)
    for row in reader:
         employee_details.append(row)

print(employee_details)



basic_salary = employee_details.Salary
def salary_calculator(basic_salary):
    # basic_salary = 
    commision = 0.5 * basic_salary
    gross_salary = int(basic_salary + commision)
    global gloss_salary
    print(f"The gross salary is Ksh: {gross_salary}")

def deduction_calculator(gross_salary):
        sha = 0.1 * gross_salary
        taxes = 0.2 * gross_salary
        rent = 0.3 * gross_salary
        total_deductions = sha + taxes + rent
        print(f"Your total deductions for this month is {total_deductions}")

deduction_calculator(200)
salary_calculator(20000)
