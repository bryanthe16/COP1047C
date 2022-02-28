tax_rate = 0.20
standard_deduction = 10000.0
dependent_deduction = 3000.0

gross_income = float(input("Enter the gross income: "))
num_dependents = int(input("Enter the number of dependents: "))

taxed_income = gross_income - standard_deduction - dependent_deduction * num_dependents
income_tax = taxed_income * tax_rate

print("The income tax is $" + str(income_tax))

