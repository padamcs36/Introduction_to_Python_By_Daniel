import random

card_points = ['Ace','2', '3', '4', '5', '6', '7', '8', '9', '10','Jack','Queen','King']
card_signs = ['Heart', 'Diamond', 'Clubs', 'spade']
random_point = random.choice(card_points)
random_sign = random.choice(card_signs)
print(f"The card you picked  is the {random_point} of {random_sign}")

month = ["jan","Fab","March","dec","Nov","May","June","July","August"]
random_month = random.choice(month)
print(random_month)