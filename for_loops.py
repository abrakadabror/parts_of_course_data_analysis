# for loop przeliczajacy dolary na euro
exchange_rate = 0.88
usd_list = [5.99, 9.99, 19.99, 24.99, 99.99]
euro_list = []
for value in usd_list:
    euro_list.append(round(value * exchange_rate, 2))
print(euro_list)

# for loop durkujacy litery ze slowa Maven
word = 'Maven'
for letter in word:
    print(letter)

#
customer_rating = [
    '5 stars', '3 stars', '5 stars', '4 stars', '4 stars',
    '1 star', '4 stars', '5 stars', '2 stars', '5 stars']
print(tuple(customer_rating))  # drukujemy tuple
print(list(customer_rating))  # drukujemy liste

# wybieramy element  z listy numer 0 o zerowym indexie 0
rating = int(customer_rating[0][0])
print(rating)  # drukujemy wynik

numeric_rating = []  # tworzymy pusta liste

for rating in customer_rating:  # kod przetwarza kazdy element w liscie customer_rating
    # we wnetrzu petli kod pobiera pierwszy znak z kazdego elementu  i zamienia na integer
    numeric_rating.append(int(rating[0]))
print(numeric_rating)

# drukujemy sume z numeric rating podzielona przez ilosc elementow w tej liscie
print(sum(numeric_rating) / len(numeric_rating))
