import json 
def greet_user():
    """问候用户，并指出其名字。"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your names ?")
        with open(filename,'w') as f:
            json.dump(username,f)
            print(f"We will remember you when you come back,{username}!")
    else:
        print(f"Welcome back,{username}")

greet_user()


def get_stored_username():
    """If the username is stored, obtain it"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """Greet the user and indicate their name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back , {username}!")
    else:
        username = input("What is your name?")
    filename = 'username.json'
    with open(filename,'w') as f:
        json.dump(username,f)
