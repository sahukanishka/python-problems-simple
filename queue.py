class Queue:
    
    def __init__(self):
        self.queue = []
        
    def enque(self,item):
        self.queue.append(item)
        return self.queue


    def dequeu(self,queue):
        if len(self.queue) < 1:
            print("queue is empty")
        else:
            self.queue.pop(0)
    
            
    def printq(self,queue):
        print(self.queue)
            
q  = Queue()
q.enque(5)
q.enque(6)
q.enque(7)
q.enque(10)
q.printq(q)
q.dequeu(q)
q.printq(q)
q.dequeu(q)
q.printq(q)
