list_of_lists = [['a', 'b', 'c'],
                 ['d','e','f'],
                 ['g', 'h', 'i']]
print(list_of_lists)


print(list_of_lists[1]) #odwolanie sie do pierwszego indexu zworic nam cala zagniezdzona liste 

print(list_of_lists[1][1]) #dodanie drugiego indexu zwroci nam poszczegolny element zagniezdzonej listy

list_of_lists[1].append('k') #dodajemy kolejny element do listy o indexie 2
print(list_of_lists)

#jak sprawdzic w nested list jaki index ma drugi element listy = 'b'

element_to_find = 'b'

for i, sublist in enumerate(list_of_lists):
    if element_to_find in sublist:
        index_of_second_element = (i, sublist.index(element_to_find))
        break
print(f" The index of the second element is:{element_to_find} is: {index_of_second_element}")

print(list_of_lists[2].count('h')) #sprawdzamy ile razy wystepuje znak "h" w liscie o indexie 2 (appeears)

#copying a list 
list_of_lists2 = list_of_lists #kopiowanie za pomoca przypisania zmiennej
list_of_lists[1] = ['x','y','z'] #zamiana oryginalnych elementow listy 
#zmiana zostanie odbita w kopii stworzonej przez kopie stworzona przez zlecenie(assigment)
print(list_of_lists2)


#copying with the .copy() method

list_of_lists2 = list_of_lists.copy() #uzywamy metody copy do stworzenia dupilkatu listy
list_of_lists[0] = ['x', 'y','z'] #zamieniamy cala liste zagniezdzaona w indexie 0 na podane wartosci
print(list_of_lists2)


list_of_lists[0][1] = 'oh no!' #zmieniamy drugi element w liscie o indexie 0
print(list_of_lists)

#deepcopy function tworzy calkiem nowa kopie listy (entirely)
from copy import deepcopy

list_of_lists = [['a', 'b', 'c'],
                 ['d','e','f'],
                 ['g', 'h', 'i']]
list_of_lists2 = deepcopy(list_of_lists)
list_of_lists[0][1] = 'oh no'
print(list_of_lists2)

