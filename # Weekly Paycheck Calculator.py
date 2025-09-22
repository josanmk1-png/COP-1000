# Weekly Paycheck Calculator

# Input
salary = float(input("Enter weekly salary: "))
numDependents = int(input("Enter number of dependents: "))

# Calculations
stateTax = salary * 0.065
federalTax = salary * 0.28
dependentDeduction = salary * 0.025 * numDependents
totalWithholding = stateTax + federalTax + dependentDeduction
takeHomePay = salary - totalWithholding

# Output
print("State Tax Withheld: $", stateTax)
print("Federal Tax Withheld: $", federalTax)
print("Dependent Deductions: $", dependentDeduction)
print("Salary: $", salary)
print("Take-Home Pay: $", takeHomePay)
