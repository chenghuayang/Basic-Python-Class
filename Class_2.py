# Assign
box_1 = 10

# Check if it's the same
print(box_1 == 10)

# Boolean
print(box_1 + 10 <= 20)

penchan_is_penguin = True
print(penchan_is_penguin == True)
print(penchan_is_penguin == False)  # True != False
print(penchan_is_penguin != True)

# Class 2
# Types: integer, floating number, Boolean, list
box_1 = []  # square brackets
box_2 = [0]
print(box_2)
box_3 = [0, 1]
print(box_3)
box_4 = [10, 20]  # [#0, #1]
print(box_4[0])
print(box_4[1])
box_5 = [1, 2, 3, 4, 5]
print(box_5[0])
print(box_5[4])
box_5[0] = 2
print(box_5)
box_5[2] = 2
box_5[3] = 2
box_5[4] = 2
print(box_5)

# Tuple
box_1 = ()  # parantheses
box_2 = (1, 2)
print(box_2[0])

# List is mutable. (changeable)
# Tuple is immutable. (not changeable)

# String
# In Nekokun's house...

house_owner = 'Nekokun'
visitor = 'Penchan'

party_time = '12:00'
party_location = 'Nekokun\'s house'  # back slash
num_of_onigiri = 2
num_of_anpan = 2

print('There is a party in', party_location, '. It will start at', party_time,
      '. The owner is', house_owner, ', and the visitor includes', visitor, '. They will have',
      num_of_onigiri, 'onigiris and', num_of_anpan, 'anpans.')

print('There is a party in ' + party_location + '. It will start at ' + party_time +
      '. The owner is ' + house_owner + ', and the visitor includes ' + visitor + '. They will have ' +
      str(num_of_onigiri) + ' onigiris and ' + str(num_of_anpan) + ' anpans.')

print(num_of_onigiri)
print(str(num_of_onigiri))

print(type(num_of_onigiri))
print(type(str(num_of_onigiri)))

num_1 = 5.2
num_2 = '5.2'
num_3 = 5

print(int(num_1))
print(float(num_3))
print(float(num_2) + num_3)

print(num_1 == num_2)
