# Transfer any number of formal parameters

# def make_pizza(*toppings):
#     """Print all ingredients ordered by the customer"""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')


def make_pizza(size,*toppings):
    """Overview of the pizza to be made"""
    print("\nMaking a {size}-inch pizza with following toppings")
    for toppings in toppings:
        print(f"-{toppings}")
# make_pizza('pepperoni')
# make_pizza('mushrooms','green peppers','extra cheese')

