resquest_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for resquest_toppings in resquest_toppings:
    print(f"adding{resquest_toppings}.")
print('\nFinsihed making your pizza')

resquest_toppings = []
if resquest_toppings:
    for resquest_topping in resquest_toppings:
        print(f"adding{resquest_topping}")
    print("\nFinsihed your pizza")
else:
    print('are you sure you want a pizza ?')
