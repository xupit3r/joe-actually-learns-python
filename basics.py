import pjoe.joebar as pj
import mygame.draw as md
import mygame.game as mg

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
