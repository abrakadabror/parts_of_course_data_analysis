new = 'ASSIGNMENT: Adding List Elements'
print(new.lower().replace(' ', '_').replace(':',''))


assignment_adding_list_elementsz

### Updated Customer Lists

Hi there, we need to add customer 'C00009' to `customer_list`, we just found their receipt in the warehouse.

I've included the original `customer_list` below.

customer_list = [
    'C00001', 'C00003', 'C00004','C00005', 'C00006', 
    'C00007', 'C00008', 'C00010', 'C00013', 'C00014', 
    'C00015', 'C00016', 'C00020'
]

customer_list.append('C00009')
print(customer_list)
customer_list.insert(7, 'C00009')
print(customer_list)

### Adding Saturday Customers

Add the customers from `saturday_list` to `customer_list` below.

saturday_list = [
    'C00004', 'C00017', 'C00019', 'C00002', 'C00008',
    'C00021', 'C00022'
]

new_list = saturday_list + customer_list
print(new_list)

