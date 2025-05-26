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

# dictonary....................................
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
# for item in range(100):
#     if item == 12:
#         break
#     print(item)

# for item in range(100):
#     if item == 10:
#         continue
#     print(item)

index=1
end=12
while index<end:
    if index == 5:
        break
    print(index)
    index=index+1