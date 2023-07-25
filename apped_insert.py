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