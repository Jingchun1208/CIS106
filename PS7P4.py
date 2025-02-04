#input phase
f = open("Code/PS7P4.txt", "r")

count = 0
total_extended_price = 0

item = f.readline().rstrip('\n')

#process phase
while item != "":
    quantity = float(f.readline())
    price = float(f.readline())
    extended_price = quantity * price
    total_extended_price = total_extended_price + extended_price
    count = count + 1
    #output phase
    print("Item is: ", item)
    print("Quantity is: ", quantity)
    print("price is: ", price)
    print("Extended price is: ", extended_price)
    item = f.readline().rstrip('\n')

average = total_extended_price / count

#output phase
print("Total extended price: ", total_extended_price)
print("Number of orders: ", count)
print("Average order: ", average)
