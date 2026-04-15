#use a fixed-size stack
class Stack:
    def __init__(self,size):
        self.size = size
        self.stack =[None]*size
        self.top = -1
        #Push with overflow check
    def push(self,value):
        if self.top == self.size -1:
            print("Stack Overflow! Cannot push",value)
        else:
            self.top +=1
            self.stack[self.top]=value
            print(value,"pushed")
            #Pop with underflow check
    def pop(self):
        if self.top==-1:
            print("Stack Underflow! Stack is empty")
        else:
            print(self.stack[self.top],"popped")
            self.top -=1
            #Display stack
    def display(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            print("Stack elements:",self.stack[:self.top+1])
#Driver code
s=Stack(3)
s.push(10)
s.push(20)
s.push(30)
#Overflow case
s.push(40)
s.display()
s.pop()
s.pop()
s.pop()
#underflow case
s.pop()
