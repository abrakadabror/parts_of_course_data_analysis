# program z wykorzystaniem petli for do przeliczania kurus usd na euro
exchange_rate = 0.88
usd_list = [5.99, 9.99, 19.99, 24.99, 99.99]
value_list = []

for value in usd_list:
    print(round(value * exchange_rate, 2))

for value in usd_list:
    value_list.append(round(value * exchange_rate, 2))
print(value_list)
