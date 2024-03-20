# alien_0 = {'color':'green','points':5}
# alien_1 = {'color':'yellow','points':10}
# alien_2 = {'color':'green','points':15}
# aliens = [alien_0,alien_1,alien_2]

# for alien in aliens:
#     print(alien)
#Create an empty list for storing aliens.
aliens=[]

#create 30 green aliens 
for alie_number in range(30):
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)

# display the top 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created
print(f"Total number of aliens:{len(aliens)}")

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10

# display the top 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")


for alien in aliens[0:3]:
    if alien['color']=='green':
        alien['color']= 'yellow'
        alien['speed']='medium'
        alien['points']=10
    elif alien['color']=='yellow':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=15

