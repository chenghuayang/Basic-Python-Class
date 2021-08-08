# Review
# list
box_1 = [1, 3, 5]
box_1[0] = 3
print(box_1)

# tuple
box_2 = (2, 4, 6)

# string
olympic_host = 'Japan'
year = 2021
print(str(year) + '\'s olympic is in ' + olympic_host + '.')
print(year + year)

year = '2021'
print(year + year)

# Today's class
# Select string characters
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
print(letters[1])
print(letters[-1])
print(letters[-2])

# String slice
# [start:], start ~ LAST
print(letters[1:])
# [:end], FIRST ~ end
print(letters[:3])
# [start:end], start ~ end
print(letters[0:3])
print(letters[:5])
print(letters[:26])
print(letters[:])
# [start:end:step]
print(letters[0:5:2])

# Single quotes and double quotes
box = 'Nekopen'
box = "Nekopen"
story = "'Hey!' said the man."
short_note = 'A "two inches" can be written as 2".'
print(story)
print(short_note)

print('\'')

## Comment & Docstring
# This is comment.
''' This is docstring. 
And this can also be triple quotes. '''

note = '''something
    here'''
print(note)

num = 50
print(num)
num = 5e1  # 5 * 10^1
print(num)
num = 5e2  # 5 * 10^2
print(num)
num = 10e3  # 10 * 10^3
print(num)
num = 1e4
print(num)
num = 1e-2  # 1 * 10^-2
print(num)
print(type(num))

two_lines = 'First\nSecond'
print(two_lines)

two_sentences = 'I\'m a penguin. ' + 'You are a penguin too.'
print(two_sentences)

# Functions of string
# length
name = 'Penchan'
print(len(name))
print(len(two_sentences))

list_1 = [10, 20, 30]
print(len(list_1))

# Split
story = "'Hey!' said the superman."
words = story.split('s')
print(words)

# Immutable: string
some_tuple = (1, 2)
some_letters = 'abc'
# some_letters[0] = 'b' -> wrong
new_letters = some_letters.replace('a', 'b')
print(new_letters)


# Practice: picnic time
# Goal: print the sentence: "Penchan has 5 りんご. Nekokun has 2 おにぎり."
name_1 = 'Penchan'
name_2 = 'Nekokun'
num_apple = 5
num_onigiri = 2

print(name_1 + ' has ' + str(num_apple) + ' りんご.')

# Practice
# Select "Karaage-kun" from the sentence: "Karaagen-kun is Nekokun and Penchan's friend."
sentence = 'Karaage-kun is Nekokun and Penchan\'s friend.'

print(sentence[0:11])  # "Karaage-kun"
print(sentence.split()[0])
