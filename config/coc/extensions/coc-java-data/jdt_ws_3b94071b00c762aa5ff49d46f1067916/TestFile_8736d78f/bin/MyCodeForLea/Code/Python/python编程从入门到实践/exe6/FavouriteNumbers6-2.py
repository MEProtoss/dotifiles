favouritenumbers={'a':'1','b':'2','c':'3','d':'4','e':'5','f':'3'}

for name,number in favouritenumbers.items():
    print(f"{name.title()}'s favourite number is {number.title()}.")
for name in favouritenumbers.keys():
    print(name.title())

for name in favouritenumbers:
    print(name.title())

friends = ['a','c']
for name in favouritenumbers.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        num = favouritenumbers[name].title()
        print(f"\t{name.title()},I see you lovw {num}")

if 'wo' not in favouritenumbers.keys():
    print("wo,please take our poll!")

print("the following numbers have been mentioned ")
for num in favouritenumbers.values():
    print(num.title())
print("the following numbers have been mentioned:")
for num in set(favouritenumbers.values()):
    print(num.title())

