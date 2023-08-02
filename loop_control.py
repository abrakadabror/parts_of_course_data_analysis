# break
subtotals = [15.98, 899.97, 799.97]
revenue = 0

for subtotal in subtotals:
    revenue += subtotal
    print(round(revenue, 2))
    if revenue > 2000:
        break

# continue
item_list = ['ski-extreme', 'snowboard-basic',
             'snowboard-extreme', 'ski-etreme', 'ski-basic', 'snowboard']
snowboards = []
for item in item_list:  # iterujemy
    if 'ski' in item:
        continue  # mozna uzyc jako funkcje skip przeksakujaca o wartosc zawierajaca znaki "ski"
    snowboards.append(item)
print(snowboards)


# pass statement
item_list = ['ski-extreme', 'snowboard-basic',
             'snowboard-extreme', 'ski-etreme', 'ski-basic', 'snowboard']
snowboards = []
for item in item_list:  # iterujemy
    if 'ski' in item:
        pass  # uzywamy aby petla dalej trwala do nastepnej lini kodu
    snowboards.append(item)
print(snowboards)
