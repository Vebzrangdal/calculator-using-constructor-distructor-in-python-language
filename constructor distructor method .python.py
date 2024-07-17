class example :
    #class constructor 
    def __init__(self):
        print("class constructor ")
        self.fun()
        
    #default function 
    def fun(self):
        print("function")
        
    #parametrized function 
    def add(self,i,j):
        print("add :",i+j)
    def sub(self,i,j):
        print("sub :",i-j)
    def mult(self,i,j):
        print("mult :",i*j)
    def div(self,i,j):
        print("div :",i/j)
        
        
    #class distructor 
    def __del__(self):
        print("class distructor ")
        
        
        
obj=example()
print("1) add ")
print("2) sub ")
print("3) mult")
print("4) div ")

op=int(input(">>>"))

if op==1:
    obj.add(int(input("1st :")),int(input("2nd :")))
elif op==2:
    obj.sub(int(input("1st :")),int(input("2nd :")))
elif op==3:
    obj.mult(int(input("1st :")),int(input("2nd :")))
elif op==4:
    obj.div(int(input("1st :")),int(input("2nd :")))

