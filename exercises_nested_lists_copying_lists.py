# Multi Order Customers

# We want to understand our multi order customers.
# Below are lists of transactions made by our companies that made multiple orders this weekend.

orders_c00001 = [1799.94, 29.98, 99.99]
orders_c00004 = [15.98, 119.99]
orders_c00006 = [24.99, 24.99]
orders_c00008 = [649.99, 99.99]
orders_c00010 = [599.99, 399.97]

# VIP List
# Create a nested list where each element is one of the customer transaction lists above, called `vip_list`


vip_list = [orders_c00001, orders_c00004,
            orders_c00006, orders_c00008, orders_c00010]
print(vip_list)

# Some of us are curious about customer C00001, given that they made three transactions.
# Report the second and third transactions they made.

vip_list = [orders_c00001[1:3]]
print(vip_list)

print(vip_list[0][1:0])

# Revenue Adjusted List

# We need to make a copy of our `vip_list`. We need to change an entire list inside that we DON'T want reflected in `vip_list`.
# Call the copy `revenue_adjusted_list`.

# kopiujemy cala liste bez zmieniania dnaych w liscie
revenue_adjusted_list = vip_list.copy()
print(revenue_adjusted_list)

# Once you have your copy, change both of customer C00004's transaction values to 0.0.
# These were gifts and shouldn't be recorded as revenue. Make sure to confirm `vip_list` hasn't changed!

# zmieniamy obie zmienne w drugim indexie[1]na 0
revenue_adjusted_list[1] = (0.0, 0.0)
print(revenue_adjusted_list)

# our original list should be unchanged
