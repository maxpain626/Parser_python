

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrir"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")







'''
students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor", 
            "Ron": "Gryffindor",
            "Draco": "Slytherin",
            }

for student in students:
    print(student, students[student], sep=", ")
'''

'''
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

for i in range(len(students)):
    print(i + 1, students[i])
'''
