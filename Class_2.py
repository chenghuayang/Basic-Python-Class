# List
box_1 = []
box_2 = [0, 1]
box_3 = [10, 20]

print(box_3[0])
print(box_3[1])
box_3[0] = 15
print(box_3)
print()


# String
# In Nekokun's house.

house_owner = 'Nekokun'
visitor = 'Penchan'

party_time = '12:00'
party_location = 'Nekokun\'s house'
num_of_onigili = 5
num_of_anpan = 2

print('There is a party in ', party_location, '. It will start at', party_time,
      '. The owner is', house_owner, ', and the visitor includes', visitor, '. They will have',
      num_of_onigili, 'onigilis and', num_of_anpan, 'anpans.')

print('There is a party in ' + party_location + '. It will start at ' + party_time +
      '. The owner is ' + house_owner + ', and the visitor includes ' + visitor + '. They will have ' +
      num_of_onigili + ' onigilis and ' + num_of_anpan + ' anpans.')


# Int() and Float()
int(5.2)
float(5)
str(5)


print('There is a party in ' + party_location + '. It will start at ' + party_time +
      '. The owner is ' + house_owner + ', and the visitor includes ' + visitor + '. They will have ' +
      str(num_of_onigili) + ' onigilis and ' + str(num_of_anpan) + ' anpans.')


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
