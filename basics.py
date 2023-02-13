from itertools import repeat
import pjoe.joebar as pj
import mygame.draw as md
import mygame.game as mg
import numpy as np
import pandas as pd
import random
from functools import partial, reduce

mylist = []

mylist.append(1)
mylist.append(2)
mylist.append(3)

for x in mylist:
    print(x)


number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7**2
cubed = 7**3
print(squared)
print(cubed)

lotsahellos = "hello" * 10
print(lotsahellos)

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = even_numbers + odd_numbers
print(all_numbers)

print([1, 2, 3] * 3)

name = "Joe"
print("Hello, %s!" % name)

name = "Joe"
age = 37
print("%s is %d years old." % (name, age))

mylist = [1, 2, 3]
print("A list: %s" % mylist)

astring = "ABCDE, FGHIJ!"
print(astring.count("l"))
print(astring[3:7])
print(astring[:7:2])
print(astring[::-1])

name = "Joe"
age = 37

if name == "Joe" and age == 37:
    print("Your name is %s and you are %d years old" % (name, age))

if name == "Joe" or name == "Rick":
    print("Your name is either Joe or Rick, i guess your name is %s" % name)

name = "Joe"
if name in ["Joe", "Shmoe"]:
    print("Your name is either joe or schmoe")


a = [1, 2, 3]
b = [1, 2, 3]
if a == b:
    print("they be equal!")

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

for x in range(3, 8, 2):
    print(x)


def my_function():
    print("sup, this is my function")


my_function()


class Joe:
    def __init__(self, thing):
        self.thing = thing

    def say(self):
        print("you said this: %s" % self.thing)


me = Joe("fuck!")

me.say()

phonebook = {}
phonebook["john"] = 12345678
phonebook["jingle"] = 1222222
phonebook["rudolph"] = 1
print(phonebook)

for name, number in phonebook.items():
    print("name is %s, phone number is %d" % (name, number))


play_state = mg.play_game()
md.draw_game(play_state)

pj.joe()

height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height**2

print(bmi)
print(bmi > 23)
print(bmi[bmi > 25])

dict = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98],
}

brics = pd.DataFrame(dict)
print(brics)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

cars = pd.read_csv("cars.csv", index_col=0)
print(cars)
print(cars.sort_values(by="awesomeness", ascending=False))


def lottery():
    for i in range(6):
        yield random.randint(1, 40)

    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is.... %d!" % random_number)

# a lengthy way to create a list of word lengths for every word except "the"
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(words)
print(word_lengths)

# a list comprehension way to do this
word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)

print(set("my name is Eric and Eric is my name".split()))

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

print(a.difference(b))
print(b.difference(a))

print(a.union(b))


def multiply(x, y):
    return x * y


dbl = partial(multiply, 2)
print(dbl(4))


def transmit(message):
    def transmitter():
        print("the nested function is printing the message %s" % message)

    return transmitter


print(transmit("test message")())


def repeater(old_function):
    # See learnpython.org/en/Multiple%20Function%20Arguments for how *args and **kwds works
    def new_function(*args, **kwds):
        old_function(*args, **kwds)
        old_function(*args, **kwds)

    # we have to return the new_function, or it wouldn't reassign it to the value
    return new_function


@repeater
def multiply(n1, n2):
    print(n1 * n2)


print(multiply(3, 2))

my_pets = ["alfred", "tabitha", "william", "arla"]
uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

first_uppered = list(map(lambda str: "%s%s" % (str[0].upper(), str[1:]), my_pets))
print(first_uppered)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, repeat(2, len(circle_areas))))

print(result)

my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [1, 2, 3, 4, 5]

zipped = list(map(lambda x, y: (x, y), my_strings, my_numbers))
print(zipped)

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)

numbers = [3, 4, 6, 9, 34, 12]
sum = reduce(lambda x, y: x + y, numbers, 10)
print(sum)
