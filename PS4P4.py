#input phase
name = input("Enter name")
cost_of_appliance = float(input("Enter cost of appliance"))

#process phase
if cost_of_appliance > 1000.00:
  warrantee_cost = 0.10 * cost_of_appliance
else: warrantee_cost = 0.05 * cost_of_appliance 

total = cost_of_appliance + warrantee_cost

#output phase
print("Name: ", name)
print("Cost of appliance: ", cost_of_appliance)
print("Cost of warrantee: ", warrantee_cost)
print("Total: ", total)
