# #   1.  Update Values in Dictionaries and Lists

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# # print(x)
# # print(students)
# # print(sports_directory)
# # print(z)

#     # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# print(x)

#     # Change the last_name of the first student from 'Jordan' to 'Bryant'
# students[0]["last_name"]= "Bryant"
# print(students)

#     # In the sports_directory, change 'Messi' to 'Andres'
# sports_directory["soccer"][0]= "Andres"
# print(sports_directory)

#     # Change the value 20 in z to 30
# z[0]["y"]= 30
# print(z)

#   2.  Iterate through a List of Dictionaries

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(students):
#     for i in range(0, len(students), 1):
#         print("first_name - " + (students[i]["first_name"]) + ", " + "last_name - " + (students[i]["last_name"]))

# iterateDictionary(students) 

#   3.  Get Values from a Lift of Dictionaries

# def iterateDictionary2(students):
#     for i in range(0, len(students), 1):
#         print(students[i]["first_name"])

# iterateDictionary2(students)

# def iterateDictionary2(students):
#     for i in range(0, len(students), 1):
#         print(students[i]["last_name"])

# iterateDictionary2(students)



#   4.  Iterate through a Dictionary with list Values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    locations = len("locations")
    instructors = len("instructors")
    print(f"{locations} LOCATIONS")
    for i in range(0, len(dojo["locations"]), 1):
        print(dojo["locations"][i])

    print(f"{instructors} INSTRUCTORS")
    for i in range(0, len(dojo["instructors"]), 1):
        print(dojo["instructors"][i])


printInfo(dojo)

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon