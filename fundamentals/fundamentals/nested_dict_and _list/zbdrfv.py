dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key in dict:
        print(len(dict[key]), key.upper())
        for i in dict[key]:
            print(i)

printInfo(dojo)

def printInfo1(dict):
    for key, val in dict.items():
        print(len(val), key.upper())
        for i in val:
            print(i)

printInfo1(dojo)