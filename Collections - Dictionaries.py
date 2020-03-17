# Dictionary is a collection which is unordered, changeable and indexed
# Use {curly brackets} and dictionaries have KEYS and VALUES
# list can be used in a dictionary as well as values

student_1 = {
    "name" : "Susan",
    "stream" : "tech",
    "completed_lessons" : 4,
    "completed_lessons_names" : ["variables", "data_types", "set_up"]
}

# print(student_1)
print(student_1["stream"])
print(student_1["completed_lessons_names"][1])

# change value in dicitonary
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])
print(student_1)

# remove an item
student_1["completed_lessons_names"].remove("data_types")
print(student_1["completed_lessons_names"]) # only if you print you can see if the data is remove or not
