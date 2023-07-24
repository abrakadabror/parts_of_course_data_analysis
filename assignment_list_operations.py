### Create a List the customers that made purchases on black friday
# The customers that made purchases on Black Friday were:
# C00001, C00003, C00004, C00005 C00006, C00007, C00018, C00010, C00013, C00014, C00015, C00016 and C00029
# Call your list `customer_list`.

customer_list = ['C00001', 'C00003', 'C00004', 'C00005', 'C00006', 'C00007', 'C00018', 'C00010', 'C00013', 'C00014', 'C00015', 'C00016', 'C00029']
'C00009' in customer_list

### Did C00009 make a purchase?
# This customer said they made a purchase we're not seeing it in our data. If they did, we need to record the revenue.
# Write code that returns 99.99 if C00009 is in the list. If not, return 0.0.

if 'C00009' in customer_list:
    print('99.99')
else:
    print('0.0')

('C00009'in customer_list)* 99.99

### Market Research Samples
# 1. Using slicing, create a list containing the fifth and sixth customer in the list called `fifth_sixth`.


fifth_sixth = customer_list[4:6]
print(fifth_sixth)

# 2. Create a list called `every_third` that contains every third customer in the list (1st, 4rd, 7th, and so on...).

every_third = customer_list[0::3]
print(every_third)

# 3. Finally, using slicing, create a list with the last two customers in our dataset, called `last_two`.

last_two = customer_list[-2:]
print(last_two)

