# Make sure it converts the string in the list below into a float. Print a warning that this was string data. Then process as usual.
# Also, have the loop skip any instances of None data type.
# Then, remove the generic except statement to avoid processing errors.
# Finally, change the hard coded value 50 into a variable so we can change this value based on each customer's budget.


price_list = [5.99, None, 19.99, 24.99, 0, '74.99', 99.99]
budget = float(input('What is the budget for the purchase?: '))
total_info = []

for price in price_list:
    if price is None:
        print("Warning: Found None data type - skipped")
        continue
    try:
        affordable_quantity = budget // price
        print(f"I can buy {affordable_quantity} of this item.")
    except ZeroDivisionError:
        print("This product is free, I can take as many as I like.")
    except TypeError:
        affordable_quantity = budget // float(price)
        print(f"I can buy {affordable_quantity} of this item.")
    except Exception:
        print(f"Warning: Invalid price '{price}'. Skipping the item.")

    total_info.append(price)

print(total_info)
