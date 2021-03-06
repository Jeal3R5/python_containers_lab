##Exercise 1 ##
students = ["Robert", "Logan", "Rachael", "Andrea", "Lulu", "Emi", "RahRah"]
#print(students[1])   #print second students name
#print(students[6])   #print the last students name



## Exercise 2 ##
foods = ('strawberry', 'cookie', 'water', 'coffee', 'salad', 'steak', 'crab')

#for food in foods:
#     print(f"{food} is a good food.")


## Exercise 3 ##
##use a for loop, print just the last two food stings from foods

# for food in foods:
#     print(foods[-2:])
#     break



## Exercise 4 ##
## Create a dictionary names home_town containing the keys of city, state, and population
## Print "I was born in city, state - population of population"

# home_town = {
#    'city': "Elizabethtown",
#    'state': "Kentucky",
#    'population': "30,179"
# }
# ##print(f"I was born in {city}, {state} - population of {population}")
# print(f"I was born in {home_town['city']}, {home_town['state']} - population in 2022: {home_town['population']}.")


## Exercise 5 ##
## Iterate over the key: value pairs in home_town and print a string for each item

# for key, val in home_town.items():
#     print(f"{key} = {val}")


## Exercise 6 ##
## Create an empty list named cohort
## Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape
##{
#   'student': 'Tina',
#    'fav_food': 'Cheeseburger'
# }


cohort = []

# -----One way to do this -----
# for index, student in enumerate(students):
#    cohort.append({
#    'student': student,
#    'fav_food': foods[index]
#    })
#for person in cohort:
#   print(f"{person['student']} really likes {person['fav_food']}")

# -----Another way to do this (Thank you Josh and Rich) -----
for student, food in zip(students, foods):              #Here we are going to pass zip two variables and combine them into tuple pairs in cohort list
  cohort.append({
    "student": student,
    "fav_food": food
  })

for person in cohort:
    print(f"{person['student']} really likes {person['fav_food']}")




## Exercise 7
##Using the list of students and list comprehension assign to a variable named awesome_students a new list containing strings similar to this:
## ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
## Iterate over the awesome_students printing out each string


# awesome_students = [f'{student} is awesome 'for student in students] 
# print(awesome_students)



## Exercise 8
##Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.

# letter = "a"
# if letter in foods:
#     print(foods)

# #food loop if statement
# for food in foods: 
#     print(food) 

# a_foods = [food for food in foods if "a" in food]
# print(a_foods)