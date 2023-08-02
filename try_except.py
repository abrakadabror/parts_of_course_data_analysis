# try_except statements
price_list = [5.99, None, 19.99, 24.99, 0, '74.99', 99.99]
# petla do obliczenia ile moge kupic produktow
for price in price_list:
    try:
        # mam jedynie 50 dolarow #zaokmrogalmy dzielenie w dół do najblizszej liczby calkowitej
        affordable_quantity = 50 // price
        print(f' i can buy {affordable_quantity} of these.')
    except:
        print('The price seems to be missing')

# next one appy
price_list = [5.99, None, 19.99, 24.99, 0, '74.99', 99.99]
for price in price_list:
    try:  # sprobuj podzielic 50 przez price i wydrukuj ile moge kupic  majac budzet 50
        affordable_quantity = 50 // price
        print(f' i can buy {affordable_quantity} of these.')
    except ZeroDivisionError:  # w przypadku wystapienia bledu zerodivisionerror poinofmuje przez wydrukowanie, ze produkt jest za darmo
        print('this product is free, i can take as many as i like')
    except:  # jesli vartosc podana w liscie nie jest liczba poinformuj jak nizej
        print('Thats not a number')
