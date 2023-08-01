# program, który oblicza roczny zysk zwiekszony o 5% i dodaje go do stock_portfolio, az do momentu gdy stock przekorczy wartosc 1 000 000

stock_portfolio = 80000
year_counter = 0

while stock_portfolio < 100000:
    investment_income = stock_portfolio * .05
    stock_portfolio += investment_income
    year_counter += 1

    print(f' At the end of year {year_counter}: ' +
          f' My balance is ${round(stock_portfolio, 2)}')
