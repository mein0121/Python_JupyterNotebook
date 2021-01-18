#파일명: my_module.py
# my_module 모듈(모듈이름: 파일명)


        
def plus(n1, n2):
    return n1 + n2
    
def minus(n1,n2):
    return n1 - n2
    
def multiply(n1,n2):
    return n1 * n2
 
def divide(n1,n2):
    return round(n1/n2,2)



print(f"__name__:{__name__}")

if __name__ == '__main__':
    print("Main")
    
    import random
    
    print(plus(1,2))
    print(minus(10,5))
    print(multiply(2,9))
    print(random.randint(1,99))
    