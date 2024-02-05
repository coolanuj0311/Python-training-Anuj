'''What are Nested Dictionaries?

Dictionaries that hold other dictionaries as values, creating a multi-level structure.
Useful for representing hierarchical data or grouping related information.

Representing complex data structures (e.g., JSON data, configuration files)
Organizing information hierarchically (e.g., employee records, product categories)
Building tree-like structures for efficient data retrieval and manipulation
Key Points:

Nested dictionaries can be arbitrarily deep.
Indentation is essential for readability.
Use dict.keys(), dict.values(), and dict.items() for common operations.
Consider alternative structures (e.g., custom classes) for very complex data.
'''

people={1:{'name':'john','age':'27','sex':'Male'},
        2:{'name':'Marie','age':'22','sex':'Female'}}
print(people)
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

people[3]={}
people[3]['name']='Luna'
people[3]['age']='24'
people[3]['sex']='Female'
people[3]['married']='No'
print(people)

people[4]={'name':'Peter','age':'29','sex':'Male','married':'yes'}
print(people[4])
print(people)

print(people[3])
print(people[4])
del people[3]['married']
del people[4]['married']
print(people[3])
print(people[4])

people={1: {'name': 'john', 'age': '27', 'sex': 'Male'},
        2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
        3: {'name': 'Luna', 'age': '24', 'sex': 'Female' },
        4: {'name': 'Peter', 'age': '29', 'sex': 'Male'}}
print(people)

del people[3],people[4]
print(people)

print(people.items())
for p_id,p_info in people.items():
    print("\nPerson ID:",p_id)
    for key in p_info:
        print(key+':',p_info[key])