assigment = '98. ASSIGNMENT: List Methods & Functions'
print(assigment.lower().replace(' ', '_').replace(':','').lstrip('98._'))

### Black Friday Data
# We've compiled lists of the black friday `customer_ids` and `subtotals`, the amount before tax, below

customer_ids = [
    'C00004', 'C00007', 'C00015', 'C00016', 'C00020',
    'C00010', 'C00006', 'C00001', 'C00003', 'C00014',
    'C00001', 'C00001', 'C00005', 'C00008', 'C00013',
    'C00004', 'C00017', 'C00019', 'C00002', 'C00008',
    'C00021', 'C00022', 'C00006', 'C00018', 'C00018',
    'C00010', 'C00016'
]

subtotals = [
    15.98, 899.97, 799.97, 117.96, 5.99,
    599.99, 24.99, 1799.94, 99.99, 254.95,
    29.98, 99.99, 25.98, 649.98, 89.99,
    119.99, 599.99, 649.98, 24.99, 99.99,
    99.99, 5.99, 24.99, 999.96, 99.99,
    399.97, 89.99
]

### Calculate the Average Transaction
# Calculate the average value of the transactions in the list  `subtotals`.
# We don't have an average function, so we might need to use sum() and len() to do so. 

amount_subtotals = len(subtotals)
sum_subtotals = sum(subtotals)
print(sum_subtotals)
print(amount_subtotals)
avg_subtotals = sum_subtotals/ amount_subtotals
print(avg_subtotals)

### Customer Deep Dive
# How many transactions did customer C00010 make?

print(customer_ids.count('C00010'))

# What is the index of customer C00010's first transaction?

print(customer_ids.index('C00010'))

# What is the revenue of C00010's first transaction? 

We will need to index `subtotals` using the index returned in the last question.

print(subtotals[5])

### Print a sorted list of customer ID's.
# We want to scan this to see if any of our loyal customers didn't make a purchase.
# Don't change `customer_ids` when you sort!

customer_ids.sort()
print(customer_ids)

