exchange_rate = 0.88
usd_list = [5.99, 9.99, 19.99, 24.99, 99.99]

euro_list = []

for i in range(len(usd_list)):
    euro_list.append(round(usd_list[i] * exchange_rate, 2))
print(euro_list)

euro_list = [5.27, 8.79, 17.59, 21.99, 87.99]
item_list = ['Snowboard', 'Boots', 'Helmet', 'Googles', 'Bindings']

for i in range(len(euro_list)):
    print(f' The {item_list[i].lower()} costs {euro_list[i]} euros.')

inventory = [10, 14, 10, 15, 8, 27]
prices = [2.99, 99.99, 219.99, 89.99, 29.99, 9.99]


for i in range(len(inventory)):

    #     print(f' We have got {inventory[i]} in price {prices[i]} euros')
    print(round(inventory[i] * prices[i], 2))

product_values = []

for i in range(len(inventory)):
    product_values.append(round(inventory[i] * prices[i], 2))
print(product_values)


print(sum(product_values))

for index, element in enumerate(euro_list):
    print(index, element)

euro_list = [5.27, 8.79, 17.59, 21.99, 87.99]
item_list = ['Snowboard', 'Boots', 'Helmet', 'Goggles', 'Bindings']

for index, element in enumerate(euro_list):
    print(item_list[index], element)

item_names = [
    'Keychain', 'Helment', 'Snowboard',
    'Ski Poles', 'Sweetshirt', 'Boots'
]
inventories = [10, 14, 10, 15, 8, 27]
prices = [2.99, 99.99, 219.99, 89.99, 29.99, 9.99]


product_values = []  # deklarujemy pusta liste

for i in range(len(inventories)):
    product_values.append(round(inventories[i] * prices[i], 2))
print(product_values)
print(sum(product_values))

product_values = []  # deklarujemy pusta liste

for i, inventory in enumerate(inventories):
    product_value = round(inventory * prices[i], 2)
    product_values.append(product_value)
    print(f'We have ${product_value} worth of {item_names[i]}.')
print(product_values)
print(sum(product_values))
