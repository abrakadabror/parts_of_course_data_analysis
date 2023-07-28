# Sales Tax

# We need to calculate the sales taxes for our customer that made three transactions in `multi_order_customers` below.
# (The customer that made three transactions was customer C00001). Run this cell to create the list.

multi_order_customers = [
    [1799.94, 29.98, 99.99],
    [15.98, 119.99],
    [24.99, 24.99],
    [649.99, 99.99],
    [599.99, 399.97]
]

# Create a tuple from the first element in the `multi_order_customers`.
# Unpack this tuple into the variables `transaction1`, `transaction2`, and `transaction3`.
# Once you've have separated the transactions, calculate the tax of .08 rounded to 2 decimals and print it.

print(multi_order_customers[0])
transaction1, transaction2, transaction3 = tuple(multi_order_customers[0])

print(round(transaction1 * .08, 2))
print(round(transaction2 * .08, 2))
print(round(transaction3 * .08, 2))
