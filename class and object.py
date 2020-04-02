# class Cars:
#     def __init__(self,color,price,ac):
#         print("inside constructor")
#         self.color = color
#         self.price = price 
#         self.ac = ac

# car1 = Cars("red",10000,True)
# car2 = Cars("black",20000,False)

# print("first car is", car1.price,car1.color,car1.ac)
# print("second car is", car2.price,car2.color,car2.ac)



# class Mobile:
#     def __init__(self, brand, price):
#         print("Inside constructor")
#         self.brand = brand
#         self.price = price

#     def purchase(self):
#         print("Purchasing a mobile")
#         print("This mobile has brand", self.brand, "and price", self.price)

# print("Mobile-1")
# mob1=Mobile("Apple", 20000)
# mob1.purchase()

# print("Mobile-2")
# mob2=Mobile("Samsung",3000)
# mob2.purchase()

# class Employee:
#     def __init__(self):
#         self.employee_id = None
#     def check_eligibility(self):
#         if(self.employee_id>=9000 and self.employee_id<=10000):
#             print("The employee is eligible for special benefits")
#         else:
#             print("The employee is not eligible for special benefits")
# emp1=Employee()
# emp1.employee_id=10000
# emp1.check_eligibility()
# emp2=Employee()
# emp2.employee_id=4500
# emp2.check_eligibility()

# class Example:
#     def __init__(self,num):
#         self.num=num

#     def set_num(self,num):
#         self.num=num

#     def get_num(self):
#         return self.num
# obj=Example(10)
# print(obj.get_num())
# obj.set_num(15)
# print(obj.get_num())

# class Customer:
#     def __init__(self):
#         self.cust_id = 100

# c1=Customer()
# print(c1.cust_id)

# class Customer:
#     def __init__(self,id):
#         self.id = 100

# c1=Customer(200)
# print(c1.id)

# class Customer:
#     def __init__(self,id1):
#         self.id1 = id1

# c1=Customer(200)
# print(c1.id1)


# class Customer:
#     def __init__(self,id1):
#         self.id = id1

# c1=Customer(200)
# print(c1.id)


# class Book:
#     def __init__(self):
#         self.title=None


# my_fav=Book()
# my_fav.title="Head First Programming"
# your_fav=Book()
# your_fav.title="Learn Python the hard way"
# my_fav.title="Learning Python"
# print("My favorite is",my_fav.title)
# print("Your's is",your_fav.title)



# class Mobile:
#     def display(self):
#         print("Displaying details")

#     def purchase(self):
#         self.display()
#         print("Calculating price")

# Mobile().purchase()




class Mobile:
    def __init__(self, brand, price):
        print("Inside the Mobile constructor")
        self.brand = brand
        self.price = price
        self.total_price = None

    def purchase(self):
        if self.brand == "Apple":
            discount = 10
        else:
            discount = 5
        self.total_price = self.price - self.price * discount / 100
        print("Total price of", self.brand, "mobile is", self.total_price)

    def return_product(self):
        print("Refund Amount for", self.brand, "mobile is", self.total_price)

class Shoe:
    def __init__(self, material, price):
        print("Inside the Shoe constructor")
        self.material = material
        self.price = price
        self.total_price = None

    def purchase(self):
        if self.material == "leather":
            tax = 5
        else:
            tax = 2
        self.total_price = self.price + self.price * tax / 100
        print("Total price of", self.material, "shoe is", self.total_price)

    def return_product(self):
        print("Refund Amount for", self.material, "shoe is", self.total_price)

mob1=Mobile("Apple", 20000)
mob2=Mobile("Samsung", 10000)

shoe1=Shoe("leather",3000)
shoe2=Shoe("canvas",200)

mob1.purchase()
mob2.purchase()

shoe1.purchase()
shoe2.purchase()

mob2.return_product()

shoe1.return_product()1533253
