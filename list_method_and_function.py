transaction = [10.44, 20.56, 200.14, 1242.66, 2.07, 8.01]

print(len(transaction)) #podaje ilosc elementow w liscie
print(sum(transaction)) #podaje sume
print(min(transaction)) #podaje minimalna 
print(max(transaction)) #podaje max wartosc z listy
      
print(sorted(transaction)) #sortuje bez przestawiania danych w oryginalnej liscie

print(transaction.index(20.56))  #zwraca info ktory to index w liscie

print(transaction.count(10.44)) #zlicza ile razy dana wartosc wystetpuje w liscie
print(transaction.reverse())   #obraca wartosci w odworoconej kolejnosci
print(transaction)