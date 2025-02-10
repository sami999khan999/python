from item import Item

products = [
    {"name": "Laptop", "price": 850.99, "quantity": 5},
    {"name": "Smartphone", "price": 599.49, "quantity": 10},
    {"name": "Headphones", "price": 49.99, "quantity": 25},
    {"name": "Tablet", "price": 399.99, "quantity": 7},
    {"name": "Smartwatch", "price": 199.99, "quantity": 15},
]

Item.create_instences(products)

print(Item.all)
item1 = Item.all[0]

item1.name = "abc"


print(item1.name)
