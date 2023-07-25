#drukujemy 3 razy komunikat zawarty w print, az do momentu gdy wartosc osiagnie 3 i nie bedzie wieksza od tej podajen w porownaniu
reminder_count = 0 #
while reminder_count < 3:
    reminder_count += 1
    print('Reminder: Stop the bot!')


#jesli inventory jest wieksze o 0 dodaje jeden produkt do sales i odejmuje jedne z inbventory az vartos bedzie = 0
sales = 0
inventory = 10
while inventory > 0 :
    sales += 1
    inventory -= 1

print(f'Sales: {sales}')
print(f'Inventory: {inventory}')