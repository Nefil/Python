print("Welcome to tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
persons = int(input("How many people to split the bill? "))
per_persons = (bill * tip /100 / persons) + (bill / persons)
print(f"Each person should pay: ${round(per_persons , 2)}")