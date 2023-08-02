items = ['skis', 'snowboards', 'googgles', 'boots']  # lista with products

item_reviews = [['5 star', '1 star', '3 stars'],
                ['5 stars', '4 stars'], ['4 stars', '2 stars'], ['1 star']]  # list with rates of products

item_reviews_num = []  # pusta lista / empty list
for item in item_reviews:
    integer_ratings = []  # pusta lista/ empty list
    for review in item:
        integer_rating = int(review[0])  # zamieniamy na integer
        # dodajemy do pustej listy integer_ratings = []
        integer_ratings.append(integer_rating)
    # dodajemy do pustej listy item_reviews_num = []
    item_reviews_num.append(integer_ratings)
    print(integer_ratings)
print(item_reviews_num)

for item in item_reviews_num:
    print(sum(item)/len(item))  # obliczamy srednia
