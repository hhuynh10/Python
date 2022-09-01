# Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]['last_name'] = 'Bryant'
print(students[0])

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

z[0]['y'] = 30
print(z)

# Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for student in students:
        print(f"first name - {student['first_name']}, last name - {student['last_name']}")

iterateDictionary(students)

# Get Values From a List of Dictionaries
def iterateDictionary2(name, students):
    for student in students:
        if name == 'first_name':
            print(student['first_name'])
            
        if name == 'last_name':
            print(student['last_name'])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# Iterate Through a Dictionary with List Values
dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    for key, val in dojo.items():
        print(len(key), key.upper())
        for i in range(0, len(val)):
            print(val[i])

printInfo(dojo)
