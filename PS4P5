#input phase
last_name = input("Enter last name")
number_of_dependents = float(input("Enter number of dependents"))
gross_income = float(input("Enter gross income"))

#process phase
adjust_gross_income = gross_income - number_of_dependents * 12000.00
if adjust_gross_income > 50000.00:
  tax_rate = 0.20
else: tax_rate = 0.10
income_tax = adjust_gross_income * tax_rate
if income_tax < 0.00:
  income_tax = 100.00

#output phase
print("Last name: ", last_name)
print("Gross income: ", gross_income)
print("Number of dependents: ", number_of_dependents)
print("Adjusted gross income: ", adjust_gross_income)
print("Income tax: ", income_tax)
