print("Welcome to Tip Calculator")
bill_amount=float(input("Enter bill amount"))
tip=float(input("Enter % of tip "))
n=float(input("How many people to split the bill"))
total_tip=(bill_amount*(tip/100))
total_bill=(bill_amount+total_tip)
split_bill=float(round(total_bill/n ,2))
print(f"Each person has to pay ${split_bill}")
