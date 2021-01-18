#파일명: my_module.py
# my_module 모듈(모듈이름: 파일명)

class Person():
    # initializer( Constructor 생성자 구현)
    def __init__(self, name, age):
        # Attribute를 매개변수로 받은 값으로 초기화.
        self.name = name
        self.age = age   
        
    def __str__(self):
        return f"{self.name}, {self.age}"
        
        
        
def greeting(name):
    print(f"{name}님 안녕하세요")
    
def helloworld():
    print("Hello world")
   
    

print(f"__name__:{__name__}")

if __name__ == '__main__':
    print("Main")
    
    import random
    
    print(plus(1,2))
    print(minus(10,5))
    print(multiply(2,9))
    print(random.randint(1,99))
    