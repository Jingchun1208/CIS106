#input phase
stock_ticker_symbol = input("Enter stock ticker symbol")
number_of_share = float(input("Enter number of share"))
cost_per_share = float(input("Enter cost per share"))

#process phase
amount_invested = number_of_share * cost_per_share

#output phase
print("Amount invested: ", amount_invested)
