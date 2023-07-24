size_in_stock = ['XS', 'S', 'L', 'XL', 'XXL']

if 'M' in size_in_stock:
    print("I'll take the medium please.")
elif 'S' in size_in_stock:
    print("It'll be tight but small will do.")
else:
    print("I'll wait until you have medium.")


#example of list

item_list = ['Snowboard', 'Boots','Helmet', 'Googles', 'Bindings']
print(item_list[0].lower())
print(item_list[3].lstrip('G')) #poda nam 4 element z listy liczac od 0 jako snowboard
#zamieniamy 'Boots' na 'Jeans'
modyfied_list = [item.replace('Boots', 'Jeans')for item in item_list] 
print(modyfied_list)

#drukujemy jedynie 3 pierwze elementy z listy
item_list = ['Snowboard', 'Boots','Helmet', 'Googles', 'Bindings']
print(item_list[:3]) 

print(item_list[::2]) #pobiera co drugu element z listy
print(item_list[2:4]) #pobiera 3 element o indexie 2(statrtujemy od zera) 
#pobiera tez 4 element o indexie 3(rowniez statrujemy od zera)

#tworzenie rozpakowanej listy. Rozumiane przez to, ze lista item_list zawiera
#dokladnie trzy elementy i sa one przypisane do trzech wartosci s,b,h.
item_list = ['Snowboard', 'Boots', 'Helmet']
s, b ,h = item_list
print(s, b, h)