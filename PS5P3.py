#input phase
principle = float(input("Enter principle"))
years_to_maturity = int(input("Enter years to maturity"))

#process phase
if principle > 100000.00 and years_to_maturity == 5:
  interest_rate = 0.06
elif 50000.00 < principle < 100000.00 and years_to_maturity == 10:
  interest_rate = 0.05
elif 50000.00 < principle < 100000.00 and years_to_maturity == 5:
  interest_rate = 0.04
else: interest_rate = 0.02

first_year_interest = principle * interest_rate

#output phase
print("Principle: ", principle)
print("Interest rate: ", interest_rate)
print("Interest amount for first year: ", first_year_interest)
