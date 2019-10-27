"""Restaurant rating lister."""


def get_restaurant_ratings(file):

    restaurant_ratings = {}

    the_file = open(file)

    for line in the_file:
        line = line.rstrip()
        list_line = line.split(":")
        name = list_line[0]
        rating = list_line[1]

        restaurant_ratings[name] = rating

    return restaurant_ratings

#Change for commit

restaurant_ratings = get_restaurant_ratings("scores.txt")
# restaurant_ratings_key_list = sorted(restaurant_ratings)

# for key in restaurant_ratings_key_list:
#     score = restaurant_ratings[key]
#     print("{} is rated at {}.".format(key, score))

new_restaurant_name = input("Enter new restaurant name. ")
new_restaurant_rating = input("Enter rating for {}. ".format(new_restaurant_name))

restaurant_ratings[new_restaurant_name] = new_restaurant_rating

restaurant_ratings_key_list = sorted(restaurant_ratings)

for key in restaurant_ratings_key_list:
    score = restaurant_ratings[key]
    print("{} is rated at {}.".format(key, score))