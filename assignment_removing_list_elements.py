variable_01 = "ASSIGNMENT: Removing List Elements"
print(variable_01.lower().replace(' ', '_').replace(':', ''))


# We now need to remove the Saturday customers from the list. 
# I've included the full `customer_list` below.
# The Saturday customers are the final seven customers in `customer_list`. 

customer_list = [
    'C00001', 'C00003', 'C00004', 'C00005', 'C00006',
    'C00007', 'C00008', 'C00009', 'C00010', 'C00013', 
    'C00014', 'C00015', 'C00016', 'C00020', 'C00004', 
    'C00017', 'C00019', 'C00002', 'C00008', 'C00021',
    'C00022'
]

lenght = len(customer_list)
print(lenght)
customer_updated_list = len(customer_list) - 7
customer_updated_lis02 = len(customer_list)
del customer_list[customer_updated_list: customer_updated_lis02]
print(customer_list)



### Delete a friend

# Please remove customer 'C00004' from the reduced list you just created. This is a friend of the owner and shouldn't be recorded as a sale.

del customer_list[2]
print(customer_list)

customer_list = customer_list[:-7]
print(customer_list)

