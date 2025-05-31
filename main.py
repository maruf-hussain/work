# from operator import index

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
# import json
# personJs ={
#     "name": "Maruf",
#     "age": 29,
#     "addres": "Satkhira",
#     "desination": [
#         "Programmer,Engineer,Writer"
#     ]
#     }
# persionObject = json.loads(personJs)
# print(persionObject)



# class Father:
#     x = 50
#     y = 20


#     def __init__(self):
#          print("father constructer")



#     def add(self):
#         print(self.x + self.y)

# class Son(Father):
#    def __init__(self):
#        super().__init__()
#        print("Son Constructer")



# obj1 = Son()


# Encapsulation ........................with atm booth bank.......

# class BankAccount :
    
#     __balance = 50

#     # Deposit............
#     def deposit(self,amount):
#         if amount > 100:
#            self.__balance += amount
#            print(amount, "Taka deposit succesfully")

#         else:
#             print("invalied Ammount")

#     # Withdraw.............................................
#     def withdraw(self,amount):
#         if amount >= 100 and amount <= self.__balance:
#          self.__balance -= amount
#          print(amount,"withdraw succesfully")

#         else:
#          print("invalied withdraw ammount")


#     # Check Balance..................
#     def check_balance(self):
#         return  self.__balance
    
    




# obj = BankAccount()

# obj.deposit(700)

# print('Total Balance',obj.check_balance())

# obj.withdraw(500)
# print('Total Balance',obj.check_balance())




# Python Module..........................................................
# import calculator 
# print(calculator.add(50,60))
# print(calculator.sub(90,60))
# print(calculator.mul(50,2))
# print(calculator.dev(50,5))
        
# from calculator import add
# print(add(45,10))



# import os
# res = os.getcwd()
# print(res)


# import sys
# res = sys.version
# print(res)


# import datetime
# current_datetime = datetime.datetime.now()
# print(current_datetime.year)



