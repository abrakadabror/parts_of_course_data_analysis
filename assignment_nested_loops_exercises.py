# Exercise description:
# We need to apply a 10% discount to every transaction in the list below.
# Assign the discounted transactions to a new list: discounted_prices

orders_c00001 = [1799.94, 29.98, 99.99]
orders_c00004 = [15.98, 119.99]
orders_c00006 = [24.99, 24.99]
orders_c00008 = [649.99, 99.99]
orders_c00010 = [599.99, 399.97]

multi_order_customers = [
    [1799.94, 29.98, 99.99],
    [15.98, 119.99],
    [24.99, 24.99],
    [649.99, 99.99],
    [599.99, 399.97]
]

multi_order_customers


discounted_prices = []  # definujemy pusta liste o nazwie dis...
# definujemy liste, ktora zawiera kwoty zamowien(order)
for customer in multi_order_customers:
    # definiujemy pusta liste o nazwie customers_discounts aby moc przechowywac kazda przeceniona transakcja
    customers_discounts = []
    print(customer)  # drukujemy
    # w wewnatrz peli zewentrznej uruchamiamy petele wewntrzna aby przeksj przez kazda transakcje na liscie zamowie klienta(customer)
    for transaction in customer:
        # przeliczamy przecenione transakcje i dodajemy do pustej  listy customers_discounts
        customers_discounts.append(round(transaction * .9, 2))
    # dodajemy customers_discounts do listy discounted_prices.
    discounted_prices.append(customers_discounts)
print(discounted_prices)
