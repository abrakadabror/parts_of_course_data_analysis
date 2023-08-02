value = '126. ASSIGNMENT: While Loops'
print(value.lstrip('126. ').replace(' ', '_').lower().replace(':', ''))

# description of the issue:
# We currently have 686 pairs of skis in inventory, and sell 84 each month.
# Write a program that keeps track of monthly inventory, by subtracting 84 pairs of skis from inventory each month.
# Your program should print 'At the end of month x, we have y pairs of inventory', where x is the number of months that has gone by and y is the remaining inventory at that month.
# If inventory goes negative, your program should stop running.

current_inventory = 686
monthly_sales = 84
month = 0  # startujemy od zera
while current_inventory > 0:  # jesli current_investory jest wieksze od zera to wykonujemy ponizsze dzialanie
    # odejmujemy (subtract) od curent_investory miesieczna sprzedaz czyli monthly_sales
    current_inventory -= monthly_sales
    month += 1  # dodajemy jeden miesiac przy wykonaniu condition/warunku
    # drukujemy {month} ilosc miesiecy ile uplynelo a {current_inventor} to pozostaly zapas towaru
    print(f' At the end of month {month}' + f' we have {current_inventory}')
