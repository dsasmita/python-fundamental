message = "This my first python project"
name = "Aqeel Adam Akma"
usia = 28
lingkar_perut = 35

print(message)
print(name)
print(usia)
print("")

# condition on python
print("Usia kamu?")
if usia <= 17:
    print("Masih muda")
else:
    print("Cukup Umur")

print("")
print("Lingkar perutmu?")
if lingkar_perut < 30:
    print("Aman")
elif lingkar_perut < 40:
    print("Cukup bahaya")
else:
    print("Mengerikan")

# looping on python
# for looping
for i in range(1, 6):
    test = str(i)
    print ("Munculkan string %s" % i)

# while looping
i = 0
while i <= 5:
    print("Run for %s" % i)
    i = i + 1

# list/array
months = ('January', 'February', 'March',
          'April', 'May', 'June',
          'July', 'August', 'September',
          'October', 'November', '  December')
print(months[10])

print("")
friends = ["John",
           "Doe",
           "Rudy",
           "Ilham"]
print(friends)
friends.append("Elvack")
print(friends)

print("")
print("Friend on loop:")
# get list in looping
for friend in friends:
    print("%s, adalah teman dari %s" % (name, friend))

# dictionary
print("")
human = {}
human["name"] = "John Doe"
human["sex"] = "Male"
human["expertise"] = "laravel"
print(human)

print("")
human["expertise"] = "%s, %s" % (human["expertise"], "Python, Golang")
human["city"] = "Surabaya"
print(human)

# Dumping dictionary into json
print("")
import json

print(json.dumps(human))
