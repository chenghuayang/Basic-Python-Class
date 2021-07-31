# If
penchan_is_penguin = True
nekokun_is_penguin = False

if penchan_is_penguin:
    print('Penchan is a penguin.')

if True:
    print('Print something here')

if nekokun_is_penguin:
    print('Nekokun is a penguin.')
else:
    print('Nekokun is NOT a penguin.')


nekokun_is_cat = True

if nekokun_is_penguin:
    print('Nekokun is a penguin.')

elif nekokun_is_cat:
    print('Nekokun is a cat!')
else:
    print('Nekokun is NOT a penguin nor a cat.')


# Nested if-else questions

penchan_is_happy = True

if penchan_is_penguin:
    if penchan_is_happy:
        print('Penchan is a happy penguin.')


nekokun_is_worried = False

if nekokun_is_cat:
    if nekokun_is_worried:
        print('Nekokun is a worried cat.')
    else:
        print('Nekokun is not a worried cat.')
else:
    print('Nekokun is not a cat.')





# For loop

for i in range(5):
    print(i)
