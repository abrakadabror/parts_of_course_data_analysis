# Nasted loops

# example

item_list = ['Snowboard', ' Boots']
size_list = ['small', 'medium', 'large']

for item in item_list:
    for size in size_list:  # najpierw petla for sprawdza czy dla elementu "Snowboard"  z item_list jest dostepny rozmiar small kolejno medium i nastepnie large.
        # po czym petla for sprawdza dla kolejnego elementu z listy item_list 'Boots' te same wartosci
        print(f' {item} is available in {size}.')
