# program, który oblicza roczny zysk zwiekszony o 5% i dodaje go do stock_portfolio, az do momentu gdy stock przekorczy wartosc 1 000 000

stock_portfolio = 80000
year_counter = 0

while stock_portfolio < 100000:
    investment_income = stock_portfolio * .05
    stock_portfolio += investment_income
    year_counter += 1

    print(f' At the end of year {year_counter}: ' +
          f' My balance is ${round(stock_portfolio, 2)}')

# another example /for instansce
bank_balance = 5000
month_counter = 0

while bank_balance > 0:  # petla trwa, az do momentu gdy bank_balance przestanie byc wiekszy od 0
    spending = 1000
    bank_balance -= spending
    month_counter += 1
    print(f' At the end of month{month_counter}: ' +
          f' My balance is ${round(bank_balance, 2)}')
