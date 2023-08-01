# program z wykorzystaniem petli for do przeliczania kurus usd na euro
exchange_rate = 0.88
usd_list = [5.99, 9.99, 19.99, 24.99, 99.99]
value_list = []

for value in usd_list:
    print(round(value * exchange_rate, 2))

for value in usd_list:
    value_list.append(round(value * exchange_rate, 2))
print(value_list)


# another mini program to iterate over the value
iterable = 'Maven'
for letter in iterable:
    print(letter.upper().lstrip('M').rstrip('N'))

#looping over list 
customer_ratings = ['5 stars', '3 stars', '5 stars', '4 stars', '1 star', '4 stars', '5 stars', '2 stars', '5 stars']

rating = int(customer_ratings[0][0]) #wyciaglamy pierwszy element listy o indexie 0 i drukujemy
print(rating)

empty_list_rating = [] #tworzymy pusta liste
for rating in customer_ratings:
    empty_list_rating.append(int(rating[0]) #dodajemy element to pustej listy empty_list
print(empty_list_rating) #drukujemy wyniki

print(round(sum(empty_list_rating) /len(empty_list_rating),1)) #obliczmay srednia i zaaokrogalmy do pierwszego miejsca po przecinku

#Looping Over Indices & Multiple Iterables

exchange_rate = 0.88
usd_list = [5.99, 9.99, 19.99, 23.99, 34.99 ]

euro_list = [] #tworzymy pusta liste

for i in range(len(usd_list)):
    euro_list.append(round(usd_list[i] * exchange_rate, 2)) #dodajemy do pustej listy przeliczone elementy z usd_list * exchaneg_rate
print(euro_list) #drukujemy wynik
 

euro_list = [5.29, 9.19, 19.69, 23.39, 34.29]
item_list = ['Snowboard', 'Boots', 'Helmet', 'Googles', "Bindings"]

for i in range(len(euro_list)): #w zakresie ilosci elementow znajdujacyh sie w liscie euro_list drukujemy:
    print(f'The {item_list[i].lower()} costs ${euro_list[i]}') 