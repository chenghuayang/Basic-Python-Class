# assign
box_1 = "Penchan"

print(box_1)
print(type(box_1))

# Boolean
penchan_is_penguin = True
nekokun_is_penguin = False

print(penchan_is_penguin)
print(penchan_is_penguin == True)
print(penchan_is_penguin == False)

print(2 <= 3)
print(10 == 10.0)  # integer 100 2, floating number 100.8 1.2

my_list = ["apple", "orange", "momo", "watermelon"]
print(my_list[0])
print(my_list[2])
my_list[2] = "grape"
print(my_list)

my_tuple = (10, 20, 30)
print(my_tuple[1])

name_1 = "Penchan"
name_2 = "Nekokun"
name_3 = "Karaagekun"

print(name_3 + " is a friend of " + name_2 + " and " + name_1 + ".")
print(name_3 + " is " + name_2 + '\'s and ' +
      name_1 + "'s friend.")  # Nekokun's

num_1 = 2.4
num_2 = "2.4"
num_3 = 3

print(type(num_1), type(num_2), type(num_3))
print(num_1 + num_3)
print(num_1 + float(num_2))
print(num_2 + num_2)

letters = "abcdefg"
print(letters[0])
print(letters[3])
print(letters[3:])
print(letters[:3])
print(letters[:])  # print(letters)
print(letters[:5:2])  # step

num = 50
print(num)

num = 5e1
print(num)

num = 5e2
print(num)
