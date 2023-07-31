# Customer Promos
# We're working on some fun promotional giveaways for our next big sale.
# We want to generate a few different sequences of lucky numbers - customers who get lucky will receive a keychain, coffee mug, or beanie!
# Coffee mugs will be given to even numbered vistors in our first 10 visitors, please generate a sequence of even integers between 1 and 10.

customers_range = range(2, 11, 1)
print(list(customers_range))
# wybieramyco drugiego klienta z listy od 2 do 12 ze skokiem co 2 pozycje
print(list(range(2, 12, 2)))

# Now generate a sequence of odd integers from 1 and 10. They'll get keychains.

print(list(range(1, 11, 2)))

# Finally, every 7th customer in our first 100 vistors will receive a beanie.
# Generate a sequence of integers containing multiples of 7 from 1 to 100.

print(list(range(7, 100, 7)))
