def calculate_tax(income):
    if income <= 250000:
        return 0
    elif income <= 400000:
        return  (income - 250000) * 0.15 
    elif income <= 800000:
        return 22500 + (income - 400000) * 0.20
    elif income <= 2000000:
        return 102500 + (income - 800000) * 0.25
    elif income <= 8000000:
        return 402500 + (income - 2000000) * 0.30
    else:
        return 2202500 + (income - 8000000) * 0.35

def compute_tax():
    annual_income = float(input("Enter your annual income: "))
    tax = calculate_tax(annual_income)
    print("Your annual tax is: ", format(tax,'.2f'))
    print("Your monthly tax is: ", format(tax/12,'.2f'))

compute_tax()
