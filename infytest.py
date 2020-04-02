# class Example:
#     def __init__(self):
#         self.__num=5

#     def set_num(self,num):
#         self.__num=num

#     def get_num(self):
#         return self.__num
# obj=Example()
# obj.set_num(6)
# print(obj.get_num())

# class Example:
#     def __init__(self):
#         self.__num=None

#     def set_num(self,num):
#         self.__num=num

#     def change_num(self):
#         self.__num=5
#         return self.__num
# obj=Example()
# obj.set_num(10)
# print(obj.change_num())



# class Dam:
#     def __init__(self,name, length):
#         self.name=name
#         self.__length=length
#     def get_length(self):
#         return self.__length

# dam1=Dam("ABC dam",3.5 )
# print("Dam name:",dam1.name)
# print("Dam Length", dam1.get_length())


# class Table:
#     def __init__(self):
#         self.no_of_legs=4
#         self.__glass_top=None
#         self.__wooden_top=None

#     def assign_data(self,glass_top,wooden_top):
#         self.__glass_top=glass_top
#         self.__wooden_top=wooden_top

#     def identify_rate(self,glass_top,wooden_top):
#         self.assign_data(glass_top, wooden_top)
#         if(self.__glass_top==True):
#             rate=20000
#         elif(self.__wooden_top==True):
#             rate=30000
#         else:
#             rate=0
#         return rate
# dining_table=Table()
# rate=dining_table.identify_rate(True, False)
# print(rate)



class Mobile:
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

mob1=Mobile(1000, "Apple")

mob2=mob1
mob2=Mobile(2000, "Samsung")
mob2.price=3000

print("Mobile", "Id","Price")
print("mob1", id(mob1), mob1.price)
print("mob2", id(mob2), mob2.price)