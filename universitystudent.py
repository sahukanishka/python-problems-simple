# class Student:
#     def __init__(self):
#         self.__student_id = None
#         self.__age = None
#         self.__marks = None

#     def validate_marks(self,student_id,marks,__age):
#         self.set_value(self.__student_id,self.__marks,self.__age)
#         if self.__marks in range(0,100):
#             return True
#         else:
#             return False
#     def validate_age(self,student_id,marks,age):
#         self.set_value(self.__student_id,self.__marks,self.__age)
#         if self.__age > 20:
#             return True
#         else:
#             return False 

#     def check_qualification(self,student_id,marks,age):
#         self.set_value(student_id,marks,age)
#         if self.validate_marks(self.__student_id,self.__marks,self.__age) and self.validate_age(self.__student_id,self.__marks,self.__age) == True:
#             if self.__marks >= 65 :
#                 return True 
#             else:
#                 return False
#         else:
#             return False

#     def set_value(self,student_id,marks,age):
#         self.__marks = marks
#         self.__student_id = student_id
#         self.__age = age 

#     def get_value(self):
#         return self.__student_id,self.__marks,self.__age


# stu1 = Student()
# # stu1.set_value(123,67,18)
# print(stu1.check_qualification(123,67,18))

# print(stu1.get_value())


class Student:
    def __init__(self):
        self.__student_id = None
        self.__age = None
        self.__marks = None

    def validate_marks(self):
        if self.__marks in range(0,101):
            return True
        else:
            return False
    def validate_age(self):
        if self.__age > 20:
            return True
        else:
            return False 

    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.__marks >= 65 :
                return True 
        return False
    def get_student_id(self):
        return self.__student_id
    def get_age(self): 
        return self.__age
    def get_marks(self):
        return self.__marks
    
    def set_student_id(self,id):
        self.__student_id=id
    def set_age(self,age):
        self.__age=age
    def set_marks(self,marks):
        self.__marks=marks

stu1 = Student()
stu1.set_student_id(123)
stu1.set_age(18)
stu1.set_marks(67)

print(stu1.check_qualification())
print(stu1.get_student_id())
print(stu1.get_age())
print(stu1.get_marks())
