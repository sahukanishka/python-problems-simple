class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data
    def set_data(self):
        self.__data=data
    def get_next(self):
        return self.__next 
    def set_next(self,next_node):
        self.__next=next_node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head
    def get_tail(self):
        return self.__tail
    def add(self,data):
        pass
    def display(self):
        pass


    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="LInked list data(head to tail):"+msg
        return msg


list1=LinkedList()
list1.add("sugar")
print("element added sucessfully")


     