import json 

def get_stored_username():
    '''如果存储了用户名就获取他'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    '''问候用户，并指出其名字'''
    username = get_stored_username()
    if username:
        print(f"Welcome back,{username}!")
    else:
        username = input('What is your name?')
        filename = 'user.json'
        with open(filename,'w') as f:
            json.dump(username,f)
            print('We will remember you when you come back,{username}！')

greet_user()

