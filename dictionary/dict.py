abc = {'color': 123}
abc['color'] = 123123
abc['colors'] = 123123

print(abc)

#
for key,value in abc.items():
    print(key)
    print(value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
languages = {
    'jen': 'json',
    'sarah': 'sabih',
    'edward': 'siddiqui',
    'phil': 'sidd',
}

for a , b in favorite_languages.items():
    print(a.title() + "'s fav language  " + b.title())

for name in sorted(favorite_languages):
 print(name.title() + ", thank you for taking the poll.")


array = [favorite_languages, languages]

print(array)

for a in array[:3]:
    for b in a:
        print(a[b])

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

# for a, b in users.items():
#     for key, value in b.items():
#         print(key  + " " + value)




for a, data in users.items():
        print("\n username " + a + ': ')
        fullName = data['first'] + " " + data['last']
        location = data['location']
        print("\t" + "Name: " + fullName)
        print("\t" + "Location: " +location)

