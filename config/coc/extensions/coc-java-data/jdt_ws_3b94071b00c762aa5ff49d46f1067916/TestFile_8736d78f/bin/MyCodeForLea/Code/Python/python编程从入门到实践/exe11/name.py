from name_function import get_formatted_name

print("Enter 'q' to quit.")
while True:
    first = input('\nPlease give me a first name: ')
    if first == 'q':
        break
    last = input('Please gime a last name: ')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print(f"\tNearly formatted name:{formatted_name}")
