#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

print("Welcome to Amr's Tip Calculator")

Bill = input("What was the total bill? ")

Tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

People = input("How many people are splitting the bill? ")

TipAmt = "1." + Tip

BilldPeople = float(Bill)/int(People)

PricepPerson = round(float(BilldPeople)*float(TipAmt), 2)

print(f"Each person should pay {PricepPerson}")