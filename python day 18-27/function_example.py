#  Simple function example
def add(a,b):
    print("Addition : ", a+b)
add(3,2)  

# function Example using return type
def mul(p,q):
    return(p * q)
print("Multiplication is :",mul(3,3))


# Method example with self keyword
class Addition:
    def add(self , m , n):
        print(m + n)      
obj = Addition()
obj.add(2,3)

#  Using @staticmethod
class Multiplication :
    @staticmethod
    def mul(m , n):
        print(m * n)

obj = Multiplication()
obj.mul(2,3)  




