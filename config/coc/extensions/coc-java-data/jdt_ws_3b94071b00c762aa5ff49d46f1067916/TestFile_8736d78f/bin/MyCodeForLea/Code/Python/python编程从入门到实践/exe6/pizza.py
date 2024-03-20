#Store information about the pizza you ordered.
pizza = {
        'crust':'thick',
        'topping':['mushrooms','extra cheese']
        }
# Overview of the pizza ordered
print(f"You orderd a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\n+{topping}")
