current_users = ['cHp', 'ch', 'Gj', 'dzi', 'npi']
new_users = ['chp', 'cH', 'a', 'b', 'c']
current_userscp = []
for current_user in current_users:
    current_userscp.append(current_user.lower())
print(current_userscp)
for new_user in new_users:
    if new_user in current_userscp:
        print(f'this name {new_user} has been used')
    else:
        print("success!")
