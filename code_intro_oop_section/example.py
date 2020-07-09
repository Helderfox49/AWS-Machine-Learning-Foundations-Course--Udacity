from shirt import Shirt
from shirt import  Jean

shirt_one = Shirt('orange', 'S', 'long sleeve', 45)
shirt_two = Shirt('red', 'XL', 'short sleeve', 30)


print(shirt_one.color)
print(shirt_two.price)

shirt_two.change_price(23)
print(shirt_two.price)

print(shirt_one.discount(.1))

shirt_one.color = 'purple'
shirt_one.size = 'L'
shirt_one.price = 38

jean_one = Jean('red', 'L', 70)
print(jean_one.color)
print(jean_one.size)
print(jean_one.price)
