from operator import index

# Pythont genarel math............
# num1=50
# num2=40
# sum=num1+num2
# print(sum)

# Python Condition.................
# age=20
# if age>=20:
#     print("you are adult")
# else: print("you are chile")
#
# mark=30
# if mark<=100 and mark>=80:
#     print("Your Grade A+")
# elif mark<=80 and mark>=70:
#     print("A")
# elif mark<=70 and mark>=60:
#     print("A-")
# elif mark<=60 and mark>=50:
#     print("B")
# elif mark<=50 and mark>=40:
#     print("C")
# elif mark<=40 and mark>=33:
#     print("D")
# else:
#     print("F")


# For Loop..................................
# List item......................
# Citis = ['dhaka','kolkata','bankok','paris']
# for City in Citis:
#     print(City)
#
    # for item in range(100):
    #     print(item)



    # for item in range(100):
#     if item == 12:
#         break
#     print(item)



# for item in range(100):
#     if item == 10:
#         continue
#     print(item)

# for loop in .......dictonary....................................
# examResult = {'bangla': 95, 'math': 85, 'english':75}
# for subject,marks in examResult.items():
#     print(subject,marks)

# while loop..........................................
# fruits = ['banana','apple', 'orange']
# index=0
# while index<len(fruits):
#     print(fruits[index])
#     index = index + 1
#
#

# index=1
# end=12
# while index<end:
#     if index == 5:
#         break
#     print(index)
#     index=index+1

# Logical Condition...................
# age = 20
# has_permission = True
#
# if age >=20 and has_permission == True:
#     print("you are adult")
# else:
#     print("you are child")


# function......................................
# def Addition(a,b):
#     sum = a + b
#     print(sum)
#
# Addition(50,30)

# List Method........................................
# country = ["Bangladesh", "India", "Pakistan"]
# # country.append("America")
# # country.append("America")
# # country.remove("America")
# country.insert(0,"America")
# print(country)

# file create and read and write....................
# with open("maruf.text", "w") as file:
#     file.write("amar sonar bangla ami tomay valobashi")
#     print("created")

# import json
# # Python Object to create Json string file................................
# persion = {
#     "name": "Maruf",
#     "age": 29,
#     "addres": "Satkhira",
#     "has_children": False,
#     "desination": ["Programmer,Engineer,Writer"]
# }
# persionJson = json.dumps(persion, indent=4)
# print(persionJson)

# Json string to Python Object..........................
import json
personJs ={
    "name": "Maruf",
    "age": 29,
    "addres": "Satkhira",
    "desination": [
        "Programmer,Engineer,Writer"
    ]
    }
persionObject = json.loads(personJs)
print(persionObject)

