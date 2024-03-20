# 2023/04/09 22:49:52
favourite_language = {
        'jen':['python','ruby'],
        'sarah':['c'],
        'edward':['ruby','go'],
        'phil':['python','haskell'],
        }
for name ,languages in favourite_language.items():
    print(f"\n{name.title()}'s favourite language are:")
    for language in languages:
        print(f"\t{language.title()}")
