salary = int(input("Enter your salary: ₹"))
allowance = int(input("Enter allowance: ₹"))
tax = int(input("How much tax deducted?: ₹"))

print(f"Total salary + allowance is: ₹{salary + allowance}")
print(f"In hand salary is ₹{salary + allowance - tax}")