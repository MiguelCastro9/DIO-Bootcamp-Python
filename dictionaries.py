# dictionaries in python

# a dictionary is an unordered set of key and value key:value pairs.

people = {'name': 'miguel castro', 'age': 24}
print(people)

car = dict(brand = 'bmw', year = 2024)
car['value'] = 50000
print(car)

contacts = {
    "fulano@gmail.com": {"name": "fulano", "phone": "3333-2221"},
    "ciclano@gmail.com": {"name": "ciclano", "phone": "3443-2121"},
    "beutrano@gmail.com": {"name": "beutrano", "phone": "3344-9871"}
}
print(contacts)
print(contacts["fulano@gmail.com"]["phone"])

# 'get' method to search for a key within the dictionary, and if it does not exist, return an empty object.

print(car.get('brand', {}))

# 'key' method to return dictionary keys.

print(contacts.keys())

# 'values' method to return dictionary values.

print(contacts.values())

# 'pop' method to remove a key from the dictionary and also if the key does not exist it returns an empty object.

contacts.pop('fulano@gmail.com')
print(contacts.keys())

# 'update' method to update dictionaries.

people.update({'name': 'miguel'})
print(people)

# 'in' method to check if a given value is a key in a dictionary.

result = 'beutrano@gmail.com' in contacts
print(result)

# 'del' method to remove keys from a dictionary.

del car['brand']
print(car)

del contacts['ciclano@gmail.com']['name']
print(contacts)