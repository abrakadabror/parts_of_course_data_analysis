new_items = ['Coat', 'Backpack', 'Snowpants'] #mozna zmieniac elementy zbioru, ale nie dodawad uzywajac ponizszej metody
new_items[1] = 'Gloves'
print(new_items)

item_list = [ 'Snowboard', 'Boots', 'Helmet', 'Googles', 'Bindings'] #append dodajemy element do naszej listy na samym koncu
item_list.append('Coat')
print(item_list)

item_list = [ 'Snowboard', 'Boots', 'Helmet', 'Googles', 'Bindings'] #coat zostal dodany jako czwarty element w liscie
item_list.insert(3, 'Coat')
print(item_list)

item_list = [ 'Snowboard', 'Boots', 'Helmet', 'Googles', 'Bindings']  #dodajemy trzy nowe pozyycje w nowej liscie all_items
new_item_list= ['Coat', 'Backpack', ' Snowpants']
all_items = item_list + new_item_list #dodajemy listy do siebie
print(all_items)
print(all_items *3) #mnozymy liste elementwo w liscie razy 3


new_items = ['Coat', 'Backpack', 'Snowpants'] #usuwamy pozycje od 2 indexu do 3 wlacznie
del new_items[1:3]
print(new_items)

new_items = ['Coat', 'Backpack', 'Snowpants'] #usuwamy pozycje o nazwie 'Coat'
new_items.remove('Coat')
print(new_items)

#cwiczenia DEMO

customer_ids = ['C00001', 'C00003','C00005', 'C00010'] #0, 1, 2 , 3 - idexy
print(customer_ids)

customer_ids[1] = 'C00004' #1 oznacza drugi element zbioru
print(customer_ids)

customer_ids.append('C00011') #dodajemy kolejna pozycje w liscie 
print(customer_ids)

customer_ids.insert(1, 'C00003') #dodajemy kolejny element zbioru listy na drugiej pozycji 
print(customer_ids)

new_customer_ids = ['C00012', 'C00015'] 
all_customers = customer_ids + new_customer_ids # dodajemy nowe elementy do listy customer_ids tworzac liste all_customers
print(all_customers)

del all_customers[1] #kasujemy pozycje numer 1 czyli 'C00003' z pomoca del

print(all_customers)

if 'C00001' in all_customers: #warunek logiczny jesli C00001 jest w zbiorze all_customers to usun C00005
    all_customers.remove('C00005')
print(all_customers)

